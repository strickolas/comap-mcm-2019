import numpy as np
import matplotlib.pyplot as plt


def plotter(vector, title="Drugs, Drugs, Drugs...", autoscale=True):
    """
    # autoscale should be in the form
        # ((-0.25, 25), (0, 10)); a tuple of tuples.
    """
    if autoscale:
        y_ceil = 0
        for element in set(vector):
            temp = vector.count(element)
            if temp > y_ceil:
                y_ceil = temp
        xlim = (0, max(set(vector)) + 3)
        ylim = (0, y_ceil + 3)
        print("max", max(vector))
    else:
        xlim, ylim = autoscale

    vector = np.array(list(vector))
    booper = []
    for bop in range(0, len(set(vector))):
        booper.append(bop)
    print('Histogram outputs (are for wieners) =', np.histogram(vector, bins=booper))

    plt.hist(vector, bins=booper, alpha=0.5)
    plt.xlim(xlim)
    plt.ylim(ylim)
    plt.title(title)
    plt.show()


def simulation(n, R, N, p, Y_0):
    t, y, Y, X, Z, Y[0] = 0, Y_0, np.zeros(R), n - Y_0, 0, Y_0

    while np.any(y > 0):
        q = 1 - (1 - (p*y) / (n - 1))**N
        y_new = np.random.binomial(X, q)
        X = X - y_new
        Y = np.roll(Y, 1)
        Y[0] = y_new
        y = sum(Y)
        Z = Z + Y[-1]
        t += 1
        # print("\x1b[33m ", q, y_new, X, Y, Y[0], y, Z, t, "\x1b[m")

    return t, Z


def main():
    # n = int(input("Enter total number of individuals in the sample: "))
    n = 200
    # R = int(input("Enter the time it will take for an individual to recover in days: "))
    R = 30
    # N = int(input("Enter the number of contacts each individual makes each day: "))
    N = 4
    # p = float(input("Enter the probability that an individual will get infected: "))
    p = .1
    # Y_0 = int(input("Enter the number of infected individuals of the first day of the epidemic: "))
    Y_0 = 2

    num_sims = 100
    sum_inf = 0
    sum_time = 0
    epidemic_duration, num_infected = [], []
    for i in range(num_sims):
        print("Simulation number = ", i + 1)
        time, num_inf = simulation(n, R, N, p, Y_0)
        epidemic_duration.append(num_inf)
        num_infected.append(time)

        print("The number of infective individuals: ", num_inf)
        print("The duration of the epidemic: ", time, "\n")

        sum_inf = sum_inf + num_inf
        sum_time = sum_time + time

    mean_inf = sum_inf / 200
    variance_inf = ((sum_inf - mean_inf)**2) / 200

    mean_time = sum_time / 200
    var_time = ((sum_time - mean_time)**2) / 200

    print("Mean of infected individuals:", mean_inf)
    print("Variance of infected individuals:", variance_inf)
    print("Mean of duration of epidemic:", mean_time)
    print("Variance of duration of epidemic:", var_time)

    plotter(epidemic_duration)


if __name__ == "__main__":
    main()
