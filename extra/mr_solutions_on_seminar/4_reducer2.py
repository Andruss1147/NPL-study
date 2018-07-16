import sys

prev_key = None
marks = []
values = []

def emit_result(key, vals):
    avg = sum(values) / len(values)
    print('{}\t{:.3f}'.format(key, avg))

for line in sys.stdin:
    key, val = line.strip().split("\t")
    if key != prev_key and prev_key is not None:
        emit_result(prev_key, values)
        values = []
    values.append(float(val))
    prev_key = key

if prev_key is not None:
    emit_result(prev_key, values)
