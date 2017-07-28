# Nouveau Front Tracking

## Changement d'architecture

- classe Evolution
    - flux, instantanné, solution, temps courant
    - interaction suivante, résolution jusqu'à
- classe Fronts
    - eg, ed, ti, xi, tf, xf, v
    - position, saut, affichage
- classe Flux
    - chaine latex
    - evaluation (`__call__`), riemann
- classe Solution
    - fronts (liste?), temps de validité
    - ajout de fronts
- classe Instantané
    - fronts (liste?), début
    - temps position et fronts de la prochaine interaction

## Aménagement algorithme

- possibilité de discrétiser le flux à la Dafermos/Bressan
- gestion des arrondis explicites pour éviter les mauvaises surprises
- utilisation des fractions dans des cas algébriques
- distinction cas scalaire/vectoriel pour la vitesse des fronts
