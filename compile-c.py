# compile the c files from a dir structure

import os, time

for (root, dirs, files) in os.walk(os.getcwd()):
    for file in files:
        source_name = '.'.join(file.split('.')[:-1])
        extension = file.split('.')[-1]
        if extension == 'c':
            print("Compiling source ", file, end=" ")
            time.sleep(2)
            os.system('gcc ' + file + ' -o ' + source_name + '.exe ' + '2>generic.err')
            print("Done")


#exit(4)

##########################################
pathc = '/opt/training-python/proiecte/training/day3/comp.c'
output = os.popen('gcc {} -o {} 2>&1'.format(pathc, 'comp.exe')).read()
print(output)
