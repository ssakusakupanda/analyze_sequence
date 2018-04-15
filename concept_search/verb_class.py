#coding:utf-8

import subprocess
import re
import sys
import MeCab

mecab = MeCab.Tagger ("-Ochasen")
triple_strage = {}

def parse(text):
  mecab.parse('')#文字列がGCされるのを防ぐ
  node = mecab.parseToNode(text)
  while node:
    #単語を取得
    word = node.surface
    #品詞を取得
    pos = node.feature.split(",")[0]
    dic[word] =  pos
    #次の単語に進める
    node = node.next
  
  verb_flag = 0
  #助+動+助のペア抽出
  for word,pos in dic.items():
   
    #初めの関門
    if pos == '助詞' or pos == '動詞':
    
      #ペア出力
      if pos == '助詞' and len(triple) > 1 :
        triple.append(word)
        
        #Concept保存 & カウント
        if not ("".join(triple)) in triple_strage:
           triple_strage["".join(triple)] = 0
        triple_strage["".join(triple)] += 1

        triple.clear()

      #探索
      if pos == '助詞':
        triple.append(word)
      elif pos == '動詞' and len(triple) > 0:
        triple.append(word)
      
      else:
        triple.clear()

    else:
      triple.clear()

#ファイル処理
f = open('concept/emortional_sentence.txt','r')
#f = open('00000002.txt','r')
w = open('concept/concept_sentence_emo.txt','w')

for line in f:
  dic = {}
  triple = []
  parse(line)

triple_freq = sorted(triple_strage.items(), key=lambda x:x[1], reverse=True)
for word,cnt in triple_freq:
  w.write(word + '\t' + str(cnt) + '\n')
    
