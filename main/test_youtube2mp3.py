import os.path
import string
import unittest

import youtube2mp3
from pytube import YouTube
from pytube.exceptions import VideoUnavailable
from youtube2mp3 import Youtube2Mp3


class TestYoutube2Mp3(unittest.TestCase):

    def setUp(self):
        self.y = Youtube2Mp3

    def test_valid_youtube_url(self):
        self.y.setVideoURL(self,'https://www.youtube.com/watch?v=Yrtm7d3TJbs')

    def test_invalid_youtube_url(self):
        with self.assertRaises(VideoUnavailable):
            self.y.setVideoURL('example invalid url')

    def test_valid_save_path(self):
        self.y.set_destination()
        destination = self.y.get_destination()
        os.path.isdir(destination)

    def test_invalid_save_path(self):
        pass

    def test_successful_mp3_save(self):
        pass


if __name__ == '__main__':
    unittest.main