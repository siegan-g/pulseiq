from typing import Optional, List, TypeVar
from models.repository import GenericRepository, PulseEntity
import random
import time
from datetime import datetime

T = TypeVar("T", bound=PulseEntity)

class MockPulseMlAdapter(GenericRepository[T]):
    """
    Mock ML model adapter for testing purposes.
    Simulates a real ML model with mock predictions and responses.
    """
    
    def __init__(self):
        self._storage: dict[int, PulseEntity] = {}
        self._counter = 1
        self._model_version = "mock-v1.0.0"
        self._prediction_accuracy = 0.85  # Mock accuracy
    
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
        Add a new entity to the repository and generate ML predictions
        Args:
            entity (T): The entity to add
        Returns:
            T: The added entity with generated ID and ML predictions
        """
        # Generate a new ID if not provided
        if entity.id is None:
            entity.id = self._counter
            self._counter += 1
        
        # Simulate ML processing time
        processing_time = random.uniform(0.1, 0.5)
        time.sleep(processing_time)
        
        # Generate mock ML predictions
        enriched_entity = self._enrich_with_ml_predictions(entity)
        
        # Store the enriched entity
        self._storage[enriched_entity.id] = enriched_entity
        
        # Log mock operation
        print(f"[MOCK ML] Processed entity with ID: {enriched_entity.id} in {processing_time:.2f}s")
        
        return enriched_entity
    
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
        
        # Re-process with ML predictions
        updated_entity = self._enrich_with_ml_predictions(record)
        
        # Update the entity
        self._storage[updated_entity.id] = updated_entity
        
        # Log mock operation
        print(f"[MOCK ML] Updated and re-processed entity with ID: {updated_entity.id}")
        
        return updated_entity
    
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
            print(f"[MOCK ML] Deleted entity with ID: {id}")
        else:
            print(f"[MOCK ML] Warning: Attempted to delete non-existent entity with ID: {id}")
    
    def _enrich_with_ml_predictions(self, entity: T) -> T:
        """
        Enrich entity with mock ML predictions
        Args:
            entity (T): The entity to enrich
        Returns:
            T: The enriched entity
        """
        # Create a copy to avoid modifying the original
        enriched = entity.model_copy(deep=True)
        
        # Generate mock predictions based on entity type
        predictions = {}
        
        if hasattr(enriched, 'type'):
            if enriched.type == 'transaction':
                predictions = {
                    'fraud_score': round(random.uniform(0.0, 1.0), 3),
                    'risk_level': random.choice(['low', 'medium', 'high']),
                    'anomaly_detected': random.random() < 0.1,  # 10% chance
                    'processing_recommendation': random.choice(['approve', 'review', 'reject']),
                    'confidence_score': round(random.uniform(0.7, 0.99), 3)
                }
            elif enriched.type == 'alert':
                predictions = {
                    'severity_prediction': random.choice(['low', 'medium', 'high', 'critical']),
                    'escalation_probability': round(random.uniform(0.0, 1.0), 3),
                    'auto_resolution_possible': random.choice([True, False])
                }
            else:
                predictions = {
                    'general_score': round(random.uniform(0.0, 1.0), 3),
                    'classification': random.choice(['type_a', 'type_b', 'type_c'])
                }
        
        # Add ML metadata
        predictions['model_version'] = self._model_version
        predictions['prediction_timestamp'] = datetime.now().isoformat()
        predictions['confidence_interval'] = round(random.uniform(0.05, 0.15), 3)
        
        # Try to add predictions to metadata if it exists and is a dict
        if hasattr(enriched, 'metadata') and enriched.metadata is not None:
            if isinstance(enriched.metadata, dict):
                enriched.metadata['ml_predictions'] = predictions
            else:
                # If metadata exists but isn't a dict, just log the predictions
                print(f"[MOCK ML] Metadata exists but is not a dict. Predictions: {predictions}")
        else:
            # If no metadata field, just log the predictions
            print(f"[MOCK ML] No metadata field found. Predictions: {predictions}")
        
        return enriched
    
    def get_model_info(self) -> dict:
        """Get mock ML model information"""
        return {
            'model_version': self._model_version,
            'prediction_accuracy': self._prediction_accuracy,
            'total_entities_processed': len(self._storage),
            'last_updated': datetime.now().isoformat()
        }
    
    def predict_for_entity(self, entity: T) -> dict:
        """
        Generate ML predictions for an entity without modifying it
        Args:
            entity (T): The entity to generate predictions for
        Returns:
            dict: ML predictions and metadata
        """
        predictions = {}
        
        if hasattr(entity, 'type'):
            if entity.type == 'transaction':
                predictions = {
                    'fraud_score': round(random.uniform(0.0, 1.0), 3),
                    'risk_level': random.choice(['low', 'medium', 'high']),
                    'anomaly_detected': random.random() < 0.1,  # 10% chance
                    'processing_recommendation': random.choice(['approve', 'review', 'reject']),
                    'confidence_score': round(random.uniform(0.7, 0.99), 3)
                }
            elif entity.type == 'alert':
                predictions = {
                    'severity_prediction': random.choice(['low', 'medium', 'high', 'critical']),
                    'escalation_probability': round(random.uniform(0.0, 1.0), 3),
                    'auto_resolution_possible': random.choice([True, False])
                }
            else:
                predictions = {
                    'general_score': round(random.uniform(0.0, 1.0), 3),
                    'classification': random.choice(['type_a', 'type_b', 'type_c'])
                }
        
        # Add ML metadata
        predictions['model_version'] = self._model_version
        predictions['prediction_timestamp'] = datetime.now().isoformat()
        predictions['confidence_interval'] = round(random.uniform(0.05, 0.15), 3)
        
        return predictions
    
    def clear_storage(self):
        """Clear all stored entities (useful for testing)"""
        self._storage.clear()
        self._counter = 1
        print("[MOCK ML] Storage cleared")
    
    def get_storage_size(self) -> int:
        """Get the number of stored entities"""
        return len(self._storage)