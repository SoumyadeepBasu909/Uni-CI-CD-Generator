from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import PlainTextResponse
from app.render import generate_pipeline
from app.models import PipelineRequest

app = FastAPI()

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Change this to specific domains in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/generate", response_class=PlainTextResponse)
async def generate_pipeline_api(request: PipelineRequest):
    return generate_pipeline(request)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
