import matplotlib.pyplot as plt
#Example Data
input_values = [1,2,3,4,5]
squares = [1, 4 , 9, 16, 25]

#Creating the basic graph
#Add a style here
plt.style.use('seaborn-v0_8')
fig, ax = plt.subplots()
ax.plot(input_values, squares, linewidth=3)
#Now work from here
ax.scatter(input_values, squares, s=100)

#Set title and axis labels
ax.set_title("Square Numbers", fontsize=24)
ax.set_xlabel('Value', fontsize=14)
ax.set_ylabel('Square of value', fontsize=14)

#Set the size of Tick labels
ax.tick_params(labelsize=14)


plt.show()
