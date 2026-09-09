"""Check the archived 604-vector construction with exact integer arithmetic.

This verifies one output artifact, not the swarm process that produced it.
No code from the downloaded repository is executed.
"""
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
SOURCE = ROOT / 'repositories/togethercomputer__EinsteinArena-new-SOTA/kissing-number/solutions/solution_n=604_d=11.json'

def nonnegative(a, b):
    """Whether a + b*sqrt(2) >= 0, using only integer comparisons."""
    if a >= 0 and b >= 0:
        return True
    if a < 0 and b < 0:
        return False
    if a >= 0:  # b < 0
        return a*a >= 2*b*b
    return 2*b*b >= a*a

def squared_norm(v):
    return sum(p*p + 2*q*q for p,q in v), sum(2*p*q for p,q in v)

raw = json.loads(SOURCE.read_text())
assert raw['n'] == 604 and raw['dim'] == 11
vectors = raw['vectors']
assert len(vectors) == 604
assert all(len(v)==22 and all(type(x) is int for x in v) for v in vectors)
vectors = [list(zip(v[::2],v[1::2])) for v in vectors]
assert all(squared_norm(v) == (36,0) for v in vectors)
pairs = 0
for i, left in enumerate(vectors):
    for right in vectors[i+1:]:
        differences=[(a-c,b-d) for (a,b),(c,d) in zip(left,right)]
        a,b=squared_norm(differences)
        assert nonnegative(a-36,b),(i,pairs,a,b)
        pairs+=1
result = {'artifact':str(SOURCE.relative_to(ROOT)),
          'sha256':hashlib.sha256(SOURCE.read_bytes()).hexdigest(),
          'vectors':len(vectors),'dimensions':11,'squared_radius':36,
          'pairwise_distance_checks':pairs,'all_squared_distances_at_least':36,
          'arithmetic':'Exact integer comparisons in Q(sqrt(2)); no floating point.',
          'verified':'Construction validity only; no causal swarm-advantage or novelty claim.'}
(ROOT/'sources/einstein-artifact-verification.json').write_text(json.dumps(result,indent=2)+'\n')
print(json.dumps(result))
