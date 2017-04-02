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
    return classLabelVector

def list2file(list,filename): #after deal with the file,we save the result to file
    file = open(filename,'w')
    for i in list:
        file.write(i[0])
        file.write(" ")
        file.write(i[1])
        file.write("\n")
    file.close()

def main():
    li = file2list("D:/cudnn/val.txt")
    list2file(li,"D:/cudnn/val1.txt")