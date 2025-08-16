from models.transaction import Transaction
from .generic_strategy_factory import GenericStrategyFactory
from models.repository import GenericRepository
from .default_transaction_strategy import DefaultTransactionStrategy 

class TransactionStrategyFactory:
    # Super hacky way of feeding our parameters to the factory just to get this run, 
    # there's probably another pattern to implement a list of adapters
    def __init__(self,database_adapter:GenericRepository,pulse_ml_model_adapter:GenericRepository)->None:
        self.database = database_adapter
        self.ml_model = pulse_ml_model_adapter
        pass

    def create(self) -> GenericStrategyFactory:
        """
        Added this Factory if there is a usecase for multiple different strategies. E.g if transaction is merchant is FNB adjust the outgoing adapters accordingly
        """
        return DefaultTransactionStrategy(self.database,self.ml_model)