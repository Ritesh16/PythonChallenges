numbers = [1, 2, 3]

new_list = [n+1 for n in numbers]

print(new_list)

names = ['Alex', 'Beth', 'Dave', 'Freddie', 'Smith', 'Stacy']
new_names = [name for name in names if len(name) < 5]
print(new_names)