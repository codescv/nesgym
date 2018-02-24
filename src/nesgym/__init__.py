import os
from gym.envs.registration import register
from .nesenv import NESEnv
from .nekketsu_soccer_env import NekketsuSoccerPKEnv
from .mario_bros_env import MarioBrosEnv
from .wrappers import wrap_nes_env

register(
    id='nesgym/NekketsuSoccerPK-v0',
    entry_point='nesgym:NekketsuSoccerPKEnv',
    max_episode_steps=9999999,
    reward_threshold=32000,
    kwargs={},
    nondeterministic=True,
)

register(
    id='nesgym/MarioBros-v0',
    entry_point='nesgym:MarioBrosEnv',
    max_episode_steps=9999999,
    reward_threshold=32000,
    kwargs={},
    # FIXME I'm pretty sure the game is deterministic! Let see...
    nondeterministic=False,
)
