import os
import stat

ROLE = "viewer"

def set_role(name):
    global ROLE
    admins = ["Lucas"]
    editors = ["Amelia"]
    viewers = ["Elijah"]

    if name in admins:
        ROLE = "admin"
    elif name in editors:
        ROLE = "editor"
    elif name in viewers:
        ROLE = "viewer"
    else:
        ROLE = "none"

def grant_permission(filename):
    # FIXME: apply least privilege permissions for all roles
    if ROLE == "admin":
        os.chmod(filename, stat.S_IRWXU)
    elif ROLE == "editor":
        os.chmod(filename, stat.S_IRUSR | stat.S_IWUSR)
    elif ROLE == "viewer":
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
