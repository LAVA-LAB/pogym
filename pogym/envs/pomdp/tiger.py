import numpy as np
import copy
from gym import error, spaces, utils
from gym.utils import seeding
from gym.envs.registration import register
from gym.error import InvalidAction
from typing import Optional
import gym


OBSERV_PROB = np.array([[0.85, 0.15], [0.15, 0.85]])


class TigerEnv(gym.Env):
    def __init__(self):
        self.start_state_prob=np.array([0.5,0.5])
        self.start_state=None
        self.current_state=copy.deepcopy(self.start_state)
        self.name="Tiger"
        self.discount=0.95
        self.action_space=spaces.Discrete(3)
        self.observation_space=spaces.Discrete(2)

    def step(self,action):
        done = False
        if action==0: ##corresponds to listen action
            reward=-1
            transition_probability=np.array([[1,0],[0,1]])
            next_state= self.sample_from(transition_probability[self.current_state, :])
            observation= self.sample_from(OBSERV_PROB[next_state, :])
           
        elif action==1: ##open left
            rewards=[-100,10]
            transition_probability=np.array([[0.5,0.5],[0.5,0.5]])
            observation_probability=np.array([[0.5,0.5],[0.5,0.5]])
            next_state= self.sample_from(transition_probability[self.current_state, :])
            observation= self.sample_from(observation_probability[next_state, :])
            reward=rewards[self.current_state]
            done = True

        elif action==2: ##open right
            rewards=[10,-100]
            transition_probability=np.array([[0.5,0.5],[0.5,0.5]])
            observation_probability=np.array([[0.5,0.5],[0.5,0.5]])
            next_state= self.sample_from(transition_probability[self.current_state, :])
            observation= self.sample_from(observation_probability[next_state, :])
            reward=rewards[self.current_state]
            done = True
        else:
            raise InvalidAction(f"the action {action} is not valid.")

        self.current_state=next_state
        return observation, reward, done, False, {}

    def sample_from(self, probability_dist):
        return self.np_random.multinomial(1, probability_dist).argmax()

    def reset(
        self,
        *,
        seed: Optional[int] = None,
        return_info: bool = False,
        options: Optional[dict] = None
    ):
        super().reset(seed=seed)
        self.start_state= self.sample_from(self.start_state_prob)
        self.current_state=copy.deepcopy(self.start_state)

        observation= self.sample_from(OBSERV_PROB[self.current_state, :])
        if not return_info:
            return observation
        else:
            return observation, {}
