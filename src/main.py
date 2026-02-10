from blocks import markdown_to_html_node
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

def extract_title(markdown):
    lines = markdown.split("\n")
    header = ""
    for line in lines:
        if not line.startswith("#"):
            continue
        if not line.startswith("##"):
            header = line.strip("# ")
    return header

def generate_page(from_path: str, template_path: str,dest_path: str):
    print(f"Generating page from {from_path} to {dest_path} using {template_path}")
    with open(from_path) as file:
        from_file = file.read()
    with open(template_path) as file:
        template_file = file.read()
    template_file = template_file.replace("{{ Title }}", extract_title(from_file))
    template_file = template_file.replace("{{ Content }}", markdown_to_html_node(from_file).to_html())
    with open(dest_path,'w') as file:
        file.write(template_file)



def main():
    clear_public_dir(PUBLIC_DIR)
    print(f"{PUBLIC_DIR} directory cleared")
    copy_files(STATIC_DIR, PUBLIC_DIR)
    generate_page('content/index.md','template.html','public/index.html')


if __name__ == "__main__":
    main()
