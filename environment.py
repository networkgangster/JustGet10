import pygame, bases, possibles, merge, justGetTenGUI
import numpy as np
import matplotlib.pyplot as plt
import pickle
from matplotlib import style
import time
import pyautogui

# Größe des Environments
SIZE = 4

# how many episodes
HM_EPISODES = 25000

# Rewards
GAMEOVER_PENALTY = 20
MOVE_REWARD = 1
HIGHER_REWARD = 5
TEN_REWARD = 50

# Q learning parameters
LEARNING_RATE = 0.1
DISCOUNT = 0.95
epsilon = 0.9
EPS_DECAY = 0.9998  # rückgang von epsilon, wird vielleicht nicht verwendet
SHOW_EVERY = 3000  # nur jede 3000. episode anzeigen damit schneller trainiert

# training mit einer bereits vorhandenen Q table fortsetzen
start_q_table = None  # or filename

#alle möglichen aktionen:
action_space = {1: (0,0),
                2: (0,1),
                3: (0,2),
                4: (0,3),
                5: (1, 0),
                6: (1, 1),
                7: (1, 2),
                8: (1, 3),
                9: (2, 0),
                10: (2, 1),
                11: (2, 2),
                12: (2, 3),
                13: (3, 0),
                14: (3, 1),
                15: (3, 2),
                16: (3, 3)}

# alle möglichen Zustände


# zufällige aktion
def action(x, y, field):
    x = np.random.randint(0, 4)
    y = np.random.randint(0, 4)
    field.append([x, y])



if start_q_table is None:
   ''' q_table = np.random.uniform(low = 1, high = 5, size = (4 * 4 * 16))
   q_table = np.zeros([board, action_space]) '''
else:
    with open(start_q_table, "rb") as f:
        q_table = pickle.load(f)

episode_rewards = []

for episode in range(HM_EPISODES):
    # initalisierungen von spielfeld usw

    if episode % SHOW_EVERY == 0:
        print(f"on # {episode}, epsilon: {epsilon}")
        print(f"{SHOW_EVERY} ep mean {np.mean(episode_rewards[-SHOW_EVERY])}")
        show = True
    else:
        show = False

    episode_reward = 0
    for not gameover:
        obs = (board)
        if np.random.random() > epsilon:
            action = np.argmax(q_table[obs])
        else:
            action = np.random.randint(1,17)


        if no moves left:
            reward = -GAMEOVER_PENALTY
        elif successful move:
            reward = MOVE_REWARD
        elif higher number:
            reward = HIGHER_REWARD
        elif got ten:
            reward = TEN_REWARD

        new_obs = (board)
        max_future_q = np.max(q_table[new_obs])
        current_q = q_table[obs][action]

        if reward == TEN_REWARD:
            new_q = TEN_REWARD
        elif reward == -GAMEOVER_PENALTY:
            new_q = -GAMEOVER_PENALTY
        else:
            new_q = (1 - LEARNING_RATE) * current_q + LEARNING_RATE * (reward + DISCOUNT * max_future_q)

        q_table[obs][action] = new_q

    episode_reward += reward
    if reward == TEN_REWARD or reward == -GAMEOVER_PENALTY:
        break bzw gameover

    episode_rewards.append(episode_reward)
    epsilon *= EPS_DECAY

moving_avg = np.convolve(episode_rewards, np.ones((SHOW_EVERY,)) / SHOW_EVERY, mode = "valid")

plt.plot([i for i in range(len(moving_avg))], moving_avg)
plt.ylabel(f"reward {SHOW_EVERY}")
plt.xlabel("episode #")
plt.show()

with open (f"qtable-{int(time.time())}.pickle", "wb") as f:
    pickle.dump(q_table, f)
