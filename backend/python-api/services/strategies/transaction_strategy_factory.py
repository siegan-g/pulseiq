from models.transaction import Transaction
from .generic_strategy_factory import GenericStrategyFactory

class TransactionStrategyFactory:
    def __init__(self)->None:
        # self.couchbase = CouchbaseAdapter()
        # self.kafka = KafkaAdapter()
        # self.prometheus = PrometheusAdapter()
        pass

    def create(self,transaction:Transaction)->GenericStrategyFactory:
        pass