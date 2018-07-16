import sys

prev_key = None
score = 0.0
cnt = 0

for line in sys.stdin:
    k, v = line.strip().split('\t')
    v = float(v)
    if k != prev_key and prev_key is not None:
        avg = score / cnt
        if avg >= 4.5:
            print('{}\t{:.2f}'.format(k, avg))
        cnt = 0
        score = 0
    prev_key = k
    score += v
    cnt += 1

if k != prev_key and prev_key is not None:
    if score / cnt >= 4.5:
        print(k)
