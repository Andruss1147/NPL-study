import sys

prev_key = None
sum = 0

for line in sys.stdin:
    k, v = line.split('\t')
    if k != prev_key and prev_key is not None:
        print(prev_key, sum)
        sum = 0
    sum += 1
    prev_key = k

if k != prev_key and prev_key is not None:
    print(prev_key, sum)
