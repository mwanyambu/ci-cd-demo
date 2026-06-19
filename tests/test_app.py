from app import app

def test_home_status_code():
    """Verifies that the web server answers successfully."""
    client = app.test_client()
    response = client.get("/")
    assert response.status_code == 200

def test_version_rendering():
    """Confirms that the word 'Version' is rendered inside the HTML document."""
    client = app.test_client()
    response = client.get("/")
    assert b"Version" in response.data
