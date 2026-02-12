import os
import stat

ROLE = "user"

def admin(filename, name):
    global ROLE
    ROLE = "admin"
    return name

def user(filename, name):
    global ROLE
    ROLE = "user"
    return name

def grant_permission(filename):
    # FIXME: set permissions based on ROLE using least privilege
    if ROLE == "admin":
        os.chmod(filename, stat.S_IRWXU)
    else:
        os.chmod(filename, stat.S_IRUSR)
    check_permission(filename)

def check_permission(filename):
    path1 = os.access(filename, os.F_OK)
    print("The path exists:", path1)

    path2 = os.access(filename, os.R_OK)
    print("Access to read the file:", path2)

    path3 = os.access(filename, os.W_OK)
    print("Access to write the file:", path3)

    path4 = os.access(filename, os.X_OK)
    print("Check if path can be executed:", path4)

if __name__ == '__main__':
    filename = input()
    name = input()

    admins = []
    with open(filename) as f:
        for line in f:
            admins.append(line.strip())

    if name in admins:
        admin(filename, name)
    else:
        user(filename, name)

    grant_permission(filename)
