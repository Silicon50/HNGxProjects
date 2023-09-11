from flask import Flask, request
from datetime import datetime
from collections import OrderedDict
import json

app = Flask(__name__)

@app.route('/api', methods = ['GET'])
def req():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    current_day = datetime.utcnow().strftime('%A')
    current_time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    github_repo_url = 'https://github.com/Silicon50/HNGxProjects'
    github_file_url = 'https://github.com/Silicon50/HNGxProjects/blob/main/getRequest.py'
    
    response_data = OrderedDict([
        ("slack_name", slack_name),
        ("current_day", current_day),
        ("utc_time", current_time),
        ("track", track),
        ("github_file_url", github_file_url),
        ("github_repo_url", github_repo_url),
        ("status_code", 200)
    ])

    # Serialize the ordered dictionary to JSON
    response_json = json.dumps(response_data, indent=2)

    return response_json, 200, {'Content-Type': 'application/json'}

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)