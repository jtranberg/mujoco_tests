# pip install gymnasium[mujoco] stable-baselines3

import gymnasium as gym
from stable_baselines3 import PPO

# 1) Create a MuJoCo-based environment
env = gym.make("HalfCheetah-v5")

# 2) Create the RL model
model = PPO(
    policy="MlpPolicy",
    env=env,
    verbose=1,
)

# 3) Train
model.learn(total_timesteps=300000)
model.save("ppo_halfcheetah")

# 4) Test the trained agent
obs, info = env.reset()
for _ in range(1000):
    action, _state = model.predict(obs, deterministic=True)
    obs, reward, terminated, truncated, info = env.step(action)

    # If the episode ends, reset
    if terminated or truncated:
        obs, info = env.reset()

env.close()