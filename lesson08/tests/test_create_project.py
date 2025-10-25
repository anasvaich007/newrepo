import requests
from lesson08.utils.config import BASE_URL, TOKEN

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

def test_create_project_positive():
    payload = {
        "title": "TestProjectSimple"
    }
    resp = requests.post(f"{BASE_URL}/projects", headers=HEADERS, json=payload)
    assert resp.status_code == 201
    body = resp.json()
    assert body.get("id") is not None

    project_id = body.get("id")
    requests.delete(f"{BASE_URL}/projects/{project_id}", headers=HEADERS)

def test_create_project_negative():
    payload = {"title": ""}
    resp = requests.post(f"{BASE_URL}/projects", headers=HEADERS, json=payload)
    assert resp.status_code == 400
