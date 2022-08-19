from gym.envs import registry


def sample_from(distribution, np_random):
    return np_random.multinomial(1, distribution).argmax()


env_ids = [env for env, spec in registry.items() if spec.entry_point.startswith("pogym")]
