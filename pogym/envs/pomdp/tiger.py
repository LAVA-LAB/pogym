from typing import Optional

import numpy as np
from gym import Env
from gym import spaces
from gym.error import InvalidAction

from pogym.utils import sample_from


OBSERV_PROB = np.array([[0.85, 0.15], [0.15, 0.85]])


class TigerEnv(Env):
    def __init__(self, isd=[0.5, 0.5]):
        self.start_state_prob = np.array(isd)
        self.current_state = None
        self.name = "Tiger"
        self.discount = 0.95
        self.action_space = spaces.Discrete(3)
        self.observation_space = spaces.Discrete(2)

    def step(self, action):
        done = False
        if action == 2:  ##corresponds to listen action
            reward = -1
            observation = sample_from(OBSERV_PROB[self.current_state, :], self.np_random)

        elif action == 0:  ##open left
            rewards = [-100, 10]
            observation = self.current_state
            reward = rewards[self.current_state]
            done = True

        elif action == 1:  ##open right
            rewards = [10, -100]
            observation = self.current_state
            reward = rewards[self.current_state]
            done = True
        else:
            raise InvalidAction(f"the action {action} is not valid.")

        return observation, reward, done, False, {}


    def reset(
            self,
            *,
            seed: Optional[int] = None,
            return_info: bool = False,
            options: Optional[dict] = None
    ):
        super().reset(seed=seed)
        self.current_state = sample_from(self.start_state_prob, self.np_random)

        observation = sample_from(OBSERV_PROB[self.current_state, :], self.np_random)
        if not return_info:
            return observation
        else:
            return observation, {}
