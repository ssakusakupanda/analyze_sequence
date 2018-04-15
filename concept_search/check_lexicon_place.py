#coding:utf-8

import subprocess
import re

def check(text):
  for word in keywords:
    matchOB = re.search(word,text)
    if matchOB:
      strage.append(text)
      if  re.search(keyword,text).start() < matchOB.start():
        strage_back.append(text)
      else:
        strage_forward.append(text)
      return

#感情
emotions = ['joy','trust','fear','surprise','sadness','disgust','anger','anticipation']

keyword = input("search file: ")
filename = 'concept/' + keyword + "/" + keyword + "_sentence.txt"

#専用ディレクトリ作成
cmd = 'mkdir ' + 'concept/' + keyword
try:
  subprocess.call(cmd,shell=True)
except:
  print("Error.")

#感情別分類
for emo in emotions:

  #辞書作成
  keywords = [] 
  with open("source/" + emo + ".txt",'r') as emo_f:
    line = emo_f.readline()
    keywords.append(line.strip())
    while line:
      line = emo_f.readline()
      keywords.append(line.strip())
    keywords.remove('')

  #分類
  f = open(filename,'r')
  strage = []
  strage_back = []
  strage_forward = [] 
  for line in f:
      check(line)
  
#ファイル書き込み(全部)
  
  #専用ディレクトリ作成
  cmd = 'mkdir ' + 'concept/' + keyword + '/match_emotion'
  try:
    subprocess.call(cmd,shell=True)
  except:
    print("Error.")
  
  #書き込み
  w = open('concept/' + keyword + '/match_emotion/' + keyword + "_" + emo + '.txt','w')
  strage_uniq = set(strage)
  for text in strage_uniq:
    w.write(text)
  
#ファイル書き込み(後半)
  
  #専用ディレクトリ作成
  cmd = 'mkdir ' + 'concept/' + keyword + '/back_lexicon'
  try:
    subprocess.call(cmd,shell=True)
  except:
    print("Error.")
  
  #書き込み
  w_b = open('concept/' + keyword + '/back_lexicon/' + keyword + "_" + emo + 'back.txt','w')
  strage_back_uniq = set(strage_back)
  for text in strage_back_uniq:
    w_b.write(text)
  


#ファイル書き込み(前半)
  
  #専用ディレクトリ作成
  cmd = 'mkdir ' + 'concept/' + keyword + '/forward_lexicon'
  try:
    subprocess.call(cmd,shell=True)
  except:
    print("Error.")

  #書き込み
  w_f = open('concept/' + keyword + '/forward_lexicon/' + keyword + "_" + emo + 'forward.txt','w')
  strage_forward_uniq = set(strage_forward)
  for text in strage_forward_uniq:
    w_f.write(text)
