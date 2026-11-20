def login(username, password):
    if username == "admin" and password == "1234":
        return "Login Successful"
    return "Invalid Login"

def calculate_marks(marks):
    return sum(marks) / len(marks)