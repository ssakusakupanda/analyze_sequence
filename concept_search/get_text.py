#coding:utf-8

import subprocess
import re

def check(text):
  if re.search(keyword,text):
    w.write(text)
    return

#対象
keyword = input("search keyword: ")

#専用ディレクトリ作成
cmd = 'mkdir ' + 'concept/'+ keyword
try:
  subprocess.call(cmd,shell=True)
except:
  print("Error.")

#ファイル処理
f = open('00000000.txt','r')
w = open("concept/" + keyword + "/" + keyword + '_sentence.txt','w')

for line in f:
  check(line)
