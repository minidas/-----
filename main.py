#!/usr/bin/python
# -*- coding: UTF-8 -*-
import  music21 as ms21
c=ms21.converter.parse('稻妻-褪淡的余忆_chord.mid')
r=ms21.converter.parse('稻妻-褪淡的余忆_medoly.mid')
# 获取持续的时间每个音符
crit=iter(c.flat.notesAndRests)
R=[]
#R的一个元素为[[CR],[MR],[nextid]]
t=0
preid=0
fstart=0#判定是否为曲头
CR=[[],[]]
#CR=[[offset],[duration]]
while True:
    try:
        note=next(crit)
        if (isinstance(note,ms21.note.Note) or isinstance(note,ms21.chord.Chord)):
            if(note.offset>=t+2):
                t=note.offset-note.offset%2
                f=1
                id=0
                for se in R:
                    if (se[0]==CR):
                        f=0
                        break
                    id+=1
                if(f):
                    R.append([CR,[],[]])
                    
                if(fstart):
                    R[preid][2].append(id)
                fstart=1
                preid=id
                CR=[[],[]]
            CR[0].append(note.offset-t)
            CR[1].append(note.duration.quarterLength)
    except StopIteration:
        break



