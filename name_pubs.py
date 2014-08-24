#提取姓名和出版物的列表

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
    if line['SELF'][2] is not None:
        self_pubs.append(line['SELF'][2])
        all_pubs.append(line['SELF'][2])
    for i in line['CR']:
        all_pubs.append(i[2])

s_self_names=sorted(list(set(self_names)))
s_all_names=sorted(list(set(all_names)))
s_self_pubs=sorted(list(set(self_pubs)))
s_all_pubs=sorted(list(set(all_pubs)))

def write_content(List,File):
    f=open(File,'w')
    for i in List:
        f.write(i+'\n')
    f.close()

write_content(s_self_names,'s-self-names.txt')
write_content(s_all_names,'s-all-names.txt')
write_content(s_self_pubs,'s-self-pubs.txt')
write_content(s_all_pubs,'s-all-pubs.txt')
