import argparse, os

import pikepdf

parser=argparse.ArgumentParser()

parser.add_argument("--target", help="Target file/folder to remove password from")
parser.add_argument("--password", help="Password to open the PDF")

args=parser.parse_args()

target_path = args.target
pdf_password = args.password

def handle_directory(folder_path):
    """"""
    for file_name in os.listdir(folder_path):
        file_path = os.path.join(folder_path, file_name)
        if file_name.lower().endswith('.pdf'):
            print(file_path)
            pdf = pikepdf.open(file_path, password=pdf_password)
            pdf.save(file_path + "_no_password.pdf")

def handle_file(file_path):
    """"""
    pdf = pikepdf.open(file_path, password=pdf_password)
    pdf.save(file_path + "_no_password.pdf")

if(os.path.isdir(target_path)):
    """Do it like a directory"""
    handle_directory(target_path)
elif os.path.isfile(target_path):
    """Do it like a single file"""
    handle_file(target_path)
else:
    """The Unknown"""
    print('Bhai! Kya pass kar rha hai tu?')