
from schemas import Receipt, Email, Article

# Test Receipt schema
receipt = Receipt(
    store_name="ABC Supermarket",
    date="November 5, 2026",
    items=[
        {
            "name": "Rice",
            "quantity": "2 kg",
            "price": 10
        },
        {
            "name": "Milk",
            "quantity": "1 litre",
            "price": 3
        }
    ],
    total_amount=13,
    currency="USD"
)

print("\nRECEIPT TEST")
print(receipt.model_dump_json(indent=2))


# Test Email schema
email = Email(
    sender="john@example.com",
    recipient="company@example.com",
    subject="Job Application",
    body="I am interested in applying for the Python Developer position."
)

print("\nEMAIL TEST")
print(email.model_dump_json(indent=2))


# Test Article schema
article = Article(
    title="Artificial Intelligence",
    summary="AI is transforming various industries."
)

print("\nARTICLE TEST")
print(article.model_dump_json(indent=2))


print("\nAll schema tests passed!")
