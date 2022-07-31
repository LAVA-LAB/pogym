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

    def test_seeding(self):
        env = pogym.make("Tiger-v0")

        def get_trajectory():
            observations = [env.reset(seed=0)]
            done = False
            while not done:
                o, _, done, _ = env.step(0)
                observations.append(o)
            return observations

        self.assertListEqual(get_trajectory(), get_trajectory())

    def test_listen_is_not_done(self):
        env = pogym.make("Tiger-v0")
        env.reset()
        _, _, done, _ = env.step(0)
        self.assertFalse(done)

    def test_open_left_door_is_done(self):
        env = pogym.make("Tiger-v0")
        env.reset()
        _, _, done, _ = env.step(1)
        self.assertTrue(done)

    def test_open_right_door_is_done(self):
        env = pogym.make("Tiger-v0")
        env.reset()
        _, _, done, _ = env.step(2)
        self.assertTrue(done)