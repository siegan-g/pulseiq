from typing import Optional, List, TypeVar
from models.repository import GenericRepository, PulseEntity
import uuid
from datetime import datetime

T = TypeVar("T", bound=PulseEntity)

class MockDatabaseAdapter(GenericRepository[T]):
    """
    Mock database adapter for testing purposes.
    Simulates a real database with in-memory storage.
    """
    
    def __init__(self):
        self._storage: dict[int, PulseEntity] = {}
        self._counter = 1
    
    def read_by_id(self, id: int) -> Optional[T]:
        """
        Get a single entity by id
        Args:
            id (int): id of the Entity
        Returns:
            Optional[T]: Entity or None
        """
        return self._storage.get(id)
    
    def list(self, **filters) -> List[T]:
        """
        Gets a list of entities 
        Args:
            **filters: Filter conditions
        Returns:
            List[T]: List of entities
        """
        entities = list(self._storage.values())
        
        # Apply filters if provided
        if filters:
            filtered_entities = []
            for entity in entities:
                if all(hasattr(entity, key) and getattr(entity, key) == value 
                       for key, value in filters.items()):
                    filtered_entities.append(entity)
            return filtered_entities
        
        return entities
    
    def add(self, entity: T) -> T:
        """
        Add a new entity to the repository
        Args:
            entity (T): The entity to add
        Returns:
            T: The added entity with generated ID
        """
        # Generate a new ID if not provided
        if entity.id is None:
            entity.id = self._counter
            self._counter += 1
        
        # Store the entity
        self._storage[entity.id] = entity
        
        # Log mock operation
        print(f"[MOCK DB] Added entity with ID: {entity.id}")
        
        return entity
    
    def update(self, record: T) -> T:
        """
        Update an existing entity in the repository
        Args:
            record (T): The entity to update (must have valid ID)
        Returns:
            T: The updated entity
        """
        if record.id is None:
            raise ValueError("Cannot update entity without ID")
        
        if record.id not in self._storage:
            raise ValueError(f"Entity with ID {record.id} not found")
        
        # Update the entity
        self._storage[record.id] = record
        
        # Log mock operation
        print(f"[MOCK DB] Updated entity with ID: {record.id}")
        
        return record
    
    def delete(self, id: int) -> None:
        """
        Delete an entity from the repository by ID
        Args:
            id (int): ID of the entity to delete
        Returns:
            None
        """
        if id in self._storage:
            del self._storage[id]
            print(f"[MOCK DB] Deleted entity with ID: {id}")
        else:
            print(f"[MOCK DB] Warning: Attempted to delete non-existent entity with ID: {id}")
    
    def clear_storage(self):
        """Clear all stored entities (useful for testing)"""
        self._storage.clear()
        self._counter = 1
        print("[MOCK DB] Storage cleared")
    
    def get_storage_size(self) -> int:
        """Get the number of stored entities"""
        return len(self._storage)