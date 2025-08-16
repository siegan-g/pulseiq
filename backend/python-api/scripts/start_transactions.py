from services.transaction import TransactionService
from services.strategies.transaction_strategy_factory import TransactionStrategyFactory

def main():
    # default_factory will send data to Couchbase and the ML Model and get a response from both
    default_factory = TransactionStrategyFactory()
    service = TransactionService(default_factory)
    service.start_server()

if __name__ == '__main__':
    main()