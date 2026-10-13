# Exact statement and scope

SC_sigma forbids one consecutive length-three pattern in the stack read from top to bottom. A failed prospective push pops the current top and retries the same input; the final stack is drained top-to-bottom. This is the scalar-pattern map in the source, not a map forbidding both 213 and 231 simultaneously.

For sigma in {213,231}, define f_(sigma,n)(pi) as the number of inputs in S_n mapping to output pi, and A_n^sigma as these values over all outputs in S_n, including unattained outputs of fertility zero. The recorded n=9 computation gives the entire spectrum and histogram for 213. A complete value-complement conjugacy proves the same histogram for 231, including empty fibers; no separate SC231 enumeration is claimed.

The original Conjecture 4.1 prints sigma={213,231} and the subset symbol. Read in the context of the two individual maps, its stated requirement is {1,...,2^(n-3)} subset A_n^sigma. The counterexample is precisely 55 missing at n=9, where the required range ends at 64. It fails whether the subset symbol denotes proper or non-strict inclusion. This note does not replace the conjecture by a vague interval claim.

Theorem 1.1 has quantifiers: for every positive fertility f and every sigma in S_3, there exist some length n and output pi in S_n with that fertility. The length can depend on f and sigma. Its truth is compatible with the fixed-length gap. The note needs no length-ten witness for 55 and makes no claim about the smallest failing n, larger complete spectra, simultaneous avoidance or worldwide priority.

The proof is conditional on the implementation, the standard-library permutation iterator, exact integer/tuple/container semantics and the recorded completed execution. Hashes identify versions; they do not by themselves certify mathematical correctness or historical execution. The portable entry is statically matched to the original mathematical AST and is explicitly unrun.
