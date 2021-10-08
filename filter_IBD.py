#! /usr/bin/python3
file = open("Mo17_B73.paf", "r")
for it in file:
    data = it.split("\t")
    if (int(data[9]) >= 10000 & (float(data[9])/float(data[10])<0.2) & (data[0] == data[5])):
        print(data[5]+"\t"+data[7]+"\t"+data[8]+"\t")
file.close()
