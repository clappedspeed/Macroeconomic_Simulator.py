# This is the policy file
# This is for the policy class and policy list


class Policy:
    # Only a string method as the actual methods would be in main simulation class
    def __init__(self, **kwargs):
        self.name = kwargs.get("name", "")
        self.description = kwargs.get("description", "")
        self.cost = kwargs.get("cost", 0)  # Include a cost attribute
        self.outcomes = kwargs.get("outcomes", [])

    def __str__(self):
        return f"Policy: {self.name}\nDescription: {self.description}\nCost: ${self.cost} million\nImpact: {self.outcomes}"


# List of Dictionaries containing policies
policy_list = [
    {
        "name": "Tax Reform",
        "description": "Implement tax reforms to stimulate the economy",
        "cost": 500,
        "outcomes": [
            {"effect_type": "GDP", "description": "Increase GDP", "magnitude": 0.05, "duration": 12},
            {"effect_type": "Inflation", "description": "Increase Inflation", "magnitude": 0.02, "duration": 6},
            {"effect_type": "Unemployment", "description": "Potential increase in work incentive", "magnitude": -0.02, "duration": 8},
            {"effect_type": "Balance of Payments", "description": "Trade balance impact", "magnitude": 0.03, "duration": 10},
            {"effect_type": "Budget", "description": "Government budget impact", "magnitude": -0.02, "duration": 8},
        ],
    },
    {
        "name": "Infrastructure Investment",
        "description": "Invest in infrastructure for economic growth",
        "cost": 1000,
        "outcomes": [
            {"effect_type": "Unemployment", "description": "Reduce Unemployment", "magnitude": -0.03, "duration": 8},
            {"effect_type": "Budget", "description": "Decreases Budget", "magnitude": -0.2, "duration": 12},
            {"effect_type": "Balance of Payments", "description": "Infrastructure-related trade impact", "magnitude": -0.01, "duration": 10},
            {"effect_type": "GDP", "description": "Potential increase in economic activity", "magnitude": 0.02, "duration": 15},
            {"effect_type": "Inflation", "description": "Potential impact on inflation", "magnitude": -0.01, "duration": 6},
        ],
    },
    {
        "name": "Education Enhancement",
        "description": "Increase spending on education for long-term economic development",
        "cost": 800,
        "outcomes": [
            {"effect_type": "GDP", "description": "Sustainable GDP growth", "magnitude": 0.03, "duration": 18},
            {"effect_type": "Unemployment", "description": "Skilled workforce, lower unemployment", "magnitude": -0.02, "duration": 12},
            {"effect_type": "Balance of Payments", "description": "Education sector impact on trade", "magnitude": 0.01, "duration": 8},
            {"effect_type": "Budget", "description": "Education spending impact on government budget", "magnitude": -0.02, "duration": 10},
            {"effect_type": "Inflation", "description": "Potential impact on inflation", "magnitude": 0.01, "duration": 8},
        ],
    },
    {
        "name": "Healthcare Expansion",
        "description": "Expand healthcare services for a healthier workforce",
        "cost": 1200,
        "outcomes": [
            {"effect_type": "GDP", "description": "Improved worker productivity", "magnitude": 0.02, "duration": 12},
            {"effect_type": "Inflation", "description": "Potential healthcare cost inflation", "magnitude": 0.03, "duration": 8},
            {"effect_type": "Unemployment", "description": "Healthcare sector impact on job market", "magnitude": -0.01, "duration": 10},
            {"effect_type": "Balance of Payments", "description": "Healthcare-related trade impact", "magnitude": -0.02, "duration": 8},
            {"effect_type": "Budget", "description": "Government budget impact", "magnitude": -0.01, "duration": 6},
        ],
    },
    {
        "name": "Trade Liberalization",
        "description": "Open up markets to international trade",
        "cost": 200,
        "outcomes": [
            {"effect_type": "GDP", "description": "Increased economic activity", "magnitude": 0.03, "duration": 10},
            {"effect_type": "Unemployment", "description": "Job displacement in certain sectors", "magnitude": 0.02, "duration": 8},
            {"effect_type": "Balance of Payments", "description": "Trade liberalization impact on trade balance", "magnitude": 0.05, "duration": 12},
            {"effect_type": "Budget", "description": "Trade liberalization impact on government budget", "magnitude": 0.01, "duration": 8},
            {"effect_type": "Inflation", "description": "Potential impact on inflation", "magnitude": 0.01, "duration": 6},
        ],
    },
    {
        "name": "Agricultural Subsidies",
        "description": "Subsidize the agricultural sector to support farmers",
        "cost": 600,
        "outcomes": [
            {"effect_type": "GDP", "description": "Stabilize rural economy", "magnitude": 0.02, "duration": 12},
            {"effect_type": "Inflation", "description": "Potential food price decrease", "magnitude": -0.01, "duration": 6},
            {"effect_type": "Unemployment", "description": "Agricultural sector impact on job market", "magnitude": -0.01, "duration": 10},
            {"effect_type": "Balance of Payments", "description": "Agricultural sector impact on trade balance", "magnitude": 0.03, "duration": 8},
            {"effect_type": "Budget", "description": "Government budget impact", "magnitude": -0.01, "duration": 8},
        ],
    },
    {
        "name": "Technology Innovation",
        "description": "Invest in research and development for technological innovation",
        "cost": 1200,
        "outcomes": [
            {"effect_type": "GDP", "description": "Stimulate high-tech industries", "magnitude": 0.04, "duration": 15},
            {"effect_type": "Unemployment", "description": "Job creation in technology sector", "magnitude": -0.03, "duration": 10},
            {"effect_type": "Balance of Payments", "description": "Technology innovation impact on trade", "magnitude": 0.02, "duration": 12},
            {"effect_type": "Budget", "description": "Government budget impact", "magnitude": -0.01, "duration": 8},
            {"effect_type": "Inflation", "description": "Potential impact on inflation", "magnitude": -0.05, "duration": 6},
        ],
    },
    {
        "name": "Housing Affordability",
        "description": "Implement policies to make housing more affordable",
        "cost": 1000,
        "outcomes": [
            {"effect_type": "GDP", "description": "Stimulate construction industry", "magnitude": 0.02, "duration": 12},
            {"effect_type": "Inflation", "description": "Potential real estate price inflation", "magnitude": 0.01, "duration": 8},
            {"effect_type": "Unemployment", "description": "Housing sector impact on job market", "magnitude": -0.02, "duration": 10},
            {"effect_type": "Balance of Payments", "description": "Housing affordability impact on trade balance", "magnitude": 0.01, "duration": 6},
            {"effect_type": "Budget", "description": "Government budget impact", "magnitude": 0.02, "duration": 8},
        ],
    },
    {
        "name": "Monetary Policy",
        "description": "Adjust interest rates to control inflation and stimulate growth",
        "cost": 1500,
        "outcomes": [
            {"effect_type": "GDP", "description": "Influence borrowing and spending", "magnitude": 0.03, "duration": 10},
            {"effect_type": "Inflation", "description": "Control inflation through interest rates", "magnitude": -0.02, "duration": 8},
            {"effect_type": "Balance of Payments", "description": "Monetary policy impact on trade balance", "magnitude": -0.01, "duration": 12},
            {"effect_type": "Budget", "description": "Government budget impact", "magnitude": 0.02, "duration": 6},
            {"effect_type": "Unemployment", "description": "Potential impact on job market", "magnitude": 0.01, "duration": 8},
        ],
    },
    {
        "name": "Labor Market Reforms",
        "description": "Introduce reforms to make the labor market more flexible",
        "cost": 100,
        "outcomes": [
            {"effect_type": "Unemployment", "description": "Increase job market flexibility", "magnitude": -0.04, "duration": 12},
            {"effect_type": "GDP", "description": "Potential increase in job creation", "magnitude": 0.03, "duration": 10},
            {"effect_type": "Balance of Payments", "description": "Labor market reforms impact on trade balance", "magnitude": 0.01, "duration": 8},
            {"effect_type": "Budget", "description": "Government budget impact", "magnitude": -0.01, "duration": 6},
            {"effect_type": "Inflation", "description": "Potential impact on inflation", "magnitude": 0.01, "duration": 8},
        ],
    },
    {
        "name": "Austerity Policy",
        "description": "Implement measures to reduce the national debt",
        "cost": -300,
        "outcomes": [
            {"effect_type": "Budget", "description": "Reduce government debt burden", "magnitude": 0.3, "duration": 12},
            {"effect_type": "GDP", "description": "High tax reduces demand", "magnitude": -0.2, "duration": 8},
            {"effect_type": "Balance of Payments", "description": "National debt reduction impact on trade balance", "magnitude": 0.01, "duration": 10},
            {"effect_type": "Unemployment", "description": "Potential impact on job market", "magnitude": 0.01, "duration": 8},
            {"effect_type": "Inflation", "description": "Potential impact on inflation", "magnitude": 0.01, "duration": 10},
        ],
    },
    {
        "name": "Social Welfare Expansion",
        "description": "Expand social welfare programs for citizen well-being",
        "cost": 800,
        "outcomes": [
            {"effect_type": "GDP", "description": "Potential increase in consumer spending", "magnitude": 0.02, "duration": 10},
            {"effect_type": "Unemployment", "description": "Potential decrease in poverty-related unemployment", "magnitude": -0.02, "duration": 8},
            {"effect_type": "Balance of Payments", "description": "Social welfare expansion impact on trade balance", "magnitude": -0.01, "duration": 12},
            {"effect_type": "Budget", "description": "Government budget impact", "magnitude": 0.04, "duration": 6},
            {"effect_type": "Inflation", "description": "Potential impact on inflation", "magnitude": 0.01, "duration": 8},
        ],
    },
    {
        "name": "Interest-Free Loans",
        "description": "Introduce interest-free loans to stimulate borrowing",
        "cost": 1100,
        "outcomes": [
            {"effect_type": "GDP", "description": "Encourage investment and spending", "magnitude": 0.03, "duration": 12},
            {"effect_type": "Inflation", "description": "Potential increase in demand and prices", "magnitude": 0.02, "duration": 8},
            {"effect_type": "Balance of Payments", "description": "Interest-free loans impact on trade balance", "magnitude": 0.02, "duration": 10},
            {"effect_type": "Budget", "description": "Government budget impact", "magnitude": -0.01, "duration": 6},
            {"effect_type": "Unemployment", "description": "Potential impact on job market", "magnitude": 0.01, "duration": 8},
        ],
    },
    {
        "name": "Central Bank Independence",
        "description": "Strengthen the independence of the central bank",
        "cost": 900,
        "outcomes": [
            {"effect_type": "GDP", "description": "Build investor confidence", "magnitude": 0.02, "duration": 10},
            {"effect_type": "Inflation", "description": "Potential stability in monetary policy", "magnitude": -0.01, "duration": 8},
            {"effect_type": "Balance of Payments", "description": "Central bank independence impact on trade balance", "magnitude": 0.01, "duration": 12},
            {"effect_type": "Budget", "description": "Government budget impact", "magnitude": -0.01, "duration": 6},
            {"effect_type": "Unemployment", "description": "Potential impact on job market", "magnitude": 0.01, "duration": 8},
        ],
    },
    {
        "name": "Quantitative Easing",
        "description": "Implement quantitative easing to increase money supply",
        "cost": 1500,
        "outcomes": [
            {"effect_type": "GDP", "description": "Boost in economic activity", "magnitude": 0.04, "duration": 15},
            {"effect_type": "Inflation", "description": "Potential inflation in monetary policy", "magnitude": 0.09, "duration": 8},
            {"effect_type": "Balance of Payments", "description": "Central bank independence impact on trade balance", "magnitude": 0.01, "duration": 12},
            {"effect_type": "Budget", "description": "Government budget impact", "magnitude": -0.01, "duration": 6},
            {"effect_type": "Unemployment", "description": "Potential impact on job market", "magnitude": 0.01, "duration": 8},
        ],
    }]

# Convert policy dictionaries to Policy instances
policy_instances = [Policy(**policy) for policy in policy_list]
