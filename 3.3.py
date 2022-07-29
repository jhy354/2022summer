#!/usr/bin/env python3

import matplotlib.pyplot as plt
import numpy as np

if __name__ == "__main__":
    x = np.linspace(0, 10, 1000)
    y1 = np.sin(x)
    y2 = np.sin(x**2)
    plt.figure(figsize=(8, 4))

    plt.title("sin(x) sin(x^2)")
    plt.plot(x, y1, label="sin(x)", color='r', linewidth=2)
    plt.scatter(x, y2, label="sin(x^2)")

    plt.xlim(0, 10)
    plt.ylim(-1.5, 1.5)
    plt.legend()

    plt.savefig("chart.jpg")

    exit(0)