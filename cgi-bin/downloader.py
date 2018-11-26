from pprint import pprint
from pytube import YouTube
import re
import sys, os

def searchInCache(url):
    for downloadedFile in os.scandir('cache'):
        if (downloadedFile.name == url.replace('https://www.youtube.com/watch?v=','')+'.webm'):
            return downloadedFile
    if(sum(os.path.getsize(f) for f in os.listdir('cache') if os.path.isfile(f))>3e+8):
        cleanCache()
    return None


def download(url):
    yt = YouTube(url)
    streams = yt.streams.filter(only_audio=True).all()
    maxAbr = 0
    selectedStream = None
    for stream in streams:
        abrStr = stream.abr.replace('kbps','')
        abr = int(abrStr)
        if(abr>maxAbr):
            maxAbr = abr
            selectedStream = stream
    pprint(selectedStream)
    selectedStream.download('cache',filename = url.replace('https://www.youtube.com/watch?v=',''))
    return yt.title+'.webm'

def cleanCache():
    folder = 'cache'
    for the_file in os.listdir(folder):
        file_path = os.path.join(folder, the_file)
        try:
            if os.path.isfile(file_path):
                os.unlink(file_path)
        except Exception as e:
            print(e)

if __name__ == '__main__':
    download('https://www.youtube.com/watch?v=mDFBTdToRmw')
    searchInCache('https://www.youtube.com/watch?v=mDFBTdToRmw')