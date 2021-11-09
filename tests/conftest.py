import pytest
@pytest.fixture
def client():
    from wsgi import app
    #app.config['TESTING'] = True
    return app.test_client()