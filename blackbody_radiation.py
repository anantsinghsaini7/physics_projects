import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


h = 6.626e-34
c = 3e8
k = 1.38e-23

# Planck function
def planck(wavelength, T):
    return (2*h*c**2)/(wavelength**5) * 1/(np.exp(h*c/(wavelength*k*T)) - 1)

# Wavelength range
wavelength = np.linspace(1e-9, 3e-6, 500)


fig, ax = plt.subplots()
line, = ax.plot([], [])
ax.set_xlim(0, 3000)  # nm
ax.set_ylim(0, 3e13)
ax.set_xlabel("Wavelength (nm)")
ax.set_ylabel("Intensity")


temp_text = ax.text(0.7, 0.9, "", transform=ax.transAxes)


def init():
    line.set_data([], [])
    return line,

# Update function
def update(frame):
    T = 3000 + frame * 50
    
    intensity = planck(wavelength, T)
    
    line.set_data(wavelength*1e9, intensity)
    
    temp_text.set_text(f"T = {T} K")

    
    
    return line, temp_text



ani = FuncAnimation(fig, update, frames=50, init_func=init, blit=True)


plt.show()
peak_dot, = ax.plot([], [], 'ro')

def update(frame):
    T = 3000 + frame * 50
    intensity = planck(wavelength, T)
    
    line.set_data(wavelength*1e9, intensity)
    
    
    idx = np.argmax(intensity)
    peak_dot.set_data(wavelength[idx]*1e9, intensity[idx])
    
    title.set_text(f"T = {T} K")
    
    return line, peak_dot, title
ani.save("blackbody.gif", writer="pillow", fps=10)