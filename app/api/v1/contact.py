from fastapi import APIRouter, BackgroundTasks, status
from ...schemas.contact import ContactRequest
from ...services.contact_service import process_contact_request

router = APIRouter(prefix="/contact", tags=["Contact"])

@router.post("/", status_code=status.HTTP_202_ACCEPTED)
async def submit_contact(request: ContactRequest, background_tasks: BackgroundTasks):
    """
    Accepts a contact request, queues it for async processing,
    and returns the full ContactRequest object for acknowledgment.
    """
    # Queue the async processing
    background_tasks.add_task(process_contact_request, request)
    
    # Return acknowledgment with the submitted object
    return {
        "success": True,
        "message": "Your contact message has been received!",
        "contact": request.dict()
    }
