from models.transaction import Transaction
from .generic_strategy_factory import GenericStrategyFactory
from models.repository import PulseEntity
from models.repository import GenericRepository

class DefaultTransactionStrategy(GenericStrategyFactory):
    """
    Strategy to send transaction data to ml model and receive a response and log the transaction in the database
    """
    def __init__(self,database:GenericRepository,machine_learning_model:GenericRepository) -> None:
        self.database = database
        self.machine_learning_model = machine_learning_model
        super().__init__()

    def send(self, entity: PulseEntity) -> PulseEntity:
        database_response = self.database.add(entity)
        ml_response = self.machine_learning_model.add(entity)
        return {"destinations":[database_response,ml_response]}