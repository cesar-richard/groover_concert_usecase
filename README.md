# Backend Technical Challenge - Usecase "Concert planning" / "Programmation des morceaux d'un concert" (durée indicative: 1h)

# French version

## **Le problème à résoudre:**

A Groover, nous créeons de plus en plus souvent des concerts/scènes ouvertes en première partie de concerts partenaires pour faire découvrir des talents issus de notre plateforme!

Néanmoins ces premières parties ont souvent une contrainte de durée de temps limitée *concert_premiere_length* en minutes et nous devons nous assurer de proposer une succession de morceaux dont la somme des durées individuelles en minutes Σtrack_length = *concert_premiere_length, exactement!*

Etant donné une liste de durées (en minutes) de morceaux de music [track_length] proposer une fonction qui renvoie un *Boolean True/False* indiquant s'il y a 3 morceaux dont la durée sommée fait exactement la durée de *concert_premiere_length.*

On considère que *concert_premiere_length* et les durées *track_length* sont des entiers positifs. 

## **Contraintes :**

- Les spectateurs attendent exactement 3 morceaux en première partie du concert
- On ne peut pas proposer le même morceau en double ou triple, chaque morceau doit être proposé une seule fois
- Optimiser le runtime plus que la mémoire dans la solution

## **Spécifications techniques :**

- Stack technique imposée :
    - Python 3
    - Les librairies third-party,l'utilisation des multi threads ou processes ne sont pas autorisés
    - itertools est interdit dans cet exo, on veut que vous proposiez une solution avec les datastructures simples

**Le rendu sera rendu accessible dans un repository [GitHub](https://github.com). Avoir un historique de commit pertinent est toujours bienvenu.**

## Questions bonus (pas obligatoire!, on peut en tester 1 seulement ou les 2 ou aucune!):

- Généralisation: et si on ne fixait pas la limite de 3 morceaux, et on voulait pouvoir proposer le premier match pour concert_*premiere_length* que ce soit 1,2,3,4.. ou plus de morceaux
- Si en gardant la solution d'exactement proposer 3 morceaux, on s'autorisait à avoir la somme de leurs durées proche de *concert_premiere_length* avec une tolérance de 5 min -/+?

# English version

## Problem to solve:

In Groover, we are creating more and more concerts / open stages as the first part of partner concerts to introduce talents from our platform!

However these first parts often have a limited time constraint *concert_premiere_length* in minutes and we must make sure to offer a succession of songs whose sum of the individual durations in minutes *Σtrack_length* = *concert_premiere_length*, *exactly*! 

Given a list of lengths (in minutes) of pieces of music [*track_length*] propose a function that returns a *Boolean True / False* indicating if there are 3 tracks whose sum duration is exactly the duration of *concert_premiere_length*.

We consider that  *concert_premiere_length*  and the durations  *track_length* are positive integers.

## Constraints:

- The spectators expect exactly 3 pieces in this concert first part *concert_premiere*
- We cannot offer the same song in double or triple, each song must be offered only once
- Optimize the runtime over the memory in the solution

# Technical specifications :

- Imposed technical stack:
    - Python 3
    - Third-party libraries, usage of threads/processes are not allowed
    - itertools is forbidden in this exercice, we want you to try building an approach using simple datastructures

**The final work needs to be accessible in a GitHub repository. Having a nice commit history is always a plus.**

## Bonus questions (not required!, you can pick one or try both, or none):

- generalizing: what if we remove the limit of 3 tracks, and want to find the first match for  *concert_premiere_length*? *it can be 1,2,3,4..* or more tracks in [track_lengths].
- what if we stuck to exactly 3 tracks but allowed the sum to be close enough to *concert_premiere_length* with a 5 min -/+ tolerance?
