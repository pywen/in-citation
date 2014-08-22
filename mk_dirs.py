from func_endnote import *

def mk_dir(i):
    f=open('ER'+str(i)+'.txt','r')
    lines=f.readlines()
    fr=open('F:\合作演化数据集内部引用网络\切割后的数据\dir\WR'+str(i)+'.txt','w')
    fr.write(str({'ID':i,'SELF':[get_au(lines),get_py(lines),get_j9(lines)],'CR':get_cr(lines)}))
    f.close()
    fr.close()

for i in range(1,2468):
    mk_dir(i)
