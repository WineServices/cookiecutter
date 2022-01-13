from fastapi import APIRouter, status

router = APIRouter()


@router.get("/", status_code=status.HTTP_200_OK)
def root():
    return {"message": "{{ cookiecutter.github_repo_name }} is active"}
