
import prob_calculator
from unittest import main

hat = prob_calculator.Hat(blue=4, red=2, green=6)
probability = prob_calculator.experiment(
    hat=hat,
    expected_balls={"red": 2,
                    "green": 1},
    num_balls_drawn=5,
    num_experiments=2000)
print(f"Probability: {probability * 100:.2f}%")

# Run unit tests automatically
main(module='test_module', exit=False)
