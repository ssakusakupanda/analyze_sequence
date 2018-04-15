# pyknp: Python Module for KNP/JUMAN

import re
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
    text=re.sub('\n', " ", text)#改行文字
    
    return text

### KNP
#-*- encoding: utf-8 -*-
from pyknp import KNP
import sys
import codecs
#sys.stdin = codecs.getreader('utf_8')(sys.stdin)
#sys.stdout = codecs.getwriter('utf_8')(sys.stdout)

# Use KNP in subprocess modei
knp = KNP()
# if you don't need case analysis
# knp = KNP(option='-dpnd -tab')

f = open('00000001.txt','r')
for text in f:
  print(text)

  result = knp.parse(format_text(text))
  
  # loop for tag (kihonku, basic phrase)
  for tag in result.tag_list():
      #print(u"ID:%s, 見出し:%s, 素性:%s" \
      #% (tag.tag_id, "".join(mrph.midasi for mrph in tag.mrph_list()), tag.fstring))
      if "<動態述語>" in tag.fstring:
          match = re.search(r'<格解析結果:(.*?)/', tag.fstring)
          if match:
                print('動:' + match.group(1), end=" ")  # 検索パターン全体に一致する文字列
          
          res = re.sub(r'.*?<格解析結果:.*?:.*?:',"",tag.fstring)
          
          match = re.findall(r'(.*?)/./(.*?)/././.*?;', res)
          if match:            
            for frame ,word in match:
              if word != '-':
                print(frame + ':' + word, end=" ")
            print()
          #print(re.sub(r'><格関係\d:ガ:','主格:',"".join(match)))  # 検索パターン全体に一致する文字列

