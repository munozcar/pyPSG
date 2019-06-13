from PSG_Wrap import PSG_Calculator 
import matplotlib.pyplot as plt  
from platon.constants import M_jup, R_jup, R_sun 

# Set system variables
T_eq = 600   
Mp = 0.1*M_jup 
Rp = 0.08*R_jup  
Rs = 0.30*R_sun   
albedo = 0 
T_star = 4000  

# Generate radiance spectrum
calculator = PSG_Calculator() 
wavelengths, depths = calculator.run_PSG(T_eq=T_eq, Mp=Mp, Rp=Rp, Rs=Rs, albedo=albedo, T_star=T_star) 

plt.plot(waves, depths)
plt.show()
