🧠 Reinforcement Learning Playground (MuJoCo + Custom Env)

A hands-on exploration of reinforcement learning using Gymnasium, Stable-Baselines3 (PPO), and MuJoCo.

This project demonstrates both:

Training an agent in a real physics simulation (HalfCheetah)
Building and training a custom reinforcement learning environment from scratch
🚀 Features
✅ PPO training with Stable-Baselines3
✅ MuJoCo physics simulation (HalfCheetah)
✅ Custom 1D control environment (SimpleReachEnv)
✅ Reward shaping and behavior refinement
✅ Step-by-step policy evaluation and debugging
📁 Project Structure
.
├── env.py               # Custom RL environment
├── train_custom.py      # Train PPO on custom environment
├── test_custom.py       # Evaluate custom trained agent
├── train_mujoco.py      # Train PPO on MuJoCo (HalfCheetah)
├── view_mujoco.py       # Visualize trained MuJoCo agent
├── mujoco_test.py       # Low-level MuJoCo physics test
├── robot.xml            # Simple MuJoCo model
└── README.md
⚙️ Installation
pip install gymnasium[mujoco] stable-baselines3 torch numpy
🤖 Training
Train custom environment
python train_custom.py
Train MuJoCo environment
python train_mujoco.py
🧪 Testing / Evaluation
Custom environment
python test_custom.py

Example output:

x=2.80, v=1.20, target=3.34
x=3.00, v=0.80, target=3.34
reset
MuJoCo visualization
python view_mujoco.py
🧠 Custom Environment Overview

The SimpleReachEnv is a 1D control problem where an agent must:

Move toward a randomly placed target
Slow down near the target
Avoid overshooting
Observation Space
[ position, velocity, target_position ]
Action Space
continuous force ∈ [-1, 1]
🎯 Reward Design

The agent is trained using reward shaping:

✅ Reward progress toward the target
⚠️ Penalize high velocity near the goal
❌ Penalize overshooting
⭐ Bonus for reaching the target

This encourages:

controlled acceleration
smooth deceleration
precise stopping behavior
📈 Results
MuJoCo (HalfCheetah)
Reward improved from negative values to ~680+
Agent learned forward locomotion behavior
Custom Environment
Learned to:
move toward target
control velocity
reduce overshoot
🔬 Key Learnings
Reward shaping directly defines agent behavior
Velocity constraints are critical for stability
Agents optimize reward, not “intended behavior”
Debugging RL requires observing both:
training metrics
runtime behavior
🧩 Tech Stack
Python
Gymnasium
Stable-Baselines3 (PPO)
MuJoCo
💡 Future Improvements
2D navigation environment
Multi-target tasks
MuJoCo-based custom robot environment
Policy visualization (graphs / plots)
Hyperparameter tuning
📌 Summary

This project demonstrates a complete reinforcement learning workflow:

Environment → Training → Evaluation → Behavior Debugging → Reward Refinement

👤 Author

Jay Tranberg