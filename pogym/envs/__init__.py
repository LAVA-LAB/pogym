from gym.envs.registration import register

register(
    id='CheeseMaze-v0',
    entry_point='pogym.envs.pomdp.cheesemaze:CheeseMazeEnv',
    max_episode_steps=300,
)

register(
    id='Tiger-v0',
    entry_point='pogym.envs.pomdp.tiger:TigerEnv',
    max_episode_steps=300,
)

register(
    id='Voicemail-v0',
    entry_point='pogym.envs.pomdp.voicemail:VoicemailEnv',
    max_episode_steps=300,
)
