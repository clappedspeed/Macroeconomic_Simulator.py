import random

class Outcome:
    def __init__(self, effect_type, description, magnitude, duration):
        self.effect_type = effect_type
        self.description = description
        self.magnitude = magnitude
        self.duration = duration

    def __str__(self):
        return f"Outcome: {self.description} ({self.effect_type}), Magnitude: {self.magnitude}, Duration: {self.duration} days"

class Event:
    def __init__(self, name, description, outcomes, impact, probability):
        self.name = name
        self.description = description
        self.outcomes = outcomes  # List of Outcome instances
        self.impact = impact
        self.probability = probability

    def apply_event(self, economic_indicator):
        for outcome in self.outcomes:
            economic_indicator.value *= (1 + outcome.magnitude)

    def __str__(self):
        return f"Event: {self.name}\nDescription: {self.description}\nImpact: {self.impact}\nProbability: {self.probability}"

    def should_occur(self):
        return random.random() < self.probability

# Data of all events
events_data = [
    {
        "name": "Global Pandemic",
        "description": "A worldwide health crisis affecting economic activity.",
        "outcomes": [
            {"effect_type": "GDP", "description": "Global health crisis", "magnitude": -0.05, "duration": 365},
            {"effect_type": "Inflation", "description": "Increased healthcare costs", "magnitude": 0.02, "duration": 365},
            {"effect_type": "Unemployment", "description": "Job losses due to economic downturn", "magnitude": 2.0, "duration": 365},
        ],
        "impact": 0.05,
        "probability": 0.1,
    },
    {
        "name": "Technological Innovation",
        "description": "A breakthrough in technology leading to increased productivity.",
        "outcomes": [
            {"effect_type": "GDP", "description": "Increased productivity", "magnitude": 0.03, "duration": 180},
            {"effect_type": "Inflation", "description": "Decreased costs of technology", "magnitude": -0.01, "duration": 180},
            {"effect_type": "Unemployment", "description": "Shifts in employment due to automation", "magnitude": -1.5, "duration": 180},
        ],
        "impact": 0.03,
        "probability": 0.15,
    },
    {
        "name": "Financial Crisis",
        "description": "A Bubble burst in the housing markets affecting economic stability.",
        "outcomes": [
            {"effect_type": "GDP", "description": "Economic contraction", "magnitude": -0.08, "duration": 365},
            {"effect_type": "Inflation", "description": "Increased uncertainty leading to inflation", "magnitude": 0.05, "duration": 365},
            {"effect_type": "Unemployment", "description": "Higher job losses in financial sectors", "magnitude": 3.0, "duration": 365},
        ],
        "impact": 0.08,
        "probability": 0.05,
    },
    {
        "name": "Natural Disaster",
        "description": "A major flood causing widespread damage and economic losses.",
        "outcomes": [
            {"effect_type": "GDP", "description": "Economic losses due to destruction", "magnitude": -0.04, "duration": 180},
            {"effect_type": "Inflation", "description": "Increased costs of rebuilding", "magnitude": 0.03, "duration": 180},
            {"effect_type": "Unemployment", "description": "Job losses in affected regions", "magnitude": 1.5, "duration": 180},
        ],
        "impact": 0.04,
        "probability": 0.1,
    },
    {
        "name": "Government Stimulus",
        "description": "An increase in government spending to boost economic activity.",
        "outcomes": [
            {"effect_type": "GDP", "description": "Economic expansion", "magnitude": 0.06, "duration": 365},
            {"effect_type": "Inflation", "description": "Potential inflation due to increased demand", "magnitude": 0.02, "duration": 365},
            {"effect_type": "Unemployment", "description": "Job creation and lower unemployment", "magnitude": -1.0, "duration": 365},
        ],
        "impact": 0.06,
        "probability": 0.2,
    },
    {
        "name": "Tarrif Reductions",
        "description": "A new international trade deal increases imports and overall global trade.",
        "outcomes": [
            {"effect_type": "GDP", "description": "Increased international trade", "magnitude": 0.04, "duration": 180},
            {"effect_type": "Inflation", "description": "Potential decrease in import costs", "magnitude": -0.01, "duration": 180},
            {"effect_type": "Unemployment", "description": "Job creation in export-oriented industries", "magnitude": -0.5, "duration": 180},
        ],
        "impact": 0.04,
        "probability": 0.15,
    },
    {
        "name": "Oil Price Shock",
        "description": "A significant change in oil prices affecting energy-dependent industries.",
        "outcomes": [
            {"effect_type": "GDP", "description": "Impact on energy-dependent sectors", "magnitude": -0.02, "duration": 90},
            {"effect_type": "Inflation", "description": "Changes in fuel costs affecting prices", "magnitude": 0.03, "duration": 90},
            {"effect_type": "Unemployment", "description": "Job losses in energy-related jobs", "magnitude": 1.0, "duration": 90},
        ],
        "impact": 0.02,
        "probability": 0.1,
    },
    {
        "name": "Population Growth",
        "description": "A surge in population leading to increased demand for goods and services.",
        "outcomes": [
            {"effect_type": "GDP", "description": "Higher consumer demand", "magnitude": 0.02, "duration": 180},
            {"effect_type": "Inflation", "description": "Potential inflation due to increased demand", "magnitude": 0.01, "duration": 180},
            {"effect_type": "Unemployment", "description": "Job creation to meet increased demand", "magnitude": -0.5, "duration": 180},
        ],
        "impact": 0.02,
        "probability": 0.15,
    },
    {
        "name": "Reduction in Economic Condidence",
        "description": "Bearish animal spirits and speculations reduces consumer and business confidence.",
        "outcomes": [
            {"effect_type": "GDP", "description": "Investor caution leading to economic slowdown", "magnitude": -0.03, "duration": 120},
            {"effect_type": "Inflation", "description": "Increased uncertainty affecting prices", "magnitude": 0.02, "duration": 120},
            {"effect_type": "Unemployment", "description": "Job losses due to decreased business investment", "magnitude": 1.5, "duration": 120},
        ],
        "impact": 0.03,
        "probability": 0.1,
    },
    {
        "name": "Climate Policy Implementation",
        "description": "Government policies to address climate change affecting industries.",
        "outcomes": [
            {"effect_type": "GDP", "description": "Transition to green industries", "magnitude": 0.04, "duration": 240},
            {"effect_type": "Inflation", "description": "Costs of transitioning to green technologies", "magnitude": -0.01, "duration": 240},
            {"effect_type": "Unemployment", "description": "Job creation in renewable energy sectors", "magnitude": -1.0, "duration": 240},
        ],
        "impact": 0.04,
        "probability": 0.1,
    },
    {
        "name": "Currency Devaluation",
        "description": "A decrease in the value of the national currency affecting international trade.",
        "outcomes": [
            {"effect_type": "GDP", "description": "Boost in exports due to favorable exchange rates", "magnitude": 0.02, "duration": 90},
            {"effect_type": "Inflation", "description": "Increased costs of imported goods", "magnitude": 0.01, "duration": 90},
            {"effect_type": "Unemployment", "description": "Potential job losses in import-dependent sectors", "magnitude": 0.5, "duration": 90},
        ],
        "impact": 0.02,
        "probability": 0.12,
    },
    {
        "name": "Healthcare Innovation",
        "description": "Breakthroughs in healthcare technology leading to improved health outcomes.",
        "outcomes": [
            {"effect_type": "Health", "description": "Improved health outcomes", "magnitude": 0.04, "duration": 180},
            {"effect_type": "Inflation", "description": "Increased costs of advanced healthcare", "magnitude": 0.02, "duration": 180},
            {"effect_type": "Unemployment", "description": "Job creation in healthcare and technology sectors", "magnitude": -0.8, "duration": 180},
        ],
        "impact": 0.04,
        "probability": 0.15,
    },
    {
        "name": "Global Trade Agreements",
        "description": "Agreements to reduce trade barriers and promote international cooperation.",
        "outcomes": [
            {"effect_type": "GDP", "description": "Increased international trade", "magnitude": 0.03, "duration": 180},
            {"effect_type": "Inflation", "description": "Potential decrease in import costs", "magnitude": -0.02, "duration": 180},
            {"effect_type": "Unemployment", "description": "Job creation in export-oriented industries", "magnitude": -0.7, "duration": 180},
        ],
        "impact": 0.03,
        "probability": 0.18,
    },
    {
        "name": "Education Reform",
        "description": "Government initiatives to enhance education impacting long-term workforce skills.",
        "outcomes": [
            {"effect_type": "GDP", "description": "Increased productivity due to skilled workforce", "magnitude": 0.02, "duration": 240},
            {"effect_type": "Inflation", "description": "Potential decrease in training costs for businesses", "magnitude": -0.01, "duration": 240},
            {"effect_type": "Unemployment", "description": "Job creation due to skilled workforce", "magnitude": -1.0, "duration": 240},
        ],
        "impact": 0.02,
        "probability": 0.15,
    },
    {
        "name": "Global Trade Tensions",
        "description": "Escalation in trade disputes impacting international commerce.",
        "outcomes": [
            {"effect_type": "GDP", "description": "Economic slowdown due to reduced trade", "magnitude": -0.03, "duration": 120},
            {"effect_type": "Inflation", "description": "Increased costs of imported goods", "magnitude": 0.02, "duration": 120},
            {"effect_type": "Unemployment", "description": "Job losses in export-oriented industries", "magnitude": 1.0, "duration": 120},
        ],
        "impact": 0.03,
        "probability": 0.12,
    },
    {
        "name": "Automation Implementation",
        "description": "Increased use of automation affecting employment patterns.",
        "outcomes": [
            {"effect_type": "GDP", "description": "Productivity gains through automation", "magnitude": 0.01, "duration": 180},
            {"effect_type": "Inflation", "description": "Decreased labor costs affecting prices", "magnitude": -0.01, "duration": 180},
            {"effect_type": "Unemployment", "description": "Job losses in manual labor sectors", "magnitude": 0.5, "duration": 180},
        ],
        "impact": 0.01,
        "probability": 0.2,
    },
]

