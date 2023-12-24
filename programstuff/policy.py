class Policy:
    def __init__(self, **kwargs):
        self.name = kwargs.get("name", "")
        self.description = kwargs.get("description", "")
        self.cost = kwargs.get("cost", 0)  # Include a cost attribute
        self.outcomes = kwargs.get("outcomes", [])

    def __str__(self):
        return f"Policy: {self.name}\nDescription: {self.description}\nCost: ${self.cost} million\nImpact: {self.outcomes}"



policy_list = [
    {
        "name": "Tax Reform",
        "description": "Implement tax reforms to stimulate the economy",
        "cost": 500,  # in millions
        "outcomes": [
            {"effect_type": "GDP", "description": "Increase GDP", "magnitude": 0.05, "duration": 12},
            {"effect_type": "Inflation", "description": "Increase Inflation", "magnitude": 0.02, "duration": 6},
        ],
    },
    {
        "name": "Infrastructure Investment",
        "description": "Invest in infrastructure for economic growth",
        "cost": 1000,  # in millions
        "outcomes": [
            {"effect_type": "Unemployment", "description": "Reduce Unemployment", "magnitude": -0.03, "duration": 8},
            {"effect_type": "Budget", "description": "Increase Budget", "magnitude": 0.1, "duration": 12},
        ],
    },
    {
        "name": "Education Enhancement",
        "description": "Increase spending on education for long-term economic development",
        "cost": 800,  # in millions
        "outcomes": [
            {"effect_type": "GDP", "description": "Sustainable GDP growth", "magnitude": 0.03, "duration": 18},
            {"effect_type": "Unemployment", "description": "Skilled workforce, lower unemployment", "magnitude": -0.02, "duration": 12},
        ],
    },
    {
        "name": "Healthcare Expansion",
        "description": "Expand healthcare services for a healthier workforce",
        "cost": 1200,  # in millions
        "outcomes": [
            {"effect_type": "GDP", "description": "Improved worker productivity", "magnitude": 0.02, "duration": 12},
            {"effect_type": "Inflation", "description": "Potential healthcare cost inflation", "magnitude": 0.03, "duration": 8},
        ],
    },
    {
        "name": "Green Energy Initiative",
        "description": "Promote the transition to sustainable energy sources",
        "cost": 1500,  # in millions
        "outcomes": [
            {"effect_type": "GDP", "description": "Boost in green energy sector", "magnitude": 0.04, "duration": 15},
            {"effect_type": "Inflation", "description": "Initial costs for green technology", "magnitude": 0.01, "duration": 6},
        ],
    },
    {
        "name": "Trade Liberalization",
        "description": "Open up markets to international trade",
        "cost": 1200,  # in millions
        "outcomes": [
            {"effect_type": "GDP", "description": "Increased economic activity", "magnitude": 0.03, "duration": 10},
            {"effect_type": "Unemployment", "description": "Job displacement in certain sectors", "magnitude": 0.02, "duration": 8},
        ],
    },
    {
        "name": "Agricultural Subsidies",
        "description": "Subsidize the agricultural sector to support farmers",
        "cost": 800,  # in millions
        "outcomes": [
            {"effect_type": "GDP", "description": "Stabilize rural economy", "magnitude": 0.02, "duration": 12},
            {"effect_type": "Inflation", "description": "Potential food price inflation", "magnitude": 0.01, "duration": 6},
        ],
    },
    {
        "name": "Technology Innovation",
        "description": "Invest in research and development for technological innovation",
        "cost": 1800,  # in millions
        "outcomes": [
            {"effect_type": "GDP", "description": "Stimulate high-tech industries", "magnitude": 0.04, "duration": 15},
            {"effect_type": "Unemployment", "description": "Job creation in technology sector", "magnitude": -0.03, "duration": 10},
        ],
    },
    {
        "name": "Housing Affordability",
        "description": "Implement policies to make housing more affordable",
        "cost": 1000,  # in millions
        "outcomes": [
            {"effect_type": "GDP", "description": "Stimulate construction industry", "magnitude": 0.02, "duration": 12},
            {"effect_type": "Inflation", "description": "Potential real estate price inflation", "magnitude": 0.01, "duration": 8},
        ],
    },
    {
        "name": "Monetary Policy",
        "description": "Adjust interest rates to control inflation and stimulate growth",
        "cost": 1500,  # in millions
        "outcomes": [
            {"effect_type": "GDP", "description": "Influence borrowing and spending", "magnitude": 0.03, "duration": 10},
            {"effect_type": "Inflation", "description": "Control inflation through interest rates", "magnitude": -0.02, "duration": 8},
        ],
    },
    {
        "name": "Labor Market Reforms",
        "description": "Introduce reforms to make the labor market more flexible",
        "cost": 1600,  # in millions
        "outcomes": [
            {"effect_type": "Unemployment", "description": "Increase job market flexibility", "magnitude": -0.04, "duration": 12},
            {"effect_type": "GDP", "description": "Potential increase in job creation", "magnitude": 0.03, "duration": 10},
        ],
    },
    {
        "name": "National Debt Reduction",
        "description": "Implement measures to reduce the national debt",
        "cost": 1200,  # in millions
        "outcomes": [
            {"effect_type": "Budget", "description": "Reduce government debt burden", "magnitude": -0.1, "duration": 12},
            {"effect_type": "GDP", "description": "Positive investor sentiment", "magnitude": 0.02, "duration": 8},
        ],
    },
    {
        "name": "Social Welfare Expansion",
        "description": "Expand social welfare programs for citizen well-being",
        "cost": 800,  # in millions
        "outcomes": [
            {"effect_type": "GDP", "description": "Potential increase in consumer spending", "magnitude": 0.02, "duration": 10},
            {"effect_type": "Unemployment", "description": "Potential decrease in poverty-related unemployment", "magnitude": -0.02, "duration": 8},
        ],
    },
    {
        "name": "Interest-Free Loans",
        "description": "Introduce interest-free loans to stimulate borrowing",
        "cost": 1400,  # in millions
        "outcomes": [
            {"effect_type": "GDP", "description": "Encourage investment and spending", "magnitude": 0.03, "duration": 12},
            {"effect_type": "Inflation", "description": "Potential increase in demand and prices", "magnitude": 0.02, "duration": 8},
        ],
    },
    {
        "name": "Central Bank Independence",
        "description": "Strengthen the independence of the central bank",
        "cost": 900,  # in millions
        "outcomes": [
            {"effect_type": "GDP", "description": "Build investor confidence", "magnitude": 0.02, "duration": 10},
            {"effect_type": "Inflation", "description": "Potential stability in monetary policy", "magnitude": -0.01, "duration": 8},
        ],
    },
    {
        "name": "Quantitative Easing",
        "description": "Implement quantitative easing to increase money supply",
        "cost": 2000,  # in millions
        "outcomes": [
            {"effect_type": "GDP", "description": "Boost in economic activity", "magnitude": 0.04, "duration": 15},
            {"effect_type": "Inflation", "description": "Potential inflation due to increased money supply", "magnitude": 0.03, "duration": 10},
        ],
    },
    {
        "name": "Inclusive Economic Policies",
        "description": "Promote policies that address income inequality",
        "cost": 1100,  # in millions
        "outcomes": [
            {"effect_type": "GDP", "description": "Potential increase in consumer base", "magnitude": 0.02, "duration": 12},
            {"effect_type": "Unemployment", "description": "Potential decrease in social unrest-related unemployment", "magnitude": -0.02, "duration": 8},
        ],
    },
    {
        "name": "Deficit Spending",
        "description": "Engage in deficit spending to stimulate economic growth",
        "cost": 1500,  # in millions
        "outcomes": [
            {"effect_type": "GDP", "description": "Increase in government spending", "magnitude": 0.05, "duration": 12},
            {"effect_type": "Budget", "description": "Potential increase in government debt", "magnitude": 0.1, "duration": 8},
        ],
    },
    {
        "name": "Currency Devaluation",
        "description": "Devalue the national currency to boost exports",
        "cost": 1300,  # in millions
        "outcomes": [
            {"effect_type": "GDP", "description": "Competitive advantage in international trade", "magnitude": 0.03, "duration": 10},
            {"effect_type": "Unemployment", "description": "Potential job creation in export-oriented sectors", "magnitude": -0.01, "duration": 8},
        ],
    },
    {
        "name": "Financial Sector Regulations",
        "description": "Implement regulations to ensure financial sector stability",
        "cost": 1100,  # in millions
        "outcomes": [
            {"effect_type": "GDP", "description": "Build investor confidence", "magnitude": 0.02, "duration": 12},
            {"effect_type": "Inflation", "description": "Potential cost implications for financial institutions", "magnitude": 0.01, "duration": 8},
        ],
    },
    {
        "name": "Job Training Programs",
        "description": "Introduce programs for job training and skill development",
        "cost": 900,  # in millions
        "outcomes": [
            {"effect_type": "Unemployment", "description": "Increase in skilled workforce", "magnitude": -0.03, "duration": 10},
            {"effect_type": "GDP", "description": "Potential increase in productivity", "magnitude": 0.02, "duration": 8},
        ],
    },
    {
        "name": "Public-Private Partnerships",
        "description": "Promote collaborations between the public and private sectors",
        "cost": 1200,  # in millions
        "outcomes": [
            {"effect_type": "GDP", "description": "Stimulate private sector investments", "magnitude": 0.03, "duration": 12},
            {"effect_type": "Budget", "description": "Shared infrastructure development costs", "magnitude": -0.02, "duration": 8},
        ],
    },
    {
        "name": "Income Tax Reduction",
        "description": "Reduce income tax rates to stimulate spending",
        "cost": 1400,  # in millions
        "outcomes": [
            {"effect_type": "GDP", "description": "Increase in consumer spending", "magnitude": 0.04, "duration": 15},
            {"effect_type": "Inflation", "description": "Potential inflation due to increased demand", "magnitude": 0.02, "duration": 10},
        ],
    },
    {
        "name": "Innovation Grants",
        "description": "Provide grants for innovative research and development",
        "cost": 1200,  # in millions
        "outcomes": [
            {"effect_type": "GDP", "description": "Stimulate innovation and technology", "magnitude": 0.03, "duration": 12},
            {"effect_type": "Unemployment", "description": "Potential job creation in innovative sectors", "magnitude": -0.02, "duration": 8},
        ],
    },
    {
        "name": "Economic Diversification",
        "description": "Diversify the economy to reduce dependence on specific sectors",
        "cost": 1000,  # in millions
        "outcomes": [
            {"effect_type": "GDP", "description": "Promote resilience against economic shocks", "magnitude": 0.02, "duration": 10},
            {"effect_type": "Unemployment", "description": "Potential job creation in emerging sectors", "magnitude": -0.01, "duration": 8},
        ],
    },
    {
        "name": "Public Sector Job Cuts",
        "description": "Implement job cuts in the public sector to reduce expenses",
        "cost": -600,  # Negative cost indicates a budget reduction
        "outcomes": [
            {"effect_type": "Budget", "description": "Savings from public sector payroll", "magnitude": -0.08,
             "duration": 10},
            {"effect_type": "Unemployment", "description": "Increase in public sector unemployment", "magnitude": 0.05,
             "duration": 8},
        ],
    },
    {
        "name": "Welfare Program Reduction",
        "description": "Reduce funding for social welfare programs",
        "cost": -900,  # Negative cost indicates a budget reduction
        "outcomes": [
            {"effect_type": "Budget", "description": "Savings from welfare program cuts", "magnitude": -0.12,
             "duration": 12},
            {"effect_type": "GDP", "description": "Potential decrease in consumer spending", "magnitude": -0.02,
             "duration": 8},
        ],
    },
    {
        "name": "Infrastructure Spending Cutback",
        "description": "Reduce spending on infrastructure projects",
        "cost": -1100,  # Negative cost indicates a budget reduction
        "outcomes": [
            {"effect_type": "Budget", "description": "Cutback in infrastructure spending", "magnitude": -0.15,
             "duration": 15},
            {"effect_type": "GDP", "description": "Potential slowdown in construction sector", "magnitude": -0.03,
             "duration": 10},
        ],
    },
    {
        "name": "Education Budget Reduction",
        "description": "Cutback on education sector budget",
        "cost": -800,  # Negative cost indicates a budget reduction
        "outcomes": [
            {"effect_type": "Budget", "description": "Reduction in education spending", "magnitude": -0.1,
             "duration": 12},
            {"effect_type": "Unemployment", "description": "Potential job cuts in education sector", "magnitude": 0.03,
             "duration": 8},
        ],
    },
    {
        "name": "Healthcare Funding Cuts",
        "description": "Reduce funding for healthcare services",
        "cost": -1000,  # Negative cost indicates a budget reduction
        "outcomes": [
            {"effect_type": "Budget", "description": "Cuts in healthcare funding", "magnitude": -0.12, "duration": 12},
            {"effect_type": "GDP", "description": "Potential impact on health sector employment", "magnitude": -0.02,
             "duration": 8},
        ],
    },
    {
        "name": "Environmental Protection Budget Cut",
        "description": "Reduce budget for environmental protection initiatives",
        "cost": -700,  # Negative cost indicates a budget reduction
        "outcomes": [
            {"effect_type": "Budget", "description": "Reduction in environmental protection spending",
             "magnitude": -0.1, "duration": 10},
            {"effect_type": "GDP", "description": "Potential impact on green sector employment", "magnitude": -0.01,
             "duration": 8},
        ],
    },
    {
        "name": "Subsidy Program Reduction",
        "description": "Cutback on subsidies for various industries",
        "cost": -1200,  # Negative cost indicates a budget reduction
        "outcomes": [
            {"effect_type": "Budget", "description": "Reduction in subsidy programs", "magnitude": -0.15,
             "duration": 12},
            {"effect_type": "GDP", "description": "Potential impact on subsidized industries", "magnitude": -0.03,
             "duration": 10},
        ],
    },
    {
        "name": "Tax Incentive Removal",
        "description": "Remove tax incentives for businesses",
        "cost": -600,  # Negative cost indicates a budget reduction
        "outcomes": [
            {"effect_type": "Budget", "description": "Reduction in tax incentives", "magnitude": -0.08, "duration": 8},
            {"effect_type": "GDP", "description": "Potential decrease in business investments", "magnitude": -0.01,
             "duration": 6},
        ],
    },
    {
        "name": "Defense Budget Cut",
        "description": "Reduce defense budget spending",
        "cost": -1500,  # Negative cost indicates a budget reduction
        "outcomes": [
            {"effect_type": "Budget", "description": "Cutback in defense spending", "magnitude": -0.2, "duration": 15},
            {"effect_type": "Unemployment", "description": "Potential job cuts in defense sector", "magnitude": 0.02,
             "duration": 10},
        ],
    },
    {
        "name": "Pension Reform",
        "description": "Implement reforms to reduce pension spending",
        "cost": -1000,  # Negative cost indicates a budget reduction
        "outcomes": [
            {"effect_type": "Budget", "description": "Reduction in pension spending", "magnitude": -0.12,
             "duration": 12},
            {"effect_type": "Unemployment", "description": "Potential impact on pension-related employment",
             "magnitude": 0.01, "duration": 8},
        ],
    },
]

# Convert policy dictionaries to Policy instances
policy_instances = [Policy(**policy) for policy in policy_list]
