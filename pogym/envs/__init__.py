from gym.envs.registration import register

register(
    id='Tiger-v0',
    entry_point='pogym.envs.pomdp.tiger:TigerEnv',
    max_episode_steps=300,
)
