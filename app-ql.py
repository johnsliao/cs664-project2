import gym
import numpy as np


def discretize(env):
    num_states = (env.observation_space.high - env.observation_space.low) * \
                 np.array([10, 100])
    num_states = np.round(num_states, 0).astype(int) + 1
    return num_states


if __name__ == '__main__':
    env = gym.make('MountainCar-v0')
    state_size = env.observation_space.shape[0]
    num_states = discretize(env)
    q = np.random.uniform(low=-1, high=1,
                          size=(num_states[0], num_states[1],
                                env.action_space.n))

    learning_rate = .8
    y = .95
    episodes = 2000
    avg_reward_list = []

    for i in range(episodes):
        state = env.reset()
        rewards_list = []
        r = time = 0

        print 'Episode', i

        while time < 250:
            env.render()
            time += 1
            state_adj = (state - env.observation_space.low) * np.array([10, 100])
            state_adj = np.round(state_adj, 0).astype(int)

            action = np.argmax(q[state_adj[0], state_adj[1]])
            state_new, state_reward, done, _ = env.step(action)

            # Discretize
            state2_adj = (state_new - env.observation_space.low) * np.array([10, 100])
            state2_adj = np.round(state2_adj, 0).astype(int)

            delta = learning_rate * (
                    state_reward + np.max(q[state2_adj[0], state2_adj[1]]) - q[state_adj[0], state_adj[1], action])
            q[state_adj[0], state_adj[1], action] += delta

            r += state_reward
            state = state_new
            rewards_list.append(r)

            if done:
                print 'Finished in %s time steps' % time
                avg_reward = np.mean(rewards_list)
                avg_reward_list.append(avg_reward)
                print 'avg reward list: ', avg_reward_list
                break
