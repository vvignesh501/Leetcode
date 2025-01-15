fp = open('sample.csv')

print(fp.read())
lines = fp.readlines()
for line in lines:
    if line.find('ZZ11') != -1:
        print(line)

afp.close()