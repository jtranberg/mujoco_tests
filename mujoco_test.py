import mujoco
import time

model = mujoco.MjModel.from_xml_path("robot.xml")
data = mujoco.MjData(model)

for i in range(200):
    mujoco.mj_step(model, data)

    print("Step:", i)
    print("Position:", data.qpos)
    print("Velocity:", data.qvel)

    time.sleep(0.05)