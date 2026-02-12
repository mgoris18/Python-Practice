import os
import stat

ROLE = "user"

def set_role(name):
    global ROLE
    admins = ["Harper", "Reagan"]
    if name in admins:
        ROLE = "admin"
    else:
        ROLE = "user"

def grant_permission(filename):
    # FIXME: apply least privilege based on ROLE and filename extension
    if ROLE == "admin":
        os.chmod(filename, stat.S_IRWXU)
    elif filename.endswith(".txt"):
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
