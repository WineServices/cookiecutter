#!/usr/bin/env python
import os

PROJECT_DIRECTORY = os.path.realpath(os.path.curdir)


def remove_file(filepath):
    os.remove(os.path.join(PROJECT_DIRECTORY, filepath))


if __name__ == '__main__':
    remove_file("src/app.yaml")
    if '{{ cookiecutter.gcp_service_type }}' == 'cloud run':
        remove_file("src/requirements.txt")
    else:
        remove_file("requirements.txt")
