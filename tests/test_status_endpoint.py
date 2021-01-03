import json
from http import HTTPStatus


def test_get_status(client):
    """
    respond successfully while requesting its status in getting("/status")
    """
    response = client.get("/status")
    assert response.status_code == HTTPStatus.OK
    assert response.headers['Content-Type'] == 'application/json'
    assert json.loads(response.data) == {"status": "ok"}
    