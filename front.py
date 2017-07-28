#! /usr/bin/env python
# -*- coding: utf-8 -*-
# vim:fenc=utf-8
#
# Copyright © 2017 perrollaz <perrollaz@vincent-MacBookPro>
#
# Distributed under terms of the MIT license.

"""
Classe pour les fronts
"""



import numpy as np
import matplotlib.pyplot as plt


class Front(object):
    """
        Classe implémentant un choc ou un front de raréfaction

        Args:
            ul (float): état gauche
            ur (float): état droite
            tD (float): instant de création
            xD (float): position de création
            i  (int)  : indice dans la liste d'une solution
            ax (axis) : axe pour l'affichage du front
    """
    def __init__(self, ul, ur, tD, xD, i, ax):
        # états gauche/droite
        self.eG = ul
        self.eD = ur
        # points initiaux/finaux
        self.tD = tD
        self.xD = xD
        self.tF = np.nan
        self.xF = np.nan
        # type de front
        if ul > ur:
            self.typ = "Choc"
        else:
            self.typ = "Raréfaction"
        # indice global
        self.ind = i
        # vitesse propagation
        self.v = (ul+ur)/2.0
        # représentation graphique
        if self.typ == "Choc":
            self.ligne, = ax.plot([], [], lw=2.0, color='red')
        else:
            self.ligne, = ax.plot([], [], lw=2.0, color='blue')

    def pos(self, t):
        """
            Renvoie la position du front à l'instant t

            Args:
                t (float): temps où l'on cherche la position
        """
        return self.xD+self.v*(t-self.tD)

    def affichage(self, fin, test=True):
        """
            Dessine le front dans le repère ax, test permet d'effacer le front
            s'il n'est pas demandé

            Args:
                fin (float): temps maximal jusqu'où l'on affiche
                test (bool): affichage désiré ou pas
        """
        if (not test):
            self.ligne.set_data([], [])
            return None

        if fin < self.tD:
            return None
        elif (not np.isnan(self.tF)) and self.tF < fin:
            self.ligne.set_data([self.xD, self.xF], [self.tD, self.tF])
            return [min(self.xD, self.xF), max(self.xD, self.xF),
                    min(self.tD, self.tF), max(self.tD, self.tF)]
        else:
            self.ligne.set_data([self.xD, self.pos(fin)], [self.tD, fin])
            return [min(self.xD, self.pos(fin)), max(self.xD, self.pos(fin)),
                    min(self.tD, fin), max(self.tD, fin)]

    def information(self):
        """
            Affichage des paramètres du front
        """
        print "\nFront d'indice", self.ind
        print "type :", self.typ
        print "etats gauche/droite", self.eG, self.eD
        print "point de  départ (t,x)", self.tD, self.xD
        print "point final (t,x)", self.tF, self.xF
        print "vitesse", self.v

    def H(self, z):
        """
            Fonction de Heavyside pour un tableau numpy

            Args:
                z (float array): argument de la fonction
        """
        return np.where(z > 0.0, 1.0, 0.0)

    def numVal(self, tt, xx):
        """
            Evaluation de la fonction valant 0 à gauche, avant et après le front
            et la valeur du saut à droite pendant son existence

            Args:
                tt (float array): tableau des temps
                xx (float array): tableau des positions
        """
        if np.isnan(self.tF):
            return (self.eD-self.eG)*self.H(tt-self.tD)*self.H(
                xx-self.xD-self.v*(tt-self.tD))
        else:
            return (self.eD-self.eG)*self.H(tt-self.tD)*self.H(
                xx-self.xD-self.v*(tt-self.tD))*self.H(self.tF-tt)

