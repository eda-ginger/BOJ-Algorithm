import sys

box = list(map(int, sys.stdin.readline().split()))

while box != [1, 2, 3, 4, 5]:
    for i in range(4):
        if box[i] > box[i+1]:
            box[i], box[i+1] = box[i+1], box[i]
            print(' '.join(map(str, box)))
