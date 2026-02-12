import os
import stat

ROLE = "guest"

def admin(filename, name):
    global ROLE
    ROLE = "admin"

def user(filename, name):
    global ROLE
    ROLE = "user"

def guest(filename, name):
    global ROLE
    ROLE = "guest"

def grant_permission(filename):
    # FIXME: apply least privilege permissions for all three roles
    if ROLE == "admin":
        os.chmod(filename, stat.S_IRWXU)
    elif ROLE == "user":
        os.chmod(filename, stat.S_IRUSR )
    else:
        os.chmod(filename, 0)

    check_permission(filename)

def check_permission(filename):
    print("The path exists:", os.access(filename, os.F_OK))
    print("Access to read the file:", os.access(filename, os.R_OK))
    print("Access to write the file:", os.access(filename, os.W_OK))
    print("Check if path can be executed:", os.access(filename, os.X_OK))

if __name__ == '__main__':
    filename = input()
    name = input()

    admins = ["Olivia", "Liam"]
    users = ["Emma", "Noah"]

    if name in admins:
        admin(filename, name)
    elif name in users:
        user(filename, name)
    else:
        guest(filename, name)

    grant_permission(filename)
