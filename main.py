import os

ENTRY = "Performance review: brilliant strategist, fearless delegator, and the only manager whose 'quick question' became a trilogy."

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(ENTRY)
