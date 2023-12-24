import random
import numpy as np

# Define economic variables
gdp = 1000000  # Initial GDP
unemployment_rate = 5.0  # Initial unemployment rate
inflation_rate = 2.0  # Initial inflation rate

# Define simulation parameters
num_years = 10  # Number of years to simulate
current_year = 1  # Start year
end_year = current_year + num_years - 1

# Lists to log economic data over time
gdp_history = [gdp]
unemployment_history = [unemployment_rate]
inflation_history = [inflation_rate]

# Main simulation loop
while current_year <= end_year:
    # Display the current year
    print(f"Year {current_year}")

    # Economic processes
    # Simulate GDP growth
    gdp_growth = np.random.normal(1, 0.1)  # Random growth rate between 1% and 5%
    gdp *= (1 + gdp_growth / 100)

    # Simulate unemployment rate changes
    unemployment_change = random.uniform(-1.0, 1.0)  # Random change between -1% and 1%
    unemployment_rate += unemployment_change
    unemployment_rate = max(2.0, min(10.0, unemployment_rate))  # Limit within a range

    # Simulate inflation rate changes
    inflation_change = random.uniform(-0.5, 0.5)  # Random change between -0.5% and 0.5%
    inflation_rate += inflation_change
    inflation_rate = max(0.0, inflation_rate)  # Ensure it's not negative

    # Random events (e.g., economic crises)
    if random.random() < 0.1:  # 10% chance of an event occurring
        event_type = random.choice(["economic_crisis", "technological_breakthrough", "natural_disaster"])
        if event_type == "economic_crisis":
            gdp *= 0.8  # GDP drops by 20%
            unemployment_rate += 2.0  # Unemployment increases by 2%
        elif event_type == "technological_breakthrough":
            gdp *= 1.2  # GDP increases by 20%
        elif event_type == "natural_disaster":
            gdp *= 0.9  # GDP drops by 10%

    # User interactions (simplified for illustration)
    user_input = input("Enter a policy decision (e.g., 'cut taxes', 'increase spending'): ")
    # Implement logic to update the economy based on user input

    # Log economic data for the current year
    gdp_history.append(gdp)
    unemployment_history.append(unemployment_rate)
    inflation_history.append(inflation_rate)

    # Display economic indicators
    print(f"GDP: {gdp}")
    print(f"Unemployment Rate: {unemployment_rate}%")
    print(f"Inflation Rate: {inflation_rate}%")

    # Check for win or loss conditions (simplified for illustration)
    if gdp > 15000:
        print("Congratulations! You've achieved a high GDP. You win!")
        break
    elif unemployment_rate > 8.0:
        print("High unemployment rate. You lose!")
        break

    # Increment the year
    current_year += 1

# End of simulation
print("Simulation completed.")

# You can use the data in gdp_history, unemployment_history, and inflation_history for further analysis or visualization.
