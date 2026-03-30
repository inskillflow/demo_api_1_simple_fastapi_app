<a id="top"></a>

# Quiz — API Testing with FastAPI
## Task Manager API — `main.py`

> **Instructions:**
> Answer every question in writing. No multiple choice — you write the answer yourself.
> The API used for all questions is the Task Manager API running at `http://127.0.0.1:8000`.
> Refer to nothing except your own knowledge.

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

```
Your answer:
```

---

**A2.** You want to add a brand new task to the list.

```
Your answer:
```

---

**A3.** You want to completely replace task number 3 with new data.

```
Your answer:
```

---

**A4.** You want to mark task number 2 as completed without changing its title or priority.

```
Your answer:
```

---

**A5.** You want to permanently remove task number 5 from the list.

```
Your answer:
```

---

**A6.** You want to check if the server is running and see how many tasks are in memory.

```
Your answer:
```

---

**A7.** You want to get the details of task number 1 only — not the full list.

```
Your answer:
```

---

**A8.** You want to change the priority of task number 4 from `"low"` to `"high"` without touching the other fields.

```
Your answer:
```

---

**A9.** What is the difference between PUT and PATCH? Write it in your own words.

```
Your answer:
```

---

**A10.** Can you use a GET request to create a new task? Explain why or why not.

```
Your answer:
```

---

<p align="right"><a href="#top">↑ Back to top</a></p>

---

<a id="sb"></a>

## Section B — URLs and Routes

**Write the complete URL for each request described below.**
**The base URL is `http://127.0.0.1:8000`.**

---

**B1.** Get the full list of tasks.

```
Your answer:
```

---

**B2.** Get task number 3.

```
Your answer:
```

---

**B3.** Get task number 7.

```
Your answer:
```

---

**B4.** Delete task number 2.

```
Your answer:
```

---

**B5.** Update only the `completed` field of task number 5.

```
Your answer:
```

---

**B6.** Completely replace task number 1 with new data.

```
Your answer:
```

---

**B7.** Check if the server is running (root endpoint).

```
Your answer:
```

---

**B8.** Get only the tasks that have `priority = "high"`.

```
Your answer:
```

---

**B9.** Get only the tasks that are not completed.

```
Your answer:
```

---

**B10.** Get only the tasks that are not completed AND have priority `"medium"`.

```
Your answer:
```

---

**B11.** A student writes this URL to get task 4:

```
http://127.0.0.1:8000/task/4
```

What is wrong with this URL? Write the correct version.

```
Your answer:
```

---

**B12.** A student writes this URL to create a new task:

```
http://127.0.0.1:8000/tasks/
```

They use the POST method and send a valid JSON body. Will this work? Explain.

```
Your answer:
```

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

```
Your answer:
```

---

**C2.** You want to create a new task with only the title `"Read chapter 5"` and use default values for everything else.

Write the JSON body.

```
Your answer:
```

---

**C3.** You send a POST request with this body:

```json
{
  "description": "Some details here",
  "priority": "low"
}
```

What happens? What status code do you get and why?

```
Your answer:
```

---

**C4.** You want to use PATCH to mark task 2 as completed. Write the JSON body you would send.

```
Your answer:
```

---

**C5.** You want to use PATCH to change the title of task 3 to `"Write integration tests"`. Write the JSON body.

```
Your answer:
```

---

**C6.** You want to use PUT to completely replace task 1. The new values should be:
- Title: `"Advanced FastAPI"`
- Description: `"Learn middleware and dependencies"`
- Completed: false
- Priority: `"high"`

Write the JSON body.

```
Your answer:
```

---

**C7.** You use PUT on task 1 but send only this body:

```json
{
  "title": "Advanced FastAPI"
}
```

What happens to the `description`, `completed`, and `priority` fields? Explain.

```
Your answer:
```

---

**C8.** For a DELETE request on task 4, what body do you need to send?

```
Your answer:
```

---

**C9.** For a GET request on `/tasks`, what body do you need to send?

```
Your answer:
```

---

**C10.** You want to send a POST request but you forget to set the `Content-Type` header to `application/json`. What might happen?

```
Your answer:
```

---

<p align="right"><a href="#top">↑ Back to top</a></p>

---

<a id="sd"></a>

## Section D — Status Codes

**For each situation below, write the HTTP status code the API should return.**

---

**D1.** A GET request to `/tasks` returns all 4 tasks successfully.

```
Your answer:
```

---

**D2.** A POST request to `/tasks` with a valid body successfully creates a new task.

```
Your answer:
```

---

**D3.** A DELETE request to `/tasks/4` successfully deletes task 4.

```
Your answer:
```

---

**D4.** A GET request to `/tasks/99` — task 99 does not exist.

```
Your answer:
```

