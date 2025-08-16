from models.transaction import Transaction
from .generic_strategy_factory import GenericStrategyFactory
from models.repository import GenericRepository
from .default_transaction_strategy import DefaultTransactionStrategy 

class TransactionStrategyFactory:
    # Super hacky way of feeding our parameters to the factory, there's probably another pattern to make this cleaner
    def __init__(self,database_adapter:GenericRepository,pulse_ml_model_adapter:GenericRepository)->None:
        self.database = database_adapter
        self.ml_model = pulse_ml_model_adapter
        pass

    def create(self, transaction: Transaction) -> GenericStrategyFactory:
        strategy =  DefaultTransactionStrategy(self.database,self.ml_model)
        strategy.send(transaction)