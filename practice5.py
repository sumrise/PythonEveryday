#!python2.7
# coding=UTF-8

# info TODO

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
