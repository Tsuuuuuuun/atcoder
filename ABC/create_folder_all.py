import os
import sys

for i in range(1, sys.argv[1] + 1):
    folder_name = f"ABC{i:03}"
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)
    file_names = ["memo.md", "A.py", "B.py", "C.py", "D.py"]
    for file_name in file_names:
        file_path = os.path.join(folder_name, file_name)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                f.write("")
    if i >= 126:
        file_names = ["E.py", "F.py"]
        for file_name in file_names:
            file_path = os.path.join(folder_name, file_name)
            if not os.path.exists(file_path):
                with open(file_path, 'w') as f:
                    f.write("")
    if i >= 212:
        file_names = ["G.py"]
        for file_name in file_names:
            file_path = os.path.join(folder_name, file_name)
            if not os.path.exists(file_path):
                with open(file_path, 'w') as f:
                    f.write("")
