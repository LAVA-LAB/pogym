# pogym
 A collection of POMDP environments 

## Quick-start 

### Installation

```bash
pip install git+ssh://git@github.com/tdsimao/pogym.git
```

```bash
pip install git+https://github.com/tdsimao/pogym
```

### API

Example using the "Tiger-v0" environment.

```python
import gym
import pogym  # register pogym environments


if __name__ == '__main__':
    print(f"list of environments: {pogym.env_ids}")

    env = gym.make("Tiger-v0")
    observation, info = env.reset(seed=123)
    for i in range(10):
        action = 2  # listen
        print(f"step:{i} observation: {observation}")
        observation, reward, terminated, truncated, info = env.step(action)
        if terminated or truncated:
            observation, info = env.reset()
    env.close()
```

Expected Output:
```
list of environments: ['CheeseMaze-v0', 'Tiger-v0', 'Voicemail-v0']
step:0 observation: 0
step:1 observation: 0
step:2 observation: 0
step:3 observation: 0
step:4 observation: 0
step:5 observation: 1
step:6 observation: 0
step:7 observation: 0
step:8 observation: 1
step:9 observation: 0
```

## Contributing

Install package in editable (develop) mode
```bash
git clone https://github.com/tdsimao/pogym.git
cd pogym
pip install -e .
```


### Tests

```bash
python -m unittest discover
```

## Acknowledgments

This project contains the environments from [AIS based PORL](https://github.com/info-structures/ais).
