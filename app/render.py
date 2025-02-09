from jinja2 import Environment, FileSystemLoader
from app.models import PipelineRequest

env = Environment(loader=FileSystemLoader("templates"))

def generate_pipeline(request: PipelineRequest):
    template = env.get_template(f"{request.ci_cd_tool.lower()}.j2")
    return template.render(**request.dict()).strip()

