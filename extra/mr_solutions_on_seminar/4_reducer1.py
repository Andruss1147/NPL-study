import sys

prev_key = None
vals = []

def emit_result(key, vals):
    scores = [
        float(val[1]) for val
            in filter(lambda v: v[0] == 'score', vals)
    ]
    discipline = list(
        filter(lambda v: v[0] == 'discipline', vals)
    )[0][1] # к концу прицепили discipline, запись для одного key одна, поэтому и берём 0 (1 поле затем)

    avg = sum(scores) / len(scores)

    print('{}\t{}'.format(discipline, avg))

for line in sys.stdin:
    key, rec_type, val = line.strip().split('\t')
    if key != prev_key and prev_key is not None:
        # Баранов, (score, 5)
        # Баранов, (discipline, Информатика)
        emit_result(prev_key, vals)
        vals = []
    vals.append((rec_type, val))
    prev_key = key

if prev_key is not None:
    emit_result(prev_key, vals)
