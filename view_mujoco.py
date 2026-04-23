import gymnasium as gym
from stable_baselines3 import PPO

env = gym.make("HalfCheetah-v5", render_mode="human")
model = PPO.load("ppo_halfcheetah")

obs, info = env.reset()

for _ in range(2000):
    action, _ = model.predict(obs, deterministic=True)

    # Step FIRST
    obs, reward, terminated, truncated, info = env.step(action)

    # THEN print reward
    print("reward:", reward)

    if terminated or truncated:
        obs, info = env.reset()

env.close()