from flask import Flask, render_template, jsonify
import pandas as pd

app = Flask(__name__)

@app.route('/')
def calendar():
    return render_template('calendar.html')

@app.route('/events')
def get_events():
    df = pd.read_csv('leave_requests.csv', parse_dates=['Start Date', 'End Date'])
    approved = df[df['Status'] == 'Approved']
    events = []

    for _, row in approved.iterrows():
        events.append({
            'title': row['Resident Name'],
            'start': row['Start Date'].strftime('%Y-%m-%d'),
            'end': (row['End Date'] + pd.Timedelta(days=1)).strftime('%Y-%m-%d'),
            'color': '#0066cc' if row['Leave Type'] == 'Casual' else '#dc3545'
        })

    return jsonify(events)

if __name__ == '__main__':
    app.run(debug=True)
