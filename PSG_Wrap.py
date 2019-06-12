# A wrapper to run PSG from Python
import subprocess
import numpy as np
import pickle
import os
import matplotlib.pyplot as plt
import pandas as pd
from pandas.compat import StringIO, BytesIO

class PSG_Calculator:

    def __init__(self, config_file_path="config.txt", plot=True):

        if os.path.exists(config_file_path) and os.path.getsize(config_file_path) > 0:
            self.config = pd.read_csv(config_file_path, sep='\t')

        else: FileNotFoundError('Configuration file not found')

        self.config_file = config_file_path
        self.plot = plot
        print(type(input))

    def run_PSG(self, save=True):

        commands = '''
        curl -d type=rad -d whdr=n --data-urlencode file@'''+self.config_file+''' https://psg.gsfc.nasa.gov/api.php
        '''

        print("Running Planetary Spectrum Generator...")
        process = subprocess.Popen('bash', stdin=subprocess.PIPE, stdout=subprocess.PIPE)
        out, err = process.communicate(commands.encode('utf-8'))
        #print(out.decode('utf-8'))
        print("Done, saving output spectrum.")
        with open('output.txt','w') as output_file:
            for line in out.decode('utf-8'):
                output_file.write(line)
        print(type(out))
        spectrum = np.loadtxt('output.txt')

        return spectrum[:,0], spectrum[:,1]
