from htmlnode import *
import os
import shutil
import logging


logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def recursive_copy(src, dst):
    """
    Recursively copies all files and directories from src to dst.
    """
    # Check if the destination directory exists, if not, create it
    if not os.path.exists(dst):
        os.mkdir(dst)
        logging.info(f"Directory created: {dst}")

    for item in os.listdir(src):
        src_item = os.path.join(src, item)
        dst_item = os.path.join(dst, item)

        # Check if the item is a directory, then recurse
        if os.path.isdir(src_item):
            recursive_copy(src_item, dst_item)
        else:
            shutil.copy(src_item, dst_item)
            logging.info(f"Copied {src_item} to {dst_item}")



def copy_static(src="static", dst="public"):
    src_directory = src
    dst_directory = dst

    # Ensure the destination directory is empty before copying
    if os.path.exists(dst_directory):
        shutil.rmtree(dst_directory)
        logging.info(f"Cleaned existing directory: {dst_directory}")

    # Copy contents from src to dst
    recursive_copy(src_directory, dst_directory)
    logging.info("All contents copied successfully.")
