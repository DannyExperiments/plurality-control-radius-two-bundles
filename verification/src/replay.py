#!/usr/bin/env python3
from collections import Counter
from itertools import combinations, permutations, product

def distance(a,b):
    rank={x:i for i,x in enumerate(a)}
    return sum(rank[x]>rank[y] for x,y in combinations(b,2))

def instance(n,ts):
    X=[('x',i) for i in range(n)]
    Y=[('y',i) for i in range(n)]
    Z=[('z',i) for i in range(n)]
    marker=[(('a',j),('b',j)) for j in range(3*len(ts))]
    ordinary=['p','g',*X,*Y,*Z,*[('d',t) for t in range(len(ts))]]
    ballots=[]
    deg=Counter(x for x,_,_ in ts)
    m=len(ts)
    for t,(x,y,z) in enumerate(ts):
        labels=['p',Z[z],X[x],Y[y],('d',t)]
        tail=[v for j,pair in enumerate(marker)
              for v in (pair[::-1] if j//3==t else pair)]
        tail += [v for v in ordinary if v not in labels]
        for code in ('31024','10324','01234','20134','20143'):
            a=[labels[int(i)] for i in code]+tail
            assert len(set(a))==len(ordinary)+2*len(marker)==len(a)
            ballots.append(a)
    bundles=[]
    for i,a in enumerate(ballots):
        bundle=frozenset(j for j,b in enumerate(ballots) if distance(a,b)<=2)
        assert bundle==frozenset(j for j in range(len(ballots))
                                 if i//5==j//5 and abs(i-j)<=1)
        bundles.append(bundle)
    start=Counter({'p':2*m,'g':3*m})
    start.update({y:3*m-1 for y in Y+Z})
    start.update({x:3*m-2*deg[x[1]]+2 for x in X})
    return ballots,bundles,start

def can_win(ballots,bundles,start,selections):
    for leaders in selections:
        union=set().union(*(bundles[i] for i in leaders))
        score=start+Counter(ballots[j][0] for j in union)
        if max(score.values(), default=0)==score['p']:
            return True
    return False

def perfect(n,ts):
    triples=set(ts)
    P=list(permutations(range(n)))
    return any(all((i,y[i],z[i]) in triples for i in range(n))
               for y,z in product(P,repeat=2))

def lift(ballots, radius):
    if radius == 3:
        base = ballots[0]
        return [tuple(ballot) + (('aux', parity), ('aux', 1-parity))
                for ballot in ballots
                for parity in [distance(base, ballot) % 2]]
    copies = radius // 2
    return [tuple((block, candidate) for block in range(copies) for candidate in ballot)
            for ballot in ballots]


def check_example_and_extensions():
    triples = [(0, 0, 0), (0, 1, 1), (1, 1, 1)]
    ballots, bundles, initial = instance(2, triples)
    focus = (1, 8, 11)
    assert can_win(ballots, bundles, initial, [focus])

    def scores(leaders):
        union = set().union(*(bundles[i] for i in leaders))
        return initial + Counter(ballots[i][0] for i in union)

    assert scores(focus)['p'] == scores(focus)['g'] == 9
    assert scores((2, 8, 11))[('x', 0)] == 10
    assert scores((1, 6, 11))[('y', 1)] == scores((1, 6, 11))[('z', 1)] == 10
    for leaders in product(*(range(5*j, 5*j+5) for j in range(3))):
        final = scores(leaders)
        rival = max(score for candidate, score in final.items() if candidate != 'p')
        assert (final['p'] >= rival) == (final['p'] + 1 > rival)
    for radius in range(2, 9):
        lifted = lift(ballots, radius)
        found = [frozenset(j for j, other in enumerate(lifted) if distance(ballot, other) <= radius)
                 for ballot in lifted]
        assert found == bundles
    print("Worked election: winning scores and two one-step failures checked.")
    print("Extensions: 7 fixed-radius lifts and 125 unique-winner score comparisons.")


def main():
    cases=wins=exhaustive=0
    all_ts=list(product(range(2),repeat=3))
    for mask in range(1<<len(all_ts)):
        triples=[t for i,t in enumerate(all_ts) if mask>>i&1]
        if {x for x,_,_ in triples}!={0,1}:
            continue
        ballots,bundles,start=instance(2,triples)
        m=len(triples)
        choices=[[i for i in range(5*j,5*j+5) if 5*j+2 in bundles[i]]
                 for j in range(m)]
        answer=perfect(2,triples)
        assert can_win(ballots,bundles,start,product(*choices))==answer
        if m<=3:
            assert can_win(ballots,bundles,start,
                (L for k in range(m+1) for L in combinations(range(5*m),k)))==answer
            exhaustive+=1
        cases+=1
        wins+=answer
    print(f"Verified {cases} complete 2×2×2 instances with no isolated X; {wins} yes.")
    print(f"Also exhaustively enumerated unrestricted subsets of leaders in {exhaustive} instances.")
    check_example_and_extensions()

if __name__=='__main__':
    main()
