<a id="top"></a>

# Quiz — API Testing with FastAPI — ANSWER KEY
## Task Manager API — `main.py`

> **For the instructor only.**
> Each answer is hidden inside a `<details>` block. Click the arrow to reveal it.

---

## Table of Contents

| # | Section |
|---|---|
| 1 | [Section A — HTTP Methods](#sa) |
| 2 | [Section B — URLs and Routes](#sb) |
| 3 | [Section C — Request Parameters and Body](#sc) |
| 4 | [Section D — Status Codes](#sd) |
| 5 | [Section E — Order of Operations](#se) |
| 6 | [Section F — Filters and Query Parameters](#sf) |
| 7 | [Section G — Errors — What Went Wrong?](#sg) |
| 8 | [Section H — Scenarios — What Do You Do?](#sh) |
| 9 | [Section I — Read the Response](#si) |
| 10 | [Section J — True or False — Justify](#sj) |

---

<a id="sa"></a>

## Section A — HTTP Methods

**For each action below, write the HTTP method you would use (GET, POST, PUT, PATCH, or DELETE).**

---

**A1.** You want to see the list of all tasks currently in the API.

<details>
<summary>Answer</summary>

**GET**

GET is used to retrieve data. It does not modify anything. `GET /tasks` returns the full list of tasks.

</details>

---

**A2.** You want to add a brand new task to the list.

<details>
<summary>Answer</summary>

**POST**

POST is used to create a new resource. The data for the new task is sent in the request body as JSON.

</details>

---

**A3.** You want to completely replace task number 3 with new data.

<details>
<summary>Answer</summary>

**PUT**

PUT replaces the entire resource. Every field of the existing task is overwritten with the values you send. Fields you omit are reset to their default values.

</details>

---

**A4.** You want to mark task number 2 as completed without changing its title or priority.

<details>
<summary>Answer</summary>

**PATCH**

PATCH is used for partial updates. You send only the field(s) you want to change — here `{"completed": true}` — and all other fields remain untouched.

</details>

---

**A5.** You want to permanently remove task number 5 from the list.

<details>
<summary>Answer</summary>

**DELETE**

DELETE removes the resource identified by the ID in the URL. `DELETE /tasks/5` deletes task 5.

</details>

---

**A6.** You want to check if the server is running and see how many tasks are in memory.

<details>
<summary>Answer</summary>

**GET**

`GET /` (the root endpoint) returns a JSON object with the message `"Task Manager API is running"` and the `total_tasks` count.

</details>

---

**A7.** You want to get the details of task number 1 only — not the full list.

<details>
<summary>Answer</summary>

**GET**

`GET /tasks/1` uses a path parameter to return a single task. The ID is placed directly in the URL, not as a query parameter.

</details>

---

**A8.** You want to change the priority of task number 4 from `"low"` to `"high"` without touching the other fields.

<details>
<summary>Answer</summary>

**PATCH**

You send `PATCH /tasks/4` with body `{"priority": "high"}`. Only the `priority` field is updated; `title`, `description`, and `completed` remain unchanged.

</details>

---

**A9.** What is the difference between PUT and PATCH? Write it in your own words.

<details>
<summary>Answer</summary>

**PUT** replaces the entire task. If you send only one field, all other fields are reset to their default values (e.g., `description` becomes `""`, `priority` becomes `"medium"`, `completed` becomes `false`).

**PATCH** updates only the fields you send. All other fields keep their current values.

Rule of thumb: use PUT when you want to rewrite everything, use PATCH when you want to change one or two fields without affecting the rest.

</details>

---

**A10.** Can you use a GET request to create a new task? Explain why or why not.

<details>
<summary>Answer</summary>

**No.**

GET is a read-only method. By convention (and by HTTP specification), GET must not have side effects — it must not create, modify, or delete data. The API route `POST /tasks` is the only route defined to create a task. Sending a GET to `/tasks` will return the list, never create anything.

</details>

---

<p align="right"><a href="#top">↑ Back to top</a></p>

---

<a id="sb"></a>

## Section B — URLs and Routes

**Write the complete URL for each request described below.**
**The base URL is `http://127.0.0.1:8000`.**

---

**B1.** Get the full list of tasks.

<details>
<summary>Answer</summary>

```
http://127.0.0.1:8000/tasks
```

Method: GET. No body, no query parameters needed for the full list.

</details>

---

**B2.** Get task number 3.

<details>
<summary>Answer</summary>

```
http://127.0.0.1:8000/tasks/3
```

Method: GET. The ID `3` is a path parameter placed directly in the URL.

</details>

---

**B3.** Get task number 7.

<details>
<summary>Answer</summary>

```
http://127.0.0.1:8000/tasks/7
```

Method: GET. This will return a 404 error because the API starts with only 4 tasks (IDs 1–4) and no task with ID 7 has been created.

</details>

---

**B4.** Delete task number 2.

<details>
<summary>Answer</summary>

```
http://127.0.0.1:8000/tasks/2
```

Method: **DELETE**. The ID is a path parameter. No body is needed.

</details>

---

**B5.** Update only the `completed` field of task number 5.

<details>
<summary>Answer</summary>

```
http://127.0.0.1:8000/tasks/5
```

Method: **PATCH**. Body: `{"completed": true}` (or `false`). The word "only" tells you to use PATCH, not PUT.

</details>

---

**B6.** Completely replace task number 1 with new data.

<details>
<summary>Answer</summary>

```
http://127.0.0.1:8000/tasks/1
```

Method: **PUT**. The body must contain all fields including the required `title`. Missing optional fields will be reset to their defaults.

</details>

---

**B7.** Check if the server is running (root endpoint).

<details>
<summary>Answer</summary>

```
http://127.0.0.1:8000/
```

or simply:

```
http://127.0.0.1:8000
```

Method: GET. Returns `{"message": "Task Manager API is running", "docs": "...", "total_tasks": N}`.

</details>

---

**B8.** Get only the tasks that have `priority = "high"`.

<details>
<summary>Answer</summary>

```
http://127.0.0.1:8000/tasks?priority=high
```

Method: GET. `priority` is a query parameter supported by the `GET /tasks` route.

</details>

---

**B9.** Get only the tasks that are not completed.

<details>
<summary>Answer</summary>

```
http://127.0.0.1:8000/tasks?completed=false
```

Method: GET. `completed` is a query parameter. The value `false` is lowercase.

</details>

---

**B10.** Get only the tasks that are not completed AND have priority `"medium"`.

<details>
<summary>Answer</summary>

```
http://127.0.0.1:8000/tasks?completed=false&priority=medium
```

Method: GET. Two query parameters are combined with `&`. Both filters are applied simultaneously.

</details>

---

**B11.** A student writes this URL to get task 4:

```
http://127.0.0.1:8000/task/4
```

What is wrong with this URL? Write the correct version.

<details>
<summary>Answer</summary>

**Problem:** The route is `/task/4` (singular) but the correct route is `/tasks/4` (plural). FastAPI will return a 404 because no route named `/task/{id}` exists.

**Correct URL:**
```
http://127.0.0.1:8000/tasks/4
```

</details>

---

**B12.** A student writes this URL to create a new task:

```
http://127.0.0.1:8000/tasks/
```

They use the POST method and send a valid JSON body. Will this work? Explain.

<details>
<summary>Answer</summary>

**Yes, it will work** in most cases.

FastAPI (and most web frameworks) treat a trailing slash as equivalent to no trailing slash on many routes. The POST request will be matched to `POST /tasks` and the task will be created normally.

However, it is better practice to write the URL without the trailing slash: `http://127.0.0.1:8000/tasks`.

</details>

---

<p align="right"><a href="#top">↑ Back to top</a></p>

---

<a id="sc"></a>

## Section C — Request Parameters and Body

---

**C1.** You want to create a new task with the following information:
- Title: `"Prepare the presentation"`
- Priority: `"high"`

Write the JSON body you would send in the POST request.

<details>
<summary>Answer</summary>

```json
{
  "title": "Prepare the presentation",
  "priority": "high"
}
```

`description` and `completed` can be omitted — they have default values (`""` and `false`).

</details>

---

**C2.** You want to create a new task with only the title `"Read chapter 5"` and use default values for everything else.

Write the JSON body.

<details>
<summary>Answer</summary>

```json
{
  "title": "Read chapter 5"
}
```

`title` is the only required field. The API will assign:
- `description`: `""`
- `completed`: `false`
- `priority`: `"medium"`

</details>

---

**C3.** You send a POST request with this body:

```json
{
  "description": "Some details here",
  "priority": "low"
}
```

What happens? What status code do you get and why?

<details>
<summary>Answer</summary>

**Status code: 422 Unprocessable Entity**

The `title` field is required by the `TaskCreate` Pydantic model (`title: str` with no default value). Since it is missing from the body, Pydantic rejects the request before it even reaches the route logic.

The response body will contain a `detail` array indicating `"Field required"` for the `title` field.

</details>

---

**C4.** You want to use PATCH to mark task 2 as completed. Write the JSON body you would send.

<details>
<summary>Answer</summary>

```json
{
  "completed": true
}
```

Only the field to change is included. All other fields (`title`, `description`, `priority`) remain unchanged.

</details>

---

**C5.** You want to use PATCH to change the title of task 3 to `"Write integration tests"`. Write the JSON body.

<details>
<summary>Answer</summary>

```json
{
  "title": "Write integration tests"
}
```

Only `title` is sent. The fields `description`, `completed`, and `priority` keep their current values.

</details>

---

**C6.** You want to use PUT to completely replace task 1. The new values should be:
- Title: `"Advanced FastAPI"`
- Description: `"Learn middleware and dependencies"`
- Completed: false
- Priority: `"high"`

Write the JSON body.

<details>
<summary>Answer</summary>

```json
{
  "title": "Advanced FastAPI",
  "description": "Learn middleware and dependencies",
  "completed": false,
  "priority": "high"
}
```

With PUT, it is good practice to include all fields explicitly, even those with default values, to avoid unintended resets.

</details>

---

**C7.** You use PUT on task 1 but send only this body:

```json
{
  "title": "Advanced FastAPI"
}
```

What happens to the `description`, `completed`, and `priority` fields? Explain.

<details>
<summary>Answer</summary>

PUT uses the `TaskCreate` model, which has default values for all optional fields:
- `description` → reset to `""`
- `completed` → reset to `false`
- `priority` → reset to `"medium"`

Even if task 1 previously had `description: "Read the official docs"` and `priority: "high"`, those values are permanently lost. This is the fundamental difference between PUT and PATCH.

</details>

---

**C8.** For a DELETE request on task 4, what body do you need to send?

<details>
<summary>Answer</summary>

**No body.** DELETE requests do not require a body. The task ID is passed as a path parameter in the URL: `DELETE /tasks/4`.

</details>

---

**C9.** For a GET request on `/tasks`, what body do you need to send?

<details>
<summary>Answer</summary>

**No body.** GET requests never have a body. Filters are passed as query parameters in the URL itself (e.g., `?completed=false&priority=high`).

</details>

---

**C10.** You want to send a POST request but you forget to set the `Content-Type` header to `application/json`. What might happen?

<details>
<summary>Answer</summary>

The server may not be able to parse the request body correctly. FastAPI expects the body to be JSON (`application/json`). If the `Content-Type` header is missing or incorrect, the server may reject the body and return a **422** error because it cannot read the fields.

Most HTTP tools (Postman, REST Client, curl with `-H "Content-Type: application/json"`) set this header automatically when you provide a JSON body, but it is important to be aware of.

</details>

---

<p align="right"><a href="#top">↑ Back to top</a></p>

---

<a id="sd"></a>

## Section D — Status Codes

**For each situation below, write the HTTP status code the API should return.**

---

**D1.** A GET request to `/tasks` returns all 4 tasks successfully.

<details>
<summary>Answer</summary>

**200 OK**

The request succeeded. The response body contains the list of tasks.

</details>

---

**D2.** A POST request to `/tasks` with a valid body successfully creates a new task.

<details>
<summary>Answer</summary>

**201 Created**

The `@app.post("/tasks", status_code=201)` decorator explicitly sets the status code to 201 for successful creation.

</details>

---

**D3.** A DELETE request to `/tasks/4` successfully deletes task 4.

<details>
<summary>Answer</summary>

**204 No Content**

The `@app.delete("/tasks/{task_id}", status_code=204)` decorator sets 204. The response body is empty.

</details>

---

**D4.** A GET request to `/tasks/99` — task 99 does not exist.

<details>
<summary>Answer</summary>

**404 Not Found**

The route handler checks `if task_id not in tasks_db` and raises `HTTPException(status_code=404)`.

</details>

---

**D5.** A POST request to `/tasks` with an empty body `{}`.

<details>
<summary>Answer</summary>

**422 Unprocessable Entity**

The `title` field is required. Sending an empty body `{}` means `title` is missing, so Pydantic validation fails immediately.

</details>

---

**D6.** A PATCH request to `/tasks/3` with `{"completed": true}` — task 3 exists.

<details>
<summary>Answer</summary>

**200 OK**

The task exists and the body is valid. The update succeeds and the full updated task is returned.

</details>

---

**D7.** A PUT request to `/tasks/50` — task 50 does not exist.

<details>
<summary>Answer</summary>

**404 Not Found**

The PUT handler also checks `if task_id not in tasks_db` and raises a 404. PUT does not create new resources in this API — it can only replace an existing one.

</details>

---

**D8.** A DELETE request to `/tasks/4` — but task 4 was already deleted earlier.

<details>
<summary>Answer</summary>

**404 Not Found**

Once a task is deleted from `tasks_db`, it no longer exists. Any subsequent request targeting that ID (GET, PUT, PATCH, or DELETE) will return 404.

</details>

---

**D9.** A POST request with `{"title": "Test", "completed": "yes"}` — `completed` must be a boolean.

<details>
<summary>Answer</summary>

**422 Unprocessable Entity**

The `completed` field is declared as `bool` in the `TaskCreate` model. The string `"yes"` is not a valid boolean. Pydantic rejects the request and returns a 422 with a `detail` message explaining the type error.

Note: `"true"` and `"false"` (strings) may be coerced by Pydantic in some configurations, but `"yes"` is never a valid boolean.

</details>

---

**D10.** In your own words, explain the difference between a 404 error and a 422 error.

<details>
<summary>Answer</summary>

**404 Not Found:** The resource you are looking for does not exist. The URL and method are valid, but the specific item (identified by its ID) is not in the database.

**422 Unprocessable Entity:** The server understood the request but the data you sent is invalid. For example, a required field is missing, a field has the wrong type, or the JSON is malformed. The URL and method are correct, but the body or parameters are wrong.

</details>

---

**D11.** You receive a 204 response after a DELETE. The response body is completely empty. Is this an error? Explain.

<details>
<summary>Answer</summary>

**No, this is normal and expected.**

204 means "No Content" — the operation succeeded, but there is nothing to return. Deleting a task removes it, so there is no resource to include in the response body. An empty body after 204 is correct behavior, not an error.

</details>

---

**D12.** Write the name and meaning of these three status codes:

<details>
<summary>Answer</summary>

| Code | Name | Meaning |
|---|---|---|
| 200 | OK | The request succeeded. The response contains the requested data. |
| 201 | Created | A new resource was successfully created. The response contains the new resource. |
| 204 | No Content | The request succeeded but there is no data to return (used after DELETE). |
| 404 | Not Found | The resource identified by the URL does not exist. |
| 422 | Unprocessable Entity | The data sent is invalid (wrong type, missing required field, etc.). |

</details>

---

<p align="right"><a href="#top">↑ Back to top</a></p>

---

<a id="se"></a>

## Section E — Order of Operations

---

**E1.** You want to test GET `/tasks/5`. The API starts with 4 sample tasks (IDs 1 to 4).
Can you run this test immediately? If not, what must you do first?

<details>
<summary>Answer</summary>

**No, you cannot run this test immediately.**

Task 5 does not exist at startup. You will get a 404. To test `GET /tasks/5`, you must first create a task using `POST /tasks`. The API auto-increments IDs starting from 5, so the first created task will have ID 5. Only then can you run `GET /tasks/5` and expect a 200 response.

</details>

---

**E2.** You run DELETE `/tasks/3` and get a 204 response.
You then run GET `/tasks/3`. What status code do you get? What does the response body contain?

<details>
<summary>Answer</summary>

**Status code: 404 Not Found**

Response body:
```json
{
  "detail": "Task with ID 3 not found"
}
```

The DELETE removed task 3 from `tasks_db`. It no longer exists, so any request targeting task 3 will now return 404.

</details>

---

**E3.** Put these 4 actions in the correct logical order to properly test the create feature:

- Run GET `/tasks` and count the total number of tasks
- Run POST `/tasks` with a valid body
- Run GET `/tasks/5` to verify the new task was created with the right data
- Run GET `/tasks` again and verify the count increased by 1

Write the correct order (1, 2, 3, 4):

<details>
<summary>Answer</summary>

```
Step 1: Run GET /tasks and count the total number of tasks  ← baseline before the test
Step 2: Run POST /tasks with a valid body                   ← perform the action
Step 3: Run GET /tasks/5 to verify the new task was created ← verify the data is correct
Step 4: Run GET /tasks again and verify the count increased  ← verify the side effect
```

The key principle: always establish a baseline (Step 1) before the action, then verify both the direct result (Step 3) and the broader effect (Step 4).

</details>

---

**E4.** You want to test that PATCH only changes the fields you send. Describe the steps you would follow, in order, to properly verify this.

<details>
<summary>Answer</summary>

```
Step 1: GET /tasks/3  → record all current field values (title, description, completed, priority)
Step 2: PATCH /tasks/3  with body {"priority": "high"}  → send only the one field to change
Step 3: GET /tasks/3  → compare the response to Step 1:
         - priority should now be "high"
         - title, description, completed must be identical to Step 1
```

If any field other than `priority` changed, the PATCH implementation is broken.

</details>

---

**E5.** You want to test that PUT resets fields you do not send to their default values. Describe the steps in order.

<details>
<summary>Answer</summary>

```
Step 1: GET /tasks/1  → record all current values, especially description, priority, completed
Step 2: PUT /tasks/1  with body {"title": "New title only"}  → send only title
Step 3: GET /tasks/1  → verify:
         - title is "New title only"
         - description is now ""  (reset to default)
         - completed is now false  (reset to default)
         - priority is now "medium"  (reset to default)
```

If the other fields still have their old values, the PUT is behaving like PATCH — that is a bug.

</details>

---

**E6.** A student runs these requests in this order:

1. `DELETE /tasks/4` → 204
2. `GET /tasks/4` → what status code?
3. `DELETE /tasks/4` → what status code?

Fill in the status codes for steps 2 and 3 and explain each one.

<details>
<summary>Answer</summary>

**Step 2: 404 Not Found**
Task 4 was deleted in step 1. It no longer exists in `tasks_db`, so the GET returns 404.

**Step 3: 404 Not Found**
Trying to delete a resource that does not exist also returns 404. The DELETE handler checks `if task_id not in tasks_db` and raises the exception before attempting to delete anything.

</details>

---

**E7.** You want to verify that your API has exactly 4 tasks at startup (before any changes).
Write the single request you would send to confirm this.

<details>
<summary>Answer</summary>

```
Method: GET
URL:    http://127.0.0.1:8000/
```

The root endpoint returns `"total_tasks": 4` when the API starts fresh. Alternatively, `GET /tasks` returns a JSON array of 4 tasks — you can count the objects in the array.

</details>

---

**E8.** After running several tests (creating, deleting, updating tasks), you want to reset the API back to its original 4 tasks. How do you do this?

<details>
<summary>Answer</summary>

**Restart the FastAPI server.**

The data is stored in memory only (`tasks_db` is a Python dictionary). It is not saved to a database or file. When the server restarts, `tasks_db` is re-initialized with the 4 sample tasks hardcoded in `main.py`.

Command: stop the server (`Ctrl+C`) and run `uvicorn main:app --reload` again.

</details>

---

<p align="right"><a href="#top">↑ Back to top</a></p>

---

<a id="sf"></a>

## Section F — Filters and Query Parameters

---

**F1.** What symbol separates the base URL from the query parameters?

<details>
<summary>Answer</summary>

**`?` (question mark)**

Example: `http://127.0.0.1:8000/tasks?completed=false`
Everything before `?` is the URL path. Everything after is the query string.

</details>

---

**F2.** What symbol separates two query parameters from each other in the same URL?

<details>
<summary>Answer</summary>

**`&` (ampersand)**

Example: `http://127.0.0.1:8000/tasks?completed=false&priority=high`

</details>

---

**F3.** Write the full URL to get only tasks where `completed` is `true`.

<details>
<summary>Answer</summary>

```
http://127.0.0.1:8000/tasks?completed=true
```

Note: use lowercase `true`, not `True` (Python boolean notation) or `"true"` (string with quotes).

</details>

---

**F4.** Write the full URL to get only tasks where `priority` is `"low"`.

<details>
<summary>Answer</summary>

```
http://127.0.0.1:8000/tasks?priority=low
```

</details>

---

**F5.** Write the full URL to get tasks that are NOT completed AND have priority `"high"`.

<details>
<summary>Answer</summary>

```
http://127.0.0.1:8000/tasks?completed=false&priority=high
```

Both filters are active simultaneously. Only tasks matching both conditions are returned.

</details>

---

**F6.** You run GET `/tasks?priority=high`. The API returns 2 tasks.
You then run GET `/tasks?priority=high&completed=true`. The API returns 1 task.
What does this tell you about the two high-priority tasks?

<details>
<summary>Answer</summary>

Among the 2 high-priority tasks, exactly 1 is completed and 1 is not completed.

From the sample data in `main.py`:
- Task 1 (`"Learn FastAPI"`) — priority: high, completed: false
- Task 2 (`"Build a REST API"`) — priority: high, completed: true

So the 2 high-priority tasks are tasks 1 and 2. Task 2 is the one that is completed.

</details>

---

**F7.** What is the difference between a query parameter and a path parameter? Give one example of each from the Task Manager API.

<details>
<summary>Answer</summary>

**Path parameter:** Part of the URL path itself, used to identify a specific resource.
- Syntax: `/tasks/{task_id}`
- Example: `GET /tasks/3` — `3` is the path parameter identifying task 3.

**Query parameter:** Appended to the URL after `?`, used to filter or customize the result.
- Syntax: `?key=value`
- Example: `GET /tasks?completed=false` — `completed=false` is a query parameter filtering by status.

Key difference: path parameters are mandatory and identify the resource. Query parameters are optional and modify how the resource is returned.

</details>

---

**F8.** A student writes this URL:

```
http://127.0.0.1:8000/tasks?completed=True
```

Note the capital `T` in `True`. Will this filter work correctly? Explain.

<details>
<summary>Answer</summary>

**It depends on the FastAPI/Pydantic version, but generally it may fail or behave unexpectedly.**

FastAPI parses query parameters as strings first, then attempts to coerce them to the declared type (`bool`). Pydantic accepts `"true"` (lowercase) and `"1"` as `True`, but may reject `"True"` (capital T) in strict mode and return a 422 error.

The safe and correct value is lowercase: `?completed=true` or `?completed=false`.

</details>

---

**F9.** You run GET `/tasks` with no filters. You get 4 tasks.
You then run GET `/tasks?completed=true`. You get 1 task.
You then run GET `/tasks?completed=false`. How many tasks should you get?

<details>
<summary>Answer</summary>

**3 tasks.**

Total tasks = 4. Completed tasks = 1. Not-completed tasks = 4 - 1 = 3.

From the sample data: tasks 1, 3, and 4 have `completed: false`. Only task 2 has `completed: true`.

</details>

---

**F10.** Is it possible to filter tasks by their title using the current API?
For example: GET `/tasks?title=FastAPI`
Explain why or why not based on what you know about the code.

<details>
<summary>Answer</summary>

**No, it is not possible.**

The `get_tasks` function in `main.py` accepts only two optional parameters:
```python
def get_tasks(completed: Optional[bool] = None, priority: Optional[str] = None):
```

`title` is not declared as a query parameter. If you add `?title=FastAPI` to the URL, FastAPI will either ignore it or return a validation error, but it will not filter by title.

To add this feature, you would need to add `title: Optional[str] = None` as a parameter and add a filtering condition in the function body.

</details>

---

<p align="right"><a href="#top">↑ Back to top</a></p>

---

<a id="sg"></a>

## Section G — Errors — What Went Wrong?

---

**G1.** A student wants to get all tasks. They send:

```
Method: POST
URL: http://127.0.0.1:8000/tasks
Body: (empty)
```

They get a 422 error. What went wrong? What is the correct request?

<details>
<summary>Answer</summary>

**Problem:** Two mistakes at once.
1. The method is POST instead of GET. POST on `/tasks` means "create a new task", not "list tasks".
2. Since POST was used, FastAPI expects a valid JSON body with a `title` field. An empty body triggers 422.

**Correct request:**
```
Method: GET
URL: http://127.0.0.1:8000/tasks
Body: (none)
```

</details>

---

**G2.** A student wants to get task number 2. They send:

```
Method: GET
URL: http://127.0.0.1:8000/tasks?id=2
```

They get all 4 tasks, not just task 2. What went wrong? Write the correct URL.

<details>
<summary>Answer</summary>

**Problem:** The student used `?id=2` as a query parameter. But `id` is not a supported query parameter for `GET /tasks`. The API only accepts `completed` and `priority` as filters. The unknown parameter `?id=2` is simply ignored, so all tasks are returned.

To get a specific task by ID, the ID must be a **path parameter**, not a query parameter.

**Correct URL:**
```
http://127.0.0.1:8000/tasks/2
```

</details>

---

**G3.** A student wants to create a new task. They send:

```json
{
  "title": "My new task",
  "completed": "false",
  "priority": "high"
}
```

They get a 422 error. What is the problem?

<details>
<summary>Answer</summary>

**Problem:** `"completed": "false"` — `completed` is declared as `bool` in the `TaskCreate` model. The value `"false"` is a string, not a boolean. Pydantic cannot convert it and raises a validation error.

**Correct body:**
```json
{
  "title": "My new task",
  "completed": false,
  "priority": "high"
}
```

Note: `false` without quotes is a JSON boolean. `"false"` with quotes is a JSON string.

</details>

---

**G4.** A student wants to delete task 3. They send:

```
Method: DELETE
URL: http://127.0.0.1:8000/tasks
Body: {"id": 3}
```

They get a 405 error (Method Not Allowed). What went wrong?

<details>
<summary>Answer</summary>

**Problem:** The route `DELETE /tasks` does not exist. The DELETE method is only defined for `/tasks/{task_id}` (with an ID in the path). The route `/tasks` only supports GET and POST.

The ID must be in the URL, not in the body.

**Correct request:**
```
Method: DELETE
URL: http://127.0.0.1:8000/tasks/3
Body: (none)
```

</details>

---

**G5.** A student wants to mark task 1 as completed. They use PUT with body `{"completed": true}`.

Task 1 now has `title: ""`, `description: ""`, `priority: "medium"`, `completed: true`. What went wrong?

<details>
<summary>Answer</summary>

**Problem:** PUT uses the `TaskCreate` model, which assigns default values to all optional fields. By sending only `{"completed": true}`, the student omitted `title`, `description`, and `priority`. Since `title` has no default (it is required), this should actually have returned 422 — unless the student also sent `"title": ""` implicitly.

The real conceptual error: **PUT replaces the entire task**. Every field not sent in the body is reset to its default value. The previous values of `title`, `description`, and `priority` are permanently lost.

**Correct method: PATCH**
```json
{ "completed": true }
```
PATCH only modifies the fields you send, leaving everything else unchanged.

</details>

---

**G6.** A student sends PATCH `/tasks/99` with `{"completed": true}` and gets a 404. Is this a bug?

<details>
<summary>Answer</summary>

**No, this is correct and expected behavior.**

Before updating, the PATCH handler verifies that the task exists:
```python
if task_id not in tasks_db:
    raise HTTPException(status_code=404, ...)
```

Task 99 was never created, so the 404 is the right response. You cannot update a resource that does not exist.

</details>

---

**G7.** A student sends POST with `title` and `priority` in the Params tab instead of the Body tab.

<details>
<summary>Answer</summary>

**Problem:** The Params tab in Postman adds values as URL query parameters (e.g., `/tasks?title=My Task&priority=high`). But the `POST /tasks` route reads its data from the **request body**, not from the URL query string. FastAPI sees an empty body and returns 422 because `title` is required in the body.

Query parameters and request body are completely separate concepts. POST data must go in the **Body tab** as raw JSON.

</details>

---

**G8.** A student sends a correct POST request and gets `curl: (7) Failed to connect to 127.0.0.1 port 8000: Connection refused`.

<details>
<summary>Answer</summary>

**Problem:** The FastAPI server is not running. The error "Connection refused" means no process is listening on port 8000. The JSON body and headers are irrelevant — the connection cannot even be established.

**Fix:** Open a terminal in the `mini_fastapi` folder and run:
```bash
uvicorn main:app --reload
```
Wait until you see `Uvicorn running on http://127.0.0.1:8000`, then retry the request.

</details>

---

<p align="right"><a href="#top">↑ Back to top</a></p>

---

<a id="sh"></a>

## Section H — Scenarios — What Do You Do?

---

**H1.** You want to verify that the API is running and check how many tasks are currently in memory.

<details>
<summary>Answer</summary>

```
Method:              GET
URL:                 http://127.0.0.1:8000/
Body:                none
Expected status:     200
What to look for:    "total_tasks" value in the response body
```

Expected response:
```json
{
  "message": "Task Manager API is running",
  "docs": "http://127.0.0.1:8000/docs",
  "total_tasks": 4
}
```

</details>

---

**H2.** You want to add the task "Learn Docker" with description, priority high, completed false.

<details>
<summary>Answer</summary>

```
Method:              POST
URL:                 http://127.0.0.1:8000/tasks
Body:
{
  "title": "Learn Docker",
  "description": "Study containers and images",
  "priority": "high",
  "completed": false
}

Expected status:     201
What to look for:    Response contains "id": 5, "title": "Learn Docker", and a "created_at" timestamp
```

</details>

---

**H3.** After H2, verify the task was saved with ID 5.

<details>
<summary>Answer</summary>

```
Method:              GET
URL:                 http://127.0.0.1:8000/tasks/5
Body:                none
Expected status:     200
What to look for:    "id": 5, "title": "Learn Docker", "priority": "high"
```

</details>

---

**H4.** Mark task 3 as completed without changing anything else.

<details>
<summary>Answer</summary>

```
Method:              PATCH
URL:                 http://127.0.0.1:8000/tasks/3
Body:
{
  "completed": true
}

Expected status:     200
```

Verify that `title`, `description`, and `priority` are unchanged compared to the original task 3.

</details>

---

**H5.** Completely replace task 2 with new data.

<details>
<summary>Answer</summary>

```
Method:              PUT
URL:                 http://127.0.0.1:8000/tasks/2
Body:
{
  "title": "Build a production API",
  "description": "Add authentication and database",
  "completed": true,
  "priority": "high"
}

Expected status:     200
```

</details>

---

**H6.** After H5, confirm task 2's title is now "Build a production API".

<details>
<summary>Answer</summary>

```
Method:              GET
URL:                 http://127.0.0.1:8000/tasks/2
Body:                none
Expected status:     200
What to look for:    "title": "Build a production API"
```

</details>

---

**H7.** Delete task 4 and confirm it no longer exists.

<details>
<summary>Answer</summary>

```
Request 1 — Delete:
  Method:             DELETE
  URL:                http://127.0.0.1:8000/tasks/4
  Expected status:    204
  Expected body:      (empty)

Request 2 — Confirm deletion:
  Method:             GET
  URL:                http://127.0.0.1:8000/tasks/4
  Expected status:    404
  Expected body:      {"detail": "Task with ID 4 not found"}
```

</details>

---

**H8.** Find all tasks that are not completed and have priority "high".

<details>
<summary>Answer</summary>

```
Method:              GET
URL:                 http://127.0.0.1:8000/tasks?completed=false&priority=high
Body:                none
Expected status:     200
Expected response:   A JSON array. From sample data, task 1 ("Learn FastAPI") matches both filters.
```

</details>

---

**H9.** Test what happens when you request a task that does not exist.

<details>
<summary>Answer</summary>

```
Method:              GET
URL:                 http://127.0.0.1:8000/tasks/999
Expected status:     404
Expected body:
{
  "detail": "Task with ID 999 not found"
}
```

</details>

---

**H10.** Full lifecycle: create, read, update, delete, confirm deletion.

<details>
<summary>Answer</summary>

```
Step 1 — Create:
  Method:   POST
  URL:      http://127.0.0.1:8000/tasks
  Body:     {"title": "Lifecycle test task"}
  Status:   201  →  note the assigned id (e.g. 5)

Step 2 — Read:
  Method:   GET
  URL:      http://127.0.0.1:8000/tasks/5
  Status:   200  →  verify title = "Lifecycle test task"

Step 3 — Update (priority to "low"):
  Method:   PATCH
  URL:      http://127.0.0.1:8000/tasks/5
  Body:     {"priority": "low"}
  Status:   200  →  verify priority = "low", other fields unchanged

Step 4 — Delete:
  Method:   DELETE
  URL:      http://127.0.0.1:8000/tasks/5
  Status:   204  →  empty body

Step 5 — Confirm deletion:
  Method:   GET
  URL:      http://127.0.0.1:8000/tasks/5
  Status:   404  →  {"detail": "Task with ID 5 not found"}
```

</details>

---

<p align="right"><a href="#top">↑ Back to top</a></p>

---

<a id="si"></a>

## Section I — Read the Response

---

**I1.** Response: `{"message": "Task Manager API is running", "docs": "...", "total_tasks": 6}`

a) What method and URL did you use?

<details>
<summary>Answer</summary>

**GET** `http://127.0.0.1:8000/`

This is the root endpoint. It returns the API status message and the current task count.

</details>

b) What does `total_tasks: 6` tell you?

<details>
<summary>Answer</summary>

There are currently 6 tasks stored in memory. The API started with 4, so 2 tasks were created (via POST) before this request was made.

</details>

---

**I2.** Response (status 201): `{"id": 5, "title": "Learn Docker", "description": "", "completed": false, "priority": "medium", "created_at": "2026-03-30 14:22:05"}`

a) What method did you use?

<details>
<summary>Answer</summary>

**POST** — status 201 is only returned by the `POST /tasks` route, which creates a new resource.

</details>

b) You did not send `description`, `completed`, or `priority`. Why do they appear?

<details>
<summary>Answer</summary>

The `TaskCreate` Pydantic model defines default values for these fields:
- `description: str = ""`
- `completed: bool = False`
- `priority: str = "medium"`

When they are not provided in the request body, the defaults are used automatically.

</details>

c) You did not send `id` or `created_at`. Why do they appear?

<details>
<summary>Answer</summary>

`id` and `created_at` are **generated by the server**, not provided by the client.
- `id` is assigned from the `next_id` auto-increment counter in `main.py`.
- `created_at` is set by calling `_now()` (which returns the current date and time as a string) at the moment of creation.

These fields should never be sent by the client — they are server-side metadata.

</details>

---

**I3.** Response (status 404): `{"detail": "Task with ID 99 not found"}`

a) Two methods and URLs that could produce this response:

<details>
<summary>Answer</summary>

Any of the following would return 404 for a non-existent task:
- `GET /tasks/99`
- `PUT /tasks/99` (with any valid body)
- `PATCH /tasks/99` (with any valid body)
- `DELETE /tasks/99`

All four route handlers check `if task_id not in tasks_db` and raise the same 404 exception.

</details>

b) Is this a bug or expected behavior?

<details>
<summary>Answer</summary>

**Expected behavior.** The API is designed to return 404 when a requested resource does not exist. This is the correct HTTP behavior as defined by the REST standard. Task 99 was never created, so the 404 is the correct and intentional response.

</details>

---

**I4.** Status 204, empty body.

a) What method did you use?

<details>
<summary>Answer</summary>

**DELETE** — the `DELETE /tasks/{id}` route has `status_code=204` set in its decorator and returns nothing.

</details>

b) Is an empty body an error here?

<details>
<summary>Answer</summary>

**No.** 204 ("No Content") means the operation succeeded and there is nothing to return. After deleting a task, the task no longer exists, so there is no data to include in the response. An empty body after 204 is the correct and expected behavior defined by the HTTP specification.

</details>

---

**I5.** Status 422 with `"loc": ["body", "title"], "msg": "Field required"`

a) What does `"loc": ["body", "title"]` tell you?

