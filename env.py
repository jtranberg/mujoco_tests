import numpy as np
import gymnasium as gym
from gymnasium import spaces

class SimpleReachEnv(gym.Env):
    def __init__(self):
        super().__init__()

        self.observation_space = spaces.Box(
            low=-10.0,
            high=10.0,
            shape=(3,),
            dtype=np.float32
        )

        self.action_space = spaces.Box(
            low=-1.0,
            high=1.0,
            shape=(1,),
            dtype=np.float32
        )

        self.robot_x = 0.0
        self.robot_v = 0.0
        self.target_x = 5.0
        self.steps = 0
        self.max_steps = 200

    def reset(self, seed=None, options=None):
        super().reset(seed=seed)

        self.robot_x = 0.0
        self.robot_v = 0.0
        self.target_x = np.random.uniform(3.0, 7.0)
        self.steps = 0

        obs = np.array([self.robot_x, self.robot_v, self.target_x], dtype=np.float32)
        return obs, {}

    def step(self, action):
        self.steps += 1

        prev_dist = abs(self.target_x - self.robot_x)

        force = float(action[0])

        # apply force
        self.robot_v += force * 0.1

        # keep velocity from growing forever
        self.robot_v = np.clip(self.robot_v, -2.0, 2.0)

        # update position
        self.robot_x += self.robot_v * 0.1

        dist = abs(self.target_x - self.robot_x)

        # reward progress toward the target
        reward = prev_dist - dist

        # penalize going too fast near target
        if dist < 1.0:
            reward -= abs(self.robot_v) * 0.2

        # penalize overshooting target
        if self.robot_x > self.target_x + 0.25:
            reward -= 5.0

        # success bonus
        if dist < 0.1:
            reward += 10.0

        terminated = dist < 0.1
        truncated = self.steps >= self.max_steps

        obs = np.array([self.robot_x, self.robot_v, self.target_x], dtype=np.float32)
        info = {"distance_to_target": dist}

        return obs, reward, terminated, truncated, info

    def render(self):
        print(f"x={self.robot_x:.2f}, v={self.robot_v:.2f}, target={self.target_x:.2f}")