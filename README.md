# PSG_python (in dev)
Wrapper code to run NASA's [Planetary Spectrum Generator](https://psg.gsfc.nasa.gov/) from Python.

Usage example:

from PSG_Wrap import PSG_Calculator \n
import matplotlib.pyplot as plt \n

calculator = PSG_Calculator() \n
wavelength, spectrum = calculator.run_PSG() \n 

plt.plot(wavelength,spectrum)     \n    
plt.show()
