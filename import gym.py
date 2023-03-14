import gym
import numpy as np
import time
from IPython.display import display, clear_output

from gym import spaces
import pygame
import matplotlib.pyplot as plt
import random

class CustomEnv(gym.Env):
    metadata = {'render.modes': ['human']}
    
    def __init__(self):
        super(CustomEnv, self).__init__()
        # Write a constructor for your enviroment
        # Define the action_space and observation_space
        # Position your agent and the target in the enviroment 
        self.size = 10  # The size of the square grid
        self.window_size = 512  # The size of the PyGame window
        
        # Observations are dictionaries with the agent's and the target's location.
        # Each location is encoded as an element of {0, ..., `size`}^2, i.e. MultiDiscrete([size, size]).
        self.observation_space = spaces.Dict(
            {
                "agent": spaces.Box(0, self.size - 1, shape=(2,), dtype=int),
                "target": spaces.Box(5, 5, shape=(2,), dtype=int),
            }
        )
        self._agent_location = self.observation_space.sample()['agent']
        self._target_location = self.observation_space.sample()['target']

        # We have 4 actions, corresponding to "right", "up", "left", "down"
        self.action_space = spaces.Discrete(4)
        self.actions = ["right", "up", "left", "down"]

        """
        The following dictionary maps abstract actions from `self.action_space` to 
        the direction we will walk in if that action is taken.
        I.e. 0 corresponds to "right", 1 to "up" etc.
        """
        self._action_to_direction = {
            0: np.array([1, 0]),
            1: np.array([0, 1]),
            2: np.array([-1, 0]),
            3: np.array([0, -1]),
        }

        """
        If human-rendering is used, `self.window` will be a reference
        to the window that we draw to. `self.clock` will be a clock that is used
        to ensure that the environment is rendered at the correct framerate in
        human-mode. They will remain `None` until human-mode is used for the
        first time.
        """
        self.window = None
        self.clock = None
        
    def step(self, action):
        # Write the step method for your enviroment. Make sure you agent does not go out of bounds
        # by performing the action.
        # Map the action (element of {0,1,2,3}) to the direction we walk in
        direction = self._action_to_direction[action]
        # We use `np.clip` to make sure we don't leave the grid
        self._agent_location = np.clip(
            self._agent_location + direction, 0, self.size - 1
        )
        # An episode is done if the agent has reached the target
        done = np.array_equal(self._agent_location, self._target_location)
        reward = 10 if done else -0.5  # Binary sparse rewards
        observation = self._get_obs()
        info = self._get_info()

        return observation, reward, done, info
        
        #return (observation, reward, done,_)
     
    def reset(self):
        # Write the reset method that results in the starting state
        # We need the following line to seed self.np_random
        #np.random.seed(1337)

        # Choose the agent's location uniformly at random
        self._agent_location = np.array([np.random.randint(0, 10), np.random.randint(0, 10)])

        # We will sample the target's location randomly until it does not coincide with the agent's location
        self._target_location = self._agent_location
        while np.array_equal(self._target_location, self._agent_location):
            self._target_location = np.array([5,5])

        observation = self._get_obs()
        info = self._get_info()
        return (observation, info) #if return_info else observation
        #return state
        
    def render(self):
        mode = self.metadata['render.modes']
        #Write a render method for your enviroment to visualize the current state in the terminal
        if self.window is None and mode == ['human']:
            pygame.init()
            pygame.display.init()
            self.window = pygame.display.set_mode((self.window_size, self.window_size))
        if self.clock is None and mode == ['human']:
            self.clock = pygame.time.Clock()

        canvas = pygame.Surface((self.window_size, self.window_size))
        canvas.fill((255, 255, 255))
        pix_square_size = (
            self.window_size / self.size
        )  # The size of a single grid square in pixels

        # First we draw the target
        pygame.draw.rect(
            canvas,
            (255, 0, 0),
            pygame.Rect(
                pix_square_size * self._target_location,
                (pix_square_size, pix_square_size),
            ),
        )
        # Now we draw the agent
        pygame.draw.circle(
            canvas,
            (0, 0, 255),
            (self._agent_location + 0.5) * pix_square_size,
            pix_square_size / 3,
        )

        # Finally, add some gridlines
        for x in range(self.size + 1):
            pygame.draw.line(
                canvas,
                0,
                (0, pix_square_size * x),
                (self.window_size, pix_square_size * x),
                width=3,
            )
            pygame.draw.line(
                canvas,
                0,
                (pix_square_size * x, 0),
                (pix_square_size * x, self.window_size),
                width=3,
            )

        if mode == ['human']:
            # The following line copies our drawings from `canvas` to the visible window
            self.window.blit(canvas, canvas.get_rect())
            pygame.event.pump()
            pygame.display.update()
            
            self.window.blit(canvas, (0, 0))
            pygame.display.flip()

            # We need to ensure that human-rendering occurs at the predefined framerate.
            # The following line will automatically add a delay to keep the framerate stable.
            self.clock.tick(4)
        else:  # rgb_array
            return np.transpose(
                np.array(pygame.surfarray.pixels3d(canvas)), axes=(1, 0, 2)
            )
        
    def decode_action(self, action):
        #decode a linear action to 2D
        return self.actions[action]

    def decode_state(self, state):
        #decode a linear state to 2D
        a = state % 10
        b = (state-a)/10
        return np.array([b,a])
    
    def encode_state(self,state):
        #encode a 2D state in 1D
        b = state['agent'][0]*10
        a = state['agent'][1]
        return b+a
    
    def _get_obs(self):
        return {"agent": self._agent_location, "target": self._target_location}
    
    def _get_info(self):
        return {"distance": np.linalg.norm(self._agent_location - self._target_location, ord=1)}


env = CustomEnv()
done = False
while done == False:
    a = env.action_space.sample()
    _,_, done,_ = env.step(a)
    clear_output(wait=True)
    env.render()
    time.sleep(0.1)