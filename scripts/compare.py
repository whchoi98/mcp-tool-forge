"""Compare Haiku 3.5 vs Opus 4.6 LLM mapping results."""
import py_compile
import json
from pathlib import Path

# Opus 4.6 current results
opus_stats = {}
opus_funcs = {}
for f in sorted(Path("output").glob("*/boto3/tools.py")):
    server = f.parts[1]
    try:
        py_compile.compile(str(f), doraise=True)
        opus_stats[server] = "OK"
    except py_compile.PyCompileError:
        opus_stats[server] = "SYNTAX_ERROR"
    with open(f) as fh:
        opus_funcs[server] = sum(1 for line in fh if line.startswith("def "))

# Haiku baseline
with open("/tmp/haiku_baseline.json") as f:
    haiku_stats = json.load(f)
with open("/tmp/haiku_func_counts.json") as f:
    haiku_funcs = json.load(f)

# Summary
opus_ok = sum(1 for v in opus_stats.values() if v == "OK")
opus_err = sum(1 for v in opus_stats.values() if v == "SYNTAX_ERROR")
opus_total = sum(opus_funcs.values())
haiku_ok = sum(1 for v in haiku_stats.values() if v == "OK")
haiku_err = sum(1 for v in haiku_stats.values() if v == "SYNTAX_ERROR")
haiku_total = sum(haiku_funcs.values())

print("=" * 65)
print("  Haiku 3.5 vs Opus 4.6 Comparison")
print("=" * 65)
print()
print(f"{'Metric':<30} {'Haiku 3.5':>12} {'Opus 4.6':>12}")
print("-" * 55)
print(f"{'boto3 files':<30} {len(haiku_stats):>12} {len(opus_stats):>12}")
print(f"{'Syntax OK':<30} {haiku_ok:>12} {opus_ok:>12}")
print(f"{'Syntax ERROR':<30} {haiku_err:>12} {opus_err:>12}")
print(f"{'Total functions':<30} {haiku_total:>12} {opus_total:>12}")
h_rate = haiku_ok / len(haiku_stats) * 100 if haiku_stats else 0
o_rate = opus_ok / len(opus_stats) * 100 if opus_stats else 0
print(f"{'Pass rate':<30} {h_rate:>11.1f}% {o_rate:>11.1f}%")
print()

# Per-server
improved = 0
degraded = 0
common = sorted(set(haiku_stats.keys()) & set(opus_stats.keys()))
print(f"{'Server':<45} {'H-fn':>5} {'O-fn':>5} {'H-syn':>8} {'O-syn':>8}")
print("-" * 72)
for s in common:
    hf = haiku_funcs.get(s, 0)
    of = opus_funcs.get(s, 0)
    hs = haiku_stats[s]
    os_ = opus_stats[s]
    marker = ""
    if hs == "SYNTAX_ERROR" and os_ == "OK":
        marker = " FIXED"
        improved += 1
    elif hs == "OK" and os_ == "SYNTAX_ERROR":
        marker = " REGRESSED"
        degraded += 1
    print(f"  {s:<43} {hf:>5} {of:>5} {hs:>8} {os_:>8}{marker}")

# Opus-only servers
opus_only = sorted(set(opus_stats.keys()) - set(haiku_stats.keys()))
if opus_only:
    print()
    print("Opus-only (new):")
    for s in opus_only:
        of = opus_funcs.get(s, 0)
        os_ = opus_stats[s]
        print(f"  {s:<43} {'':>5} {of:>5} {'':>8} {os_:>8}")

print()
print(f"Syntax fixes: {improved}, Regressions: {degraded}")
