import os, sys

test_file_data = ''

existing_filename = 'test_file.txt'
new_filename = 'new_test_file.txt'

if not os.path.exists(existing_filename):
    print("file " + existing_filename + " not exists")
    sys.exit()

if not os.path.isfile(existing_filename):
    print("file " + existing_filename + " is not a file")
    sys.exit()

existing_test_file = open(existing_filename, 'r')
try:
    test_file_data = existing_test_file.read()
except:
    print("unable to read " + existing_filename)
    sys.exit()
finally:
    existing_test_file.close()


try:
    new_file = open(new_filename, 'w')
    test_file_data_len = len(test_file_data)
    k = test_file_data_len - 1

    while True:
        if k < 0:
            break
        new_file.write(test_file_data[k])
        k = k - 1
except:
    print("unable to open or create " + new_filename)
    sys.exit()
finally:
    new_file.close()