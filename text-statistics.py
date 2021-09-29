import pprint

# model data structure
stat = {
    'nr_lines' : 0,
    'nr_words' : 0,
    'nr_unique_words' : 0,
    'unique_words' : {'somnoroase', 'lebada'},
    'word_frecquency' : {
        'somonoroase' : 3,
        'lebada' : 1
        #...
    }
}

stat = {}

with open("day2/poezie.txt", 'r', encoding='utf-8') as my_file:
    lines = my_file.readlines()
    stat['nr_lines'] = len(lines)

sum = 0 # suma totala a cuvintelor
mul = set() # set cu toate cuvintele unice
dictionar = {}

for line in lines:
    word_list = line.split()
    sum += len(word_list)
    for word in word_list:
        word = word.lower()
        mul.add(word)
        if word not in dictionar:
            dictionar[word] = 1
        else:
            dictionar[word] += 1

stat['nr_words'] = sum
stat['unique_words'] = sorted(mul)
stat['word_frequency'] = dictionar
pprint.pprint(stat)
