import logging
import os
import shutil


PUBLIC_DIR = "./public"
STATIC_DIR = "./static"


def clear_public_dir(public_dir: str):
    dir = os.path.exists(public_dir)
    if dir:
        shutil.rmtree(public_dir)
    os.mkdir(public_dir)

def copy_files(static_dir: str, public_dir: str):
    files = os.listdir(static_dir)
    for file in files:
        if os.path.is_dir(file):
            new_folder = os.path.join(public_dir,file)
            print(new_folder,os.path.isfile(file))
            os.mkdir(new_folder)

            new_static_dir = os.path.join(static_dir,file)
            logging.info(new_static_dir)

            new_public_dir = os.path.join(public_dir,file)
            logging.info(new_public_dir)

            copy_files(new_static_dir, new_public_dir)
            continue
        result = shutil.copy(file,public_dir)
        logging.info("Coppied:", result)

def main():
    clear_public_dir(PUBLIC_DIR)
    print(f"{PUBLIC_DIR} directory cleared")
    copy_files(STATIC_DIR, PUBLIC_DIR)


if __name__ == "__main__":
    main()
