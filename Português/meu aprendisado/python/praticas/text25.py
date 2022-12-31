import os
n = r'E:'
nr = ''
for root, dirt, files in os.walk(n):
    print(dirt, files)
    for file in files:
        v = os.path.join(root, file)
        print(v)
        print(os.path.splitext(file))
