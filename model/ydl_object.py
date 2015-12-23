class YDLObject():
    def __init__(self):
        self.__title = None
        self.__current_format = None
        self.__format_info = []
        self.__url = None

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def current_format(self):
        return self.__current_format

    @current_format.setter
    def current_format(self, current_format):
        self.__current_format = current_format

    @property
    def format_info(self):
        return self.__format_info

    @format_info.setter
    def info(self, info):
        self.__format_info = info

    @property
    def url(self):
        return self.__url

    @url.setter
    def url(self, url):
        self.__url = url
