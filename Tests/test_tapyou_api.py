import pytest
from Utils.api import TapyouAPI
from Utils.response_checker import ResponseChecker

class TestTapyouAPI:

    # Тест, включающий тест-кейсы № 1-6 к запросу списка ID
    @pytest.mark.parametrize("gender", ["male", "female", "magic", "McCloud"])
    def test_gender(self, gender):

        '''Проверка наличия обязательных полей, их формата и статус-кода ответа'''

        response = TapyouAPI.get_users_by_gender(gender)
        ResponseChecker.check_response(response, gender)

    # Тест, включающий тест-кейсы № 1-4 к запросу информации о пользователе
    @pytest.mark.parametrize("user_id", [5, 10])
    def test_user_by_id(self, user_id):

        '''Проверка наличия обязательных полей, их формата и статус-кода ответа'''

        response = TapyouAPI.get_user_by_id(user_id)
        ResponseChecker.check_response_user(response, user_id)

    # Тест-кейс № 13  к запросу списка ID
    def test_no_duplicate_ids_across_genders(self):

        '''Проверка на отсутствие дублей разного пола  с одинаковым ID'''

        genders = ["male", "female", "magic", "McCloud"]
        all_ids = {}

        for gender in genders:
            response = TapyouAPI.get_users_by_gender(gender)
            ResponseChecker.check_response(response, gender)
            json_data = response.json()
            ids = json_data["idList"]

            # Проверяем, чтобы ID не повторялись между полами
            for user_id in ids:
                if user_id in all_ids:
                    pytest.fail(f"Duplicate ID found: {user_id} for genders '{all_ids[user_id]}' and '{gender}'")
                all_ids[user_id] = gender

    # Тест-кейс № 8  к запросу списка ID
    def test_invalid_gender_value(self):

        '''Запрос с некорректным значением параметра gender'''

        invalid_gender = "others"
        response = TapyouAPI.get_users_by_gender(invalid_gender)
        ResponseChecker.check_error_response(response, 400)




