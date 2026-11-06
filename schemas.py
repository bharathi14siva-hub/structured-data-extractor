

from pydantic import BaseModel, Field
from typing import List, Optional


# Receipt item schema
class ReceiptItem(BaseModel):
    name: str = Field(description="Name of the purchased item")
    quantity: str = Field(description="Quantity of the item, including its unit")
    price: float = Field(description="Price of the item")


# Receipt schema
class Receipt(BaseModel):
    store_name: str = Field(description="Name of the supermarket or store")
    date: str = Field(description="Date printed on the receipt")
    receipt_number: str = Field(description="Receipt number or Unknown")
    items: List[ReceiptItem] = Field(
        description="List of all purchased items"
    )
    subtotal: Optional[float] = Field(
        description="Subtotal before tax, or null if unavailable"
    )
    tax: Optional[float] = Field(
        description="Tax amount, or null if unavailable"
    )
    total_amount: Optional[float] = Field(
        description="Final amount paid, or null if unavailable"
    )
    currency: str = Field(
        description="Currency code, such as USD, INR or EUR"
    )
    payment_method: str = Field(
        description="Payment method, such as Cash or Card"
    )


# Email schema
class Email(BaseModel):
    sender: str = Field(description="Email sender")
    recipient: str = Field(description="Email recipient")
    date: str = Field(description="Email date or Unknown")
    subject: str = Field(description="Email subject or Unknown")
    body: str = Field(description="Main email content")


# Article schema
class Article(BaseModel):
    title: str = Field(description="Article title")
    author: str = Field(description="Article author or Unknown")
    publication_date: str = Field(
        description="Publication date or Unknown"
    )
    summary: str = Field(description="Summary of the article")


