from random import choice

class RandomWalk:
    '''a class to generate random wlak'''

    def __init__(self, n_steps=5000):
        '''initialise attributes of a walk'''
        self.n_steps = n_steps

        # initialise step record
        self.xpos = [0]
        self.ypos = [0]

    def generate_steps(self):
        '''to generate the steps'''

        def generate():
            '''a function to generate a step on either axis'''
            # determine the direction on x/y axis
            # direction = choice([-1, 1])
            direction = choice([-1, 1])
            # determine the distance
            distance = choice(range(6))
            # to form a step by multiplying the aboves
            step = direction * distance
            return step
            
        while len(self.xpos) < self.n_steps:
            # generate a step on x axis
            x_step = generate()

            # generate a step on y axis
            y_step = generate()

            if x_step == 0 and y_step == 0:
                continue
            
            # get exact step position and append it to the position list
            xpos = x_step + self.xpos[-1]
            ypos = y_step + self.ypos[-1]
            self.xpos.append(xpos)
            self.ypos.append(ypos)
