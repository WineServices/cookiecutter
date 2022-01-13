def test_default_route(client):
    with client:
        response = client.get("/")
        assert response.status_code == 200
        assert response.json() == {"message": "{{ cookiecutter.github_repo_name }} is active"}
