import os
import re
import requests

from urllib.parse import urlparse


def write(file_path, content):
    with open(file_path, 'w') as f:
        f.write(content)


def strip_scheme(url):
    parsed = urlparse(url)
    scheme = "%s://" % parsed.scheme
    return parsed.geturl().replace(scheme, '', 1)


def make_file_name_from_url(url):
    parsed_url = strip_scheme(url)
    url_without_ext = os.path.splitext(parsed_url)[0]
    result_url = re.sub(r'[^\da-zA-Z]', '-', url_without_ext)
    file_name = f'{result_url}.html'
    return file_name


def download(url, output_dir):
    file_name = make_file_name_from_url(url)
    file_path = os.path.join(output_dir, file_name)
    r = requests.get(url)
    write(file_path, r.text)
    return file_path
