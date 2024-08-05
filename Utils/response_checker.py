import pytest

class ResponseChecker:

    @staticmethod
    def check_response(response, gender):
        if response.status_code != 200:
            pytest.fail(f"Request with gender='{gender}' returned status code {response.status_code}. Response text: {response.text}")

        json_data = response.json()


        assert "isSuccess" in json_data, f"Missing 'isSuccess' in response for gender='{gender}'"
        assert isinstance(json_data["isSuccess"], bool), f"'isSuccess' should be a boolean for gender='{gender}'"

        assert "errorCode" in json_data, f"Missing 'errorCode' in response for gender='{gender}'"
        assert isinstance(json_data["errorCode"], int), f"'errorCode' should be an integer for gender='{gender}'"

        assert "errorMessage" in json_data, f"Missing 'errorMessage' in response for gender='{gender}'"
        assert json_data["errorMessage"] is None or isinstance(json_data["errorMessage"], str), \
            f"'errorMessage' should be a string or None for gender='{gender}'"

        assert "idList" in json_data, f"Missing 'idList' in response for gender='{gender}'"
        assert isinstance(json_data["idList"], list), f"'idList' should be a list for gender='{gender}'"
        for item in json_data["idList"]:
            assert isinstance(item, int), f"Each item in 'idList' should be an integer for gender='{gender}'"

    @staticmethod
    def check_response_user(response, user_id):
        if response.status_code != 200:
            pytest.fail(f"Request with user ID='{user_id}' returned status code {response.status_code}. Response text: {response.text}")

        json_data = response.json()


        assert "isSuccess" in json_data, f"Missing 'isSuccess' in response for user ID='{user_id}'"
        assert isinstance(json_data["isSuccess"], bool), f"'isSuccess' should be a boolean for user ID='{user_id}'"

        assert "errorCode" in json_data, f"Missing 'errorCode' in response for user ID='{user_id}'"
        assert isinstance(json_data["errorCode"], int), f"'errorCode' should be an integer for user ID='{user_id}'"

        assert "errorMessage" in json_data, f"Missing 'errorMessage' in response for user ID='{user_id}'"
        assert json_data["errorMessage"] is None or isinstance(json_data["errorMessage"], str), \
            f"'errorMessage' should be a string or None for user ID='{user_id}'"

        assert "user" in json_data, f"Missing 'user' in response for user ID='{user_id}'"
        user_data = json_data["user"]
        assert isinstance(user_data, dict), f"'user' should be an object for user ID='{user_id}'"

        assert "id" in user_data, f"Missing 'id' in 'user' for user ID='{user_id}'"
        assert isinstance(user_data["id"], int), f"'id' should be an integer for user ID='{user_id}'"

        assert "name" in user_data, f"Missing 'name' in 'user' for user ID='{user_id}'"
        assert isinstance(user_data["name"], str), f"'name' should be a string for user ID='{user_id}'"

        assert "gender" in user_data, f"Missing 'gender' in 'user' for user ID='{user_id}'"
        assert isinstance(user_data["gender"], str), f"'gender' should be a string for user ID='{user_id}'"

        assert "age" in user_data, f"Missing 'age' in 'user' for user ID='{user_id}'"
        assert isinstance(user_data["age"], int), f"'age' should be an integer for user ID='{user_id}'"

        assert "city" in user_data, f"Missing 'city' in 'user' for user ID='{user_id}'"
        assert isinstance(user_data["city"], str), f"'city' should be a string for user ID='{user_id}'"

        assert "registrationDate" in user_data, f"Missing 'registrationDate' in 'user' for user ID='{user_id}'"
        assert isinstance(user_data["registrationDate"], str), f"'registrationDate' should be a string for user ID='{user_id}'"

    @staticmethod
    def check_error_response(response, expected_status_code):
        assert response.status_code == expected_status_code, \
            f"Expected status code {expected_status_code} but got {response.status_code}. Response text: {response.text}"
        json_data = response.json()
        assert "errorMessage" in json_data, "Missing 'errorMessage' in response"
        assert isinstance(json_data["errorMessage"], str), f"'errorMessage' should be a string but got {type(json_data['errorMessage'])}"
