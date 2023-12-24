# I originally had a wider scope for this project
# This is now redundant as i simplified my project to omit this

import numpy as np
import time

class Individual:
    def __init__(self, initial_income):
        self.income = initial_income

    def update_income(self, economic_factors):
        # Simulate how individual income changes based on economic factors
        income_growth_factor = np.random.normal(1.02, 0.01)  # Adjust the parameters as needed
        self.income *= income_growth_factor

class Population:
    def __init__(self, size, initial_income_range):
        self.individuals = [Individual(np.random.normal(*initial_income_range)) for _ in range(size)]

    def update_population(self, economic_factors):
        # Update the incomes of all individuals in the population
        for individual in self.individuals:
            individual.update_income(economic_factors)

    def get_total_income(self):
        # Calculates the total income of the population
        total_income = sum(individual.income for individual in self.individuals)
        return total_income



    def get_average_income(self):
        # Calculate the average income of the population
        total_income = sum(individual.income for individual in self.individuals)
        average_income = total_income / len(self.individuals)
        return average_income

# Example usage:
initial_population_size = 100000
initial_income_range = (30000, 80000)  # Adjust the income range as needed

# Create a population
population = Population(size=initial_population_size, initial_income_range=initial_income_range)

# Simulate economic factors and update the population
economic_factors = {"gdp_growth_factor": 1.02, "inflation": 0.03, "unemployment": 5.0}
population.update_population(economic_factors)

# Get the average income of the population
average_income = population.get_average_income()
total_income = population.get_total_income()


