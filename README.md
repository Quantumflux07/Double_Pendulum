# 🔬 Double Pendulum Simulation (RK4 Method)

A physics-based simulation of a chaotic double pendulum system implemented using numerical integration (Runge-Kutta 4th Order method).

This project demonstrates nonlinear dynamics, chaos theory, and scientific computing using Python.

---

## 📌 Project Overview

The double pendulum is a classic example of a deterministic chaotic system.  
Even very small changes in initial conditions result in drastically different motion over time.

This simulation:

- Solves coupled nonlinear differential equations
- Uses the RK4 numerical integration method
- Animates the pendulum motion in real time
- Traces the trajectory of the second mass

---

## ⚙️ Technologies Used

- Python
- NumPy (vectorized numerical computation)
- Matplotlib (animation & visualization)
- Matplotlib FuncAnimation

---

## 🧠 Mathematical Model

The system is governed by coupled second-order nonlinear differential equations derived from Lagrangian mechanics.

State vector used:

[ θ₁, ω₁, θ₂, ω₂ ]

Where:
- θ = angle
- ω = angular velocity

The equations account for:
- Gravitational acceleration
- Coupling between pendulums
- Nonlinear trigonometric interactions

---

## 🔢 Numerical Method

This project uses the **Runge-Kutta 4th Order (RK4)** integration method.

Why RK4?

- Higher accuracy than Euler method
- Better stability for chaotic systems
- Suitable for nonlinear differential equations

Time step:
dt = 0.02 (chosen for smooth and stable simulation)

---

## 🎥 Features

- Real-time animated motion
- Smooth RK4-based physics update
- Trajectory tracing of second mass
- Adjustable initial conditions
- Demonstrates chaos with slight angle variation

Initial conditions example:
θ₁ = π/2  
θ₂ = π/2 + 0.01  

Even a 0.01 difference creates divergent motion over time.

---

## ▶️ How to Run

1. Clone the repository:

   git clone https://github.com/yourusername/double-pendulum.git

2. Install dependencies:

   pip install numpy matplotlib

3. Run the script:

   python main.py

---

## 📊 What This Project Demonstrates

- Numerical integration of ODE systems
- Implementation of RK4 from scratch
- Simulation of chaotic systems
- Scientific visualization techniques
- Physics-based modeling in Python

---

## 🚀 Possible Improvements

- Energy conservation analysis
- Phase-space visualization
- Adjustable UI sliders
- Comparison between Euler and RK4
- 3D extension
- Export animation as GIF

---

## 📚 Learning Outcome

Through this project, I strengthened my understanding of:

- Nonlinear dynamics
- Chaotic systems
- Numerical methods (RK4)
- Scientific programming in Python

---

⭐ If you found this interesting, feel free to fork and experiment with different initial conditions.
