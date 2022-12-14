print("create a new account")
username =  input("Enter user Name: ")
password =  input("Enter your Password")

print("your account is created successfully")

print("login now")

login_username =  input("Enter user Name: ")
login_password =  input("Enter your Password")

if login_username == username and login_password == password:
     print("login successfully")
else:
    print("invalid cradintials")