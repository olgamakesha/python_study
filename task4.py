dict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}
new_dict = {}

for k in dict:
    if dict[k] >= 3:
        new_dict[k] = dict[k]

print(new_dict)