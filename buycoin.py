#!/usr/bin/python
def save_to_file(file_name, contents):
    fh = open(file_name, 'w')
    fh.write(contents)
    fh.close()

x=raw_input("input your price now:")
xf=float(x)

level=raw_input("input level by \n9.95,0.9,0.85... :")
print("level:"+`level`)
if level is '':
    lf=0.85
else:
    lf=float(level)

file_name=raw_input("input filename:")
contents="Price is below:"

for i in range(1,5):
    ii=int(i)
    high= xf*pow(2-lf,ii)
    contents=contents+"\nprice +"+`pow(2,ii)`+" is " +'%.5f' % high

for i in range(1,5):
    ii=int(i)
    low= xf*pow(lf,ii)
    contents=contents+"\nprice -"+`pow(2,ii)`+" is " +'%.5f' % low

print(contents)
save_to_file(file_name, contents)
