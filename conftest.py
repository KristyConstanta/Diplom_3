import pytest
from selenium import webdriver
import urls
import helper
import requests


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):

    browser = None

    if request.param == 'firefox':
        browser = webdriver.Firefox()
    elif request.param == 'chrome':
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_argument('start-maximized')
        browser = webdriver.Chrome(options=chrome_options)

    browser.get(urls.BASE_URL)

    yield browser

    browser.quit()


@pytest.fixture(scope='function')
def default_user():

    payload = helper.generate_payload_for_user()
    response = requests.post(urls.BASE_URL + urls.CREATE_USER_ENDPOINT, json=payload)
    access_token = response.json()['accessToken']
    payload['accessToken'] = access_token

    yield payload

    requests.delete(urls.BASE_URL + urls.DELETE_USER_ENDPOINT, headers={'Authorization': access_token})


@pytest.fixture(scope='function')
def create_order(default_user):

    payload = {'ingredients': helper.get_payload_for_order()}
    access_token = default_user['accessToken']
    response = requests.post(urls.BASE_URL + urls.CREATE_ORDER_ENDPOINT, json=payload,
                             headers={'Authorization': access_token})
    order_number = response.json()['order']['number']
    order = {'order_number': order_number,
             'user_email': default_user['email'],
             'user_password': default_user['password']}

    return order