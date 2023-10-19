from flask import Flask, render_template, jsonify
import random

app = Flask(__name__)

# Sample data with date attribute
events = [
    {"id": 1, "name": "Workshop A", "type": "Workshop", "importance": "High", "freebies": "Food", "mood": ["Curious", "Hungry"], "badge": "Hot!", "description": "A detailed workshop on topic A.", "date": "2023-10-20"},
    {"id": 1, "name": "Workshop B", "type": "Workshop", "importance": "High", "freebies": "Drinks", "mood": ["Curious", "Hungry"], "badge": "Hot!", "description": "A detailed workshop on topic A.", "date": "2023-10-22"},
    {"id": 1, "name": "Workshop C", "type": "Workshop", "importance": "High", "freebies": "Food", "mood": ["Curious", "Hungry"], "badge": "Hot!", "description": "A detailed workshop on topic A.", "date": "2023-10-24"},
    {"id": 1, "name": "Workshop D", "type": "Workshop", "importance": "High", "freebies": "Nunchucks", "mood": ["Curious", "Adventurous"], "badge": "Hot!", "description": "A detailed workshop on topic A.", "date": "2023-10-26"},
    {"id": 1, "name": "Workshop E", "type": "Workshop", "importance": "High", "freebies": "Hat", "mood": ["Curious"] , "description": "A detailed workshop on topic A.", "date": "2023-10-28"},    
    # ... Add more events with dates as needed
]

@app.route('/')
def index():
    sorted_events = sorted(events, key=lambda x: x['date'])  # Sorting events by date
    return render_template('index.html', events=sorted_events)

@app.route('/surprise-me')
def surprise_me():
    return jsonify(random.choice(events))

if __name__ == '__main__':
    app.run(debug=True)
