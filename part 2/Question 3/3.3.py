from string import Template

CONFIG = {
    "ADMIN_SECRET": "root_admin_key_exposed"
}

class Employee:

    def __init__(self, first, last):
        self.first = first
        self.last = last

    def __str__(self):
        return f"{self.first} {self.last}"

if __name__ == '__main__':
    first = input()
    last = input()

    emp = Employee(first, last)

    # FIXME: Remove insecure code
    # print(emp.__class__.__init__.__globals__['CONFIG']['ADMIN_SECRET'])

    # TODO: Use Template to safely print:
    # "<first> <last> has been added to the system.
    t = Template("$first $last has been added to the system.")
    output = t.substitute(first = first, last = last)
    print(output)
