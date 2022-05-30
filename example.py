import  music21 as ms21
s=ms21.converter.parse('稻妻-褪淡的余忆_medoly.mid')
# 获取持续的时间每个音符
print([note.duration.quarterLength for note in s.flat.notesAndRests])

for note in s.flat.notesAndRests :

    if isinstance(note, ms21.note.Rest):
        print(note.name,note.duration.quarterLength)

    elif isinstance(note,ms21.note.Note):
        print(note.name,note.octave,note.pitch,note.pitch.midi,note.duration.quarterLength)
    # 取和弦
    else:
        for c_note in note.notes:
            print(c_note.name, c_note.pitch.midi,c_note.duration.quarterLength)