<details>
<summary>Answer</summary>

It tells you exactly where the error is located:
- `"body"` → the problem is in the request body (not the URL or headers)
- `"title"` → the specific field that is missing or invalid is `title`

</details>

b) What was wrong with your request?

<details>
<summary>Answer</summary>

The POST request body did not include the `title` field, which is required by the `TaskCreate` model (`title: str` with no default value).

</details>

c) Minimum JSON body to fix this:

<details>
<summary>Answer</summary>

```json
{
  "title": "Any title here"
}
```

`title` is the only required field. All other fields have defaults.

</details>

---

**I6.** Response to `GET /tasks?completed=false` returns tasks 1, 3, 4.

a) How many tasks are NOT completed?

<details>
<summary>Answer</summary>

**3** (tasks 1, 3, and 4).

</details>

b) Task 2 is missing. What does that tell you?

<details>
<summary>Answer</summary>

Task 2 (`"Build a REST API"`) has `completed: true`. Since the filter `?completed=false` excludes completed tasks, task 2 does not appear in this response.

</details>

c) The response starts with `[` and ends with `]`. What does that mean?

<details>
<summary>Answer</summary>

`[...]` is a **JSON array** (list). It means the response contains multiple items (zero or more objects). Each `{...}` inside the array is a single task object. This is different from a single object response like `{...}` which contains exactly one resource.

