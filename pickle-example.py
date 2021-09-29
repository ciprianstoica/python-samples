import pickle

data1 = { 'a': ['hello', 'world'],
         'b' : 123
         }

data2 = { 'c': [12, 14],
         'd' : 'sdf'
         }


with open('filename.pickle', 'wb') as file:
    pickle.dump(data1, file)

with open('filename.pickle', 'ab') as file:
    pickle.dump(data2, file)

with open('filename.pickle', 'rb') as file:
    datar1 = pickle.load(file)
    datar2 = pickle.load(file)


print(datar1, datar2)

#######################################

# with open('filename.pickle', 'wb') as file:
#     pickle.dump(data, file)

##########################################

