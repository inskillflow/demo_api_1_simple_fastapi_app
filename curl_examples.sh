# ============================================================
#  curl equivalents — same requests as test_api.http
# ============================================================
#
#  Run in any terminal (Windows PowerShell, macOS, Linux)
#  Make sure the server is running first:
#    uvicorn main:app --reload
#
# ============================================================

# --- Root ---
curl http://127.0.0.1:8000/

# --- GET all tasks ---
curl http://127.0.0.1:8000/tasks

# --- GET with filter ---
curl "http://127.0.0.1:8000/tasks?completed=false&priority=high"

# --- GET single task ---
curl http://127.0.0.1:8000/tasks/1

# --- GET not found (404) ---
curl http://127.0.0.1:8000/tasks/999

# --- POST create ---
curl -X POST http://127.0.0.1:8000/tasks \
     -H "Content-Type: application/json" \
     -d '{"title": "New task", "description": "Created via curl", "priority": "high"}'

# --- PUT replace ---
curl -X PUT http://127.0.0.1:8000/tasks/1 \
     -H "Content-Type: application/json" \
     -d '{"title": "Updated title", "description": "Full replace", "completed": true, "priority": "high"}'

# --- PATCH partial update ---
curl -X PATCH http://127.0.0.1:8000/tasks/3 \
     -H "Content-Type: application/json" \
     -d '{"completed": true}'

# --- DELETE ---
curl -X DELETE http://127.0.0.1:8000/tasks/4

# ============================================================
#  Windows PowerShell — use Invoke-RestMethod
# ============================================================

# GET all
Invoke-RestMethod -Uri "http://127.0.0.1:8000/tasks" -Method GET | ConvertTo-Json

# POST create
Invoke-RestMethod -Uri "http://127.0.0.1:8000/tasks" `
  -Method POST `
  -ContentType "application/json" `
  -Body '{"title": "PowerShell task", "priority": "medium"}' | ConvertTo-Json

# PATCH update
Invoke-RestMethod -Uri "http://127.0.0.1:8000/tasks/3" `
  -Method PATCH `
  -ContentType "application/json" `
  -Body '{"completed": true}' | ConvertTo-Json

# DELETE
Invoke-RestMethod -Uri "http://127.0.0.1:8000/tasks/4" -Method DELETE
