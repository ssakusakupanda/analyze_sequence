#coding:utf-8

import subprocess
import re

def check(text):
    for word in keywords:
        if re.search(word,text):
            w.write(text)

#専用ディレクトリ作成
cmd = 'mkdir concept'
try:
  subprocess.call(cmd,shell=True)
except:
  print("Error.")

#ファイル処理
fn = '00000000.txt'
w = open('concept/emotion_sequence.txt','w')
keywords = []

#感情
emotions = ['joy','trust','fear','surprise','sadness','disgust','anger','anticipation']

#感情別分類
for emo in emotions:

    #辞書作成
    with open("source/" + emo + ".txt",'r') as emo_f:
        line = emo_f.readline()
        keywords.append(line.strip())
        while line:
            line = emo_f.readline()
            keywords.append(line.strip())
        keywords.remove('')

#文章チェック
f = open(fn,'r')
for line in f:
    check(line)
