#!/usr/bin/python
# -*- coding: UTF-8 -*-
import  music21 as ms21
c=ms21.converter.parse('稻妻-褪淡的余忆_chord.mid')
m=ms21.converter.parse('稻妻-褪淡的余忆_medoly.mid')
# 获取持续的时间每个音符
crit=iter(c.flat.notesAndRests)
mrit=iter(m.flat.notesAndRests)
R=[]
#R的一个元素为[[CR],[MR],[nextid]]
t=0
preid=0
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
                        if(m_note.offset>=note.offset-note.offset%2):
                            break
                        MR[0].append(m_note.offset-t)
                        MR[1].append(m_note.duration.quarterLength)
                    m_note=next(mrit)
                t=note.offset-note.offset%2
                f=1
                id=0
                for se in R:
                    if (se[0]==CR):
                        f=0
                        se[1].append(MR)
                        break
                    id+=1
                if(f):
                    R.append([CR,[MR],[]])
                if(fstart):
                    R[preid][2].append(id)
                fstart=1
                preid=id
                CR=[[],[]]
            CR[0].append(note.offset-t)
            CR[1].append(note.duration.quarterLength)
    except StopIteration:
        break



