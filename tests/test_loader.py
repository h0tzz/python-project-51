import os
import pytest
import tempfile
import requests
import requests_mock

from page_loader import download
from page_loader.loader import make_resource_path


@pytest.fixture(scope='module')
def out_dir():
    return tempfile.TemporaryDirectory()

def test_loader(out_dir, requests_mock):
    url = 'https://ru.hexlet.io/courses'
    requests_mock.register_uri('GET', url, text='resp')

    expected = make_resource_path(url, out_dir.name, '.html')
    actual = download(url, out_dir.name)

    assert requests.get(url).text == 'resp'
    assert expected == actual
