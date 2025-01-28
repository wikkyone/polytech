import matplotlib.pyplot as plt

def two_plots(y1, y2):
    fig, ax = plt.subplots()
    ax.plot(y1, label='Dataset 1')
    ax.plot(y2, label='Dataset 2')
    ax.set_xlabel('Индекс')
    ax.set_ylabel('Значение')
    ax.set_title('Сравнение двух датасетов')
    ax.legend()
    plt.show()
    return ax
