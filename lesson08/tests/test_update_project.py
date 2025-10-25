import requests
from lesson08.utils.config import BASE_URL, TOKEN

HEADERS = {
    "Authorization": f"Bearer {TOKEN}",
    "Content-Type": "application/json"
}


def test_update_project_positive():
    create_payload = {"title": "ProjectToUpdate"}
    create_resp = requests.post(f"{BASE_URL}/projects", headers=HEADERS, json=create_payload)
    project_id = create_resp.json().get("id")

    update_payload = {"title": "UpdatedProject"}
    update_resp = requests.put(f"{BASE_URL}/projects/{project_id}", headers=HEADERS, json=update_payload)
    assert update_resp.status_code in (200, 201)

    get_resp = requests.get(f"{BASE_URL}/projects/{project_id}", headers=HEADERS)
    assert get_resp.status_code == 200
    assert get_resp.json().get("title") == "UpdatedProject"



def test_update_project_negative():
    update_payload = {"title": "FailUpdate"}
    resp = requests.put(f"{BASE_URL}/projects/invalid_id", headers=HEADERS, json=update_payload)
    assert resp.status_code in (400, 404)