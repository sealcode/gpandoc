from tempfile import NamedTemporaryFile
import tempfile
import os
import subprocess
import zipfile 


def unzip(source_filename, dest_dir):
    with zipfile.ZipFile(source_filename) as zf:
        zf.extractall(dest_dir)

def extract_template_file():     
    unzip("/home/afar/gpandoc2/zips/nowy.zip", "/home/afar/gpandoc2/temp/")


def main():
    extract_template_file()
    subprocess.call(["ls","-la"])


if __name__ == '__main__':
    main()


