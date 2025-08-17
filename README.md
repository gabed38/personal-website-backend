# Personal Website Backend

FastAPI backend for my personal website.  
Currently includes:
- **Contact form endpoint** (`/api/v1/contact`)  
- **Agent workflow placeholder endpoint** (`/api/v1/agent_workflow`)

---

## 🚀 Running Locally

### 1. Create and activate the virtual environment
```bash
python3 -m venv personal-website-backend
# Mac/Linux
source personal-website-backend/bin/activate
# Windows PowerShell
personal-website-backend\Scripts\Activate.ps1
2. Install dependencies
bash
Copy code
pip install -r requirements.txt
3. Run the server
bash
Copy code
uvicorn app.main:app --reload --port 8000
API docs: http://localhost:8000/docs

📝 API Endpoints
1. Contact Form
URL: POST /api/v1/contact/
Description: Submits a contact form. Processes the request asynchronously.

Request Body (JSON):

json
{
  "name": "Alice",
  "email": "alice@example.com",
  "message": "Hello!"
}
Response (202 Accepted):

json
{
  "success": true,
  "message": "Your message has been received and is being processed."
}
Example Fetch Request (React Frontend):

javascript
fetch("http://localhost:8000/api/v1/contact/", {
  method: "POST",
  headers: { "Content-Type": "application/json" },
  body: JSON.stringify({
    name: "Alice",
    email: "alice@example.com",
    message: "Hello!"
  })
})
  .then(res => res.json())
  .then(data => console.log(data));
2. Agent Workflow Placeholder
URL: GET /api/v1/agent_workflow/
Description: Placeholder endpoint for future agent workflow API.

Response (200 OK):

json
{
  "success": false,
  "message": "Agent workflow API not implemented yet."
}
🔧 Notes
The project is structured for future expansion with versioned API modules (/api/v1/...)

Contact form logic is handled in a service layer (app/services/contact_service.py)

CORS middleware is configured for http://localhost:3000 and your production domain