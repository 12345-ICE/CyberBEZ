word = input('Write a word: ')

normalAphabet = {'a':1, 'b':2, 
'c':3, 'd':4, 'e':5, 'f':6, 
'g':7, 'h':8, 'i':9, 'j':10, 
'k':11, 'l':12, 'm':13, 'n':14, 
'o':15, 'p':16, 'q':17, 'r':18, 
's':19, 't':20, 'u':21, 'v':22, 
'w':23, 'x':24, 'y':25, 'z':26}

changedAphabet = {1:'x', 2:'y', 
3:'z', 4:'a', 5:'b', 6:'c', 
7:'d', 8:'e', 9:'f', 10:'g', 
11:'h', 12:'i', 13:'j', 14:'k', 
15:'l', 16:'m', 17:'n', 18:'o', 
19:'p', 20:'q', 21:'r', 22:'s', 
23:'t', 24:'u', 25:'v', 26:'w'}

shifr = []

for i in word:
	shifr.append(changedAphabet[normalAphabet[i]])

print(''.join(shifr))