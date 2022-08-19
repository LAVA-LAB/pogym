import unittest
import pogym
from pogym.tests.utils import get_trajectory
from pogym.utils import env_ids


class TestTiger(unittest.TestCase):
    def test_make(self):
        tiger_env = pogym.make("Tiger-v0", new_step_api=True)
        self.assertIsNotNone(tiger_env)

    def test_listen_reward(self):
        tiger_env = pogym.make("Tiger-v0", new_step_api=True)
        tiger_env.reset()
        _, r, _, _, _ = tiger_env.step(2)
        self.assertEqual(r, -1)

    def test_open_door_reward(self):
        tiger_env = pogym.make("Tiger-v0", new_step_api=True)
        tiger_env.reset()
        state = tiger_env.current_state
        o, r, _, _, _ = tiger_env.step(0)
        self.assertEqual(o, state)
        if state == 0:
            self.assertEqual(r, -100)
        else:
            self.assertEqual(r, 10)

    def check_determinism(self, env_id):
        env = pogym.make(env_id, new_step_api=True)
        self.assertListEqual(get_trajectory(env), get_trajectory(env), env_id)

    def test_determinism(self):
        for env_id in env_ids:
            self.check_determinism(env_id)

    def test_listen_dont_terminate(self):
        env = pogym.make("Tiger-v0", new_step_api=True)
        env.reset()
        _, _, terminated, _, _ = env.step(2)
        self.assertFalse(terminated)

    def test_open_left_door_terminates(self):
        env = pogym.make("Tiger-v0", new_step_api=True)
        env.reset()
        _, _, terminated, _, _ = env.step(0)
        self.assertTrue(terminated)

    def test_open_right_door_terminates(self):
        env = pogym.make("Tiger-v0", new_step_api=True)
        env.reset()
        _, _, terminated, _, _ = env.step(1)
        self.assertTrue(terminated)
