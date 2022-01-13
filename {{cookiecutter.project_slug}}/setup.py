import setuptools

setuptools.setup(
    setup_requires=['wheel'],
    package_dir={'': '{{ cookiecutter.project_slug }}'},
)
