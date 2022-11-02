'''
Python 扫描指定根目录的*.java文件，并将license.txt的内容写入开头
@author: changgg
'''
# encoding=utf-8
import sys
import os
import argparse

def get_license_content(file_name,file_encode):
	with open(file_name,'r',encoding=file_encode) as file:
		return file.readlines()

def scan_java_file(base_path):
	names=os.listdir(base_path)
	java_files=[]
	for name in names :
		if not os.path.isfile(base_path+"\\"+name):
			java_files.extend(scan_java_file(base_path+"\\"+name))
		else:
			if name.endswith(".java"):
				java_files.append(base_path+"\\"+name)
	return java_files

def add_license_to_java_head(license_content,file_name,file_encode):
	oldContent=""
	with open(file_name,"r",encoding=file_encode) as file :
		oldContent=file.readlines()
	# 移除旧的license描述
	while len(oldContent)>0 :
		if oldContent[0].startswith("package") or "class" in oldContent[0] :
			break
		oldContent.pop(0)
	newContent=license_content+["\n"]+oldContent
	with open(file_name,"w",encoding=file_encode) as file:
		file.writelines(newContent)

def main(args):
	# 获取待写入licnese字符
	license_content=get_license_content(args['license_file'],args['encode'])
	# 待处理的java文件
	files=scan_java_file(args['base_path'])
	print("find %s [.java] file in %s"%(len(files),args['base_path']))
	for file in files :
		add_license_to_java_head(license_content,file,args['encode'])
	print("finish add license to .java's head")

if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='命令行参数')
	parser.add_argument('--encode','-fe', type=str, help='文件编码格式',default='utf-8')
	parser.add_argument('--license-file','-lf', type=str, help='license文件路径',default='./license.txt')
	parser.add_argument('base_path', type=str, help='扫描根目录')
	args = vars(parser.parse_args());
	main(args)