---

**D5.** A POST request to `/tasks` with an empty body `{}`.

```
Your answer:
```

---

**D6.** A PATCH request to `/tasks/3` with `{"completed": true}` — task 3 exists.

```
Your answer:
```

---

**D7.** A PUT request to `/tasks/50` — task 50 does not exist.

```
Your answer:
```

---

**D8.** A DELETE request to `/tasks/4` — but task 4 was already deleted earlier.

```
Your answer:
```

---

**D9.** A POST request with `{"title": "Test", "completed": "yes"}` — `completed` must be a boolean.

```
Your answer:
```

---

**D10.** In your own words, explain the difference between a 404 error and a 422 error.

```
Your answer:
```

---

**D11.** You receive a 204 response after a DELETE. The response body is completely empty. Is this an error? Explain.

```
Your answer:
```

---

**D12.** Write the name and meaning of these three status codes:

| Code | Name | Meaning |
|---|---|---|
| 200 | | |
| 201 | | |
| 204 | | |
| 404 | | |
| 422 | | |

---

<p align="right"><a href="#top">↑ Back to top</a></p>

---

<a id="se"></a>

## Section E — Order of Operations

**These questions test whether you understand what must happen before what.**

---

**E1.** You want to test GET `/tasks/5`. The API starts with 4 sample tasks (IDs 1 to 4).
Can you run this test immediately? If not, what must you do first?

```
Your answer:
```

---

**E2.** You run DELETE `/tasks/3` and get a 204 response.
You then run GET `/tasks/3`. What status code do you get? What does the response body contain?

```
Your answer:
```

---

**E3.** Put these 4 actions in the correct logical order to properly test the create feature:

- Run GET `/tasks` and count the total number of tasks
- Run POST `/tasks` with a valid body
- Run GET `/tasks/5` to verify the new task was created with the right data
- Run GET `/tasks` again and verify the count increased by 1

Write the correct order (1, 2, 3, 4):

```
Your order:

Step 1:
Step 2:
Step 3:
Step 4:
```

---

**E4.** You want to test that PATCH only changes the fields you send. Describe the steps you would follow, in order, to properly verify this.

```
Your answer:
```

---

**E5.** You want to test that PUT resets fields you do not send to their default values. Describe the steps in order.

```
Your answer:
```

---

**E6.** A student runs these requests in this order:

1. `DELETE /tasks/4` → 204
2. `GET /tasks/4` → what status code?
3. `DELETE /tasks/4` → what status code?

Fill in the status codes for steps 2 and 3 and explain each one.

```
Your answer for step 2:

Your answer for step 3:

Explanation:
```

---

**E7.** You want to verify that your API has exactly 4 tasks at startup (before any changes).
Write the single request you would send to confirm this.

```
Method:
URL:
What you check in the response:
```

---

**E8.** After running several tests (creating, deleting, updating tasks), you want to reset the API back to its original 4 tasks. How do you do this?

```
Your answer:
```

---

<p align="right"><a href="#top">↑ Back to top</a></p>

---

<a id="sf"></a>

## Section F — Filters and Query Parameters

---

**F1.** What symbol separates the base URL from the query parameters?

```
Your answer:
```

---

**F2.** What symbol separates two query parameters from each other in the same URL?

```
Your answer:
```

---

**F3.** Write the full URL to get only tasks where `completed` is `true`.

```
Your answer:
```

---

**F4.** Write the full URL to get only tasks where `priority` is `"low"`.

```
Your answer:
```

---

**F5.** Write the full URL to get tasks that are NOT completed AND have priority `"high"`.

```
Your answer:
```

---

**F6.** You run GET `/tasks?priority=high`. The API returns 2 tasks.
You then run GET `/tasks?priority=high&completed=true`. The API returns 1 task.
What does this tell you about the two high-priority tasks?

```
Your answer:
```

---

**F7.** What is the difference between a query parameter and a path parameter? Give one example of each from the Task Manager API.

```
Query parameter — explanation and example:

Path parameter — explanation and example:
```

---

**F8.** A student writes this URL:

```
http://127.0.0.1:8000/tasks?completed=True
```

Note the capital `T` in `True`. Will this filter work correctly? Explain.

```
Your answer:
```

---

**F9.** You run GET `/tasks` with no filters. You get 4 tasks.
You then run GET `/tasks?completed=true`. You get 1 task.
You then run GET `/tasks?completed=false`. How many tasks should you get?

```
Your answer:
```

---

**F10.** Is it possible to filter tasks by their title using the current API?
For example: GET `/tasks?title=FastAPI`
Explain why or why not based on what you know about the code.

```
Your answer:
```

---

<p align="right"><a href="#top">↑ Back to top</a></p>

---

