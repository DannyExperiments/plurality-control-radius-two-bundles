# Reproducibility

Run from the repository root with Python 3.11 or later.

    python3 -I scripts/verify_repository.py
    python3 -I verification/src/replay.py

The standard-library replay reconstructs the full rankings, computes Kendall distances and checks the exact neighborhood graph for every small instance tested. It compares plurality outcomes with a direct perfect-matching check on the 225 nonisolated-X instances of size two per part. In the 64 instances with at most three triples, it also tests all leader subsets within the budget. It checks the example, seven fixed-radius lifts and 125 unique-winner comparisons. [Recorded replay](verification/results/replay.txt).

Open the HTML from the [offline explorer archive](visualization/radius-two-explorer.zip) to try the choices. [Build the paper](paper/BUILD.md).
