import pytest

import test_logindata


@pytest.fixture()
def registration_data():
    username = test_logindata.Test.test_input_file_excel('self')
    return username[0], username[1]


@pytest.fixture()
def login_data():

    username = test_logindata.Test.test_login_input_file_excel('self')
    return username[0], username[1]


@pytest.fixture()
def login_code_data():

    username = test_logindata.Test.test_login_code_input_file_excel('self')
    return username


@pytest.fixture()
def auth_token_data():

    username = test_logindata.Test.test_auth_token_data_file_excel('self')
    return username


@pytest.fixture()
def send_code_data():

    username = test_logindata.Test.test_send_confirmation_code_file_excel('self')
    return username


@pytest.fixture()
def reset_password_data():

    username = test_logindata.Test.test_reset_password_file_excel('self')
    return username


@pytest.fixture()
def verify_code_data():

    username = test_logindata.Test.test_verify_code_file_excel('self')
    return username













