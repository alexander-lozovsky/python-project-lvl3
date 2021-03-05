import os

from page_loader import download


class TestPageLoader:
    def test_download(self, requests_mock, tmp_path):
        url = 'https://ru.hexlet.io/courses'
        requests_mock.get(url, text='mocked response')
        path = download(url, tmp_path)

        assert path == os.path.join(tmp_path, 'ru-hexlet-io-courses.html')