</details>

---

<p align="right"><a href="#top">↑ Back to top</a></p>

---

<a id="sj"></a>

## Section J — True or False — Justify

---

**J1.** A GET request can have a JSON body.

<details>
<summary>Answer</summary>

**TRUE** (technically) — but **should never be used in practice.**

The HTTP specification does not formally prohibit a body on GET requests, but it is strongly discouraged. REST conventions and most API frameworks (including FastAPI) do not support or read a body on GET requests. Data must be passed as query parameters instead.

</details>

---

**J2.** After a successful DELETE, the response body should be empty.

<details>
<summary>Answer</summary>

**TRUE.**

The `DELETE /tasks/{id}` route returns status 204 ("No Content") with no body. This is the correct and expected behavior after a successful deletion. There is no resource left to return.

</details>

---

**J3.** If you send PATCH with an empty body `{}`, all fields are reset to defaults.

<details>
<summary>Answer</summary>

**FALSE.**

PATCH with `{}` sends no fields. The `TaskUpdate` model has all fields as `Optional[...] = None`. With `exclude_none=True`, the empty body results in zero updates — no fields are changed. The task remains exactly as it was.

Reset to defaults would only happen with PUT.

</details>

---

**J4.** To use a query parameter filter, you must put it in the JSON body.

<details>
<summary>Answer</summary>