events = [Event(event["name"], event["description"], [Outcome(**outcome) for outcome in event["outcomes"]],
                event["impact"], event["probability"]) for event in events_data]


class EconomicIndicator:
    def __init__(self, gdp, inflation, unemployment, balance_of_payment, budget):
        self.gdp = gdp
        self.inflation = inflation
        self.unemployment = unemployment
        self.balance_of_payment = balance_of_payment
        self.budget = budget

    def apply_event(self, event):
        for outcome in event.outcomes:
            if outcome.effect_type == "GDP":
                self.gdp *= (1 + outcome.magnitude)
            elif outcome.effect_type == "Inflation":
                self.inflation *= (1 + outcome.magnitude)
            elif outcome.effect_type == "Unemployment":
                self.unemployment *= (1 + outcome.magnitude)
            elif outcome.effect_type == "Balance of Payment":
                self.balance_of_payment *= (1 + outcome.magnitude)
            elif outcome.effect_type == "Budget":
                self.budget *= (1 + outcome.magnitude)

    def __str__(self):
        return f"GDP: {self.gdp}, Inflation: {self.inflation}%, Unemployment: {self.unemployment}%, " \
               f"Balance of Payment: {self.balance_of_payment}, Budget: {self.budget}"

# Example usage
economic_indicator = EconomicIndicator(1000, 2, 5, 500, 300)
print("Initial Economic Indicators:")
print(economic_indicator)

# (Previous code...)



# Test all events
for event in events:
    if event.should_occur():
        print(f"\nApplying Event: {event.name}")
        print(f"Event Description: {event.description}")
        event.apply_event(economic_indicator)
        print("Updated Economic Indicators:")
        print(economic_indicator)
    else:
        print(f"\nEvent {event.name} did not occur.")




