import subprocess

#対象
keyword = input()

#初期設定
filenames = []
emotions = ['joy', 'trust', 'fear','surprise','sadness','disgust','anger','anticipation']
title = keyword + '_sentence_lexicon_'

#ファイル名作成
for i in range(len(emotions)):
  filenames.append(title + emotions[i] + ".txt")

#専用ディレクトリ作成
cmd = 'mkdir ' + keyword+ '/uniq'
try:
  subprocess.call(cmd,shell=True)
except:
  print("Error.")

#コマンド作成 & uniq実行
for i in range(len(filenames)):
  
  command = []
  command.append('cat')
  command.append(str(filenames[i]))
  command.append('| sort')
  command.append('| uniq >')
  command.append(keyword + "/uniq/" + str(title) + "uniq_" + str(emotions[i]) + ".txt")

  cmd = " ".join(command)

  try:
    subprocess.call(cmd,shell=True)
  except:
    print("Error.")
