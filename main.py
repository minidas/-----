#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
import numpy as py
import music21 as ms21
from math import *
#从本地获取midi流并转调
c=[]
m=[]
c.append(ms21.converter.parse('璃月-璃月的晴空_chord.mid'))
ky=c[0].analyze('key')
print(ky)
if ky.mode == 'minor':
    i = ms21.interval.Interval(ky.parallel.tonic, ms21.pitch.Pitch('C'))
else:
    i = ms21.interval.Interval(ky.tonic, ms21.pitch.Pitch('C'))
c[0]=c[0].transpose(i)
#整合所有样本
c.append(ms21.converter.parse('璃月-不再年轻的村庄_chord.mid'))
ky=c[1].analyze('key')
print(ky)
if ky.mode == 'minor':
    i = ms21.interval.Interval(ky.parallel.tonic, ms21.pitch.Pitch('C'))
else:
    i = ms21.interval.Interval(ky.tonic, ms21.pitch.Pitch('C'))
c[1]=c[1].transpose(i)

c.append(ms21.converter.parse('璃月-虹霞垂天_chord.mid'))
ky=c[2].analyze('key')
print(ky)
if ky.mode == 'minor':
    i = ms21.interval.Interval(ky.parallel.tonic, ms21.pitch.Pitch('C'))
else:
    i = ms21.interval.Interval(ky.tonic, ms21.pitch.Pitch('C'))
c[2]=c[2].transpose(i)

c.append(ms21.converter.parse('璃月-晚安璃月_chord.mid'))
ky=c[3].analyze('key')
print(ky)
if ky.mode == 'minor':
    i = ms21.interval.Interval(ky.parallel.tonic, ms21.pitch.Pitch('C'))
else:
    i = ms21.interval.Interval(ky.tonic, ms21.pitch.Pitch('C'))
c[3]=c[3].transpose(i)

c.append(ms21.converter.parse('璃月-希望的明日_chord.mid'))
ky=c[4].analyze('key')
print(ky)
if ky.mode == 'minor':
    i = ms21.interval.Interval(ky.parallel.tonic, ms21.pitch.Pitch('C'))
else:
    i = ms21.interval.Interval(ky.tonic, ms21.pitch.Pitch('C'))
c[4]=c[4].transpose(i)

c.append(ms21.converter.parse('璃月-岩壑之崩_chord.mid'))
ky=c[5].analyze('key')
print(ky)
if ky.mode == 'minor':
    i = ms21.interval.Interval(ky.parallel.tonic, ms21.pitch.Pitch('C'))
else:
    i = ms21.interval.Interval(ky.tonic, ms21.pitch.Pitch('C'))
c[5]=c[5].transpose(i)

c.append(ms21.converter.parse('璃月-源流汇响_chord.mid'))
ky=c[6].analyze('key')
print(ky)
if ky.mode == 'minor':
    i = ms21.interval.Interval(ky.parallel.tonic, ms21.pitch.Pitch('C'))
else:
    i = ms21.interval.Interval(ky.tonic, ms21.pitch.Pitch('C'))
c[6]=c[6].transpose(i)

#旋律部分
m.append(ms21.converter.parse('璃月-璃月的晴空_melody.mid'))
ky=m[0].analyze('key')
print(ky)
if ky.mode == 'minor':
    i = ms21.interval.Interval(ky.parallel.tonic, ms21.pitch.Pitch('C'))
else:
    i = ms21.interval.Interval(ky.tonic, ms21.pitch.Pitch('C'))
m[0]=m[0].transpose(i)

m.append(ms21.converter.parse('璃月-不再年轻的村庄_melody.mid'))
ky=m[1].analyze('key')
print(ky)
if ky.mode == 'minor':
    i = ms21.interval.Interval(ky.parallel.tonic, ms21.pitch.Pitch('C'))
else:
    i = ms21.interval.Interval(ky.tonic, ms21.pitch.Pitch('C'))
m[1]=m[1].transpose(i)

m.append(ms21.converter.parse('璃月-虹霞垂天_melody.mid'))
ky=m[2].analyze('key')
print(ky)
if ky.mode == 'minor':
    i = ms21.interval.Interval(ky.parallel.tonic, ms21.pitch.Pitch('C'))
else:
    i = ms21.interval.Interval(ky.tonic, ms21.pitch.Pitch('C'))
m[2]=m[2].transpose(i)

m.append(ms21.converter.parse('璃月-晚安璃月_melody.mid'))
ky=m[3].analyze('key')
print(ky)
if ky.mode == 'minor':
    i = ms21.interval.Interval(ky.parallel.tonic, ms21.pitch.Pitch('C'))
