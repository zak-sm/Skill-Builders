import matplotlib.pyplot as plt

x_values = (range (1,5000))
y_values = [value**3 for value in x_values]

plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.scatter(x_values, y_values, s = 15, c= y_values, cmap=plt.get_cmap('pink'))

ax.axis([0,5000,0,125000000000])
ax.set_title('Graph of Cubed Values!',fontsize= 25)
ax.set_ylabel('Values Squared',fontsize= 12)
ax.set_xlabel('Values',fontsize= 12)

ax.tick_params(labelsize=14)
ax.ticklabel_format(style='plain')

plt.show()