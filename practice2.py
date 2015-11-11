#!python2.7
# coding=UTF-8

# info TODO

__author__ = 'sumrise'

import random, string

field = string.letters + string.digits


def generator():
    return '-'.join([''.join(random.sample(field, 4)) for i in range(4)])


if __name__ == '__main__':
    for i in range(200):
        print str(i) + " " + generator()
