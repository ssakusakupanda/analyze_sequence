# pyknp: Python Module for KNP/JUMAN

### Juman
#-*- encoding: utf-8 -*-
from pyknp import Juman
import sys
import codecs
#sys.stdin = codecs.getreader('utf_8')(sys.stdin)
#sys.stdout = codecs.getwriter('utf_8')(sys.stdout)

# Use Juman in subprocess mode
juman = Juman()
result = juman.analysis(u"(^^;北京オリンピック終わったら価格は落ち着くかなぁサエコさんとの結婚も、また北京オリンピックの出場も関係するとあり、慎重に検討した結果、10月29日に、ダルビッシュさんの母親の郁代さんが、ダルビッシュさん本人が記入した国籍選択届を故郷の大阪・羽曳野の市役所に提出して、受理され目を離すと時代が変わってます(笑)北京に双子649組大集結")
print(','.join(mrph.midasi for mrph in result))

for mrph in result.mrph_list():
    print(u"見出し:%s, 読み:%s, 原形:%s, 品詞:%s, 品詞細分類:%s, 活用型:%s, 活用形:%s, 意味情報:%s, 代表表記:%s" \
          % (mrph.midasi, mrph.yomi, mrph.genkei, mrph.hinsi, mrph.bunrui, mrph.katuyou1, mrph.katuyou2, mrph.imis, mrph.repname))

# Use Juman in server mode
juman = Juman(server='localhost', port=12345)
...

#### Read from file
#data = ""
#with open("result.juman") as file_in:
#    for line in file_in:
#        data += line.decode('utf-8')
#        if line.strip() == "EOS":
#            result = juman.result(data)
#            print(",".join(mrph.genkei for mrph in result.mrph_list()))
#            data = ""

### KNP
#-*- encoding: utf-8 -*-
from pyknp import KNP
import sys
import codecs
#sys.stdin = codecs.getreader('utf_8')(sys.stdin)
#sys.stdout = codecs.getwriter('utf_8')(sys.stdout)

# Use KNP in subprocess mode
knp = KNP()
# if you don't need case analysis
# knp = KNP(option='-dpnd -tab')
result = knp.parse(u"(^^;北京オリンピック終わったら価格は落ち着くかなぁサエコさんとの結婚も、また北京オリンピックの出場も関係するとあり、慎重に検討した結果、10月29日に、ダルビッシュさんの母親の郁代さんが、ダルビッシュさん本人が記入した国籍選択届を故郷の大阪・羽曳野の市役所に提出して、受理され目を離すと時代が変わってます(笑)北京に双子649組大集結")

# loop for bunsetsu
for bnst in result.bnst_list():
    print(u"ID:%s, 見出し:%s, 係り受けタイプ:%s, 親文節ID:%s, 素性:%s" \
    % (bnst.bnst_id, "".join(mrph.midasi for mrph in bnst.mrph_list()), bnst.dpndtype, bnst.parent_id, bnst.fstring))

# loop for tag (kihonku, basic phrase)
#for tag in result.tag_list():
    #print(u"ID:%s, 見出し:%s, 係り受けタイプ:%s, 親文節ID:%s, 素性:%s" \
    #% (tag.tag_id, "".join(mrph.midasi for mrph in tag.mrph_list()), tag.dpndtype, tag.parent_id, tag.fstring))

# loop for mrph
#for mrph in result.mrph_list():
    #print(u"見出し:%s, 読み:%s, 原形:%s, 品詞:%s, 品詞細分類:%s, 活用型:%s, 活用形:%s, 意味情報:%s, 代表表記:%s" \
    #% (mrph.midasi, mrph.yomi, mrph.genkei, mrph.hinsi, mrph.bunrui, mrph.katuyou1, mrph.katuyou2, mrph.imis, mrph.repname))

#### Read from file
#data = ""
#with open("result.knp") as file_in:
#    for line in file_in:
#        data += line.decode('utf-8')
#        if line.strip() == "EOS":
#            result = knp.result(data)
#            print(",".join(mrph.genkei for mrph in result.mrph_list()))
#            data = ""

