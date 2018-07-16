import sys
prev_key = None
values = []

def print_res(key, values):
    res = sum(values)
    print("%s\t%s" % (key, '#' * int(res)))

for line in sys.stdin:
    key, value = line.strip().split("\t")
    if key != prev_key and prev_key is not None:
        print_res(prev_key, values)
        values = []
    values.append(float(value))
    prev_key = key

if prev_key is not None:
    print_res(prev_key, values)