**FALSE.**

Query parameters are part of the **URL**, not the body. They are placed after the `?` character in the URL:
```
GET /tasks?completed=false&priority=high
```
The request body is empty for GET requests.

</details>

---

**J5.** A 404 error means the server crashed.

<details>
<summary>Answer</summary>

**FALSE.**

A 404 error means the **resource was not found** — the server is working correctly. If the server had crashed, you would receive a connection error (e.g., "Connection refused") or a 500 error (Internal Server Error), not a 404. A 404 is a normal, intentional response from the API.

</details>

---

**J6.** The `id` and `created_at` fields must be included in the POST body when creating a task.

<details>
<summary>Answer</summary>

**FALSE.**

`id` and `created_at` are **server-generated fields**. They are not part of the `TaskCreate` model that the POST route accepts. The server assigns the `id` automatically using `next_id` and generates `created_at` using the `_now()` function. The client should never send these fields.

</details>

---

**J7.** If you restart the FastAPI server, all tasks created during the session are lost.

<details>
<summary>Answer</summary>

**TRUE.**

The data is stored in the `tasks_db` Python dictionary, which lives in memory only. When the server stops, all memory is cleared. On restart, `tasks_db` is re-initialized from the hardcoded sample data in `main.py`. This is an in-memory database — it has no persistence.

