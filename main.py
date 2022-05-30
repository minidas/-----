#!/usr/bin/python
# -*- coding: UTF-8 -*-
import random
import numpy as py
import music21 as ms21
#从本地获取midi流并转调
c=ms21.converter.parse('稻妻-褪淡的余忆_chord.mid')
ky=c.analyze('key')
print(ky)
if ky.mode == 'minor':
    i = ms21.interval.Interval(ky.parallel.tonic, ms21.pitch.Pitch('C'))
else:
    i = ms21.interval.Interval(ky.tonic, ms21.pitch.Pitch('C'))
c=c.transpose(i)

m=ms21.converter.parse('稻妻-褪淡的余忆_medoly.mid')
ky=m.analyze('key')
print(ky)
if ky.mode == 'minor':
    i = ms21.interval.Interval(ky.parallel.tonic, ms21.pitch.Pitch('C'))
else:
    i = ms21.interval.Interval(ky.tonic, ms21.pitch.Pitch('C'))
m=m.transpose(i)

crit=iter(c.flat.notesAndRests)
mrit=iter(m.flat.notesAndRests)
R=[]
#R的一个元素为[[CR],[MR],[nextid]]
t=0
pre_id=0
fstart=0#判定是否为曲头
CR=[[],[]]
#CR=[[offset],[duration]]
m_note=next(mrit)
while True:
    try:
        note=next(crit)
        if (isinstance(note,ms21.note.Note) or isinstance(note,ms21.chord.Chord)):
            if(note.offset>=t+2):
                MR=[[],[]]
                while(1):
                    if (isinstance(m_note,ms21.note.Note) or isinstance(m_note,ms21.chord.Chord)):
                        if(m_note.offset>=note.offset-note.offset%2):#对应chord分段
                            break
                        MR[0].append(m_note.offset-t)
                        MR[1].append(m_note.duration.quarterLength)
                    m_note=next(mrit)
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
        break
crit=iter(c.flat.notesAndRests)
mrit=iter(m.flat.notesAndRests)
#初始化迭代器
C=[]
t=0
pre_id=0
fstart=0
Cstep=py.linspace(0,0,12)
m_note=next(mrit)
while True:
    try:
        note=next(crit)
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
                    m_note=next(mrit)
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
        break
MM=[]
mrit=iter(m.flat.notesAndRests)
fstart=0
while True:
    try:
        note=next(mrit)
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
        break
cstream=ms21.stream.Stream()
mstream=ms21.stream.Stream()
rid=0
t=0
while(1):
    for i in range(len(R[rid][0][0])):
        c_newnote=ms21.note.Note()
        if(R[rid][0][1][i]==3.75):
            c_newnote.duration.quarterLength=4
        elif(R[rid][0][1][i]==2.75):
            c_newnote.duration.quarterLength=3
        else:
            c_newnote.duration.quarterLength=R[rid][0][1][i]
        cstream.insert(t+R[rid][0][0][i],c_newnote)
    j=random.randint(0,len(R[rid][1])-1)
    for i in range(len(R[rid][1][j][0])):
        m_newnote=ms21.note.Note()
        m_newnote.duration.quarterLength=R[rid][1][j][1][i]
        mstream.insert(t+R[rid][1][j][0][i],m_newnote)
    i=random.randint(0,len(R[rid][3])-1)
    t+=R[rid][3][i]
    if(len(R[rid][2])!=0):
        i=random.randint(0,len(R[rid][2])-1)
        rid=R[rid][2][i]
    else:
        break
cstream.show()
mstream.show()