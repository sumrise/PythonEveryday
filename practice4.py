#!python2.7
# coding=UTF-8

# info 第 0004 题：任一个英文的纯文本文件，统计其中的单词出现的个数。

__author__ = 'sumrise'

import re

fileName = "/Users/guowei07/Desktop/article.txt"

linesCount = 0
wordsCount = 0
charsCount = 0
wordsDict = {}
linesList = []

with open(fileName, "r") as f:
    for line in f:
        linesCount += 1
        charsCount += len(line)
        match = re.findall(r'[^a-zA-Z0-9]+', line)
        for i in match:
            line = line.replace(i, ' ')
        linesList = line.split()

        for i in linesList:
            if i not in wordsDict:
                wordsDict[i] = 1
            else:
                wordsDict[i] += + 1
print("words count is ", len(wordsDict))
