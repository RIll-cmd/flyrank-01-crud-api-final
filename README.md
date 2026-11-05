# Task API — final stage-verified reconstruction

This is the third public reconstruction of A1 from earlier AI-assisted work. It corrects the previous rebuild's Stage 1 sequencing issue by checking exact root metadata before its Stage 1 commit. Both prior public repositories and all other assignments remain unchanged. This is AI-assisted work, not a claim of hand-written authorship. Current-time commits follow the required stages, each gated by actual runtime checks.

![New final-reconstruction Swagger screenshot](swagger.png)

Requires Python 3.12+. Install dependencies: `python -m pip install -r requirements.txt`.
Run: `python -m uvicorn app:app --port 8111`. Open http://localhost:8111/docs.

| Method | Endpoint | Result |
|---|---|---|
| GET | / | 200 exact API name/version/endpoints |
| GET | /health | 200 status ok |
| GET | /tasks | 200 task list |
| GET | /tasks/{task_id} | 200 task; 404 unknown |
| POST | /tasks | 201 new task; 400 invalid body |
| PUT | /tasks/{task_id} | 200 updated task; 400 invalid; 404 unknown |
| DELETE | /tasks/{task_id} | 204 empty body; 404 unknown |

Tasks live only in memory; restarting restores three examples. POST needs a non-empty string title. PUT accepts title and/or boolean done, rejects an empty/invalid body. Errors have a JSON error field. Each new ID is unique during a process lifetime.

## Requirement checks
- [x] One documented server command and in-memory five-endpoint CRUD.
- [x] Exact Stage 1 root metadata and health verified in actual curl and Chromium before Stage 1 commit.
- [x] 200/201/204/400/404, JSON errors and body validation verified with real curl before relevant commits.
- [x] Full Swagger create/list/read/update/delete and new screenshot verified before Stage 5 commit.
- [x] New public repo, seven exact stage commits with current timestamps; no prior history rewritten.
- [x] Fresh clone, clean virtual environment dependency installation and actual full CRUD run checked before Stage 6 commit.

Full actual request headers and response bodies are recorded in stage-N-verification.txt files. BUILDLOG.md records each gate. This reconstruction covers A1 only; all other assignment repositories are unchanged.

Actual curl create response:

```http
HTTP/1.1 201 Created
date: Thu, 05 Nov 2026 08:23:48 GMT
server: uvicorn
content-length: 40
content-type: application/json

{"id":4,"title":"Buy milk","done":false}
```
