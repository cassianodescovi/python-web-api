from jinja2 import Environment, FileSystemLoader


env = Environment(loader=FileSystemLoader("."))
template = env.get_template("email.template.txt")

data = {
    "name": "Cassiano",
    "products": [
        {"name": "iphone", "price": 13000.320},
        {"name": "ferrari", "price": 900000.430},
    ],
    "special_customer": True
}

print(template.render(**data))