import os

for tab in os.walk('.\\data'):
    if len(tab) < 3:
        continue
    path, sub, files = tab
    path = path[1:]
    for file in files:
        fullpath = f"{path}\\{file}"
        if len(fullpath.split('\\')) < 4:
            continue
        print(fullpath)