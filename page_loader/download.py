import os
import re
from urllib.parse import urlparse

import requests


def download(url, output_path):
    parsed_url = urlparse(url)
    file_name = re.sub(
        r'\W',
        '-',
        parsed_url.netloc + parsed_url.path,
    ) + '.html'

    path_to_file = os.path.join(output_path, file_name)

    with open(path_to_file, 'w') as file_object:
        response = requests.get(url)
        file_object.write(response.text)

        return path_to_file
