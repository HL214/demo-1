from uinitest import get_username,get_password

def test_login_username():
    except_username = 'test01'
    acntl_username = get_username()
    assert except_username == acntl_username

def test_login_password():
    except_password = 'test01'
    acntl_password = get_password()
    assert except_password == acntl_password

test_login_username()
test_login_password()
