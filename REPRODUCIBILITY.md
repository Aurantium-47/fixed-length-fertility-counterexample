# Reproducibility and version binding

## Completed original run

The original independent n=9 script completed on 13 October 2026. Its process receipt records start `2026-10-13T04:27:46.4455254Z`, end `2026-10-13T04:27:51.1014079Z`, exit 0, null stop reason, and observed peak working set 31113216 bytes with 50 ms sampling. The historical monitor imposed a 60-second time cap and 128-MiB working-set cap by process polling; it was not a Windows Job Object commit-memory guard. The receipt names an executable but does not record its interpreter version; no version is inferred.

The program's internal census timer reports 4.4192823 seconds. It visits all 362880 inputs, computes 97278 attained outputs, and inserts the 265602 unattained outputs into histogram bin 0. Its original assertions check both total-output and weighted-input accounting identities and the exact support. Only after computing and saving the complete result does it compare the histogram with an author-supplied record; archived stdout reports that comparison passed. This is not merely agreement of two supplied files.

`data/n9.recomputed.json`, `evidence/original_stdout.jsonl` and the empty `evidence/original_stderr.txt` preserve the original bytes. The path-free `evidence/EXECUTION.json` transcribes the receipt fields and binds their source hashes. It does not expose the original machine paths.

| Artifact | SHA-256 |
|---|---|
| Original executed script, frozen version | `2decdeaeaa39953e0a99c14b3ee25e047a717b82a47001d7523082fcb8d3641e` |
| Original process receipt | `a826e9391f3727ec1289f5681742f3e83ba1cb1a2499ed2dc84f30d448fb4469` |
| Original complete result | `ccf28642e4004512df0bd4054c0f98ce85d007442cc42effa17e697d2bbed882` |
| Packaged stdout-only entry | `201d88f7fd9ee367a4749e74f4ed7ede511f0ea2bce41704a0157c1224a5e3ff` |

These hashes identify retained versions; they are not independent attestations of execution or proof-assistant certificates.

## Portable entry: not executed in this preparation

`code/reproduce_n9.py` preserves the original `sc` function and every statement from it through result construction: the two initial example assertions, timer setup, all-input iteration, tuple Counter, histogram construction, accounting/support assertions and result fields. Static AST comparison excludes location/formatting metadata and finds this entire mathematical block identical. No census function was imported or executed for that comparison.

Only a neutral header, removal of the unused pathlib import, and stdout-only final output differ. The original path-specific file write and post-computation author-record comparison are omitted. The newly packaged bytes have **not** been run. The `independent_full_n9_executed` field in the archived data describes the original completed run, not a claimed run of this wrapper.

For a future authorized reproduction, use a Python interpreter supporting this standard-library source with assertions enabled:

```text
python -I -B code/reproduce_n9.py
```

It reads no evidence file and writes only complete JSON to stdout. Capture stdout and stderr in a new output directory outside the package. Do not use `-O`. There are no command-line options: invoking the script, including with unsupported arguments, performs the full enumeration. No `--help` run is part of this preparation. Compare the histogram and exact count fields with the archived data; elapsed time naturally varies.

No new enumeration, larger scan, original author suite or new resource request was needed to document the already completed computation. The program computes only SC213; the manuscript's value-complement proof establishes the SC231 histogram.

## Manuscript build

`paper/proof.tex` is standalone. With its standard LaTeX packages installed, run `pdflatex proof.tex` twice from `paper/` for references. The histogram table is a transcription of the saved result, with an explicit zero entry for 55; no enumeration is invoked by LaTeX. Rebuilding may change PDF metadata or font encoding. MANIFEST.json identifies the supplied bytes. PDF layout checks are separate from mathematical review and execution.