</details>

---

**J8.** PUT and PATCH produce the same result.

<details>
<summary>Answer</summary>

**FALSE.**

- **PUT** replaces the entire task. Fields not included in the body are reset to their default values.
- **PATCH** updates only the fields sent. All other fields keep their current values.

They produce the same result **only** if you send all fields in both methods.

</details>

---

**J9.** You can combine two query parameters in a single GET request using `&`.

<details>
<summary>Answer</summary>

**TRUE.**

Example:
```
GET /tasks?completed=false&priority=high
```
The `&` separates multiple query parameters. Both filters are applied simultaneously (logical AND).

</details>

---

**J10.** A 422 error means the URL you typed is wrong.

<details>
<summary>Answer</summary>

**FALSE.**

A 422 error means the **data you sent is invalid** — not the URL. The URL was correct (the route was found), but the request body or parameters failed validation (missing required field, wrong type, etc.). A wrong URL would produce a **404** error.

</details>

---

**J11.** To delete a task, you need to send a JSON body containing the task's ID.

<details>
<summary>Answer</summary>

**FALSE.**

The task ID is passed as a **path parameter** in the URL: `DELETE /tasks/4`. No body is needed or expected. The route handler reads the ID directly from the URL.

</details>

---

**J12.** If `GET /tasks` returns 4 tasks and you then run `POST /tasks` successfully, `GET /tasks` will return 5 tasks.

<details>
<summary>Answer</summary>

**TRUE.**

A successful POST creates a new task and adds it to `tasks_db`. The next GET retrieves all tasks from `tasks_db`, which now contains 5 entries. The count increases by exactly 1 per successful POST.

</details>

---

<p align="right"><a href="#top">↑ Back to top</a></p>

---

<p align="center">
  <strong>End of Answer Key — API Testing Quiz</strong><br/>
  <a href="#top">↑ Back to the top</a>
</p>
