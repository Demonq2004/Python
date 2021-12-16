#Dictionary
#zbiór wartości, nie posiada indexu, zawiera pary klucz-wartość, mutowalność

options = {
    'env':'production',
    'db':'mysql',
    'version':1.0,
    'show_errors': True
}

print(options)

print(options['env'])
print(options['version'])

options['version'] = 2.0

print(options['version'])

options['user'] = 'root'

print(options)

# del options['db']
# print(options)


print(options.get('db'))


options.update({
    'user' : 'admin',
    'app' : 0,
    'version' : 2.0
})

print(options)

for key in options:
    print(options[key])