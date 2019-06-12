# PSG_python (in dev)
Wrapper code to run NASA's [Planetary Spectrum Generator](https://psg.gsfc.nasa.gov/) from Python.

Usage example:

from PSG_Wrap import PSG_Calculator
import matplotlib.pyplot as plt

calculator = PSG_Calculator()
wavelength, spectrum = calculator.run_PSG() 

plt.plot(wavelength,spectrum)         
plt.show()
