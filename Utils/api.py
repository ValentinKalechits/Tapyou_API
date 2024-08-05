import requests
from Utils.HTTP_methods import Http_method

class TapyouAPI:
    base_url_users = "https://hr-challenge.dev.tapyou.com/api/test/users"
    base_url_user = "https://hr-challenge.dev.tapyou.com/api/test/user"

    @staticmethod
    def get_users_by_gender(gender):
        url = f"{TapyouAPI.base_url_users}?gender={gender}"
        response = Http_method.get(url)
        return response

    @staticmethod
    def get_user_by_id(user_id):
        url = f"{TapyouAPI.base_url_user}/{user_id}"
        response = Http_method.get(url)
        return response



