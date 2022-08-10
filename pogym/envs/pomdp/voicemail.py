from abc import ABC
from typing import Optional

import gym
import numpy as np
from gym import spaces
from gym.error import InvalidAction
from gym.utils import seeding

from pogym.utils import sample_from

OBS_PROB = np.array([[0.8, 0.2], [0.3, 0.7]])


class VoicemailEnv(gym.Env, ABC):
    def __init__(self, isd=(0.65, 0.35)):
        self.start_state_probs = np.array(isd)  # assuming user wants the message to be saved
        self.start_state = None
        self.current_state = None
        self.name = "Voicemail"
        self.discount = 0.95
        self.action_space = spaces.Discrete(3)
        self.observation_space = spaces.Discrete(2)
        self.seed()

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        if action == 0:  # refers to asking the user
            reward = -1
            observation = sample_from(OBS_PROB[self.current_state, :], self.np_random)
            done = False

        elif action == 1:  # refers to Saving the data
            rewards = [5, -10]
            observation = self.current_state
            reward = rewards[self.current_state]
            done = True

        elif action == 2:  # refers to deleting the data
            rewards = [-20, 5]
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
        self.start_state = sample_from(self.start_state_probs, self.np_random)
        self.current_state = self.start_state
        observation = sample_from(OBS_PROB[self.current_state, :], self.np_random)
        if not return_info:
            return observation
        else:
            return observation, {}
