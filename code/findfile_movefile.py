def findfile_movefile(li):
    import os,shutil
    for filena in li:
        filename = filena[0]
        filename=os.path.join(r'/home/meng/ILSVRC12/val',filename.strip())
        print filename
        if os.path.exists(filename):
            shutil.copy(filename,r'/home/meng/ILSVRC12/val1')
def file2list(filename):
    fr = open(filename)
    numberOfLines = len(fr.readlines())         #get the number of lines in the file
    classLabelVector = []                       #prepare labels return
    fr = open(filename)
    for line in fr.readlines():
        line = line.strip()
        line = line.split(' ')
        if line[-1] == '0' or line[-1] == '1' or line[-1] == '2' or line[-1] == '3' or line[-1] == '4':
            classLabelVector.append(line)     #write the file to a 2-d list
    classLabelVector
    return classLabelVector
def main():
    li = file2list("/home/meng/caffe/examples/imagenet/myself/val.txt")
    findfile_movefile(li)
