# Dépression et anxiété : qui est le plus exposé ?

**Équipe :** Dieu-Donné FIANKO, Faustine DESSI 

**Mail(s) de contact :** dieudonne.fianko1@gmail.com, abla.dessi02@gmail.com 

**Défi :** Défi 1 — Santé mentale

## Notre question

La dépression et l'anxiété concernent-elles tout le monde de la même façon, ou certaines populations sont-elles particulièrement exposées ?

## Notre visualisation

Site web interactif, statique et sans dépendance externe : https://phoenix-laboratoire.github.io/dieudo_faustine_Odisse_Dataviz_Challenge_2026/

Code source : https://github.com/phoenix-laboratoire/dieudo_faustine_Odisse_Dataviz_Challenge_2026

Il propose :
- une carte des régions (métropole et DROM) pour les épisodes dépressifs (filtrables par sexe et par âge) et pour le trouble anxieux généralisé ;
- les profils de prévalence de l'anxiété en France selon l'âge, le diplôme, la profession, le type de ménage et la situation financière, séparément pour les femmes et les hommes, avec intervalles de confiance ;
- les épisodes dépressifs par âge et par sexe pour la région choisie ;
- une section « Lire avec prudence » (limites des données) et l'affichage permanent du 3114, numéro national de prévention du suicide.

## Les données utilisées

| Source | Jeu de données | Lien |
|---|---|---|
| Odissé | Épisodes dépressifs : Indicateurs du Baromètre de Santé publique France 2024 - Détail Région — `data/episodes_depressifs_2024.csv` | https://odisse.santepubliquefrance.fr/explore/dataset/episodes-depressifs-indicateurs-du-barometre-de-sante-publique-france-2024-detail-region/ |
| Odissé | Trouble anxieux généralisé : Indicateurs du Baromètre de Santé publique France 2024 — `data/trouble_anxieux_generalise_2024.csv` | https://odisse.santepubliquefrance.fr/explore/dataset/trouble-anxieux-generalise-indicateurs-du-barometre-2024/ |
| IGN / Etalab (via france-geojson) | Contours des régions avec outre-mer, simplifiés dans `data/regions.json` | https://github.com/gregoiredavid/france-geojson |

Les CSV sont des extractions des jeux Odissé indiqués. Mayotte n'est pas couverte par le Baromètre.

## Les outils employés

- HTML, CSS et JavaScript natifs : aucune bibliothèque, aucune police ni requête externe (choix de frugalité).
- Python et la bibliothèque Shapely, uniquement pour simplifier le fonds de carte (`scripts/build_map.py`).
- GitHub Pages pour l'hébergement.

Pour tester en local : `python -m http.server 8000`, puis http://localhost:8000.

## Licence

Ce projet est publié sous licences libres :

| Type de contenu | Licence |
|---|---|
| Code source (`index.html`, `scripts/`) | Licence MIT |
| Données (`data/`) | Licence Ouverte 2.0 (données Odissé et contours IGN/Etalab) |
| Contenus textuels et visuels | Creative Commons CC-BY 4.0 |

Les données issues d'Odissé sont disponibles sous Licence Ouverte 2.0 ; leur réutilisation doit respecter cette licence.
