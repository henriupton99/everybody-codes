from ec.api import Client

def test_client():
    client = Client()
    cache = client.cache
    assert "session_cookie" in cache
    assert "seed" in cache
