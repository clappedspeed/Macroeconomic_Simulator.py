import random
import sqlite3
import time
import tkinter as tk
from datetime import datetime, timedelta
from tkinter import ttk, messagebox

import matplotlib.pyplot as plt
import numpy as np
import pygame
from PIL import ImageTk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

from Database import cursor, connect, load_simulation_state
from programstuff.event import events
from programstuff.policy import policy_instances

import json


pygame.init()
pygame.mixer_music.load("theme.mp3")
pygame.mixer_music.play(loops=1)



class EconomicSimulatorGraphs:
    def __init__(self, root, user_id):
        self.root = root
        self.root.title("Economy Simulator")
        self.root.geometry("1280x720")
        self.user_id = user_id  # Store the user ID

        self.database_connection = connect
        self.database_cursor = cursor
        self.load_simulation()




        # Initialize economic data
        self.events = events
        self.dates = [self.current_date]
        self.gdp_data = [self.gdp]
        self.inflation_data = [self.inflation * 100]  # this is stored as a percentage
        self.unemployment_data = [self.unemployment]
        self.balance_of_payment_data = [self.balance_of_payment]
        self.budget_data = [self.budget]
        # Create a boolean variable to track the pause state
        self.paused = False

        self.last_policy_application_time = time.time()
        self.policy_cooldown_duration = 60  # Set the cooldown duration in seconds

        # Initialize event frame
        self.event_frame = tk.Frame(root, bg="white", bd=5)
        self.event_frame.place(relx=0.5, rely=0.8, relwidth=0.75, relheight=0.5, anchor="n")
        self.event_label = tk.Label(self.event_frame, font=('Courier', 12), anchor="nw", justify="left", bd=4)
        self.event_label.place(relwidth=1, relheight=1)


        # Create labels for economic data with left justification
        self.country_label = tk.Label(root, text="Libertas Stats")
        self.gdp_label = tk.Label(root, text=f"GDP: ${self.gdp:.2f} billion")
        self.inflation_label = tk.Label(root, text=f"Inflation: {self.inflation * 100:.2f}%")
        self.unemployment_label = tk.Label(root, text=f"Unemployment Rate: {self.unemployment:.2f}%")
        self.balance_of_payment_label = tk.Label(root, text=f"Balance of Payment: ${self.balance_of_payment:.2f} billion")
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

        # Create a policy tab
        self.policy_tab = ttk.Frame(root)
        self.policy_tab.pack(side="top", fill="both", expand=True)
        self.add_policy_tab()

        # Create a button to toggle between graphs
        root.bind('t', lambda event: self.switch_graph())
        root.bind('k', lambda event: self.toggle_pause())
        root.bind('p', lambda event: self.toggle_policy_tab())
        root.bind('s', lambda event: self.toggle_music())
        root.bind('g', lambda event: self.toggle_graph())






        # Place widgets on the screen
        self.gdp_label.pack()
        self.inflation_label.pack()
        self.unemployment_label.pack()
        self.balance_of_payment_label.pack()
        self.budget_label.pack()
        self.canvas_widget_gdp.pack_forget()
        self.canvas_widget_inflation.pack_forget()  # Hide the inflation graph initially
        self.canvas_widget_unemployment.pack_forget()  # Hide the unemployment graph initially
        self.canvas_widget_balance_of_payment.pack_forget()  # Hide the balance of payment graph initially
        self.canvas_widget_budget.pack_forget()  # Hide the budget graph initially

        # Start automatic updates
        self.update_economic_data()
        # Schedule the first event
        self.schedule_event()

    def __del__(self):
        # Close the database connection when the instance is deleted
        self.database_connection.close()

    def toggle_pause(self):
        # Toggle the pause state
        self.paused = not self.paused
        # Check if the simulation is paused
        if not self.paused:
            # Schedule the next update after 750 milliseconds (monthly)
            self.root.after(750, self.update_economic_data)

    def toggle_music(self):
        if pygame.mixer_music.get_busy():
            pygame.mixer_music.pause()
        else:
            pygame.mixer_music.unpause()



    def update_economic_data(self): # this is the method that allows for constant updates of graphs
        # normal distribution is used to simulate the economy
        self.gdp_growth_factor = np.random.normal(1.002, 0.02)
        self.gdp *= self.gdp_growth_factor
        self.inflation = np.random.normal(0.02, 0.009)
        self.unemployment = np.random.normal(4.5, 0.5)
        self.balance_of_payment = np.random.normal(0, 3)
        self.current_date += timedelta(days=30)  # Increment the current date of simulation

        # Simulate conflicts between economic indicators
        self.inflation += self.gdp_growth_factor * 0.03  # Inflation increases with GDP growth
        self.balance_of_payment += 0.5 * (self.gdp_growth_factor - 1)  # Balance of Payment improves with GDP growth
        # Simulate the inverse relationship between inflation and unemployment (Phillips curve)
        self.unemployment -= 0.05 * (self.inflation - 2)

        # Simulate the feedback loop between unemployment and economic growth
        self.gdp_growth_factor -= 0.01 * self.unemployment  # Economic growth decreases with higher unemployment

        # Ensure indicators don't go below zero
        self.inflation = max(0, self.inflation)
        self.unemployment = max(0, self.unemployment)
        self.balance_of_payment = max(0, self.balance_of_payment)
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

        # Check if the year has changed
        if self.current_date.year > self.dates[-2].year:
            # Save economic data to the database
            self.save_simulation_state_to_database()

        # Check if the simulation is paused
        if not self.paused:
            # Schedule the next update after 750 milliseconds (monthly)
            self.root.after(20, self.update_economic_data)

    def switch_graph(self):
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

    def toggle_graph(self):
        if self.canvas_widget_gdp.winfo_ismapped():
            self.canvas_widget_gdp.pack_forget()
            self.canvas_widget_inflation.pack_forget()
            self.canvas_widget_unemployment.pack_forget()
            self.canvas_widget_balance_of_payment.pack_forget()
            self.canvas_widget_budget.pack_forget()
        else:
            self.canvas_widget_gdp.pack()
            # Adjust the following lines accordingly based on your desired default graph
            self.canvas_widget_inflation.pack_forget()
            self.canvas_widget_unemployment.pack_forget()
            self.canvas_widget_balance_of_payment.pack_forget()
            self.canvas_widget_budget.pack_forget()


    def schedule_event(self):
        # Select a random event
        event = random.choice(self.events)

        # Schedule a single event occurrence with a random time delay between 10 seconds and 1 minute
        delay_time = random.uniform(10, 60) * 1000  # Convert seconds to milliseconds
        self.root.after(int(delay_time), lambda: self.apply_events(event))

    def apply_events(self, event):
        # Display event information on the frame for 5 seconds

        # Bring the event frame to the top
        self.event_frame.lift()

        # Clear event text and lower the frame after 5 seconds
        self.root.after(5000, lambda: [self.event_label.config(text=""), self.event_frame.lower()])

        # Apply the outcome to the corresponding economic indicator
        for outcome in event.outcomes:  # Assuming the attribute is named 'outcomes'
            if outcome.effect_type == "GDP":
                print(f"Old GDP: {self.gdp}")
                self.gdp *= (1 + outcome.magnitude)
                print(f"new GDP: {self.gdp}")
            elif outcome.effect_type == "Inflation":
                print(f"old inflation: {self.inflation}")
                self.inflation += outcome.magnitude
                print(f"new inflation: {self.inflation}")
            elif outcome.effect_type == "Unemployment":
                print(f"old unemployment: {self.unemployment}")
                self.unemployment += outcome.magnitude
                print(f"new unemployment: {self.unemployment}")
            elif outcome.effect_type == "Balance of Payment":
                print(f"old balance of payment: {self.balance_of_payment}")
                self.balance_of_payment += outcome.magnitude
                print(f"new balance of payment: {self.balance_of_payment}")
            elif outcome.effect_type == "Budget":
                print(f"old budget: {self.budget}")
                self.budget += outcome.magnitude
                print(f"new budget: {self.balance_of_payment}")

        self.show_event(event.name, event.description, self.current_date)


        # Schedule the next event
        self.schedule_event()

    def add_policy_tab(self):
        # Create and set up the Combobox for policy selection
        self.policy_combobox = ttk.Combobox(self.policy_tab, values=[policy.name for policy in policy_instances])
        self.policy_combobox.pack(pady=20)

        # Create a button to apply the selected policy
        apply_policy_button = ttk.Button(self.policy_tab, text="Apply Policy", command=self.apply_selected_policy)
        apply_policy_button.pack(pady=10)

    def toggle_policy_tab(self):
        # Toggle the visibility of the policy tab
        if self.policy_tab.winfo_ismapped():
            self.policy_tab.pack_forget()
        else:
            self.policy_tab.lift()
            self.policy_tab.pack(fill="both", expand=True)

    def apply_selected_policy(self):
        selected_policy_name = self.policy_combobox.get()
        selected_policy = next((policy for policy in policy_instances if policy.name == selected_policy_name), None)

        if selected_policy:
            # Apply the selected policy
            self.apply_policy(selected_policy)

    def apply_policy(self, policy):
        # Check if the simulator has enough budget to implement the policy
        if policy.cost > self.budget:
            print(f"Not enough budget to implement {policy.name}. cost = {policy.cost}\nbudget = {self.budget}")
            return


        # Deduct the cost from the budget
        self.budget -= policy.cost

        # Update economic indicators based on policy outcomes
        for outcome in policy.outcomes:
            if "effect_type" in outcome:
                effect_type = outcome["effect_type"]

                if effect_type == "GDP":
                    print(f"Old GDP: {self.gdp}")
                    self.gdp *= (1 + outcome["magnitude"])
                    print(f"new GDP: {self.gdp}")
                elif effect_type == "Inflation":
                    print(f"old inflation: {self.inflation}")
                    self.inflation += outcome["magnitude"]
                    print(f"new inflation: {self.inflation}")
                elif effect_type == "Unemployment":
                    print(f"old unemployment: {self.unemployment}")
                    self.unemployment += outcome["magnitude"]
                    print(f"new unemployment: {self.unemployment}")
                elif effect_type == "Balance of Payment":
                    print(f"old balance of payment: {self.balance_of_payment}")
                    self.balance_of_payment += outcome["magnitude"]
                    print(f"new balance of payment: {self.balance_of_payment}")
                elif effect_type == "Budget":
                    print(f"old budget: {self.budget}")
                    self.budget += outcome["magnitude"]
                    print(f"new budget: {self.balance_of_payment}")




    def show_event(self, date, title, description):
        # Display event with date in newspaper style
        event_text = f"{date}\n\n{title}\n\n{description}"
        self.event_label.config(text=event_text)

    def save_simulation_state_to_database(self):
        try:
            simulation_state = {
                'current_date': str(self.current_date),
                'gdp': self.gdp,
                'inflation': self.inflation,
                'unemployment': self.unemployment,
                'balance_of_payment': self.balance_of_payment,
                'budget': self.budget,
                # Add any other relevant simulation state data
            }
            serialized_state = json.dumps(simulation_state)

            # Insert the simulation state into the tblSimulationState table
            self.database_cursor.execute("""
                INSERT INTO tblSimulationState (user_id, saved_state, timestamp)
                VALUES (?, ?, ?)
            """, (self.user_id, serialized_state, int(time.time())))

            self.database_connection.commit()

            print(f"Simulation state for year: {self.current_date} saved to the database.")

        except sqlite3.Error as error:
            print(f"Error saving simulation state to the database: {error}")

    def load_simulation(self):
        # Use self.user_id to load the simulation
        saved_state = load_simulation_state(self, self.user_id)
        if saved_state:
            # Load the simulation state
            self.set_simulation_state(saved_state)
        else:
            messagebox.showinfo("No Saved Simulation", "No saved simulation found. Starting a new simulation.",
                                parent=self.root)
            self.start_new_simulation()

    def start_new_simulation(self):
        # Initialize a new simulation state
        self.initialize_simulation()


    def set_simulation_state(self, state):
        # Set the simulation state based on the loaded data
        self.gdp = state.get("gdp", 1000.0)
        self.inflation = state.get("inflation", 0.03)
        self.unemployment = state.get("unemployment", 5.0)
        self.balance_of_payment = state.get("balance_of_payment", 0)
        self.budget = state.get("budget", 10000.0)
        self.current_date = state.get("current_date", datetime(2023, 1, 1))
        self.dates = state.get("dates", [self.current_date])
        self.gdp_data = state.get("gdp_data", [self.gdp])
        self.inflation_data = state.get("inflation_data", [self.inflation * 100])
        self.unemployment_data = state.get("unemployment_data", [self.unemployment])
        self.balance_of_payment_data = state.get("balance_of_payment_data", [self.balance_of_payment])
        self.budget_data = state.get("budget_data", [self.budget])
        self.paused = state.get("paused", False)

    def initialize_simulation(self):
        # Initialize the simulation with default values
        self.gdp = 1000.0
        self.inflation = 0.03
        self.unemployment = 5.0
        self.balance_of_payment = 0
        self.budget = 10000.0
        self.current_date = datetime(2023, 1, 1)
        self.dates = [self.current_date]
        self.gdp_data = [self.gdp]
        self.inflation_data = [self.inflation * 100]
        self.unemployment_data = [self.unemployment]
        self.balance_of_payment_data = [self.balance_of_payment]
        self.budget_data = [self.budget]
        self.paused = False




def main():
    root = tk.Tk()
    user_id = 12345
    app = EconomicSimulatorGraphs(root, user_id)
    root.mainloop()

main()