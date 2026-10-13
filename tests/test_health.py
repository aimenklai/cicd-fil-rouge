def test_health_returns_ok(client):
    response = client.get("/health")
    # Test cassé volontairement pour le TP (attend 500 au lieu de 200)
    assert response.status_code == 500
    assert response.json()["status"] == "ok"