else:
    i = ms21.interval.Interval(ky.tonic, ms21.pitch.Pitch('C'))
m[3]=m[3].transpose(i)

m.append(ms21.converter.parse('璃月-希望的明日_melody.mid'))
ky=m[4].analyze('key')
print(ky)
if ky.mode == 'minor':
    i = ms21.interval.Interval(ky.parallel.tonic, ms21.pitch.Pitch('C'))
else:
    i = ms21.interval.Interval(ky.tonic, ms21.pitch.Pitch('C'))
m[4]=m[4].transpose(i)

m.append(ms21.converter.parse('璃月-岩壑之崩_melody.mid'))
ky=m[5].analyze('key')
print(ky)
if ky.mode == 'minor':
    i = ms21.interval.Interval(ky.parallel.tonic, ms21.pitch.Pitch('C'))
else:
    i = ms21.interval.Interval(ky.tonic, ms21.pitch.Pitch('C'))
m[5]=m[5].transpose(i)

m.append(ms21.converter.parse('璃月-源流汇响_melody.mid'))
ky=m[6].analyze('key')
print(ky)
if ky.mode == 'minor':
    i = ms21.interval.Interval(ky.parallel.tonic, ms21.pitch.Pitch('C'))
else:
    i = ms21.interval.Interval(ky.tonic, ms21.pitch.Pitch('C'))
m[6]=m[6].transpose(i)

m.append(ms21.converter.parse('璃月-品茗尝清心_melody.mid'))
ky=m[7].analyze('key')
print(ky)
if ky.mode == 'minor':
    i = ms21.interval.Interval(ky.parallel.tonic, ms21.pitch.Pitch('C'))
else:
    i = ms21.interval.Interval(ky.tonic, ms21.pitch.Pitch('C'))
m[7]=m[7].transpose(i)

crit=[]
mrit=[]
for i in range(7):
    crit.append(iter(c[i].flat.notesAndRests))
    mrit.append(iter(m[i].flat.notesAndRests))
mrit.append(iter(m[7].flat.notesAndRests))
R=[]
#R的一个元素为[[CR],[MR],[nextid],[interval]]
t=0
pre_id=0
sc_num=0#曲目序号
fstart=0#判定是否为曲头
CR=[[],[]]
#CR=[[offset],[duration]]
m_note=next(mrit[sc_num])
while True:
    try:
        note=next(crit[sc_num])
        if (isinstance(note,ms21.note.Note) or isinstance(note,ms21.chord.Chord)):
            if(note.offset>=t+2):
                MR=[[],[]]
                while(1):
                    if (isinstance(m_note,ms21.note.Note) or isinstance(m_note,ms21.chord.Chord)):
                        if(m_note.offset>=note.offset-note.offset%2):#对应chord分段
                            break
                        MR[0].append(m_note.offset-t)
                        MR[1].append(m_note.duration.quarterLength)
                    m_note=next(mrit[sc_num])
                temp=note.offset-note.offset%2-t
                t=note.offset-note.offset%2
                f=1
                id=0
                for se in R:
                    if (se[0]==CR):
                        f=0
                        se[1].append(MR)
                        se[3].append(temp)
                        break
                    id+=1
                if(f):
                    R.append([CR,[MR],[],[temp]])
                if(fstart):
                    R[pre_id][2].append(id)
                fstart=1
                pre_id=id
                CR=[[],[]]
            if(isinstance(note,ms21.note.Note)):
                CR[0].append(note.offset-t)
                CR[1].append(note.duration.quarterLength)
            else:
                for i in note.notes:
                    CR[0].append(note.offset-t)
                    CR[1].append(note.duration.quarterLength)
    except StopIteration:
        if(sc_num<6):sc_num+=1
        else:break
crit=[]
mrit=[]
for i in range(7):
    crit.append(iter(c[i].flat.notesAndRests))
    mrit.append(iter(m[i].flat.notesAndRests))
