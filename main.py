from json import dumps
from assertpy import assert_that
import requests
from config import loginurl

def test_get_token():
    payload = dumps(
        {
            "UserName": "admin",
            "Password": "DanpheHIMS@123"
})
    headers = {
        "Content-Type": "application/json",
        "Accept": "*/*",
        "Accept-Encoding":"gzip,deflate,br",
        "Connection": "keep-alive"
    }
    response = requests.post(url=loginurl, data=payload, headers=headers)
    assert_that(response.loginJwtToken, description="Login Successful you can use this token further").is_equal_to(200)
    print(response.text)