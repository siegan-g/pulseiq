from typing import Generic, TypeVar, Optional, List, Dict, Any
from abc import ABC, abstractmethod
from models.repository import PulseEntity  # absolute import
from couchbase_client import CouchbaseClient

T = TypeVar('T', bound=PulseEntity)

class GenericRepository(Generic[T], ABC):
    def __init__(self, db: CouchbaseClient, collection_name: str):
        self.db = db
        self.collection_name = collection_name

    @abstractmethod
    def _to_entity(self, data: Dict[str, Any]) -> T:
        """Convert raw Couchbase document to entity"""
        raise NotImplementedError

    @abstractmethod
    def _from_entity(self, entity: T) -> Dict[str, Any]:
        """Convert entity to Couchbase document"""
        raise NotImplementedError

    def get(self, id: str) -> Optional[T]:
        """Get single document by ID"""
        doc = self.db.get_document(self.collection_name, id)
        return self._to_entity(doc) if doc else None

    def list(self, limit: int = 100, offset: int = 0, **filters) -> PaginatedResponse[T]:
        """List documents with pagination and filtering"""
        where_clause = " AND ".join([f"{k} = ${k}" for k in filters.keys()])
        query = f"""
        SELECT d.*, META(d).id as _id
        FROM `{self.db.bucket_name}`.`{self.db.scope_name}`.`{self.collection_name}` d
        {f"WHERE {where_clause}" if filters else ""}
        ORDER BY d.timestamp DESC
        LIMIT $limit
        OFFSET $offset
        """
        
        params = {**filters, "limit": limit, "offset": offset}
        result = self.db.cluster.query(query, params)
        
        items = [self._to_entity(row) for row in result]
        total = next(self.db.cluster.query(f"""
            SELECT COUNT(*) as total 
            FROM `{self.db.bucket_name}`.`{self.db.scope_name}`.`{self.collection_name}`
            {f"WHERE {where_clause}" if filters else ""}
        """, filters)).get("total", 0)
        
        return PaginatedResponse[T](
            items=items,
            total=total,
            limit=limit,
            offset=offset
        )

    def add(self, entity: T) -> T:
        """Insert new document"""
        doc = self._from_entity(entity)
        self.db.insert_document(self.collection_name, entity.id, doc)
        return entity

    def update(self, entity: T) -> T:
        """Update existing document"""
        doc = self._from_entity(entity)
        self.db.upsert_document(self.collection_name, entity.id, doc)
        return entity

    def delete(self, id: str) -> bool:
        """Delete document by ID"""
        return self.db.delete_document(self.collection_name, id)