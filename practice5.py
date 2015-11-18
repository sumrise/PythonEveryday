#!python2.7
# coding=UTF-8

# info 第 0005 题：你有一个目录，装了很多照片，把它们的尺寸变成都不大于 iPhone5 分辨率的大小。

__author__ = 'sumrise'

from PIL import Image
import glob, os

filespath = '/Users/guowei07/Desktop/picpractice/*.jpg'


def process():
    for files in glob.glob(filespath):
        path, filename = os.path.split(files)

        opfile = r'/Users/guowei07/Desktop/picpractice2/'
        if not os.path.isdir(opfile):
            os.mkdir(opfile)
        im = Image.open(files)
        w, h = im.size
        while w > 1136 or h > 640:
            w /= 2
            h /= 2
        im_ss = im.resize((int(w), int(h)))
        im_ss.save(opfile + filename)


if __name__ == '__main__':
    process()
    print 'over'
