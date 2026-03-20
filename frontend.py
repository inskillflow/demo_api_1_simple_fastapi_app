"""
Streamlit frontend for the Task Manager API
--------------------------------------------
Run:
  streamlit run frontend.py

The FastAPI server must be running at http://127.0.0.1:8000
  uvicorn main:app --reload
"""

import streamlit as st
import requests

API_URL = "http://127.0.0.1:8000"

# ---------------------------------------------------------------------------
# Page config
# ---------------------------------------------------------------------------

st.set_page_config(
    page_title="Task Manager",
    page_icon="✓",
    layout="wide",
)

st.title("Task Manager")
st.caption("Streamlit interface connected to the FastAPI backend")

# ---------------------------------------------------------------------------
# Helper — check the server is reachable
# ---------------------------------------------------------------------------

def server_is_up() -> bool:
    try:
        r = requests.get(f"{API_URL}/", timeout=2)
        return r.status_code == 200
    except Exception:
        return False

if not server_is_up():
    st.error(
        "Cannot reach the FastAPI server at http://127.0.0.1:8000  \n"
        "Start it first:  `uvicorn main:app --reload`"
    )
    st.stop()

# ---------------------------------------------------------------------------
# Sidebar — navigation
# ---------------------------------------------------------------------------

st.sidebar.title("Navigation")
page = st.sidebar.radio(
    "Go to",
    ["View all tasks", "Create a task", "Edit a task", "Delete a task"],
)

# ---------------------------------------------------------------------------
# Page 1 — View all tasks
# ---------------------------------------------------------------------------

if page == "View all tasks":
    st.header("All Tasks")

    col1, col2 = st.columns(2)
    with col1:
        filter_completed = st.selectbox(
            "Filter by status",
            ["All", "Completed", "Not completed"],
        )
    with col2:
        filter_priority = st.selectbox(
            "Filter by priority",
            ["All", "high", "medium", "low"],
        )

    params = {}
    if filter_completed == "Completed":
        params["completed"] = "true"
    elif filter_completed == "Not completed":
        params["completed"] = "false"
    if filter_priority != "All":
        params["priority"] = filter_priority

    response = requests.get(f"{API_URL}/tasks", params=params)

    if response.status_code == 200:
        tasks = response.json()

        if not tasks:
            st.info("No tasks match the selected filters.")
        else:
            st.write(f"**{len(tasks)} task(s) found**")

            for task in tasks:
                status_icon = "✅" if task["completed"] else "⬜"
                priority_color = {
                    "high": "🔴",
                    "medium": "🟡",
                    "low": "🟢",
                }.get(task["priority"], "⚪")

                with st.expander(
                    f"{status_icon} #{task['id']} — {task['title']}  {priority_color} {task['priority'].upper()}"
                ):
                    col_a, col_b = st.columns(2)
                    with col_a:
                        st.write(f"**Description:** {task['description'] or '—'}")
                        st.write(f"**Priority:** {task['priority']}")
                    with col_b:
                        st.write(f"**Status:** {'Completed' if task['completed'] else 'In progress'}")
                        st.write(f"**Created:** {task['created_at']}")
                        st.write(f"**ID:** {task['id']}")
    else:
        st.error(f"Error {response.status_code}: {response.text}")

# ---------------------------------------------------------------------------
# Page 2 — Create a task
# ---------------------------------------------------------------------------

elif page == "Create a task":
    st.header("Create a New Task")

    with st.form("create_form", clear_on_submit=True):
        title = st.text_input("Title *", placeholder="e.g. Learn FastAPI")
        description = st.text_area("Description", placeholder="Optional description...")
        priority = st.selectbox("Priority", ["medium", "high", "low"])
        completed = st.checkbox("Mark as completed immediately", value=False)

        submitted = st.form_submit_button("Create Task", type="primary")

    if submitted:
        if not title.strip():
            st.warning("Title is required.")
        else:
            payload = {
                "title": title.strip(),
                "description": description.strip(),
                "priority": priority,
                "completed": completed,
            }
            response = requests.post(f"{API_URL}/tasks", json=payload)

            if response.status_code == 201:
                created = response.json()
                st.success(
                    f"Task created successfully!  \n"
                    f"ID: **{created['id']}** — {created['title']}"
                )
                st.json(created)
            elif response.status_code == 422:
                errors = response.json().get("detail", [])
                for err in errors:
                    field = " → ".join(str(x) for x in err.get("loc", []))
                    st.error(f"Validation error in {field}: {err.get('msg')}")
            else:
                st.error(f"Error {response.status_code}: {response.text}")

