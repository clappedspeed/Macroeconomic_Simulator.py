import tkinter as tk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime, timedelta
import numpy as np

from population import Population, Individual, population


class Graphs:
    def __init__(self, root):
        self.root = root
        self.root.title("Economy Simulator")
        self.root.geometry("1280x720")

        # Create a boolean variable to track the pause state
        self.paused = False

        # Create a pause button
        self.pause_button = tk.Button(root, text="Pause/Resume", command=self.toggle_pause)
        self.pause_button.pack()

        # Initialize economic data (initial variables)
        self.gdp = 1000
        self.inflation = 0.03
        self.unemployment = 5.0
        self.balance_of_payment = 0
        self.spending = 10
        total_income = population.get_total_income()
        self.tax = (total_income * 0.3)
        self.budget = self.tax - self.spending
        self.current_date = datetime(2023, 1, 1)
        self.dates = [self.current_date]
        self.gdp_data = [self.gdp]
        self.inflation_data = [self.inflation * 100]  # Store inflation as a percentage
        self.unemployment_data = [self.unemployment]
        self.balance_of_payment_data = [self.balance_of_payment]
        self.budget_data = [self.budget]

        # Create labels for economic data
        self.gdp_label = tk.Label(root, text=f"GDP: ${self.gdp:.2f} billion")
        self.inflation_label = tk.Label(root, text=f"Inflation: {self.inflation * 100:.2f}%")
        self.unemployment_label = tk.Label(root, text=f"Unemployment Rate: {self.unemployment:.2f}%")
        self.balance_of_payment_label = tk.Label(root,text=f"Balance of Payment: ${self.balance_of_payment:.2f} billion")
        self.budget_label = tk.Label(root, text=f"Budget: ${self.budget:.2f} billion")

        # Create Matplotlib figures for GDP, Inflation, Unemployment, Balance of Payment, and Budget
        self.fig_gdp, self.ax_gdp = plt.subplots(figsize=(9, 6))
        self.fig_inflation, self.ax_inflation = plt.subplots(figsize=(9, 6))
        self.fig_unemployment, self.ax_unemployment = plt.subplots(figsize=(9, 6))
        self.fig_balance_of_payment, self.ax_balance_of_payment = plt.subplots(figsize=(9, 6))
        self.fig_budget, self.ax_budget = plt.subplots(figsize=(9, 6))

        self.canvas_gdp = FigureCanvasTkAgg(self.fig_gdp, master=root)
        self.canvas_inflation = FigureCanvasTkAgg(self.fig_inflation)
        self.canvas_unemployment = FigureCanvasTkAgg(self.fig_unemployment)
        self.canvas_balance_of_payment = FigureCanvasTkAgg(self.fig_balance_of_payment)
        self.canvas_budget = FigureCanvasTkAgg(self.fig_budget)

        self.canvas_widget_gdp = self.canvas_gdp.get_tk_widget()
        self.canvas_widget_inflation = self.canvas_inflation.get_tk_widget()
        self.canvas_widget_unemployment = self.canvas_unemployment.get_tk_widget()
        self.canvas_widget_balance_of_payment = self.canvas_balance_of_payment.get_tk_widget()
        self.canvas_widget_budget = self.canvas_budget.get_tk_widget()

        # Create a button to toggle between graphs
        self.toggle_button = tk.Button(root, text="Toggle Graph", command=self.toggle_graph)
        # Place widgets on the screen
        self.gdp_label.pack()
        self.inflation_label.pack()
        self.unemployment_label.pack()
        self.balance_of_payment_label.pack()
        self.budget_label.pack()
        self.toggle_button.pack()
        self.canvas_widget_gdp.pack()
        self.canvas_widget_inflation.pack_forget()  # Hide the inflation graph initially
        self.canvas_widget_unemployment.pack_forget()  # Hide the unemployment graph initially
        self.canvas_widget_balance_of_payment.pack_forget()  # Hide the balance of payment graph initially
        self.canvas_widget_budget.pack_forget()  # Hide the budget graph initially

        # Start automatic updates
        self.update_economic_data()

    def toggle_pause(self):
        # Toggle the pause state
        self.paused = not self.paused

        # Update the label of the pause button
        if self.paused:
            self.pause_button.config(text="Resume")
        else:
            self.pause_button.config(text="Pause")
        # Check if the simulation is paused
        if not self.paused:
            # Schedule the next update after 750 milliseconds (monthly)
            self.root.after(750, self.update_economic_data)

    def update_economic_data(self): # this is the method that allows for constant updates of graphs
        # normal distribution is used to simulate the economy
        self.gdp_growth_factor = np.random.normal(1.002, 0.02)
        self.gdp *= self.gdp_growth_factor
        self.inflation = np.random.normal(0.02, 0.015)
        self.unemployment = np.random.normal(4.5, 0.5)
        self.balance_of_payment = np.random.normal(0, 3)
        economic_factors = {"gdp_growth_factor": 1.02, "inflation": 0.03, "unemployment": 5.0}
        population.update_population(economic_factors)
        self.budget = self.tax - self.spending


        self.current_date += timedelta(days=30)  # Increment the current date of simulation


        # Simulate conflicts between economic indicators
        self.inflation += self.gdp_growth_factor * 0.05  # Inflation increases with GDP growth
        self.balance_of_payment += 0.5 * (self.gdp_growth_factor - 1)  # Balance of Payment improves with GDP growth
        # Simulate the inverse relationship between inflation and unemployment (Phillips curve)
        self.unemployment -= 0.05 * (self.inflation - 2)

        # Simulate the feedback loop between unemployment and economic growth
        self.gdp_growth_factor -= 0.01 * self.unemployment  # Economic growth decreases with higher unemployment

        # Ensure indicators don't go below zero
        self.inflation = max(0, self.inflation)
        self.unemployment = max(0, self.unemployment)
        self.balance_of_payment = max(0, self.balance_of_payment)
        self.budget = max(0, self.budget)
        self.gdp_growth_factor = max(0.8, self.gdp_growth_factor)  # Ensure a minimum growth factor

        # Simulate the impact of a balance of payment deficit on economic growth
        if self.balance_of_payment < 0:
            # Increase GDP due to increased consumption from a balance of payment deficit
            self.gdp *= 1.02
        # Simulate baseline budget and balance of payment
        baseline_budget = 0.2 * self.gdp_growth_factor  # Adjust the coefficient as needed
        baseline_balance_of_payment = 0.1 * self.gdp_growth_factor  # Adjust the coefficient as needed
        random_budget_fluctuation = np.random.normal(0, 0.5)  # Adjust the parameters as needed
        random_balance_of_payment_fluctuation = np.random.normal(0, 0.3)  # Adjust the parameters as needed
        self.budget = baseline_budget + random_budget_fluctuation
        self.balance_of_payment = baseline_balance_of_payment + random_balance_of_payment_fluctuation


        # Add the associated data of each variable into its own array
        self.dates.append(self.current_date)
        self.gdp_data.append(self.gdp)
        self.inflation_data.append(self.inflation * 100)
        self.unemployment_data.append(self.unemployment)
        self.balance_of_payment_data.append(self.balance_of_payment)
        self.budget_data.append(self.budget)

        # Update labels with new data
        self.gdp_label.config(text=f"GDP: ${self.gdp:.2f} billion ({self.current_date.strftime('%B %Y')})")
        self.inflation_label.config(
            text=f"Inflation: {self.inflation * 100:.2f}% ({self.current_date.strftime('%B %Y')})")
        self.unemployment_label.config(
            text=f"Unemployment Rate: {self.unemployment:.2f}% ({self.current_date.strftime('%B %Y')})")
        self.balance_of_payment_label.config(
            text=f"Balance of Payment: ${self.balance_of_payment:.2f} billion ({self.current_date.strftime('%B %Y')})")
        self.budget_label.config(text=f"Budget: ${self.budget:.2f} billion ({self.current_date.strftime('%B %Y')})")

        # Update the graphs themselves
        self.ax_gdp.clear()
        self.ax_inflation.clear()
        self.ax_unemployment.clear()
        self.ax_balance_of_payment.clear()
        self.ax_budget.clear()

        self.ax_gdp.plot(self.dates, self.gdp_data, label="GDP")
        self.ax_inflation.plot(self.dates, self.inflation_data, label="Inflation")
        self.ax_unemployment.plot(self.dates, self.unemployment_data, label="Unemployment Rate")
        self.ax_balance_of_payment.plot(self.dates, self.balance_of_payment_data, label="Balance of Payment")
        self.ax_budget.plot(self.dates, self.budget_data, label="Budget")

        # axis labels
        self.ax_gdp.set_xlabel("Date")
        self.ax_inflation.set_xlabel("Date")
        self.ax_unemployment.set_xlabel("Date")
        self.ax_balance_of_payment.set_xlabel("Date")
        self.ax_budget.set_xlabel("Date")
        self.ax_gdp.set_ylabel("GDP (billions)")
        self.ax_inflation.set_ylabel("Inflation (%)")
        self.ax_unemployment.set_ylabel("Unemployment Rate (%)")
        self.ax_balance_of_payment.set_ylabel("Balance of Payment (billions)")
        self.ax_budget.set_ylabel("Budget (billions)")

        # information on the lines of graphs
        self.ax_gdp.legend()
        self.ax_inflation.legend()
        self.ax_unemployment.legend()
        self.ax_balance_of_payment.legend()
        self.ax_budget.legend()

        # draws the graph if it has not been redrawn
        self.canvas_gdp.draw()
        self.canvas_inflation.draw()
        self.canvas_unemployment.draw()
        self.canvas_balance_of_payment.draw()
        self.canvas_budget.draw()

        # Check if the simulation is paused
        if not self.paused:
            # Schedule the next update after 750 milliseconds (monthly)
            self.root.after(750, self.update_economic_data)

    def toggle_graph(self):
        # this method allows the user to cycle through the 5 different graphs with a button, self.toggle_button
        if self.canvas_widget_gdp.winfo_ismapped():
            self.canvas_widget_gdp.pack_forget()
            self.canvas_widget_inflation.pack()
        elif self.canvas_widget_inflation.winfo_ismapped():
            self.canvas_widget_inflation.pack_forget()
            self.canvas_widget_unemployment.pack()
        elif self.canvas_widget_unemployment.winfo_ismapped():
            self.canvas_widget_unemployment.pack_forget()
            self.canvas_widget_balance_of_payment.pack()
        elif self.canvas_widget_balance_of_payment.winfo_ismapped():
            self.canvas_widget_balance_of_payment.pack_forget()
            self.canvas_widget_budget.pack()
        else:
            self.canvas_widget_budget.pack_forget()
            self.canvas_widget_gdp.pack()


def main():
    root = tk.Tk()
    app = Graphs(root)
    root.mainloop()


if __name__ == "__main__":
    main()
