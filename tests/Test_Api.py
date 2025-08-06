import pytest

from Demo import generate_user_id
from utils.api_client import Api_Client
from utils import Utils_1

request = Api_Client()

@pytest.mark.regression
def test_get_users():
    get_endpoint = "posts"
    response_get = request.get(get_endpoint)
    assert response_get.status_code == 200
    get_response = response_get.json()
    print(get_response)
    count = 0
    for i in get_response:
        count+=1
    print(f"Number of records {count}")

def test_add_user(load_json_file):
    post_endpoint = "posts"
    new_user_data = load_json_file["new_user"]
    post_response = request.post(post_endpoint,new_user_data)
    post_response_json = post_response.json()
    print(post_response_json)
    assert post_response.status_code == 201
    assert len(post_response.json())>0
    assert new_user_data["userId"] == post_response_json["userId"]

def test_update_user(load_json_file):
    post_endpoint = "posts/1"
    new_user_id = Utils_1.generate_user_id()
    new_user_data = load_json_file["new_user"]
    new_user_data["userId"] = new_user_id
    put_request = request.put(post_endpoint,new_user_data)
    put_request_response = put_request.json()
    print("Response", put_request_response)
    assert put_request.status_code == 200
    #assert put_request_response["userId"] == new_user_id
    assert put_request_response["userId"] == new_user_data["userId"]
    print(f"new userID{new_user_data}")

def test_get_a_user():
    get_a_user_endpoint = "posts/1"
    get_a_user_request = request.get(get_a_user_endpoint)
    get_user_response  = get_a_user_request.json()
    print(get_user_response)
    assert get_a_user_request.status_code == 200
    assert len(get_user_response)>0

def test_delete_a_user():
    delete_endpoint = "posts/1"
    delete_a_user_request = request.delete(delete_endpoint)
    delete_response = delete_a_user_request.json()
    print(delete_response)
    assert len(delete_response) == 0
