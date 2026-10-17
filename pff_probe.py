#!/usr/bin/env python3
"""
pff_probe.py - LOCAL, PRIVATE inventory of everything your PFF key can pull.

Run from ~/football-intel:  python3 pff_probe.py [--season 2026] [--week 6] [--call]

1. Lists every `restish pff` command (from `restish pff --help`).
2. For each one, reads its --help to see what arguments it needs.
3. With --call, calls every command whose only arguments are league/season/week (nfl, season, week),
   saves a small sample, and records the field names it returns.

Output (gitignored, never published): private/pff/probe/inventory.json, inventory.txt, sample_<cmd>.json
"""
import argparse, json, os, re, shutil, subprocess, sys

ROOT = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(ROOT, "private", "pff", "probe")


def run(args, timeout=120):
    r = subprocess.run(args, capture_output=True, text=True, timeout=timeout)
    return r.returncode, r.stdout, r.stderr


def find_restish():
    return shutil.which("restish") or (os.path.expanduser("~/go/bin/restish")
                                       if os.path.exists(os.path.expanduser("~/go/bin/restish")) else None)


SKIP = {"logout", "whoami", "openapi-json", "openapi-yaml", "help", "completion"}


def clean(t):
    return re.sub(r"\x1b\[[0-9;]*m", "", t)


def list_commands(rs):
    _, out, err = run([rs, "pff", "--help"])
    text = clean(out + "\n" + err)
    cmds = []
    for line in text.splitlines():
        m = re.match(r"^  ([a-z][a-z0-9-]+)\s{2,}\S", line)
        if m and m.group(1) not in SKIP:
            cmds.append(m.group(1))
    return sorted(set(cmds)), text


def arg_names(rs, cmd):
    _, out, err = run([rs, "pff", cmd, "--help"])
    text = clean(out + "\n" + err)
    open(os.path.join(OUT, "help_%s.txt" % cmd), "w").write(text)
    for line in text.splitlines():
        m = re.search(r"restish pff %s\s+(.*)$" % re.escape(cmd), line)
        if m:
            toks = [t for t in m.group(1).split() if t.startswith("<")]
            return [t.strip("<>") for t in toks], text
    return None, text


def shape(x, depth=0):
    if isinstance(x, dict):
        return {k: shape(v, depth + 1) for k, v in list(x.items())[:40]} if depth < 3 else "dict"
    if isinstance(x, list):
        return [shape(x[0], depth + 1)] if x and depth < 3 else "list[%d]" % len(x)
    return type(x).__name__


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--season", default="2026")
    ap.add_argument("--week", default="6")
    ap.add_argument("--call", action="store_true", help="actually call the season/week commands")
    a = ap.parse_args()
    rs = find_restish()
    if not rs:
        sys.exit("restish not found")
    os.makedirs(OUT, exist_ok=True)
    cmds, raw = list_commands(rs)
    if not cmds:
        open(os.path.join(OUT, "help_raw.txt"), "w").write(raw)
        sys.exit("Could not parse command list; raw help saved to private/pff/probe/help_raw.txt - paste it to Claude.")
    inv = {}
    for c in cmds:
        args, _ = arg_names(rs, c)
        entry = {"args": args}
        values = {"league": "nfl", "season": a.season, "week": a.week}
        if a.call and args is not None and all(x.lower() in values for x in args):
            code, out, err = run([rs, "pff", c] + [values[x.lower()] for x in args], timeout=180)
            if code == 0:
                try:
                    data = json.loads(out)
                    json.dump(data, open(os.path.join(OUT, "sample_%s.json" % c), "w"))
                    entry["status"] = "ok"
                    entry["shape"] = shape(data)
                except ValueError:
                    entry["status"] = "not json"
            else:
                entry["status"] = "failed: " + err.strip()[:160]
        inv[c] = entry
        print("%-50s %s %s" % (c, args, entry.get("status", "")))
    json.dump(inv, open(os.path.join(OUT, "inventory.json"), "w"), indent=1)
    with open(os.path.join(OUT, "inventory.txt"), "w") as f:
        for c, e in inv.items():
            f.write("%s  args=%s  %s\n" % (c, e["args"], e.get("status", "")))
    with open(os.path.join(OUT, "help_all.txt"), "w") as f:
        for c in cmds:
            f.write("=" * 70 + "\n" + c + "\n" + "=" * 70 + "\n")
            f.write(open(os.path.join(OUT, "help_%s.txt" % c)).read() + "\n")
    print("\nSaved private/pff/probe/inventory.txt, help_all.txt and samples. Attach inventory.txt AND help_all.txt for Claude.")


if __name__ == "__main__":
    main()
