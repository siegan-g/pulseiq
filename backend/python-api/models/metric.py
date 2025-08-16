from typing import Optional
from pydantic import Field
from repository import PulseEntity


class Metric(PulseEntity):
    """
    Metric model implementing PulseEntity with all fields from metrics.json
    """
    type: str = Field(..., description="Metric type")
    metricId: str = Field(..., description="Unique metric identifier")
    timestamp: str = Field(..., description="Metric timestamp in ISO format")
    metricType: str = Field(..., description="Type of metric being measured")
    value: float = Field(..., description="Metric value")
    unit: str = Field(..., description="Unit of measurement")
    node: str = Field(..., description="Node identifier where metric was collected") 