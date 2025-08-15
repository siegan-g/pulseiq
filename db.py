from __future__ import annotations
from couchbase.cluster import Cluster
from couchbase.options import ClusterOptions, PingOptions
from couchbase.auth import PasswordAuthenticator
from couchbase.exceptions import CouchbaseException
from datetime import timedelta
from dotenv import load_dotenv
from couchbase.result import PingResult
from couchbase.diagnostics import PingState, ServiceType
import os
import json
from functools import cache
from typing import Optional, Dict, Any, List

class CouchbaseClient:
    """Class to handle interactions with Couchbase cluster for PulseIQ"""
    
    def __init__(
        self, 
        conn_str: str, 
        username: str, 
        password: str,
        bucket_name: str = "pulseiq",
        scope_name: str = "payment_analytics"
    ) -> None:
        self.cluster = None
        self.bucket = None
        self.scope = None
        self.conn_str = conn_str
        self.username = username
        self.password = password
        self.bucket_name = bucket_name
        self.scope_name = scope_name
        self.connect()

    def connect(self) -> None:
        """Connect to the Couchbase cluster"""
        if not self.cluster:
            try:
                auth = PasswordAuthenticator(self.username, self.password)
                cluster_opts = ClusterOptions(auth)
                cluster_opts.apply_profile("wan_development")
                
                self.cluster = Cluster(self.conn_str, cluster_opts)
                self.cluster.wait_until_ready(timedelta(seconds=5))
                
                self.bucket = self.cluster.bucket(self.bucket_name)
                self.scope = self.bucket.scope(self.scope_name)
                
                print("✓ Successfully connected to Couchbase")
                
            except CouchbaseException as error:
                raise ConnectionError(
                    f"Could not connect to cluster: {error}\n"
                    "Ensure your IP is whitelisted and credentials are correct"
                )

    def ping(self) -> Dict[str, Any]:
        """Check cluster health status"""
        try:
            result: PingResult = self.cluster.ping()
            return {
                "id": result.id,
                "sdk": result.sdk,
                "version": result.version,
                "endpoints": {
                    "kv": [e.state for e in result.endpoints[ServiceType.KeyValue]],
                    "query": [e.state for e in result.endpoints[ServiceType.Query]],
                    "search": [e.state for e in result.endpoints[ServiceType.Search]]
                }
            }
        except Exception as e:
            return {"error": str(e)}

    def close(self) -> None:
        """Close the connection to the Couchbase cluster"""
        if self.cluster:
            try:
                self.cluster.close()
                print("Connection closed")
            except Exception as e:
                print(f"Error closing cluster: {e}")

    # Core CRUD Operations
    def get_document(self, collection: str, key: str) -> Optional[Dict]:
        """Get document by key"""
        try:
            return self.scope.collection(collection).get(key).content_as[dict]
        except Exception as e:
            print(f"Error getting document: {e}")
            return None

    def insert_document(self, collection: str, key: str, doc: Dict) -> bool:
        """Insert document with specified key"""
        try:
            self.scope.collection(collection).insert(key, doc)
            return True
        except Exception as e:
            print(f"Error inserting document: {e}")
            return False

    def upsert_document(self, collection: str, key: str, doc: Dict) -> bool:
        """Insert or update document"""
        try:
            self.scope.collection(collection).upsert(key, doc)
            return True
        except Exception as e:
            print(f"Error upserting document: {e}")
            return False

    def delete_document(self, collection: str, key: str) -> bool:
        """Delete document by key"""
        try:
            self.scope.collection(collection).remove(key)
            return True
        except Exception as e:
            print(f"Error deleting document: {e}")
            return False

    # Collection-specific operations
    def create_transaction(self, data: Dict) -> Optional[Dict]:
        """Create a transaction document"""
        doc_id = f"txn_{data.get('transactionId', os.urandom(3).hex())}"
        doc = {
            "type": "transaction",
            "timestamp": data.get("timestamp") or datetime.utcnow().isoformat() + "Z",
            **data
        }
        if self.insert_document("transactions", doc_id, doc):
            return {"id": doc_id, **doc}
        return None

    def get_recent_alerts(self, limit: int = 10) -> List[Dict]:
        """Query recent alerts"""
        query = f"""
        SELECT alerts.* 
        FROM `{self.bucket_name}`.`{self.scope_name}`.`alerts` alerts
        ORDER BY alerts.timestamp DESC
        LIMIT {limit}
        """
        try:
            result = self.cluster.query(query)
            return [row["alerts"] for row in result]
        except Exception as e:
            print(f"Error querying alerts: {e}")
            return []

    # Analytics queries
    def get_transaction_stats(self, time_range: str = "1h") -> Dict:
        """Get transaction statistics"""
        query = f"""
        SELECT 
            COUNT(*) as total,
            SUM(CASE WHEN status = "completed" THEN 1 ELSE 0 END) as completed,
            SUM(CASE WHEN status = "failed" THEN 1 ELSE 0 END) as failed,
            AVG(processingTimeMs) as avg_processing_time
        FROM `{self.bucket_name}`.`{self.scope_name}`.`transactions`
        WHERE timestamp > NOW() - INTERVAL '{time_range}'
        """
        try:
            result = self.cluster.query(query)
            return result.execute().rows()[0]
        except Exception as e:
            print(f"Error getting stats: {e}")
            return {}

    # Index management
    def create_primary_indexes(self) -> None:
        """Create primary indexes for all collections"""
        collections = ["transactions", "predictions", "alerts", "users", "system_metrics"]
        for col in collections:
            try:
                self.cluster.query(
                    f"CREATE PRIMARY INDEX ON `{self.bucket_name}`.`{self.scope_name}`.`{col}`"
                )
                print(f"Created primary index for {col}")
            except Exception as e:
                print(f"Index creation for {col} may already exist: {e}")

@cache
def get_db() -> CouchbaseClient:
    """Get cached Couchbase client instance"""
    load_dotenv()
    return CouchbaseClient(
        conn_str=os.getenv("COUCHBASE_CONN_STR"),
        username=os.getenv("COUCHBASE_USERNAME"),
        password=os.getenv("COUCHBASE_PASSWORD")
    )