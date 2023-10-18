import gdown
import argparse

parser = argparse.ArgumentParser(description="...")
parser.add_argument("--link", type=str)
my_link = parser.parse_args()
set_link = my_link.link

gdown.download_folder(set_link, quiet=True)
