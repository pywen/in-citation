#coding: utf-8
#用于提取AU,PY,J9和CR字段的参考文献的函数
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
