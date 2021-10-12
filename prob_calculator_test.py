import prob_calculator
import pytest

prob_calculator.random.seed(95)

def test_hat_class_contents():
    hat = prob_calculator.Hat(red=3, blue=2)
    assert hat.contents == ["red","red","red","blue","blue"], "Expected creation of hat object to add correct contents."

def test_hat_draw():
    hat = prob_calculator.Hat(red=5, blue=2)
    assert hat.draw(2) == ['blue', 'red'], "Expected hat draw to return two random items from hat contents."
    assert len(hat.contents) == 5, "Expected hat draw to reduce number of items in contents."

def test_prob_experiment():
    hat = prob_calculator.Hat(blue=3, red=2, green=6)
    probability = prob_calculator.experiment(hat=hat, expected_balls={"blue":2,"green":1}, num_balls_drawn=4, num_experiments=1000)
    assert 0.272 == pytest.approx(probability, 0.01), "Expected experiment method to return a different probability."
    hat = prob_calculator.Hat(yellow=5,red=1,green=3,blue=9,test=1)
    probability = prob_calculator.experiment(hat=hat, expected_balls={"yellow":2,"blue":3,"test":1}, num_balls_drawn=20, num_experiments=100)
    assert 1.0 == pytest.approx(probability, 0.01), "Expected experiment method to return a different probability."