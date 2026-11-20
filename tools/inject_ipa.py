import json

base = r"C:\Users\机械革命\Doubao\chats\2026-11-20\new-chat\词盒背单词"
p = base + r"\词盒背单词.html"
html = open(p, encoding="utf-8").read()
ipa = json.load(open(base + r"\tools\ipa_map.json", encoding="utf-8"))
data = json.dumps(ipa, ensure_ascii=False, separators=(",", ":"))

anchor = "const KEY = 'cihe_v1';"
if "const IPA =" in html:
    print("already patched")
else:
    html = html.replace(anchor, anchor + "\nconst IPA = " + data + ";", 1)
    open(p, "w", encoding="utf-8").write(html)
    print("patched, ipa entries:", len(ipa), "chars:", len(data))
