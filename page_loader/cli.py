import os

import argparse


def parse_arguments():
    parser = argparse.ArgumentParser(description='download page')

    parser.add_argument('url', type=str, help='url to download from')
    parser.add_argument(
        '-o', '--output',
        help='directory to download',
        default=os.getcwd()
    )

    args = parser.parse_args()

    return args
