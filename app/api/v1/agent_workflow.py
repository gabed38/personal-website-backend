from fastapi import APIRouter, status

router = APIRouter(prefix="/agent_workflow", tags=["Agent Workflow"])

@router.get("/")
async def agent_workflow_placeholder():
    """
    Placeholder for the agent workflow endpoint.
    Returns a simple 'not implemented yet' message.
    """
    return {
        "success": False,
        "message": "Agent workflow API not implemented yet."
    }
