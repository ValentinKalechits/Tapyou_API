import requests

class Http_method:
    headers = {'Content-Type': 'application/json'}
    cookie = ""

    @staticmethod
    def get(url):
        result= requests.get(url, headers=Http_method.headers, cookies=Http_method.cookie)
        return result


