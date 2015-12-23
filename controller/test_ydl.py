import logging

from youtube_dl import YoutubeDL
from youtube_dl.utils import format_bytes
from model.ydl_logger import YDLLogger


def my_hook(d):
    print(d)

ydl_opt = {
    'logger': YDLLogger(),
    'progress_hooks': [my_hook]
}


def test_ydl():
    ydl = YoutubeDL(ydl_opt)
    with ydl:
        try:
            info_dict = ydl.extract_info('https://www.youtube.com/watch?v=QwoghxwETng', download=False)
            # print(info_dict.keys())
            #print(info_dict['title'])
            #print(ydl.list_formats(info_dict))
            #for f in info_dict['formats']:
            #    filesize = f.get('filesize') if f.get('filesize') else f.get('filesize_approx')
            #    filesize2 = f['filesize'] if f['filesize'] else f['filesize_approx']
            #    print("%s, %s, %s, %s" % (f['format'], f['ext'], ydl.format_resolution(f), format_bytes(filesize2)))

            #print(ydl.list_formats(info_dict))

        except Exception as e:
            print(e)
