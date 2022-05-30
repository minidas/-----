import music21 as ms21
import numpy as np

c=ms21.converter.parse('master\蒙德-风洗的群山_chord.mid')

##Change the key
ky=c.analyze('key')
print(ky)

if ky.mode == 'minor':
    i = ms21.interval.Interval(ky.parallel.tonic, ms21.pitch.Pitch('C'))
else:
    i = ms21.interval.Interval(ky.tonic, ms21.pitch.Pitch('C'))
c=c.transpose(i)







#get a chord vector:
ChNotes=[0,4,7]
r1=3 #上一次的中心位置，r1最好在1-4之间
N=len(ChNotes)
r1=r1+np.random.randint(-1,2)
if r1<1:
    r1+=1
elif r1>4:
    r1-=1
r2=np.random.randint(0,N)
for j in range(N):
    ChNotes[j]+=r1*12
for j in range(r2):
    ChNotes[j]+=12

ChordTry=ms21.chord.Chord(ChNotes)
print(ChordTry)

