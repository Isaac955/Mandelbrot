# Ensemble de Mandelbrot

Ce projet consiste à explorer l'ensemble de Mandelbrot, une fractale célèbre dans le domaine des mathématiques. L'ensemble de Mandelbrot est une représentation graphique de l'ensemble des nombres complexes pour lesquels l'itération d'une fonction simple ne diverge pas.

## À propos de l'ensemble de Mandelbrot

L'ensemble de Mandelbrot est défini par l'ensemble de points \(c\) dans le plan complexe pour lesquels la suite récurrente \(z_{n+1} = z_{n}^2 + c\), avec \(z_{0} = 0\), reste bornée lorsque \(n\) tend vers l'infini.

## Fonctionnalités

Ce projet offre les fonctionnalités suivantes :

- Génération d'une représentation graphique de l'ensemble de Mandelbrot.
- Paramétrage de la précision de l'image générée.

## Prérequis

Avant de commencer, assurez-vous d'avoir les éléments suivants installés :

### - Python 3
### - `pip install Pillow`

## Comment exécuter le projet

1. Clonez ce dépôt sur votre machine locale.
2. Assurez-vous d'avoir les prérequis installés.
3. Paramétrer la précision de l'image et explorer l'ensemble.
4. Exécutez le fichier principal `mandelbrot_tp.py` pour générer l'image de l'ensemble de Mandelbrot.
<br>
PS : Veuillez noter que plus vous augmentez la précision, plus le temps de calcul sera long pour générer une image plus détaillée. Soyez donc patient pendant la génération de la fractale


## Exemple d'utilisation

```bash
$ python mandelbrot_tp.py
