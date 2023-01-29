with open('scoring.json') as q:
    with open('scoring.json', 'a') as w:
        w.write(q.read().replace('"', "'"))