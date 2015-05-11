import matplotlib.pyplot as plt

def plot_rewards(episode_rewards):
    x = [x for x in range(len(episode_rewards))]
    y = episode_rewards
    plt.xlabel('Episodes')
    plt.ylabel('Total reward')
    plt.title('Agent learning')
    plt.grid()
    plt.plot(x, y, 'b')
