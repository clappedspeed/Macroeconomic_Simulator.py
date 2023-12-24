# The database that stores data and stuff
import sqlite3
import json
import datetime

# Database connection
connect = sqlite3.connect("database.db")
cursor = connect.cursor()

def setup_database():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tblUserData (
        user_id INTEGER PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL,
        last_login INTEGER DEFAULT NULL,
        current_simulation_state VARCHAR(65535) DEFAULT NULL
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tblEconomicData (
        data_id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        year INTEGER NOT NULL,
        gdp FLOAT NOT NULL,
        inflation_rate FLOAT NOT NULL,
        unemployment_rate FLOAT NOT NULL,
        balance_of_payment FLOAT NOT NULL,
        budget FLOAT NOT NULL,
        FOREIGN KEY (user_id) REFERENCES tblUserData(user_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tblUserInteraction (
        interaction_id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        timestamp INTEGER NOT NULL,
        interaction_description VARCHAR(65535) NOT NULL,
        policy_applied VARCHAR(255) DEFAULT NULL,
        event_triggered VARCHAR(255) DEFAULT NULL,
        FOREIGN KEY (user_id) REFERENCES tblUserData(user_id)
    )
    """)

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tblSimulationState (
        state_id INTEGER PRIMARY KEY,
        user_id INTEGER NOT NULL,
        saved_state VARCHAR(65535) NOT NULL,
        timestamp INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES tblUserData(user_id)
    )
    """)

    connect.commit()

def save_simulation_state(user_id, simulation_data):
    serialized_state = json.dumps(simulation_data)
    timestamp = int(datetime.now().timestamp())
    cursor.execute("""
        INSERT INTO tblSimulationState (user_id, saved_state, timestamp)
        VALUES (?, ?, ?)
    """, (user_id, serialized_state, timestamp))
    connect.commit()


from datetime import datetime

def load_simulation_state(self, user_id):
    cursor.execute("""
        SELECT saved_state FROM tblSimulationState
        WHERE user_id = ?
        ORDER BY timestamp DESC
        LIMIT 1
    """, (user_id,))
    state_row = cursor.fetchone()
    if state_row:
        state = json.loads(state_row[0])
        state['current_date'] = datetime.strptime(state['current_date'], '%Y-%m-%d %H:%M:%S')
        return state
    return None



setup_database()
