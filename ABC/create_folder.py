import os
import sys

def create_folder_with_memo(folder_name):
    if not os.path.exists(folder_name):
        os.mkdir(folder_name)

    file_names = ["A.py", "B.py", "C.py", "D.py", "E.py", "F.py", "G.py", "memo.md"]
    for file_name in file_names:
        file_path = os.path.join(folder_name, file_name)
        if not os.path.exists(file_path):
            with open(file_path, 'w') as f:
                f.write("")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python create_folder.py FOLDER_NAME")
        sys.exit(1)
    folder_name = sys.argv[1]
    create_folder_with_memo(folder_name)
