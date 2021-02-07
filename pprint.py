import pprint

message = 'It is my first python program'
i = {}

for j in message:
    i.setdefault(j, 0)
    i[j] = i[j] + 1

pprint.pprint(i)
