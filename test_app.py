from app import login, calculate_marks

def test_login():
    assert login("admin", "1234") == "Login Successful"

def test_invalid_login():
    assert login("user", "123") == "Invalid Login"

def test_marks():
    assert calculate_marks([80, 90, 100]) == 90