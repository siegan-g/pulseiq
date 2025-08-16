from typing import Optional, List, Generic, TypeVar
from abc import ABC,abstractmethod
from pydantic import Field,BaseModel

class PulseEntity(BaseModel):
    """
    The Base Entity for any Model in PulseIQ
    """
    id: Optional[str | int] = Field(None, description="Entity ID")


T = TypeVar("T",bound=PulseEntity)
class GenericRepository(Generic[T],ABC):

    @abstractmethod
    def read_by_id(self,id:int)->Optional[T]:
        """
        Get a single entity by id
        Args:
            id (int): id of the Entity
        Returns:
            Optional[T]: Entity or None
        """
        raise NotImplementedError()
    
    @abstractmethod
    def list(self,**filters)->List[T]:
        """
        Gets a list of entites 
        Args:
            **filtesr: Filter conditions
        Returns:
            List[T]: List of entities
        """
        raise NotImplementedError()
    
    @abstractmethod
    def add(self,entity:T)->T:
        """
        Add a new entity to the repository
        Args:
            entity (T): The entity to add
        Returns:
            T: The added entity with generated ID
        """
        raise NotImplementedError()

    @abstractmethod
    def update(self,record:T)->T:
        """
        Update an existing entity in the repository
        Args:
            record (T): The entity to update (must have valid ID)
        Returns:
            T: The updated entity
        """
        raise NotImplementedError()
    
    @abstractmethod
    def delete(self,id:int)->None:
        """
        Delete an entity from the repository by ID
        Args:
            id (int): ID of the entity to delete
        Returns:
            None
        """
        raise NotImplementedError()