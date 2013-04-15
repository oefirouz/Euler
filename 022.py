FILENAME = '022.txt'

def nScore(name):
    return sum(map(lambda x: ord(x) - 64, name))

f = open(FILENAME, 'r')
names = f.read()
f.close()
names = names.split('","')
names[0] = names[0][1:]
names[-1] = names[-1][:-1]
names.sort()

score = 0
for i in range(0, len(names)):
    score += nScore(names[i])*(i+1)

print score
