# -*- coding: utf-8 -*-
'''
train数据集的文件名都是332.JPEG这样的形式，所以我们用下面的代码生成train.txt文件和val.txt文件。
train.txt文件的内容：
图片所在位置 类别
train/320.jpg 3
train/321.jpg 3
train/322.jpg 3
'''
def generate_label(frompath,topath):
	import os,shutil
	for r,ds,fs in os.walk(frompath):
		for f in fs:
			picture_label = int(f.split('.')[0]) / 100 #the train picture is numbered as 301(label 3),434(label 4) 
			write_label(f,picture_label,topath)  

def write_label(f,picture_label,topath):  #将标签和图片路径写入train.txt
	file = open(topath,'a') 
	file.write('val/')
	file.write(f)
	file.write(' ')
	file.write(str(picture_label))
	file.write('\n')

def main():
    frompath=r"C:\Users\admin\Desktop\re\test"  #生成train.txt时只需更改路径
    topath=r"C:\Users\admin\Desktop\re\val.txt"
    generate_label(frompath,topath)
