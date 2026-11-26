# Q364: Full-distance-two voter bundles of size at most three

**Theorem.** Given a plurality election with a distinguished candidate p and a budget k, deciding whether adding the union of the bundles of at most k potential voter leaders makes p a co-winner is NP-complete when each bundle is exactly all potential voters at adjacent-swap distance at most two and has size at most three. Hardness holds when the graph of distinct potential voters at distance at most two is a disjoint union of induced five-vertex paths.

**Membership in NP.** Given the selected leaders, compute Kendall distances by counting unordered candidate pairs ranked in opposite orders. This count equals the minimum number of adjacent swaps; bubble sorting is one proof. Compute the bundle union and count first places. The time is polynomial in the explicit election size.

**Source problem.** Balanced perfect three-dimensional matching: disjoint X,Y,Z have common cardinality n; triples T are a subset of X×Y×Z. Decide whether n triples cover every element exactly once. This is the perfect 3DM problem (Karp's three coordinate copies can be renamed to obtain disjoint parts). Write m=|T|. Restrict to positive n and every x in at least one triple, without affecting hardness: the excluded cases are trivial and can be mapped to fixed yes/no instances (e.g. no potential voters, k=0, and one registered voter supporting p or another candidate).

**Election.** Candidates include p, a sentinel g, and all elements of X,Y,Z. Add one private dummy d_t per triple t and six distinct marker candidates per triple, partitioned into three pairs with a fixed internal orientation. Fix a global order of marker pairs and a global order of all other candidates. For t=(x,y,z), use five potential voters. In this table 0=p, 1=z, 2=x, 3=y, and 4=d_t. The initial five ranks in order are:

| Voter | Initial five candidates |
|---|---|
| 1 | 31024 |
| 2 | 10324 |
| 3 | 01234 |
| 4 | 20134 |
| 5 | 20143 |

Append all marker pairs in their global order, reversing exactly the three private pairs of t, then all remaining candidates in the global order restricted to those remaining. Each row is a strict complete ranking. Between two gadgets the private three pairs of each gadget are reversed in exactly one ranking, giving at least six Kendall disagreements. Within a gadget only the five initial ranks vary. In table order, the distances above the diagonal are (2,4,6,7) for row 1, (2,4,5) for row 2, (2,3) for row 3, and (1) for row 4. Thus the radius-two graph has exactly the consecutive edges within each gadget. Every bundle is the leader plus its path neighbors and has size at most three.

Set k=m. For registered voters, assign p initial score 2m, g score 3m, each y and z score 3m−1, and each x score 3m−(2d(x)−2), where d(x) counts triples using x. All others start at zero. These scores are nonnegative because 1≤d(x)≤m. Realize them with that many voters ranking the indicated candidate first and all others in any fixed order. There are polynomially many candidates and voters, and a polynomial output size even with explicit full rankings.

**Forcing the choices.** Each gadget has one p-voter (number 3), g never receives a new vote, and different gadgets' bundles are disjoint. Therefore p must obtain all m new p-votes to reach 3m. Budget m forces one leader per gadget from among voters 2, 3, 4. These three leader choices respectively add one p-vote and the following opponent vote multisets:
- L: {y,z};
- M: {z,x};
- R: {x,x}.

Hence each y and z tolerates one extra vote and each x tolerates 2d(x)−2. If all gadgets using x chose R, they would award 2d(x) x-votes. Thus at least one gadget for each x must choose L or M, and either such choice uses one z vote. With n z candidates of capacity one, at most n gadgets can choose L or M in all. Consequently exactly one per x does so. That gadget must choose L: M saves only one x-vote versus the all-R baseline, but the capacity requires saving at least two. The n L-triples have distinct y and distinct z by their capacities, and exactly one per x, forming a perfect matching.

Conversely, select L for the matching triples, and R elsewhere. The x-votes added are exactly 2d(x)−2; each y and z receives one, and p ties g and all these candidates at 3m. No dummy or marker candidate receives any vote. This proves equivalence.

## Scope and sources

- [Chen dissertation §6.8, printed p. 149](https://depositonce.tu-berlin.de/bitstreams/01ad4a50-8834-4ecd-9607-88785af545eb/download#page=177) asks for full distance two and maximum size three in the constructive plurality problem.
- [Bulteau, Chen, Faliszewski, Niedermeier, Talmon, TCS 2015](https://igm.univ-mlv.fr/~bulteau/pdf/BCFNT-tcs15.pdf) prove hardness for size three at radius at least three (Theorem 7), and for radius one with size four (Theorem 8). Arbitrary symmetric small bundles do not automatically realize the fixed-radius condition. This proof uses a different path gadget and perfect 3DM. No new priority claim is made.
- [Karp, Reducibility Among Combinatorial Problems](https://doi.org/10.1007/978-1-4684-2001-2_9), problem 17.
- [Pinned catalog Q364](https://github.com/10m-u/open-problems-catalog/blob/ca8d4d44ba3db527f19f28928c240168f545ecfe/problems/game_theory/social-choice-voting-theory.md#q364).
