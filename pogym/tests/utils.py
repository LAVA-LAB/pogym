def get_trajectory(env):
    observations = [env.reset(seed=0)]
    truncated = False
    while not truncated:
        o, _, _, truncated, _ = env.step(2)
        observations.append(o)
    return observations
