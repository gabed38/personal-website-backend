from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from .api.v1 import contact, agent_workflow

app = FastAPI(
    title="Personal Website Backend",
    description="General purpose API layer for my personal website",
    version="1.0.0"
)

# Allow frontend requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000", "https://yourdomain.com"], 
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include versioned APIs
app.include_router(contact.router, prefix="/api/v1")
app.include_router(agent_workflow.router, prefix="/api/v1")
