# The database that stores data and stuff
import sqlite3
import json
import datetime
from datetime import datetime

# Database connection
connect = sqlite3.connect("database.db")
cursor = connect.cursor()

def setup_database():
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS tblUserData (
        user_id INTEGER PRIMARY KEY,
        username VARCHAR(255) NOT NULL,
        password VARCHAR(255) NOT NULL
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

# Function to save simulation when called
def save_simulation_state(user_id, simulation_data):
    serialized_state = json.dumps(simulation_data)
    timestamp = int(datetime.now().timestamp())
    cursor.execute("""
        INSERT INTO tblSimulationState (user_id, saved_state, timestamp)
        VALUES (?, ?, ?)
    """, (user_id, serialized_state, timestamp))
    connect.commit()

# Function to load the data from a given user
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

def get_user_id(username):
    cursor.execute("""
        SELECT user_id FROM tblUserData WHERE username = ?
    """, (username,))
    result = cursor.fetchone()
    return result[0] if result else None

