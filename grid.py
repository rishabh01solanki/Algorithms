import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Define figure and axis
fig, ax = plt.subplots()

# Initialize grid and particles
grid_size = 100
grid = np.zeros((grid_size, grid_size))
center = (grid_size // 2, grid_size // 2)
grid[center[0]][center[1]] = 1

# Define gravitational constant and particle masses
G = 1 #6.674 * 10 ** -11

    
# Define number of particles
num_particles = 3

# Define particle masses randomly
particle_masses = np.random.rand(num_particles) * 100

# Initialize positions and velocities of particles randomly
positions = [(np.random.rand()*grid_size, np.random.rand()*grid_size) for _ in range(num_particles)]
velocities = [(np.random.rand(), np.random.rand()) for _ in range(num_particles)]


# Define time step
dt = 0.1

# Define function to calculate gravitational force
def calculate_force(pos1, pos2, mass1, mass2):
    dx = pos2[0] - pos1[0]
    dy = pos2[1] - pos1[1]
    r = np.sqrt(dx ** 2 + dy ** 2)
    f = G * mass1 * mass2 / r ** 2
    fx = f * dx / r
    fy = f * dy / r
    return fx, fy

# Define function to update positions and velocities
# Define function to update positions and velocities
def update_positions(positions, velocities, masses, dt):
    merged = []  # list of indices of merged particles
    for i in range(len(positions)):
        if i in merged:  # skip particles that have already been merged
            continue
        fx, fy = 0, 0
        for j in range(i+1, len(positions)):
            if j in merged:  # skip particles that have already been merged
                continue
            force = calculate_force(positions[i], positions[j], masses[i], masses[j])
            fx += force[0]
            fy += force[1]
            dx = positions[j][0] - positions[i][0]
            dy = positions[j][1] - positions[i][1]
            r = np.sqrt(dx ** 2 + dy ** 2)
            if r < (masses[i] ** (1/3) + masses[j] ** (1/3)) / 2:  # check for collision
                # merge particles i and j
                positions[i] = ((masses[i]*positions[i][0] + masses[j]*positions[j][0]) / (masses[i] + masses[j]), 
                                (masses[i]*positions[i][1] + masses[j]*positions[j][1]) / (masses[i] + masses[j]))
                velocities[i] = ((masses[i]*velocities[i][0] + masses[j]*velocities[j][0]) / (masses[i] + masses[j]), 
                                 (masses[i]*velocities[i][1] + masses[j]*velocities[j][1]) / (masses[i] + masses[j]))
                masses[i] = masses[i] + masses[j]
                merged.append(j)
        vel = velocities[i]
        vel = (vel[0] + fx / masses[i] * dt, vel[1] + fy / masses[i] * dt)
        positions[i] = (positions[i][0] + vel[0] * dt, positions[i][1] + vel[1] * dt)
        velocities[i] = vel
    # remove merged particles
    positions = [positions[i] for i in range(len(positions)) if i not in merged]
    velocities = [velocities[i] for i in range(len(velocities)) if i not in merged]
    masses = [masses[i] for i in range(len(masses)) if i not in merged]
    return positions, velocities, masses


# Define function to update animation
def update(frame):
    global positions, velocities
    positions, velocities = update_positions(positions, velocities, particle_masses, dt)
    ax.clear()
    ax.imshow(grid, cmap='gray')
    for i in range(len(positions)):
        ax.plot(positions[i][0], positions[i][1], 'o', color='C{}'.format(i))



# Create animation
ani = animation.FuncAnimation(fig, update, frames=1000, interval=10)
plt.show()
