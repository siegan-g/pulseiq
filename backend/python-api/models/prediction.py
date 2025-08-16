from typing import Optional, Dict, Any
from pydantic import Field
from repository import PulseEntity


class PredictionFeatures(PulseEntity):
    """Features used for prediction"""
    transactionVolume: int = Field(..., description="Transaction volume")
    avgLatency: int = Field(..., description="Average latency")
    errorRate: float = Field(..., description="Error rate")


class Prediction(PulseEntity):
    """
    Prediction model implementing PulseEntity with all fields from predictions.json
    """
    type: str = Field(..., description="Prediction type")
    predictionId: str = Field(..., description="Unique prediction identifier")
    timestamp: str = Field(..., description="Prediction timestamp in ISO format")
    timeWindow: str = Field(..., description="Time window for prediction")
    predictedMetric: str = Field(..., description="Metric being predicted")
    predictedValue: float = Field(..., description="Predicted value")
    confidence: float = Field(..., description="Prediction confidence level")
    threshold: float = Field(..., description="Threshold value for alerting")
    isAlertTriggered: bool = Field(..., description="Whether alert was triggered")
    features: PredictionFeatures = Field(..., description="Features used for prediction") 