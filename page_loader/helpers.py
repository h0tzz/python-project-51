import os
import re

from urllib.parse import urlparse


def write(file_path, content):
    with open(file_path, 'a') as f:
        f.write(content)


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


def extract_root_domain(url):
    t = urlparse(url).netloc
    return '.'.join(t.split('.')[-2:])


def strip_scheme(url):
    parsed = urlparse(url)
    scheme = "%s://" % parsed.scheme
    return parsed.geturl().replace(scheme, '', 1)


def make_download_name(url, ext='.html'):
    strip_url = strip_scheme(url)
    url_without_ext = os.path.splitext(strip_url)[0]
    file_name = re.sub(r'[^\da-zA-Z]', '-', url_without_ext)
    return f'{file_name}{ext}'


def make_download_path(root_dir, sub_dir_or_file):
    return os.path.join(root_dir, sub_dir_or_file)


def is_local_resource(main_url, src):
    main_url_root_domain = extract_root_domain(main_url)
    src_root_domain = extract_root_domain(src)
    return main_url_root_domain == src_root_domain
