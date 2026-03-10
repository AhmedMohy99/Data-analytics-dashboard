from flask import Flask, render_template, jsonify

app = Flask(__name__, template_folder='../templates')

@app.route('/')
def index():
    # Data is structured for easy updates and scalability
    dashboard_data = {
        "months": ["Jan", "Feb", "Mar", "Apr", "May", "Jun"],
        "revenue": [15200, 18500, 14000, 21000, 29500, 36000],
        "leads": [45, 52, 38, 65, 88, 110],
        "sources": ["Social Media", "Direct", "Paid Ads", "SEO"],
        "shares": [40, 20, 25, 15]
    }
    return render_template('index.html', data=dashboard_data)

# Required for serverless execution
if __name__ == "__main__":
    app.run()
