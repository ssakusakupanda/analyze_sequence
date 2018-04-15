#!/usr/bin/python
# coding: utf-8

import sys
import re
import os
import MeCab
import collections
from BeautifulSoup import BeautifulSoup


def n_searcher(word):
	
	number_of_examples = '200' 
	stop = '3000' #取ってくる文章の上限（速度の関係）
	count = '0'	
	sentences = []
	
	while True:
		url = 'http://ark6.media.eng.hokudai.ac.jp/blog?query=' + word + '\&num=' + number_of_examples + '\&start=' +  count + '\&exact=1'
		command = 'lynx -source '+url+' > /tmp/resp.html'
		os.system(command)

		#html文章のタグを消してる
		soup = BeautifulSoup(open('/tmp/resp.html').read())
		paragraphs = soup.fetch('p')
		for p in paragraphs:
			pp = re.sub('<[^<]+?>', '', str(p))
			ppp = re.split('\n', pp)
			for line in ppp:
				if word in line:
					sentences.append(line)
			
		fetch = soup.fetch('div')
		fetch2 = re.sub('<[^<]+?>', '', str(fetch[0]))
		fetch3 = re.sub('\n', '', fetch2)
		fetch4 = fetch3.split(' ')
		
		count = int(count) + 200
		count = str(count)

		if not fetch4[10] == count or fetch4[10] == stop:
			break
	

	pattern = re.compile(",")
	mecab = MeCab.Tagger()
	target_noun = []
	
	for sentence in sentences:
		node = mecab.parseToNode(sentence).next
		while node.next:
			features = pattern.split(node.feature)
			if features[6] == word:
				node = node.next
				features = pattern.split(node.feature)
				if features[0] == "名詞" and features[1] == "一般":
					if not features[6] == '*':
						target_noun.append(features[6])
				if node.prev.prev:
					node = node.prev.prev
					features = pattern.split(node.feature)
					if features[6] == "が" or features[6] == "は":
						if node.prev:
							node = node.prev
							features = pattern.split(node.feature)
							if features[0] == "名詞" and features[1] == "一般":
								if not features[6] == '*':
									a = features[6]
									if node.prev:
										node = node.prev
										features = pattern.split(node.feature)
										if features[0] == "形容詞":
											can = features[6] + a
											target_noun.append(can)
										elif features[0] == "助詞" or features[0] == "助動詞":
											b = "の"
											if node.prev:
												node = node.prev
												features = pattern.split(node.feature)
												if features[0] == "名詞":
													can = features[6] + b + a
													if not "*" in can:
														target_noun.append(can)
					break
				else:
					break
			node = node.next


	ans = []
	counter=collections.Counter(target_noun)
	topn = (counter.most_common())
	for n in topn:
		m = re.match("[ぁ-ん]",n[0])
		if m == None or len(n[0])>3:
			ans.append(n[0])
		if len(ans) >= 20:
			break
     
	return ans
	
if __name__ == '__main__':

	if len(sys.argv) < 2: #コマンドラインに入力された文字数が１文字以下だったら（何も入力がない場合）
		sys.exit('Usage Examples:\n filename.py botに話したいこと\n')
	phrase = sys.argv[1] #sys.argv[1]=クエリ
	print phrase
	ans = []
	ans = n_searcher(phrase)

	for a in ans:
		print a

