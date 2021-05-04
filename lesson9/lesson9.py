# f = open('text.txt', 'w')
# f.write('Basketball\n')
# f.write('Micheal Jordan\n')
# f.close()
# w = open('text.txt', 'r')
# print(list(w))
# print(w.seek(0))
# print(w.readlines())
# print(w.seek(18))
# print(w.tell())
# print(w.read())
# w.close()

# with open('text.txt', 'w') as some_file:
#     # some_file = open('text.txt', 'w')
#     some_file.write('Basketball\n')
#     some_file.write('Micheal Jordan\n')
#
# print('')

# import json

# films = {'actions': ['John Wick', 'Avatar']}
# json_obj = json.dumps(films)
# with open('new_db.json', 'w') as json_file:
#     json_file.write(json_obj)
# with open('new_db.json') as json_file:
#     films = json.load(json_file)
# json_obj = json.dumps(films)
# print(json_obj)
# print(type(json_obj))
# value = json.loads(json_obj)
# print(value)
# print(type(value))
