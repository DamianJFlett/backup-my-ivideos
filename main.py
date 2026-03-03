import sys
import os
import argparse
from convert import convert_and_save

def valid_dir(path):
    if not os.path.isdir(path):
        raise argparse.ArgumentTypeError(f"'{path}' is not a valid directory")
    return os.path.abspath(path)

def main():
    parser = argparse.ArgumentParser(description="extract and move files from iphone")
    parser.add_argument('iphone_photo_location', type=valid_dir, help="The folder where the iphone's photos are located")
    parser.add_argument('save_location', type=valid_dir, help="The location to save to")

    args = parser.parse_args()

    in_loc = args.iphone_photo_location
    out_loc = args.save_location



if __name__ == "__main__":
    main()