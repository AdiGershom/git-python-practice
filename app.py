from datetime import datetime

def greet(name):
    current_time = datetime.now().strftime("%H:%M:%S")
    return f"Hello, {name}! The current time is {current_time}"


if __name__ == "__main__":
    user = "Adi Gershom"
    username ="agershom"
    print(greet(user))