from stable_baselines3 import PPO
from env import SimpleReachEnv

env = SimpleReachEnv()

model = PPO("MlpPolicy", env, verbose=1)
model.learn(total_timesteps=100000)

model.save("ppo_custom")