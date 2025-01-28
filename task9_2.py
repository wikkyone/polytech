import matplotlib.pyplot as plt
def data_plot(x, y):
    fig, ax = plt.subplots()
    ax.plot(x,y)
    ax.set_xlabel("Ось X")
    ax.set_ylabel("Ось Y")
    ax.set_title("Линейный график")
    plt.show()
    return ax
data_plot([1, 2, 3, 4, 5], [2, 4, 6, 8, 10])