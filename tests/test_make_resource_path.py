import os

from page_loader.loader import make_resource_path


def test_make_resource_path():
    test_urls = ['https://ru.hexlet.io/courses', 'http://gmail.com/index.html']
    expected_names = [
        os.path.join(os.getcwd(), 'ru-hexlet-io-courses.html'),
        os.path.join(os.getcwd(), 'gmail-com-index.html')
    ]
    actual_names = [make_resource_path(name, postfix='.html') for name in test_urls]
    assert expected_names == actual_names