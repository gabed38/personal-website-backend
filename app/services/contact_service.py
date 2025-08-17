import asyncio
from ..schemas.contact import ContactRequest

async def process_contact_request(request: ContactRequest) -> None:
    """
    Pretend to process the contact request.
    In a real-world app this could send emails, 
    push to Slack, store in a DB, etc.
    """
    # Simulate async work (e.g., email API call)
    await asyncio.sleep(1)
    print(f"[Contact Service] Processed request from {request.name} <{request.email}>")
    print(f"Message: {request.message}")
