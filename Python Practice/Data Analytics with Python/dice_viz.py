import plotly.express as px
from dice import Dice

D6 = Dice(8)
G6 = Dice(8)

#Rolls the 2 dice as many times as specified and returns a list of all the results
def get_results(rolls=1000) -> list:
    results = []
    for i in range(rolls):
        result = D6.roll() + G6.roll()
        results.append(result)
    return (results)

#Range of possible totals 
pos_results= range(2,(D6.num_sides + G6.num_sides + 1))

#Takes the list of results and returns the frequency of each side being rolled 
def get_frequency(results) -> list:
    frequencies = []
    
    for i in pos_results:
        frequencies.append(results.count(i))
    return frequencies


#Will run the dice game simulation as many times as specified and return the average frequencies of each side from all the games
def get_mean(cycles=1) ->list:
    #stores all the frequencies of the different simmulations
    big_list = []
    if cycles > 1:

        for i in range(cycles):

            results:list = get_results()
            frequencies:list = get_frequency(results)
            big_list.append(frequencies)


        test_freq:list = []
        for i in range(len(big_list[1])):
            count:int = 0
            for j in range(len(big_list)):
                count += (big_list[j][i])
            test_freq.append(count)
            
        print(test_freq)
#takes all lists of frequencies and returns one with the averages across all simulations
        for i in range(len(test_freq)):
            test_freq[i] = int(test_freq[i]/len(big_list))
        return test_freq
    else: 
        results = get_results()
        frequencies:list = get_frequency(results)
        big_list.append(frequencies)
        return big_list

#calling simmulation
big_sim = get_mean(1000)
print(big_sim)

#This will create a bar chart showing the mean results of a 6-sided dice roll across 1000 simulations.

##Now for the visualization part
title = "Mean results of a 6 Sided Dice roll 1000 times across 1000 simulations"
label = {'x' : 'Result', 'y' : 'Frequency of Result'}
fig = px.bar(x=pos_results, y=big_sim, title = title, labels=label)
fig.update_layout(xaxis_dtick=1)
fig.show()