<a id="sg"></a>

## Section G — Errors — What Went Wrong?

**Each scenario below contains a mistake. Identify the problem and write how to fix it.**

---

**G1.** A student wants to get all tasks. They send:

```
Method: POST
URL: http://127.0.0.1:8000/tasks
Body: (empty)
```

They get a 422 error. What went wrong? What is the correct request?

```
Problem:

Correct request:
```

---

**G2.** A student wants to get task number 2. They send:

```
Method: GET
URL: http://127.0.0.1:8000/tasks?id=2
```

They get all 4 tasks, not just task 2. What went wrong? Write the correct URL.

```
Problem:

Correct URL:
```

---

**G3.** A student wants to create a new task. They send:

```
Method: POST
URL: http://127.0.0.1:8000/tasks
Body:
{
  "title": "My new task",
  "completed": "false",
  "priority": "high"
}
```

They get a 422 error. What is the problem?

```
Problem:

Correct body:
```

---

**G4.** A student wants to delete task 3. They send:

```
Method: DELETE
URL: http://127.0.0.1:8000/tasks
Body: {"id": 3}
```

They get a 405 error (Method Not Allowed). What went wrong?

```
Problem:

Correct request:
```

---

**G5.** A student wants to mark task 1 as completed. They use PUT:

```
Method: PUT
URL: http://127.0.0.1:8000/tasks/1
Body: {"completed": true}
```

The request returns 200 but now task 1 has:
- `title: ""`
- `description: ""`
- `priority: "medium"`
- `completed: true`

The student is surprised — they only wanted to change `completed`. What went wrong?
What method should they have used?

```
Problem:

Correct method and explanation:
```

---

**G6.** A student sends this request:

```
Method: PATCH
URL: http://127.0.0.1:8000/tasks/99
Body: {"completed": true}
```

They get a 404 error. Is this a bug in the API? Explain.

```
Your answer:
```

---

**G7.** A student wants to create a task using the Params tab in Postman instead of the Body tab:

```
Method: POST
URL: http://127.0.0.1:8000/tasks
Params: title=My Task, priority=high
Body: (empty)
```

They get a 422 error. Why?

```
Your answer:
```

---

**G8.** A student sends a perfectly correct POST request but gets this error:

```
curl: (7) Failed to connect to 127.0.0.1 port 8000: Connection refused
```

The JSON body is valid. What is the real problem and how do they fix it?

```
Your answer:
```

---

<p align="right"><a href="#top">↑ Back to top</a></p>

---

<a id="sh"></a>

## Section H — Scenarios — What Do You Do?

**Read each scenario and describe exactly what request(s) you would send, in order.**
**Specify: method, URL, body (if needed), and expected status code.**

---

**H1.** You want to verify that the API is running and check how many tasks are currently in memory.

```
Method:
URL:
Body:
Expected status code:
What you look for in the response:
```

---

**H2.** You want to add this task to the API:
- Title: `"Learn Docker"`
- Description: `"Study containers and images"`
- Priority: `"high"`
- Completed: false

```
Method:
URL:
Body:

Expected status code:
What the response should contain:
```

---

**H3.** After running H2, you want to verify the task was actually saved and was assigned ID 5.

```
Method:
URL:
Body:
Expected status code:
What you look for in the response:
```

---

**H4.** You want to mark task 3 as completed without changing anything else.

```
Method:
URL:
Body:

Expected status code:
```

---

**H5.** You want to completely update task 2 with these values:
- Title: `"Build a production API"`
- Description: `"Add authentication and database"`
- Completed: true
- Priority: `"high"`

```
Method:
URL:
Body:

Expected status code:
```

---

**H6.** After running H5, you want to confirm that task 2's title is now `"Build a production API"`.

```
Method:
URL:
Body:
Expected status code:
What you look for in the response:
```

---

**H7.** You want to delete task 4 and then confirm it no longer exists.

Describe the two requests in order:

```
Request 1:
  Method:
  URL:
  Expected status code:
  Expected body:

Request 2:
  Method:
  URL:
  Expected status code:
  Expected body:
```

---

**H8.** You want to find all tasks that are not completed and have priority `"high"`.

```
Method:
URL (include the filters):
Body:
Expected status code:
What you expect to see in the response:
```

---

**H9.** You want to test what happens when you try to get a task that does not exist.

```
Method:
URL (use an ID that does not exist):
Expected status code:
Expected response body:
```

---

**H10.** You want to test the full lifecycle of a task: create it, read it, update it, then delete it, then confirm it is gone.

Write all 5 requests in order:

