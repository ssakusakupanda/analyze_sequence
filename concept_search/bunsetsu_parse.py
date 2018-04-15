# coding:utf-8
# pyknp: Python Module for KNP/JUMAN

import re
import subprocess

def format_text(text):
    '''
        MeCabに入れる前のツイートの整形方法例
        '''
    text=re.sub(r'https?://[\w/:%#\$&\?\(\)~\.=\+\-…]+', "", text)
    text=re.sub('RT', "", text)
    text=re.sub('お気に入り', "", text)
    text=re.sub('まとめ', "", text)
    text=re.sub(r'\s', "", text)#半角記号,数字,英字
    text=re.sub(r'[!-~]', "", text)#半角記号,数字,英字
    text=re.sub(r'[︰-＠]', "", text)#全角記号
    text=re.sub('\n', "", text)#改行文字
    text=re.sub(' ', "", text)#改行文字
    
    return text

### KNP
#-*- encoding: utf-8 -*-
from pyknp import KNP
import sys
import codecs

# Use KNP in subprocess modei
knp = KNP()

keyword = input("search file: ")
filename = 'concept/' + keyword + "/" + keyword + "_sentence.txt"

#感情
emotions = ['joy','trust','fear','surprise','sadness','disgust','anger','anticipation']

#感情別分類
for emo in emotions:
    
#ファイル書き込み
    #専用ディレクトリ作成
    cmd = 'mkdir ' + 'concept/' + keyword + '/match_emotion'
    try:
        subprocess.call(cmd,shell=True)
    except:
        print("Error.")
    #書き込みファイル
    w = open('concept/' + keyword + '/match_emotion/' + keyword + "_" + emo + '.txt','w')
    
    #辞書作成
    keywords = []
    with open("source/" + emo + ".txt",'r') as emo_f:
        line = emo_f.readline()
        keywords.append(line.strip())
        while line:
            line = emo_f.readline()
            keywords.append(line.strip())
        keywords.remove('')

    f = open(filename,'r')

    for text in f:
      #print(text)

      result = knp.parse(format_text(text))
     
      #該当するかチェック
      verb_relation = ""
      lexicon = ""
      
      verd_parent_id = 0
      lexi_bnst_id = -2
      last_bnst_id = -4

      # loop for tag (kihonku, basic phrase)
      for tag in result.tag_list():
          
          if "<動態述語>" in tag.fstring:
              match = re.search(r'<格解析結果:(.*?)/', tag.fstring)
              if match:
                #print('動:' + match.group(1), end=" ")
                verb_relation = '動:' + match.group(1) + " "
                
                res = re.sub(r'.*?<格解析結果:.*?:.*?:',"",tag.fstring)

                match = re.findall(r'(.*?)/./(.*?)/././.*?;', res)
                if match:
                    for frame ,word in match:
                        if word != '-':
                            #print(frame + ':' + word, end=" ")
                            verb_relation += frame + ':' + word + " "
                    #print()
      
    # loop for bunsetsu
      if  verb_relation != "" :
          for bnst in result.bnst_list():
              word = "".join(mrph.midasi for mrph in bnst.mrph_list())
              verb_part = verb_relation.split('動:')[1].split(' ')[0]
              if verb_part != "" and word != "" and verb_part in word and verb_part in keyword:
                   verd_parent_id = bnst.parent_id
             
              for lexi in keywords:
                  if lexi in word:
                    lexi_bnst_id = bnst.bnst_id
                    lexicon = '感情:' + emo

              if bnst.parent_id == -1:
                 last_bnst_id = bnst.parent_id

      if verd_parent_id == lexi_bnst_id:
          print(verb_relation + lexicon + " text:" + text.strip())
          w.write(verb_relation + lexicon + " text:" + text.strip())
