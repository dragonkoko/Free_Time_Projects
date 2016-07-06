#!/usr/bin/env python
# -*- coding: utf-8 -*-
from __future__ import division
from nltk.corpus import stopwords
import re

def main():
    datafile = "write the name of the file to read from"
    outputFile = "write the name of the file to write the output"
    fileRead = open(datafile, 'r+')
    text = fileRead.read()
    removeCharacters = [':',',','.',';','/','"','[',']','{','}','<','>','#','$','%','^','&','*','“','”','’','‘','€','£'
                        '?','!','\\','~','`','0','1','2','3','4','5','6','7','8','9','(',')','@']

    for char in removeCharacters:
        print 'replacing ' + char
        text = text.replace(char,'')
    print 'got the chars'

    dashes = ['-','‒','—','―','+','=','–']
    for dash in dashes:
        text = text.replace(dash, ' ')
    print 'got the dashes'

    text = text.replace('\n',' ')
    text = re.sub(' +',' ',text.lower())
    print text

    stop = stopwords.words('english')
    finalText = [i for i in text.split() if i not in stop]
    data = finalText
    wordCountData = {}
    for word in data:
        try:
            word.decode('ascii')
        except UnicodeDecodeError:
            continue
        if word in wordCountData:
            wordCountData[word] += 1
        else:
            wordCountData[word] = 1

    valueAccumulator = 0
    for key,value in wordCountData.iteritems():
        valueAccumulator += value
    print valueAccumulator
    print valueAccumulator
    print 10000/valueAccumulator
    itemValue = 10000/valueAccumulator
    print itemValue

    naturalDisasterWordsDataWrite = {}
    for key,value in wordCountData.iteritems():
        naturalDisasterWordsDataWrite[key] = value*itemValue
        if (value*itemValue) % 1 > 0.5:
            naturalDisasterWordsDataWrite[key] = int(value*itemValue) + 1
        else:
            naturalDisasterWordsDataWrite[key] = int(value*itemValue)

    file = open(outputFile, 'w+')
    uselessWords = ['one','two','three','four','five','six','seven','eight','nine','zero','ten','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
    for key,value in naturalDisasterWordsDataWrite.iteritems():
        for i in range(0, value):
            if key in uselessWords:
                continue
            else:
                file.write(key+"\n")

    file.close()

if __name__ == "__main__":
    main()
