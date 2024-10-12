import matplotlib.pyplot as plt
from randomwalk import RandomWalk

#access Random Walk

#Build Plot

while True:
    rw = RandomWalk(50_000)
    rw.fill_walk()


    plt.style.use('ggplot')
    fig, ax= plt.subplots(figsize=(14, 7))
    point_number = range(rw.num_points)
    #ax.plot(rw.x_values, rw.y_values, linewidth= 1)
    ax.scatter(rw.x_values, rw.y_values, s=1, c=point_number, cmap='Blues', edgecolors='none')
    ax.set_aspect('equal')


    #emphasize the first and last points
    plt.scatter(0,0, c='green',edgecolors='none', s = 25)
    ax.scatter(rw.x_values[-1], rw.y_values[-1], c='red', edgecolors= 'none', s=25)

    ax.get_yaxis().set_visible(False)
    ax.get_xaxis().set_visible(False)


    plt.show()

    keeprunning =  input("would you like to continue? y or n: ")
    if keeprunning == 'n':
        break