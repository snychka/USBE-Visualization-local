import random 

file = open("data.csv.org", "r")
line = file.readline()
print(line)
line = file.readline()
while line:
    en = line.split(",")[1]
    val_f = random.random() * float(en)
    #print(val_f)
    val = int(val_f)
    #print(val)
    girls = str(val)
    print(line.rstrip() + ',' + girls)
    line = file.readline()
file.close()
