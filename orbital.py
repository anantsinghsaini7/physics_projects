import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

G = 4 * np.pi**2  


masses = np.array([1.0, 3e-6, 9.5e-4])  # Sun, Earth, Jupiter

# Initial positions
positions = np.array([
    [0.0, 0.0],   # Sun
    [1.0, 0.0],   # Earth
    [5.2, 0.0]    # Jupiter
], dtype=float)

# Initial velocities
velocities = np.array([
    [0.0, 0.0],
    [0.0, 2*np.pi],
    [0.0, 2*np.pi/np.sqrt(5.2)]
], dtype=float)

dt = 0.001
steps = 5000

# Store trajectories
traj = np.zeros((steps, len(masses), 2))

def compute_acceleration(pos):
    acc = np.zeros_like(pos)
    for i in range(len(pos)):
        for j in range(len(pos)):
            if i != j:
                r = pos[j] - pos[i]
                dist = np.linalg.norm(r)
                acc[i] += G * masses[j] * r / dist**3
    return acc

# Simulation loop
for t in range(steps):
    acc = compute_acceleration(positions)
    velocities += acc * dt
    positions += velocities * dt
    traj[t] = positions



fig, ax = plt.subplots()
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_aspect('equal')

lines = [ax.plot([], [], lw=1)[0] for _ in range(len(masses))]
points = [ax.plot([], [], 'o')[0] for _ in range(len(masses))]

labels = ["Sun", "Earth", "Jupiter"]

def init():
    for line, point in zip(lines, points):
        line.set_data([], [])
        point.set_data([], [])
    return lines + points

def update(frame):
    
    for i in range(len(masses)):
        lines[i].set_data(traj[:frame, i, 0], traj[:frame, i, 1])
        points[i].set_data(
            [traj[frame, i, 0]],
            [traj[frame, i, 1]]
        )
        
        
    return lines + points

ani = FuncAnimation(fig, update, frames=steps, init_func=init, blit=True, interval=20)

plt.title("3-Body Orbital Simulation")
ani.save("orbital_simulation.gif", writer="pillow", fps=30)
plt.show()
