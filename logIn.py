## password

def password(user):
    admin = user
    if(admin == "admin1"):
        password = input("Password\t: ")
        if (password == "2021"):
            return "hidayah"
        else:
            print("Password salah!")
    elif(admin == "admin2"):
        password = input("Password\t: ")
        if (password == "2022"):
            return "hidayah"
        else:
            print("Password salah!")
    else:
        print("User tidak terdaftar!")

## warning : interpreted      
def user():
    user = input("Nama User\t: ")
    logIn = password(user)
    return logIn