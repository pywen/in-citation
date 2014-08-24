self_record=[]
cr_record=[]
for i in range(1,2468):
    f=open('WR'+str(i)+'.txt','r')
    line=eval(f.readline())
    self_record.append(line['SELF'])
    for j in line['CR']:
        cr_record.append(j)
    f.close()

def namelist(i):
    lname=[]
    for j in cr_record:
        if i[1:3]==j[1:3] and i[0][0:3]==j[0][0:3] and i[0]!=j[0] and (j[0] not in lname):
            lname.append(j[0])
    return lname

f=open('pre-name-list.txt','w')
for i in self_record:
    f.write(str((i[0],namelist(i)))+'\n')
f.close()
