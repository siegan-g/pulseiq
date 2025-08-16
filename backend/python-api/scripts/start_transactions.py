from services.transaction import TransactionService
from services.strategies.transaction_strategy_factory import TransactionStrategyFactory
from adapters.mock_database_adapter import MockDatabaseAdapter
from adapters.mock_pulse_ml_adapter import MockPulseMlAdapter

def main():
    # default_factory will send data to Couchbase and the ML Model and get a response from both
    database = MockDatabaseAdapter()
    pulse_ml = MockPulseMlAdapter()
    default_factory = TransactionStrategyFactory(database_adapter=database,pulse_ml_model_adapter=pulse_ml)
    service = TransactionService(default_factory)
    service.start_server()

if __name__ == '__main__':
    main()