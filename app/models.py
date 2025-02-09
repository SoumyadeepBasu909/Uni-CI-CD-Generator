from pydantic import BaseModel

class PipelineRequest(BaseModel):
    ci_cd_tool: str
    github_url: str
    project_type: str
    build_tool: str
    deployment: str
    build_command: str
    test_command: str
    artifact: str
    docker_image: str = None
