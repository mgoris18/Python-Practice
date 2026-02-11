from string import Template

CONFIG = {
    "DB_PASSWORD": "super_hidden_password"
}

class Client:

    def __init__(self, company, contact):
        self.company = company
        self.contact = contact

    def __str__(self):
        return self.company

if __name__ == '__main__':
    company = input()
    contact = input()

    client = Client(company, contact)

    # FIXME: Remove insecure reference
    # print(client.__init__.__globals__['CONFIG']['DB_PASSWORD'])

    # TODO: Use Template to safely print:
    # "<company> is managed by <contact>."
    t = Template("$company is managed by $contact")
    output = t.substitute(company = company, contact = contact)
    print(output)