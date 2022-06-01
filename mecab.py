import codecs 
import csv 
import re 
import os
import MeCab
#今自分がいるディレクトリをosモジュールを使って読み込む
__location__ = os.path.realpath( os.path.join(os.getcwd(), os.path.dirname(__file__)))


tagger = MeCab.Tagger()

print(tagger.parse("すもももももももものうち").split())
print(__location__ )