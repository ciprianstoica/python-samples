import pprint


def my_sort(e):
    return e[1]


nr_nonempty_lines = 0
nr_words = 0
dict_frecv = {}

with open(r'poezie.txt', 'r', encoding='utf-8') as poezie:
    for line in poezie:
        # skip empty lines
        if line.strip() == '':
            continue

        nr_nonempty_lines += 1
        words = line.split()
        for c in words:
            c = c.strip('*;?-„ .,\'"').lower()
            # skip empty words
            if c != '':
                nr_words += 1
                if c in dict_frecv:
                    dict_frecv[c] += 1
                else:
                    dict_frecv[c] = 1


print('Nr linii nenule: ', nr_nonempty_lines)
print('Nr cuvinte: ', nr_words)
print('Set cuvinte unice: ', sorted(list(dict_frecv.keys())))
print('Frecvente cuvinte: ', dict_frecv)
pprint.pprint(dict_frecv)

list_frecv = []

for k in dict_frecv:
    list_frecv.append((k, dict_frecv[k]))

print(list_frecv)
print(sorted(list_frecv, key=my_sort, reverse=True))



