import argparse
import os

from page_loader import download


def run():
    default_output_path = os.getcwd()

    parser = argparse.ArgumentParser()
    parser.add_argument(
        '-o',
        '--output',
        help=f"output dir (default: '{default_output_path}')",
        default=default_output_path,
    )
    parser.add_argument('-v', '--version', help='output the version number')
    parser.add_argument('url', help='url to download')

    args = parser.parse_args()
    file_path = download(
        args.url,
        args.output,
    )
    print(f"Page was successfully downloaded into '{file_path}'")
