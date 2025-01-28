import matplotlib.pyplot as plt
def data_plots(x, y1, y2):
    plt.subplot(1, 2, 1)
    plot1, = plt.plot(x,y1, linestyle='-', color='g')
    plt.subplot(1, 2, 2)
    plot2, = plt.plot(x,y2, linestyle='-.', color='r')
    return plot1, plot2