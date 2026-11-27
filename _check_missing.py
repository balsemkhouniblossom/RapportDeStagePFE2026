import re, io, os
base = r"C:\Users\Balsem\Desktop\PFE DOC REPORT"
for f in ["contenu_sprint1.tex","contenu_sprint2.tex","contenu_sprint3.tex","contenu_sprint4.tex","contenu_sprint5.tex","contenu_sprint6.tex","contenu_sprint7.tex"]:
    t = io.open(os.path.join(base,"contenu",f), encoding="utf-8").read()
    for m in re.finditer(r"\\IfFileExists\{([^}]*)\}", t):
        p = m.group(1)
        exists = os.path.exists(os.path.join(base, p.replace("/", "\\")))
        if not exists: print(f, "MISSING", p)
