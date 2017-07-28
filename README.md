# Wave Front Tracking

On va chercher à implémenter un algorithme de wave front tracking pour la résolution des lois de conservation en dimension un.

## Objectifs
- loi scalaire sur la droite/cercle
- loi scalaire sur un segment
- système nxn sur la droite
- système nxn sur un segment

## Design

- Découpler au maximum en particulier du solveur de Riemann
- Faire attention aux erreurs d'arrondis pour éviter les traversées de fronts
- Interactions multiples ou algorithme pour ajuster les vitesses de fronts
