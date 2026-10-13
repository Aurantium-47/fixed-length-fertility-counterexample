# A length-nine gap in consecutive-stack fertility spectra

Aurantium · v0.1.0 · 14 October 2026

For each single forbidden pattern sigma=213 or sigma=231, the exact fertility spectrum at length nine is

\[
A_9^\sigma=\{0,128\}\cup(\{1,\ldots,64\}\setminus\{55\}).
\]

The completed independent SC213 enumeration visited all 362880 inputs, obtaining 97278 positive-fertility outputs and 265602 zero-fertility outputs. The full histogram is retained. Value complement conjugates SC213 to SC231 operation by operation, so the same histogram holds without a second enumeration.

Since 55<=2^(9-3), this refutes the specific fixed-length inclusion {1,...,2^(n-3)} subset A_n^sigma proposed in Kemeklis's Conjecture 4.1. It does not refute Theorem 1.1, which permits the length to vary. No smallest-counterexample-length claim, length-ten result or simultaneous-pattern-avoidance statement is made.

- [Complete note](paper/proof.pdf) and [standalone TeX](paper/proof.tex)
- [Unchanged original histogram/result](data/n9.recomputed.json)
- [Path-free execution receipt](evidence/EXECUTION.json), [original stdout](evidence/original_stdout.jsonl), [original empty stderr](evidence/original_stderr.txt)
- [Portable census code](code/reproduce_n9.py), [reproducibility](REPRODUCIBILITY.md), [scope](SCOPE.md), [reference](REFERENCES.md), [rights](RIGHTS.md)

The census was not rerun for this version. The portable stdout-only entry preserves the mathematical function, full enumeration and assertions at the AST level, but **its new packaged bytes have not been executed**. The completed execution belongs to the original script identified in the receipt. Running the supplied script performs the full n=9 enumeration; it has no command-line options.

This is an exhaustive computational proof with an explicit implementation/runtime trust boundary, not a proof-assistant certificate or hand classification of all fibers. Prepared with AI assistance; no independent human peer review or worldwide-priority certification is asserted. Third-party source PDFs are linked, not redistributed. WHITELIST.txt and MANIFEST.json identify the complete payload.
