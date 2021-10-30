import copy
import random

class Hat:
    def __init__(self, **args):
        self.contents = []
        for key in args:
            for i in range(args[key]):
                self.contents.append(key)

    def draw(self, number):
        picked_balls = []
        for i in range(number):
            picked_ball = random.choice(self.contents)
            picked_balls.append(picked_ball)
            self.contents.remove(picked_ball)

        return picked_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    if num_balls_drawn >= len(hat.contents):
        return 1.00
    
    success = 0
    for i in range(num_experiments):
        hat_copy = copy.deepcopy(hat)
        picked_balls = hat_copy.draw(num_balls_drawn)
        
        picked_balls_dict = dict()
        for ball in picked_balls:
            picked_balls_dict[ball] = picked_balls_dict.get(ball, 0) + 1

        criteria = 0
        for key in expected_balls:
            if picked_balls_dict.get(key, 0) >= expected_balls[key]:
                criteria = criteria + 1
            
        if criteria == len(expected_balls):
            success = success + 1

    return success / num_experiments

print('')
hat =  Hat(blue = 7, green = 3, red = 4, gray = 5, black = 2)
print('Balls in the hat:', hat.contents)
print('')
print('Probability to draw 1 black ball and 3 blue balls from a 4 ball draw:', str(experiment(hat, {"black": 1, "blue": 3}, 5, 1000)*100) + '%')
print('')