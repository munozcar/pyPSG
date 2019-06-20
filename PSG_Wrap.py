'''
pyPSG: Python wrapper for NASA's Planetary Spectrum Generator
Written by Carlos E. Munoz-Romero, June 2019
'''
import subprocess
import os
import csv
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import psg_utils as utils
from platon.constants import M_jup, R_jup, R_sun

class PSG_Calculator:

    def __init__(self, config_file_path="config.txt"):

        if os.path.exists(config_file_path) and os.path.getsize(config_file_path) > 0:
            self.config = pd.read_csv(config_file_path, sep='>',header=None, skipinitialspace=True).T

            n_keys = len(self.config.keys())

            for i in range(0,n_keys):
                self.config[i][0]+='>'

            self.config.columns = [self.config[i][0] for i in range(0,n_keys)]
            self.config = self.config.drop(0)

        else: FileNotFoundError('Configuration file not found')

        self.config_file = config_file_path

    def compute_depths(self, T_eq=500, Mp=M_jup, Rp=R_jup, Rs=R_sun, albedo=0, T_star=5777,
    resolution=200):

        self.Dp = 2*Rp/1000 # PSG takes diameter as input, in km
        self.albedo = albedo
        self.T_eq = T_eq
        self.T_star = T_star
        self.Rs = Rs
        self.resolution = resolution

        # Find distance to parent star, in AU
        self.Orb_rad = utils.temp_to_orb(self.T_eq,self.T_star,self.albedo,self.Rs)

        self.config['<OBJECT-GRAVITY>'][1] = str(Mp)
        self.config['<OBJECT-DIAMETER>'][1] = str(self.Dp)
        self.config['<OBJECT-STAR-RADIUS>'][1] = str(self.Rs/R_sun)
        self.config['<OBJECT-STAR-DISTANCE>'][1] = str(self.Orb_rad)
        self.config['<SURFACE-ALBEDO>'][1] = str(self.albedo)
        self.config['<GENERATOR-RESOLUTION>'][1] = str(self.resolution)
        self.config['<OBJECT-STAR-TEMPERATURE>'][1] = str(self.T_star)

        with open(self.config_file,'w') as mod_config:
            for key in self.config.columns:
                mod_config.write(key+str(self.config[key][1])+'\n')

        commands = '''
        curl -d type=rad -d whdr=n --data-urlencode file@'''+self.config_file+''' https://psg.gsfc.nasa.gov/api.php
        '''
        process = subprocess.Popen('bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        out, err = process.communicate(commands.encode('utf-8'))

        with open('output.txt','w') as output_file:
            for line in out.decode('utf-8'):
                output_file.write(line)
        spectrum = np.loadtxt('output.txt')

        print('Done')
        return spectrum[:,0], spectrum[:,-2]
