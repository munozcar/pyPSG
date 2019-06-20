'''
psg_utils
Written by Carlos E. Munoz-Romero, June 2019
'''

import numpy as np

def temp_to_orb(T_eq,T_star,albedo,Rs):
    '''
    temp_to_orb: Calculates distance from target exoplanet to host star, in AU.

    PARAMETERS:
                T_eq: Equilibrium temperature (K)
                T_star: Stellar temperature (K)
                albedo: planetary albedo
                Rs: Stellar radius (m)

    PRODUCES:
                Orb_rad: orbital radius (AU)
    '''

    M_TO_AU = 6.68459e-12
    return (( (T_eq / (T_star*(1-albedo)**(0.25)) )**2 )*2/Rs )**(-1) * M_TO_AU
