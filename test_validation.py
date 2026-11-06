
from pydantic import ValidationError
from schemas import Receipt


# Test invalid receipt data
try:

    receipt = Receipt(
        store_name="ABC Supermarket",
        date="November 5, 2026",
        items=[
            {
                "name": "Rice",
                "quantity": "2 kg",
                "price": "ten dollars"
            }
        ],
        total_amount=10,
        currency="USD"
    )

    print(receipt.model_dump_json(indent=2))

except ValidationError as e:

    print("\nValidation Error Detected!")
    print(e)
