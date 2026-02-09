import os
import shutil


PUBLIC_DIR = "./public/"
STATIC_DIR = "./static/"


def clear_public_dir(public_dir: str):
    public_dir = os.path.abspath(public_dir)
    dir = os.path.exists(public_dir)
    if dir:
        shutil.rmtree(public_dir)
    os.mkdir(public_dir)

def copy_files(static_dir: str, public_dir: str):
    static_dir = os.path.abspath(static_dir)
    public_dir = os.path.abspath(public_dir)
    files = os.listdir(static_dir)
    for file in files:
        print("processing: ",file)
        path_source = os.path.join(static_dir,file)
        path_dest = os.path.join(public_dir,file)
        if os.path.isdir(path_source):
            os.mkdir(path_dest)
            copy_files(path_source, path_dest)

        if os.path.isfile(path_source):
            result = shutil.copy(path_source,public_dir)
            print(result)

def main():
    clear_public_dir(PUBLIC_DIR)
    print(f"{PUBLIC_DIR} directory cleared")
    copy_files(STATIC_DIR, PUBLIC_DIR)


if __name__ == "__main__":
    main()
