"""Merge repeated CSV sections and union their columns without data loss."""

def analyze(text):
    import csv,io
    chunks=text.split('\n---\n');rows=[];cols=[]
    for chunk in chunks:
        if not chunk.strip():continue
        reader=csv.DictReader(io.StringIO(chunk))
        for col in reader.fieldnames or []:
            if col not in cols:cols.append(col)
        rows.extend(dict(x) for x in reader)
    return {'columns':cols,'rows':[{col:r.get(col,'') for col in cols} for r in rows],'count':len(rows)}
