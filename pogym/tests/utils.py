from gym.envs.registration import registry


def get_trajectory(env):
    observations = [env.reset(seed=0)]
    truncated = False
    while not truncated:
        o, _, _, truncated, _ = env.step(2)
        observations.append(o)
    return observations


testing_env_ids = [env for env, spec in registry.items() if spec.entry_point.startswith("pogym")]
