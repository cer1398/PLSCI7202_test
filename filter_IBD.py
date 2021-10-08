#! /usr/bin/python3
file = open("Mo17_B73.paf", "r")
for it in file:
    data = it.split("\t")
    if int(data[9]) >= 10000 & float(data[9])/float(data[10])<0.2:
        print(data[5,7:9])
data.close()
