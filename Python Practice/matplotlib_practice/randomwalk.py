from random import choice


class RandomWalk():

#
    def __init__(self, num_points = 5000):
        self.num_points = num_points

#initialize values, these are going to store the x and y coordinated that are generated 
        self.x_values = [0]
        self.y_values = [0]


#the action that performs the random walk

    def fill_walk(self):
        #The loop that will complete all the different movements
        while len(self.x_values) < self.num_points:

            #X Move L or R in x many paces
            x_direction = choice([1,-1])
            x_distance = choice([0,1,2,3,4])
            x_step = x_direction * x_distance

            #y Move N or S 
            y_direction = choice([1,-1])
            y_distance = choice([0,1,2,3,4])
            y_step = y_direction * y_distance

            #did I move?
            if x_step and y_step == 0:
                continue
        
            #New Pos.
            x = self.x_values[-1] + x_step
            y = self.y_values[-1] + y_step

            self.x_values.append(x)
            self.y_values.append(y)

        