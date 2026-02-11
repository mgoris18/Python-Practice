from string import Template

CONFIG = {
    "SECRET_TOKEN": "super_sensitive_token_value"
}

class Person:

    name = ""
    city = ""

    def __init__(self, name, city):
        self.name = name
        self.city = city

    def __str__(self):
        return self.name

if __name__ == '__main__':
    name = input()
    city = input()

    person = Person(name, city)

    # FIXME: Remove this insecure access and use Template instead
    # print(f"The token is {person.__init__.__globals__['CONFIG']['SECRET_TOKEN']}")

    # ✅ Use Template here to safely print:
    # "Hi, my name is <name> and I live in <city>."
    template = Template('Hi, my name is $name and I live in $city.')
    output = template.substitute(name=name, city=city)
    print(output)