from fastapi import FastAPI
app=FastAPI(docs_url=None,redoc_url=None,openapi_url=None)
@app.get("/",summary="Describe the API")
def root(): return {"name":"Task API","version":"1.0","endpoints":["/tasks"]}
@app.get("/health",summary="Check service health")
def health(): return {"status":"ok"}