```
Step 1 — Create:
  Method:
  URL:
  Body:
  Expected status code:

Step 2 — Read:
  Method:
  URL:
  Expected status code:

Step 3 — Update (change only the priority to "low"):
  Method:
  URL:
  Body:
  Expected status code:

Step 4 — Delete:
  Method:
  URL:
  Expected status code:

Step 5 — Confirm deletion:
  Method:
  URL:
  Expected status code:
```

---

<p align="right"><a href="#top">↑ Back to top</a></p>

---

<a id="si"></a>

## Section I — Read the Response

**Read each API response below and answer the questions.**

---

**I1.** You send a request and receive this response:

```json
{
  "message": "Task Manager API is running",
  "docs": "http://127.0.0.1:8000/docs",
  "total_tasks": 6
}
```

a) What method and URL did you use?

```
Your answer:
```

b) What does `total_tasks: 6` tell you?

```
Your answer:
```

---

**I2.** You send a request and receive this response with status code 201:

```json
{
  "id": 5,
  "title": "Learn Docker",
  "description": "",
  "completed": false,
  "priority": "medium",
  "created_at": "2026-03-30 14:22:05"
}
```

a) What method did you use?

```
Your answer:
```

b) You did not send `description`, `completed`, or `priority` in your request body. Why do they appear in the response?

```
Your answer:
```

c) You did not send `id` or `created_at` in your request body either. Why do they appear in the response?

```
Your answer:
```

---

**I3.** You send a request and receive this response with status code 404:

```json
{
  "detail": "Task with ID 99 not found"
}
```

a) What method and URL could have produced this response? Give two different examples.

```
Example 1 (method + URL):

Example 2 (method + URL):
```

b) Is this response a server bug or expected behavior? Explain.

```
Your answer:
```

---

**I4.** You send a request and the response has status code 204 and the body is completely empty.

a) What method did you use?

```
Your answer:
```

b) Is an empty body an error here? Explain.

```
Your answer:
```

---

**I5.** You send a POST request and receive this response with status code 422:

```json
{
  "detail": [
    {
      "type": "missing",
      "loc": ["body", "title"],
      "msg": "Field required",
      "input": {}
    }
  ]
}
```

a) What does `"loc": ["body", "title"]` tell you?

```
Your answer:
```

b) What was wrong with your request?

```
Your answer:
```

c) Write the minimum JSON body you need to fix this error.

```
Your answer:
```

---

**I6.** You send GET `/tasks?completed=false` and receive this response:

```json
[
  {
    "id": 1,
    "title": "Learn FastAPI",
    "completed": false,
    "priority": "high",
    ...
  },
  {
    "id": 3,
    "title": "Write unit tests",
    "completed": false,
    "priority": "medium",
    ...
  },
  {
    "id": 4,
    "title": "Deploy to production",
    "completed": false,
    "priority": "low",
    ...
  }
]
```

a) How many tasks are NOT completed?

```
Your answer:
```

b) The list does NOT contain task 2. What does that tell you about task 2?

```
Your answer:
```

c) The response starts with `[` and ends with `]`. What does that mean in JSON?

```
Your answer:
```

---

<p align="right"><a href="#top">↑ Back to top</a></p>

---

<a id="sj"></a>

## Section J — True or False — Justify

**Write TRUE or FALSE, then write one sentence explaining why.**

---

**J1.** A GET request can have a JSON body.

```
True or False:

Justification:
```

---

**J2.** After a successful DELETE, the response body should be empty.

```
True or False:

Justification:
```

---

**J3.** If you send PATCH with an empty body `{}`, all fields of the task are reset to their default values.

```
True or False:

Justification:
```

---

**J4.** To use a query parameter filter, you must put it in the JSON body of the request.

```
True or False:

Justification:
```

---

**J5.** A 404 error means the server crashed.

```
True or False:

Justification:
```

---

**J6.** The `id` and `created_at` fields must be included in the POST request body when creating a task.

```
True or False:

Justification:
```

---

**J7.** If you restart the FastAPI server, all tasks created during the session are lost.

```
True or False:

Justification:
```

---

**J8.** PUT and PATCH can both be used to update a task, and they produce the same result.

```
True or False:

Justification:
```

---

**J9.** You can combine two query parameters in a single GET request using the `&` character.

```
True or False:

Justification:
```

---

**J10.** A 422 error means the URL you typed is wrong.

```
True or False:

Justification:
```

---

**J11.** To delete a task, you need to send a JSON body containing the task's ID.

```
True or False:

Justification:
```

---

**J12.** If `GET /tasks` returns 4 tasks and you then run `POST /tasks` successfully, `GET /tasks` will return 5 tasks.

```
True or False:

Justification:
```

---

<p align="right"><a href="#top">↑ Back to top</a></p>

---

<p align="center">
  <strong>End of Quiz — API Testing</strong><br/>
  <a href="#top">↑ Back to the top</a>
</p>
