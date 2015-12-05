class YDLObject():
    def __init__(self):
        self.__title = None
        self.__info = []

    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title):
        self.__title = title

    @property
    def info(self):
        return self.__info

    @info.setter
    def info(self, info):
        self.__info = info

