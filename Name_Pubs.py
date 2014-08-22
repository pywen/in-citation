self_names=[]
all_names=[]
self_pubs=[]
all_pubs=[]
for i in range(1,2468):
    f=open('WR'+str(i)+'.txt','r')
    line=eval(f.readline())
    self_names.append(line['SELF'][0])
    all_names.append(line['SELF'][0])
    for i in line['CR']:
        all_names.append(i[0])
    self_pubs.append(line['SELF'][2])
    all_pubs.append(line['SELF'][2])
    for i in line['CR']:
        all_pubs.append(i[2])

