#!/usr/bin/env bash
rm -rf env
python{{cookiecutter.python_version}} -m venv env
source "env/bin/activate"
pip{{cookiecutter.python_version}} install --upgrade pip
{% if cookiecutter.gcp_service_type == 'cloud run' %}
pip{{cookiecutter.python_version}} install -r requirements.txt
{% else %}
pip{{cookiecutter.python_version}} install -r src/requirements.txt
{% endif %}
pip{{cookiecutter.python_version}} install -r requirements_test.txt
