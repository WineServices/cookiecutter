FROM wineservice/{{ cookiecutter.github_repo_name }}:latest


ENV APP_HOME /app


# Copy local code to the container image.
WORKDIR $APP_HOME

{% if cookiecutter.gcp_service_type == 'cloud run' %}
COPY requirements.txt .
{% else %}
COPY .src/requirements.txt .
{% endif %}

# Install production dependencies.
RUN pip install --no-cache-dir -r requirements.txt

RUN apt-get remove -y gcc &&  apt-get autoremove -y

COPY ./src ./

CMD gunicorn main:app -c api/gunicorn_config.py  --timeout 0
