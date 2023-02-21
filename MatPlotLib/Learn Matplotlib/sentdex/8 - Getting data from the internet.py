import matplotlib.pyplot as plt
import numpy as mp

def graph_data(stock):
    stock_price_url = "http://"

    plt.xlabel("x")
    plt.ylabel("y")
    plt.title("Data from internet")
    plt.legend()
    plt.show()

graph_data("TESLA")