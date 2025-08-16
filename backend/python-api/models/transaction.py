from typing import Optional
from pydantic import Field
from .repository import PulseEntity


class Merchant(PulseEntity):
    """Merchant information for a transaction"""
    name: str = Field(..., description="Merchant name")


class Customer(PulseEntity):
    """Customer information for a transaction"""
    country: str = Field(..., description="Customer country")


class TransactionMetadata(PulseEntity):
    """Metadata associated with a transaction"""
    swiftMessage: str = Field(..., description="SWIFT message content")
    messageType: str = Field(..., description="Message type (e.g., PACS008)")
    messageSubtype: str = Field(..., description="Message subtype (e.g., 001)")


class Transaction(PulseEntity):
    """
    Transaction model implementing PulseEntity with all fields from transaction.json
    """
    type: str = Field(..., description="Transaction type")
    transactionId: str = Field(..., description="Unique transaction identifier")
    timestamp: str = Field(..., description="Transaction timestamp in ISO format")
    amount: float = Field(..., description="Transaction amount")
    currency: str = Field(..., description="Transaction currency")
    status: str = Field(..., description="Transaction status")
    paymentMethod: str = Field(..., description="Payment method used")
    merchant: Merchant = Field(..., description="Merchant information")
    customer: Customer = Field(..., description="Customer information")
    processingTimeMs: int = Field(..., description="Processing time in milliseconds")
    errorCode: Optional[str] = Field(None, description="Error code if transaction failed")
    metadata: TransactionMetadata = Field(..., description="Transaction metadata")