# ---------------------------------------------------------------------------
# Page 3 — Edit a task
# ---------------------------------------------------------------------------

elif page == "Edit a task":
    st.header("Edit a Task")

    # Load all tasks to populate the selector
    all_tasks = requests.get(f"{API_URL}/tasks").json()

    if not all_tasks:
        st.info("No tasks available. Create one first.")
    else:
        task_options = {
            f"#{t['id']} — {t['title']}": t["id"] for t in all_tasks
        }
        selected_label = st.selectbox("Select a task to edit", list(task_options.keys()))
        selected_id = task_options[selected_label]

        current = requests.get(f"{API_URL}/tasks/{selected_id}").json()

        st.subheader("Current values")
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"**Title:** {current['title']}")
            st.write(f"**Description:** {current['description'] or '—'}")
        with col2:
            st.write(f"**Priority:** {current['priority']}")
            st.write(f"**Status:** {'Completed' if current['completed'] else 'In progress'}")

        st.divider()
        st.subheader("New values (leave blank to keep current)")

        mode = st.radio(
            "Update mode",
            ["PATCH — update specific fields only", "PUT — replace everything"],
            horizontal=True,
        )

        with st.form("edit_form"):
            new_title = st.text_input(
                "Title",
                value=current["title"] if "PUT" in mode else "",
                placeholder="Leave blank to keep current" if "PATCH" in mode else "",
            )
            new_description = st.text_area(
                "Description",
                value=current["description"] if "PUT" in mode else "",
            )
            new_priority = st.selectbox(
                "Priority",
                ["medium", "high", "low"],
                index=["medium", "high", "low"].index(current["priority"]),
            )
            new_completed = st.checkbox(
                "Completed",
                value=current["completed"],
            )
            save = st.form_submit_button("Save Changes", type="primary")

        if save:
            if "PUT" in mode:
                # PUT — all fields required
                if not new_title.strip():
                    st.warning("Title is required for PUT.")
                else:
                    payload = {
                        "title": new_title.strip(),
                        "description": new_description.strip(),
                        "priority": new_priority,
                        "completed": new_completed,
                    }
                    response = requests.put(f"{API_URL}/tasks/{selected_id}", json=payload)
                    if response.status_code == 200:
                        st.success("Task replaced successfully (PUT).")
                        st.json(response.json())
                    else:
                        st.error(f"Error {response.status_code}: {response.text}")
            else:
                # PATCH — only send changed fields
                payload = {}
                if new_title.strip():
                    payload["title"] = new_title.strip()
                if new_description.strip() != current["description"]:
                    payload["description"] = new_description.strip()
                if new_priority != current["priority"]:
                    payload["priority"] = new_priority
                if new_completed != current["completed"]:
                    payload["completed"] = new_completed

                if not payload:
                    st.info("No changes detected.")
                else:
                    response = requests.patch(
                        f"{API_URL}/tasks/{selected_id}", json=payload
                    )
                    if response.status_code == 200:
                        st.success(
                            f"Task updated successfully (PATCH).  \n"
                            f"Fields changed: {', '.join(payload.keys())}"
                        )
                        st.json(response.json())
                    else:
                        st.error(f"Error {response.status_code}: {response.text}")

# ---------------------------------------------------------------------------
# Page 4 — Delete a task
# ---------------------------------------------------------------------------

elif page == "Delete a task":
    st.header("Delete a Task")

    all_tasks = requests.get(f"{API_URL}/tasks").json()

    if not all_tasks:
        st.info("No tasks available.")
    else:
        task_options = {
            f"#{t['id']} — {t['title']}": t["id"] for t in all_tasks
        }
        selected_label = st.selectbox("Select a task to delete", list(task_options.keys()))
        selected_id = task_options[selected_label]

        current = requests.get(f"{API_URL}/tasks/{selected_id}").json()

        st.warning(
            f"You are about to delete:  \n"
            f"**#{current['id']} — {current['title']}**  \n"
            f"Priority: {current['priority']} | "
            f"Status: {'Completed' if current['completed'] else 'In progress'}"
        )

        col1, col2 = st.columns([1, 4])
        with col1:
            if st.button("Confirm Delete", type="primary"):
                response = requests.delete(f"{API_URL}/tasks/{selected_id}")
                if response.status_code == 204:
                    st.success(f"Task #{selected_id} deleted successfully.")
                    st.rerun()
                elif response.status_code == 404:
                    st.error(f"Task #{selected_id} not found.")
                else:
                    st.error(f"Error {response.status_code}: {response.text}")
        with col2:
            st.write("")
