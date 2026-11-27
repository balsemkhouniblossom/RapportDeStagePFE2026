import re, io, os
base = "C:\\Users\\Balsem\\Desktop\\PFE DOC REPORT\\contenu"
labels = ["fig:sprint1-login","fig:sprint1-user-approval","fig:sprint2-machines-list","fig:sprint2-machine-detail","fig:sprint2-document-viewer","fig:sprint3-preventive-validation","fig:sprint3-plans-list","fig:sprint4-work-orders","fig:sprint4-intervention-report","fig:sprint5-stock-list","fig:sprint5-dashboard","fig:sprint6-devices","fig:sprint6-live-monitoring","fig:sprint6-anomaly-analysis"]
for f in sorted(os.listdir(base)):
    if not f.endswith(".tex"): continue
    t = io.open(os.path.join(base,f), encoding="utf-8").read()
    for l in labels:
        n = len(re.findall(r"\\ref\{"+re.escape(l)+r"\}", t))
        if n: print(f, l, "refs:", n)
