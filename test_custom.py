from stable_baselines3 import PPO
from env import SimpleReachEnv

env = SimpleReachEnv()
model = PPO.load("ppo_custom")

obs, info = env.reset()

for _ in range(200):
    action, _ = model.predict(obs, deterministic=True)
    obs, reward, terminated, truncated, info = env.step(action)
    env.render()

    if terminated or truncated:
        print("reset")
        obs, info = env.reset()