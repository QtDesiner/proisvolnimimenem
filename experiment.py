import json
with open('scoring.json') as q:
    q = json.load(q)
    with open('scoring.json', 'w') as w:
        w.write(json.dumps(q, indent=3))