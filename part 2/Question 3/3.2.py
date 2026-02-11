from string import Template

CONFIG = {
    "API_TOKEN": "my_super_secret_key"
}

class Account:

    def __init__(self, username, email):
        self.username = username
        self.email = email

    def __str__(self):
        return self.username

if __name__ == '__main__':
    username = input()
    email = input()

    account = Account(username, email)

    # FIXME: Remove insecure global access
    # print(account.__init__.__globals__['CONFIG']['API_TOKEN'])

    # Use Template to print:
    # "User <username> registered with email <email>."
    template = Template("User $username registered with email $email.")
    output = template.substitute(username = username, email = email)
    print(output)