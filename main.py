import json
from fastapi import FastAPI, Query
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware

# Load marks data from JSON file at startup
with open('q-vercel-python.json', 'r') as f:
    data_list = json.load(f)
     marks_data = {item["name"]: item["marks"] for item in data_list}

app = FastAPI()

# Enable CORS for all origins and GET requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["GET"],
    allow_headers=["*"],
)

@app.get("/api")
def get_marks(name: list[str] = Query([])):
    result = [marks_data.get(n, None) for n in name]
    return JSONResponse(content={"marks": result})
