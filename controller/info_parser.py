from youtube_dl import YoutubeDL
from youtube_dl.utils import format_bytes

from model.ydl_object import YDLObject


class InfoParser():
    def __init__(self, url=None, ydl_opt={}):
        self.__ydl_opt = ydl_opt
        self.__url = url
        self.__ydl = YoutubeDL(self.__ydl_opt)
        self.__ydl_obj = YDLObject()

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url):
        self.__url = url

    @property
    def ydl_object(self):
        return self.__ydl_obj

    def generate_info(self):
        try:
            info_dict = self.__ydl.extract_info(self.__url, download=False)
            self.__ydl_obj.title = info_dict['title']
            self.__ydl_obj.url = self.__url
            for format in info_dict['formats']:
                filesize = format.get('filesize') if format.get('filesize') else format.get('filesize_approx')
                self.__ydl_obj.format_info.append({
                    'format_id': format['format'],
                    'extension': format['ext'],
                    'resolution': self.__ydl.format_resolution(format),
                    'filesize': format_bytes(filesize)
                })
            return True
        except Exception as e:
            print(e)
            return False



