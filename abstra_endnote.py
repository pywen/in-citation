import re

def get_au(lines):
    pattern=r'AU\s{1}(.*)'
    for line in lines:
        mau=re.match(pattern,line)
        if mau:
            return mau.group(1).lower().strip()

def get_py(lines):
    pattern=r'PY\s{1}(.*)'
    for line in lines:
        mpy=re.match(pattern,line)
        if mpy:
            return mpy.group(1).strip()

def get_j9(lines):
    pattern=r'J9\s{1}(.*)'
    for line in lines:
        mj9=re.match(pattern,line)
        if mj9:
            return mj9.group(1).lower().strip()

def get_cr(lines):
    crlist=[]
    pattern=r'CR\s{1}(.*)'
    prest=r'\s{3}(.*)'
    for line in lines:
        mcr=re.match(pattern,line)
        if mcr:
            if len(mcr.group(1).split(','))>=3:
                crlist.append([i.strip() for i in mcr.group(1).lower().split(',')[0:3]])
            n=1
            while re.match(prest,lines[lines.index(line)+n]):
                if len(re.match(prest,lines[lines.index(line)+n]).group(1).split(','))>=3:
                    crlist.append([i.strip() for i in re.match(prest,lines[lines.index(line)+n]).group(1).lower().split(',')[0:3]])
                    n+=1
    return crlist

f=open(r'F:\合作演化数据集内部引用网络\切割后的数据\ER1.txt','r')
lines=f.readlines()
print str({'SELF':[get_au(lines),get_py(lines),get_j9(lines)],'CR':get_cr(lines)})
