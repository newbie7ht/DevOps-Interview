
 #Usage: You can schedule this script using cron or a task scheduler to periodically check the health of the service and send alerts if it’s down.
 

import requests

# Define the URL of the web service
url = "http://example.com/api/health"

try:
    # Send a GET request to the health endpoint
    response = requests.get(url, timeout=5)
    if response.status_code == 200:
        print(f"Service is up. Status code: {response.status_code}")
    else:
        print(f"Service is down. Status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    print(f"Service is down. Error: {e}")
