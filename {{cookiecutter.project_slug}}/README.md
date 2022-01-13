# Description
{{ cookiecutter.project_short_description }}

# Requirements:
Python version: {{ cookiecutter.python_version }}



# Update Base dockerfile:

To update the base image:
- create locally the new image: `docker build -t wineservice/{{ cookiecutter.github_repo_name }} -f DockerHubFile .`
- Open Docker Desktop and log in to Docker hub
- Go to images -> `wineservice/{{ cookiecutter.github_repo_name }}`  -> Push to Hub


### Launch locally:

1- Create postgres database with docker: `docker-compose up -d`

2- Open `localhost:8000/docs` and you can try all routes.


# Developers section

- To install virtual environment: `export venv.sh`
- To launch unit tests: 

   1 - `source PYTHONPATH=<src-directory>`
   
   2- `pytest` 
