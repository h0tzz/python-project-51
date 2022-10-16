import os
import pytest
import tempfile
import requests
import requests_mock

from page_loader import download
from page_loader.loader import make_file_name_from_url


@pytest.fixture(scope='module')
def out_dir():
    return tempfile.TemporaryDirectory()

def test_loader(out_dir, requests_mock):
    url = 'https://ru.hexlet.io/courses'
    expected_name = make_file_name_from_url(url)
    out_dir_name = out_dir.name

    requests_mock.register_uri('GET', url, text='resp')

    actual = download(url, out_dir_name)
    expected = os.path.join(out_dir_name, expected_name)

    assert requests.get(url).text == 'resp'
    assert expected == actual
