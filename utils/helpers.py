import json

def calculate_percentage(part, total):
# Calculates the percentage representation of a part relative to a total
    if total == 0:
        return 0.0
    return (part / total) * 100.0

# Load initial setup data
def load_initial_data():
    with open('data/initial_data.json', 'r') as file:
        initial_data = json.load(file)
    return initial_data

# Load event definitions
def load_event_definitions():
    with open('data/events.json', 'r') as file:
        event_definitions = json.load(file)
    return event_definitions

# Load resource properties
def load_resource_properties():
    with open('data/resources.json', 'r') as file:
        resource_properties = json.load(file)
    return resource_properties

# Example usage
initial_data = load_initial_data()
event_definitions = load_event_definitions()
resource_properties = load_resource_properties()