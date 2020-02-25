import sys

file = open('demo.txt', mode='wt', encoding='utf-8')

file.write('What are the roots that clutch, ')
file.write('what branch is grow\n')
file.write('some other fake text!')

file.close()

readFile = file = open('demo.txt', mode='rt', encoding='utf-8')

print(readFile.read())
