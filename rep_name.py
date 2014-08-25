#按整理出来的姓名字典进行替换操作，得到最终的数据

f=open('copy_mid_name_list.txt','r')
rep_list=[]
for i in f.readlines():
    rep_list.append(eval(i))
f.close()

def replace_name(i):
    f=open('C:\Users\Administrator\Desktop\实验数据\WRs\WR'+str(i)+'.txt','r')
    line=eval(f.readlines()[0])
    for j in rep_list:
        if line['SELF'][0] in j[1]:
            print line['SELF'][0]
            line['SELF'][0]=j[0]
    for k in line['CR']:
        for l in rep_list:
            if k[0] in l[1]:
                print k[0]
                k[0]=l[0]
    fo=open('C:\Users\Administrator\Desktop\实验数据\NWRs\NWR'+str(i)+'.txt','w')
    fo.write(str(line))
    f.close()
    fo.close()

for i in range(1,2468):
    replace_name(i)
