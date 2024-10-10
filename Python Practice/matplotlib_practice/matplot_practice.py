import matplotlib.pyplot as plt
#Example Data
#-- OLD
#input_values = [1,2,3,4,5]
#squares = [1, 4 , 9, 16, 25]
#-- NEW
x_values = range(1,1001)
y_values = [x**2 for x in x_values]
#Creating the basic graph
#Add a style here
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
#ax.plot(x_values, y_values, linewidth=1)
ax.scatter(x_values, y_values, c=y_values, s=10, cmap=plt.get_cmap('pink'))
#Now work from here

#Set title and axis labels
ax.axis([0,1100, 0, 1_100_000])
ax.set_title("Square Numbers", fontsize=24, color='blue')
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of value', fontsize=14)

#Set the size of Tick labels
ax.tick_params(labelsize=14)
ax.ticklabel_format(style='plain')


path = 'Python Practice/Matplotlib'

plt.show()
#plt.savefig('squares_plt.png', bbox_inches='tight')