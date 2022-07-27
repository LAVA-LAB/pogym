import unittest
import pogym
from gym import logger
logger.set_level(logger.DISABLED)


class TestTiger(unittest.TestCase):
    def test_make(self):
        tiger_env = pogym.make("Tiger-v0")
        self.assertIsNotNone(tiger_env)

    def test_listen_reward(self):
        tiger_env = pogym.make("Tiger-v0")
        tiger_env.reset()
        _, r, _, _ = tiger_env.step(0)
        self.assertEqual(r, -1)

    def test_open_door_reward(self):
        tiger_env = pogym.make("Tiger-v0")
        tiger_env.reset()
        state = tiger_env.current_state
        _, r, _, _ = tiger_env.step(1)
        if state == 0:
            self.assertEqual(r, -100)
        else:
            self.assertEqual(r, 10)
