import requests
from lesson08.utils.config import BASE_URL, TOKEN

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}

def test_get_project_positive():

    create_payload = {"title": "ProjectToGet"}
    create_resp = requests.post(f"{BASE_URL}/projects", headers=HEADERS, json=create_payload)
    project_id = create_resp.json().get("id")

    resp = requests.get(f"{BASE_URL}/projects/{project_id}", headers=HEADERS)
    assert resp.status_code == 200
    assert resp.json().get("id") == project_id

    requests.delete(f"{BASE_URL}/projects/{project_id}", headers=HEADERS)


def test_get_project_negative():
    resp = requests.get(f"{BASE_URL}/projects/invalid_id", headers=HEADERS)
    assert resp.status_code in (400, 404)
