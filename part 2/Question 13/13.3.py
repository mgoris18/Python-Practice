import os
import stat

ROLE = "user"

def set_role(name):
    global ROLE
    admins = ["Zoe", "Mia"]
    auditors = ["Ethan", "Aiden"]

    if name in admins:
        ROLE = "admin"
    elif name in auditors:
        ROLE = "auditor"
    else:
        ROLE = "user"

def grant_permission(filename):
    # FIXME: apply least privilege permissions based on ROLE
    if ROLE == "admin":
        os.chmod(filename, stat.S_IRWXU)
    elif ROLE == "auditor":
        os.chmod(filename, stat.S_IRUSR)
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

    set_role(name)
    grant_permission(filename)
