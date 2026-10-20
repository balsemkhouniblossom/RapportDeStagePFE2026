# Rapport de stage PFE 2026

Ce dépôt contient le rapport de projet de fin d'études réalisé au sein d'**IPROTEX Tunisie**. Le projet porte sur la conception et le développement d'une plateforme web de Gestion de la Maintenance Assistée par Ordinateur (**GMAO**).

La solution couvre notamment la gestion des équipements, la maintenance préventive et corrective, les ordres de travail, les stocks, les documents techniques, la supervision en temps réel et la détection d'anomalies.

## Structure du dépôt

- `main.tex` : point d'entrée du document LaTeX ;
- `contenu/` : contenu principal du rapport et remerciements ;
- `pages/` : couverture, page de titre et tables ;
- `preambule/` : packages, styles, couleurs et macros ;
- `figures/` : illustrations et diagrammes PlantUML ;
- `images/` et `Logos/` : ressources graphiques ;
- `references.bib` : références bibliographiques ;
- `main.pdf` : version PDF générée du rapport.

## Compilation

Une distribution LaTeX telle que [MiKTeX](https://miktex.org/) ou [TeX Live](https://www.tug.org/texlive/) est nécessaire.

```bash
latexmk -pdf main.tex
```

Pour supprimer les fichiers de compilation intermédiaires :

```bash
latexmk -c
```

## Auteur

Balsem Khouni — Projet de fin d'études, 2026.
