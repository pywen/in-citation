#在pre_name_list进一步处理，对第一个姓名字段进行去重后输出mid_name_list.txt文件

f=open('s-self-names.txt','r')
s_self_names=[]
for line in f.readlines():
    s_self_names.append(line[:-1])
f.close()

pre_name_list=[]
fp=open('pre-name-list.txt','r')
for line in fp.readlines():
    pre_name_list.append(eval(line))
fp.close()

def mid_name_list(i):
    midlist=[]
    for j in pre_name_list:
        if i==j[0]:
            for m in j[1]:
                if m not in midlist:
                    midlist.append(m)
    return (i,midlist)

fm=open('mid_name_list.txt','w')
for i in s_self_names:
    if len(mid_name_list(i)[1])!=0:
        fm.write(str(mid_name_list(i))+'\n')
fm.close()
