FILENAME = '42.txt'
f = open(FILENAME, 'r')
words = f.read()
words = words.split('","')
words[0] = words[0][1:]
words[-1] = words[-1][:-1]

def wordScore(word):
    Sum = 0
    for letter in word:
        Sum += ord(letter) - 64
    return Sum

scores = list(map(wordScore, words))

n = 0
while int(n*(n+1)/2) <= max(scores):
    n += 1

tri = [0]*(int((n*(n+1)/2) + 1))
for i in range(1,n+1):
    tri[i*(i+1)//2] = 1
count = 0
for score in scores:
    count += tri[score]
print(count)
