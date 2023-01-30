from gym import Env


def get_trajectory(env: Env):
    o, info = env.reset(seed=123)
    env.action_space.seed(123)
    observations = [o]
    terminated, truncated = False, False

    while not (truncated or terminated):
        a = env.action_space.sample()
        o, _, terminated, truncated, _ = env.step(a)
        observations.append(o)
    return observations


