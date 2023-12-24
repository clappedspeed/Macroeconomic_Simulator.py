import matplotlib.pyplot as plt

def plot_gdp(data, time_steps):
    plt.figure(figsize=(8, 6))
    plt.plot(time_steps, data, label='GDP')
    plt.xlabel('Time Steps')
    plt.ylabel('GDP Value')
    plt.title('GDP Over Time')
    plt.legend()
    plt.grid(True)
    plt.show()

plot_gdp([5,6,7,8], [1,2,3,4])