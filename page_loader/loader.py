import os
import requests
import urllib.request

from bs4 import BeautifulSoup
from page_loader.helpers import (make_download_name, make_download_path,
                                 is_local_resource, write, read)


def download_file(url, dir):
    r = requests.get(url)
    write(dir, r.text)


def download_local_files(url, main_file_path, output_dir):
    files_dir = make_download_path(
        output_dir,
        make_download_name(url, '_files')
    )
    os.mkdir(files_dir)

    html_doc = read(main_file_path)
    soup = BeautifulSoup(html_doc, 'html.parser')

    for img in soup.find_all('img'):
        source = img.get('src')
        if is_local_resource(source, url):
            file_ext = source.split('.')[-1]
            file_name = make_download_name(source, f'.{file_ext}')
            file_path = make_download_path(files_dir, file_name)
            urllib.request.urlretrieve(source, file_path)
            img['src'] = file_path

    write(main_file_path, soup.prettify())


def download(url, output_dir):
    main_file_name = make_download_name(url)
    main_file_path = make_download_path(output_dir, main_file_name)

    download_file(url, main_file_path)
    download_local_files(url, main_file_path, output_dir)

    return main_file_path