mrit.append(iter(m[7].flat.notesAndRests))
#初始化迭代器
C=[]#[[step],[M],[nextid]]
t=0
pre_id=0
fstart=0
sc_num=0
Cstep=py.linspace(0,0,12)
m_note=next(mrit[sc_num])
while True:
    try:
        note=next(crit[sc_num])
        if (isinstance(note,ms21.note.Note) or isinstance(note,ms21.chord.Chord)):
            if(note.offset>=t+2):
                M=[]
                while(1):
                    if (isinstance(m_note,ms21.note.Note) or isinstance(m_note,ms21.chord.Chord)):
                        if(m_note.offset>=note.offset-note.offset%2):#对应chord分段
                            break
                        if(isinstance(m_note,ms21.note.Note)):
                            M.append(m_note.pitch.midi)
                        else:
                            for i in m_note.notes:
                                M.append(i.pitch.midi)
                    m_note=next(mrit[sc_num])
                t=note.offset-note.offset%2
                f=1
                id=0
                bi_Cstep=0#Cstep数组的二进制表示
                for i in range(12):
                    if(Cstep[i]):
                        bi_Cstep+=1
                    bi_Cstep<<=1
                bi_Cstep>>=1
                for se in C:
                    if (se[0]==bi_Cstep):
                        f=0
                        se[1].extend(M)
                        break
                    id+=1
                if(f):
                    C.append([bi_Cstep,M,[]])
                if(fstart):
                    C[pre_id][2].append(id)
                fstart=1
                pre_id=id
                Cstep=py.linspace(0,0,12)
            if(isinstance(note,ms21.note.Note)):
                Cstep[note.pitch.midi%12]=1
            else:
                for i in note.notes:
                    Cstep[i.pitch.midi%12]=1
    except StopIteration:
        if(sc_num<6):sc_num+=1
        else:break
MM=[]
mrit=[]
for i in range(8):
    mrit.append(iter(m[i].flat.notesAndRests))
fstart=0
sc_num=0
while True:
    try:
        note=next(mrit[sc_num])
        if (isinstance(note,ms21.note.Note)):
            f=1
            id=0
            for i in MM:
                if (i[0]==note.pitch.midi):
                    f=0    
                    break
                id+=1
            if(f):
                MM.append([note.pitch.midi,[]])
            if(fstart):
                MM[pre_id][1].append(id)
            fstart=1
            pre_id=id        
        if(isinstance(note,ms21.chord.Chord)):
            for thisnote in note.notes:
                f=1
                id=0
                for i in MM:
                    if (i[0]==thisnote.pitch.midi):
                        f=0    
                        break
                    id+=1
                if(f):
                    MM.append([thisnote.pitch.midi,[]])
                if(fstart):
                    MM[pre_id][1].append(id)
                fstart=1
                pre_id=id 
    except StopIteration:
        if(sc_num<7):sc_num+=1
        else:break
cstream=ms21.stream.Part()
mstream=ms21.stream.Part()
rid=0
mid=0
cid=0
t=0
while(1):
    lst_Cstep=[]
    cstep=11
    bi_Cstep=C[cid][0]
    for i in range(12):
        if(bi_Cstep&1):
            lst_Cstep.append(cstep)
        bi_Cstep>>=1
        cstep-=1
    random.shuffle(lst_Cstep)
    for i in range(max(len(R[rid][0][0]),len(lst_Cstep))):
        if(len(R[rid][0][0])*len(lst_Cstep)==0):break
        c_newnote=ms21.note.Note()
        if(i<len(R[rid][0][0])):
            c_newnote.duration.quarterLength=R[rid][0][1][i]
        else:
            k=random.randint(0,len(R[rid][0][0])-1)
            c_newnote.duration.quarterLength=R[rid][0][1][k]
        c_newnote.pitch.midi=12*(floor(3.2+random.random()))+lst_Cstep[i%len(lst_Cstep)]
        if(i<len(R[rid][0][0])):
            cstream.insert(t+R[rid][0][0][i],c_newnote)
        else:
            cstream.insert(t+R[rid][0][0][k],c_newnote)
    j=random.randint(0,len(R[rid][1])-1)
    for i in range(len(R[rid][1][j][0])):
        m_newnote=ms21.note.Note()
        m_newnote.duration.quarterLength=R[rid][1][j][1][i]
        m_newnote.pitch.midi=MM[mid][0]
        if (len(MM[mid][1])!=0):
            mid=random.choice(MM[mid][1])
        else:
            mid=random.randint(0,len(MM)-1)
        mstream.insert(t+R[rid][1][j][0][i],m_newnote)
    i=random.randint(0,len(R[rid][3])-1)
    t+=R[rid][3][i]
    if(len(R[rid][2])!=0):
        rid=random.choice(R[rid][2])
    else:
        break
    if(len(C[cid][2])!=0):
        cid=random.choice(C[cid][2])
    else:
        cid=random.randint(0,len(C)-1)
resit=iter(cstream.flat.notesAndRests)
t=0
pitch_temp=[]
while True:
    try:
        note=next(resit)
        if (isinstance(note,ms21.note.Note)):
            if(note.offset!=t):
                t=note.offset
                pitch_temp=[]
            for thispitch in pitch_temp:
                if(note.pitch.midi==thispitch):
                    note.pitch.midi+=12
            pitch_temp.append(note.pitch.midi)
    except StopIteration:
        break
s = ms21.stream.Score(id='mainScore')
s.insert(0,mstream)
s.insert(0,cstream)
s.show()
