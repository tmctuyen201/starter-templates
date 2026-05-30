"""
🌶️ FastAPI + HTMX Template
A minimal full-stack web app with no JavaScript framework required.
"""

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from datetime import datetime

app = FastAPI(title="FastAPI + HTMX", version="1.0.0")
templates = Jinja2Templates(directory="templates")

# ── In-memory store (replace with database in production) ──────────────
todos: list[dict] = [
    {"id": 1, "text": "Learn FastAPI", "done": True, "created": "2024-01-15"},
    {"id": 2, "text": "Build something with HTMX", "done": False, "created": "2024-01-16"},
]
next_id = 3


# ── HTML Routes ────────────────────────────────────────────────────────

@app.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Main page — renders the full HTML layout."""
    return templates.TemplateResponse("index.html", {
        "request": request,
        "todos": todos,
        "total": len(todos),
        "done": sum(1 for t in todos if t["done"]),
    })


# ── HTMX API Endpoints (return HTML fragments) ────────────────────────

@app.post("/todos", response_class=HTMLResponse)
async def create_todo(request: Request, text: str = Form(...)):
    """Add a new todo — returns an HTML fragment for HTMX to insert."""
    global next_id
    todo = {
        "id": next_id,
        "text": text,
        "done": False,
        "created": datetime.now().strftime("%Y-%m-%d"),
    }
    todos.append(todo)
    next_id += 1
    return templates.TemplateResponse("partials/todo_item.html", {
        "request": request, "todo": todo
    })


@app.put("/todos/{todo_id}/toggle", response_class=HTMLResponse)
async def toggle_todo(request: Request, todo_id: int):
    """Toggle todo done status — returns updated item HTML."""
    for todo in todos:
        if todo["id"] == todo_id:
            todo["done"] = not todo["done"]
            return templates.TemplateResponse("partials/todo_item.html", {
                "request": request, "todo": todo
            })
    return HTMLResponse("<li>Todo not found</li>", status_code=404)


@app.delete("/todos/{todo_id}", response_class=HTMLResponse)
async def delete_todo(todo_id: int):
    """Delete a todo — returns empty response (HTMX removes the element)."""
    global todos
    todos = [t for t in todos if t["id"] != todo_id]
    return HTMLResponse("")


@app.get("/todos/stats", response_class=HTMLResponse)
async def todo_stats(request: Request):
    """Return updated stats badge."""
    return templates.TemplateResponse("partials/stats.html", {
        "request": request,
        "total": len(todos),
        "done": sum(1 for t in todos if t["done"]),
    })


# ── JSON API (for non-HTMX clients) ──────────────────────────────────

@app.get("/api/todos")
async def api_list_todos():
    """REST API — returns JSON list of todos."""
    return {"todos": todos, "total": len(todos)}


@app.get("/health")
async def health_check():
    """Health check endpoint."""
    return {"status": "healthy", "timestamp": datetime.now().isoformat()}


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000, reload=True)
