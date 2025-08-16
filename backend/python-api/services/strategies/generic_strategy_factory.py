from abc import ABC, abstractmethod
from models.repository import PulseEntity 

class GenericStrategyFactory(ABC):
    @abstractmethod
    def send(self,entity:PulseEntity)->PulseEntity:
        """
        Generic strategy to send a pulse entity to multiple outgoing adapters
        """
        pass