name = 'wOJciech'

print(len(name))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name[-3:])
print(name[2:5])
print(name[3:])

channel = 'Jak żyć panie jeden'
print(channel.split(" "))

join_string = " "
print(join_string.join(['Jak', 'żyć', 'panie', 'jeden']))

print(join_string.join(channel))

print(name.startswith("W"))
print(name.startswith("w"))
print(name.endswith("h"))
print(name.endswith("H"))
print(name.rstrip("h"))
print(name.lstrip("w"))
print(name.strip())

first_name = 'Wojciech'
last_name = 'Jarczak'

print(first_name + " " + last_name)
join_string = " "
print(join_string.join([first_name, last_name]))

james_bond = 7
print(str(james_bond).zfill(3))

