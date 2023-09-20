from fastapi.testclient import TestClient
from main import app, labels


client = TestClient(app)


def test_detection():
    response = client.post("/wastes/detection",
                           files={"img": open("test.jpg", "rb")})

    assert response.status_code == 200


def test_get_labels():
    response = client.get("/wastes/labels")

    assert response.status_code == 200
    assert response.json() == [
        {"id": label, "name": labels[label]} for label in labels]


def test_report():
    response = client.post("/wastes/report",
                           files={"img": open("test.jpg", "rb")},
                           params={"label": 1})

    assert response.status_code == 200
    assert response.json() == {"message": "Thank you for your report!"}
