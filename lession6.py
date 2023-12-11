from jinja2 import Environment, FileSystemLoader


persons = [
    {'name': 'Алексей', 'old': 18, 'balance': 5000},
    {'name': 'Михаил', 'old': 32, 'balance': 12400},
    {'name': 'Пётр', 'old': 44, 'balance': 4000},
    {'name': 'Евгений', 'old': 24, 'balance': 3900}
]

file_loader = FileSystemLoader('templates')
env = Environment(loader=file_loader)

template = env.get_template('about.html')

output = template.render(users=persons)

print(output)
