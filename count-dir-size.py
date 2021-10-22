import os

# my_dir = '/opt/training-python/proiecte/training'
my_dir = os.getcwd()


size = 0
nr_files = 0

for root, dirs, files in os.walk(my_dir):
    print(root, dirs, files)
    for file in files:
        size += os.path.getsize(root + '/' + file)
    for dir in dirs:
        size += os.path.getsize(root + '/' + dir)

    nr_files += len(dirs) + len(files)

print('Total size {} bytes on {} files.'.format(size, nr_files))