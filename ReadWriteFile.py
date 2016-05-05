__author__ = 'Acedia'

def readfile():
    f = open('date/text.txt', 'r')
    str = ""
    dict = [
    ]
    while(str.find('end') < 0):
        name = f.readline()[:-1]
        comp = f.readline()[:-1]
        tema = f.readline()[:-1]
        text = ""
        str = ""
        while(str.find('--') < 0 and str.find('end') < 0):
            str = f.readline()
            if (str.find('--') < 0 and str.find('end') < 0):
                str = str[:-1]
                text += str
        dict.append([name , comp, tema, text])
    return dict

def writefile(list):
    f = open('date/text.txt', 'w')
    for i in range(0, len(list)):
        for j in range(0, len(list[i])):
            f.writelines(list[i][j] +' \n')
        if i == len(list) - 1:
            f.writelines('end')
        else:
            f.writelines('-- \n')
    return 0
