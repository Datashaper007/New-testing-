users = {"admin": "1234", "user1": "abcd"}

username = input("Enter username: ")
password = input("Enter password: ")

if username in users and users[username] == password:
    print("Login successful!")
else:
    print("Invalid username or password.")
    print ("This is invalid for the user login")
