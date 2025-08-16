from typing import Optional
from pydantic import Field
from repository import PulseEntity


class Alert(PulseEntity):
    """
    Alert model implementing PulseEntity with all fields from alerts.json
    """
    type: str = Field(..., description="Alert type")
    alertId: str = Field(..., description="Unique alert identifier")
    timestamp: str = Field(..., description="Alert timestamp in ISO format")
    severity: str = Field(..., description="Alert severity level")
    predictionId: str = Field(..., description="Associated prediction ID")
    message: str = Field(..., description="Alert message content")
    status: str = Field(..., description="Alert status")
    acknowledgedBy: Optional[str] = Field(None, description="User who acknowledged the alert")
    acknowledgedAt: Optional[str] = Field(None, description="Timestamp when alert was acknowledged")
    resolvedAt: Optional[str] = Field(None, description="Timestamp when alert was resolved") 