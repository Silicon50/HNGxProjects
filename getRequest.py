from flask import Flask, request
from datetime import datetime

app = Flask(__name__)

@app.route('/api', methods = ['GET'])
def req():
    slack_name = request.args.get('slack_name')
    track = request.args.get('track')
    current_date = datetime.utcnow().strftime('%A')
    current__time = datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%SZ")
    github_repo_url = 'https://github.com/Silicon50/HNGxProjects'
    github_file_url = 'https://github.com/Silicon50/HNGxProjects/blob/main/getRequest.py'
    response_data = {
        "slack_name" : slack_name,
        "current_date" : current_date,
        "utc_time" : current__time,
        "track": track,
        "github_file_url" : github_file_url,
        "github_repo_url" : github_repo_url,
        "status_code" : 200
	}
    return (response_data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)