from page_loader.loader import make_file_name_from_url


def test_make_name_from_url():
    test_urls = ['https://ru.hexlet.io/courses', 'http://gmail.com/index.html']
    expected_names = ['ru-hexlet-io-courses.html', 'gmail-com-index.html']
    actual_names = [make_file_name_from_url(name) for name in test_urls]
    assert expected_names == actual_names