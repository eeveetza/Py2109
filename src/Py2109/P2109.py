# -*- coding: utf-8 -*-
# pylint: disable=invalid-name,line-too-long,too-many-lines,too-many-arguments,too-many-locals,too-many-statements
"""
Created on 29 Aug 2026

@author: Ivica Stevanovic

Building entry loss according to ITU-R P.2109-2.

Python translation of bel_p2109.m
"""

import warnings

import numpy as np
from scipy.special import erfinv


def bel_p2109(f, p, cl, th):
    """
    Building entry loss not exceeded for the probability p, as defined in
    ITU-R P.2109.

    L = bel_p2109(f, p, cl, th)

    Input parameters:
        f   - Frequency (GHz): 0.08 <= f <= 100
        p   - probability for which the loss is not exceeded (%): 0 < p < 100
        cl  - building class (1 - 'traditional', 2 - 'thermally efficient')
        th  - elevation angle at the building facade
              (degrees above the horizontal)

    Output parameters:
        L   - Building entry loss not exceeded for the probability p

    Example:
        L = bel_p2109(f, p, cl, th)

    Rev   Date        Author                          Description
    -----------------------------------------------------------------------
    v0    01MAY17     Ivica Stevanovic, OFCOM         Initial MATLAB version
    v0    29AUG26     Ivica Stevanovic, OFCOM         Python translation
    """

    # Read the input arguments and check them

    if f < 0.08 or f > 100:
        warnings.warn('Frequency is outside the valid domain [0.08, 100] GHz')

    if th < -90 or th > 90:
        warnings.warn('Elevation angle is outside the valid domain [-90, 90] degrees')

    if p <= 0 or p >= 100:
        warnings.warn('Percentage of locations is outside the valid domain (0, 100) %')

    if cl == 1:
        # traditional building
        r = 12.64
        s = 3.72
        t = 0.96
        u = 9.6
        v = 2.0
        w = 9.1
        x = -3.0
        y = 4.5
        z = -2.0

    elif cl == 2:
        # thermally efficient building
        r = 28.19
        s = -3.00
        t = 8.48
        u = 13.5
        v = 3.8
        w = 27.8
        x = -2.9
        y = 9.4
        z = -2.1

    else:
        raise ValueError('Wrong building class type.')

    Le = 0.212 * abs(th)                              # (10)
    Lh = r + s * np.log10(f) + t * (np.log10(f)) ** 2  # (9)

    sigma2 = y + z * np.log10(f)  # (8)
    sigma1 = u + v * np.log10(f)  # (7)

    mu2 = w + x * np.log10(f)  # (6)
    mu1 = Lh + Le              # (5)
    C = -3                     # (4)

    # Finv = norm.ppf(p / 100)  # equivalent when scipy.stats is available
    Finv = np.sqrt(2) * erfinv(2 * p / 100 - 1)  # Using definition in P.1057
    B = mu2 + sigma2 * Finv

    A = mu1 + sigma1 * Finv
    L = 10 * np.log10(10 ** (0.1 * A) + 10 ** (0.1 * B) + 10 ** (0.1 * C))

    return L
