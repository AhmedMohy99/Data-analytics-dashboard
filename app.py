from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    # Simulated performance data 
    performance_data = {
        'months': ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'],
        'revenue': [12000, 19000, 15000, 22000, 28000, 34000],
        'client_acquisition': [12, 18, 14, 25, 30, 42],
        'campaign_sources': ['Social Media', 'Organic Search', 'Paid Ads', 'Referrals'],
        'traffic_share': [45, 25, 20, 10]
    }
    
    return render_template('index.html', data=performance_data)

if __name__ == '__main__':
    app.run(debug=True)
