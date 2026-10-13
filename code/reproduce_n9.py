"""Exact n=9 SC_213 census. Running this script enumerates all inputs.
No command-line options; complete JSON is written only to stdout.
"""
from collections import Counter,deque
from itertools import permutations
from math import factorial
import json
import time
def sc(p):
    stack=deque(); output=[]
    for x in p:
        while len(stack)>=2:
            triple=(x,stack[0],stack[1])
            order=tuple(1+sum(b<a for b in triple) for a in triple)
            if order!=(2,1,3): break
            output.append(stack.popleft())
        stack.appendleft(x)
    return tuple(output)+tuple(stack)
assert sc((5,2,4,1,3))==(2,1,3,4,5)
assert sum(sc(p)==(1,2,4,3) for p in permutations(range(1,5)))==2
t=time.perf_counter()
counts=Counter()
inputs=0
for p in permutations(range(1,10)):
    counts[sc(p)]+=1
    inputs+=1
assert inputs==factorial(9)
hist=Counter(counts.values()); hist[0]=factorial(9)-len(counts)
assert sum(hist.values())==sum(k*v for k,v in hist.items())==factorial(9)
assert set(hist)=={0,128}|(set(range(1,65))-{55})
out=dict(n=9,inputs=inputs,positive_outputs=len(counts),histogram=dict(sorted(hist.items())),
         missing_within_1_64=sorted(set(range(1,65))-set(hist)),elapsed_seconds=time.perf_counter()-t,
         independent_full_n9_executed=True,algorithm='top-first deque, comparison-count standardization, tuple Counter')
print(json.dumps(out,indent=2),flush=True)
