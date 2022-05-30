#!/usr/bin/python
# -*- coding: UTF-8 -*-
import  music21 as ms21
c=ms21.converter.parse('稻妻-褪淡的余忆_chord.mid')
r=ms21.converter.parse('稻妻-褪淡的余忆_medoly.mid')
# 获取持续的时间每个音符
crit=iter(c.flat.notesAndRests)
R=[]
t=0
id=0
CR=[[],[]]
while True:
    try:
        note=next(crit)
        if (isinstance(note,ms21.note.Note) or isinstance(note,ms21.chord.Chord)):
            if(note.offset>=t+2):
                t=note.offset-note.offset%2
                f=1
                for se in R:
                    if (se[0]==CR):f=0
                if(f):
                    R.append([CR])
                CR=[[],[]]
            CR[0].append(note.offset-t)
            CR[1].append(note.duration.quarterLength)
    except StopIteration:
        break
if isinstance(note, ms21.note.Rest):
    print(note.offset,note.name,note.duration.quarterLength)

elif isinstance(note,ms21.note.Note):
    print(note.offset,note.name,note.octave,note.pitch,note.pitch.midi,note.duration.quarterLength)
    # 取和弦
else:
    for c_note in note.notes:
        print(c_note.name,c_note.pitch.midi)
    print(note.offset,note.duration.quarterLength)


