import json, re, sys

base = r"C:\Users\机械革命\Doubao\chats\2026-11-20\new-chat\词盒背单词"
html = open(base + r"\词盒背单词.html", encoding="utf-8").read()

words = set()
for m in re.finditer(r"^([A-Za-z][A-Za-z' -]*)\|", html, re.M):
    w = m.group(1).strip().lower()
    if " " in w:
        continue
    words.add(w)

ipa = {}
with open(base + r"\tools\en_US.txt", encoding="utf-8") as f:
    for line in f:
        parts = line.rstrip("\n").split("\t")
        if len(parts) != 2:
            continue
        k = parts[0].strip().lower()
        if k in words and k not in ipa:
            ipa[k] = parts[1].strip().split(",")[0].strip()

missing = sorted(words - set(ipa.keys()))
print("words", len(words), "matched", len(ipa), "missing", len(missing))
print("sample missing:", missing[:30])

with open(base + r"\tools\ipa_map.json", "w", encoding="utf-8") as f:
    json.dump(ipa, f, ensure_ascii=False)
