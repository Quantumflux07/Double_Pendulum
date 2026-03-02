import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# Physical constants
g = 9.8
m1 = 1.0
m2 = 1.0
l1 = 1.0
l2 = 0.8
dt = 0.02   # SMALL = slow + smooth

# Initial conditions
theta1 = np.pi / 2
theta2 = np.pi / 2+ 0.01
omega1 = omega2 = 0.0

state = np.array([theta1, omega1, theta2, omega2])

def derivatives(s):
    t1, w1, t2, w2 = s
    d = t1 - t2

    den = 2*m1 + m2 - m2*np.cos(2*d)

    a1 = (-g*(2*m1+m2)*np.sin(t1)
          - m2*g*np.sin(t1-2*t2)
          - 2*np.sin(d)*m2*(w2**2*l2 + w1**2*l1*np.cos(d))
         ) / (l1 * den)

    a2 = (2*np.sin(d)*(w1**2*l1*(m1+m2)
          + g*(m1+m2)*np.cos(t1)
          + w2**2*l2*m2*np.cos(d))
         ) / (l2 * den)

    return np.array([w1, a1, w2, a2])

# RK4 integrator
def rk4(s):
    k1 = derivatives(s)
    k2 = derivatives(s + dt*k1/2)
    k3 = derivatives(s + dt*k2/2)
    k4 = derivatives(s + dt*k3)
    return s + dt*(k1 + 2*k2 + 2*k3 + k4)/6

# Plot setup
fig, ax = plt.subplots()
ax.set_xlim(-2.2, 2.2)
ax.set_ylim(-2.2, 2.2)
ax.set_aspect('equal')
ax.axis('off')

rod, = ax.plot([], [], 'o-', lw=2)
trace, = ax.plot([], [], '-', lw=1, alpha=0.7)

x_path, y_path = [], []

def update(frame):
    global state
    state = rk4(state)

    t1, _, t2, _ = state

    x1 = l1*np.sin(t1)
    y1 = -l1*np.cos(t1)

    x2 = x1 + l2*np.sin(t2)
    y2 = y1 - l2*np.cos(t2)

    x_path.append(x2)
    y_path.append(y2)

    rod.set_data([0, x1, x2], [0, y1, y2])
    trace.set_data(x_path, y_path)

    return rod, trace

ani = FuncAnimation(fig, update, interval=20)
plt.show()
