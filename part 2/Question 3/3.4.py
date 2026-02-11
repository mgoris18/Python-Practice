from string import Template

CONFIG = {
    "SECRET_FLAG": "TOP-SECRET"
}

class Member:

    def __init__(self, username, role):
        self.username = username
        self.role = role

    def __str__(self):
        return self.username

if __name__ == '__main__':
    username = input()
    role = input()

    member = Member(username, role)

    # FIXME: Do NOT print secrets
    # print(member.__init__.__globals__['CONFIG']['SECRET_FLAG'])

    # TODO: Use Template to safely print:
    # "<username> has role <role>."
    t = Template('$username has role $role')
    output = t.substitute(username = username, role = role)
    print(output)