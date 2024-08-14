import requests
import time
from datetime import datetime

def fetch_data():
    url = "http://211.184.196.130/rest/JejuSewerWaterQDataService/getJejuSewerWaterQData/"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.text
        timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
        filename = f"data_{timestamp}.txt"
        with open(filename, "w") as file:
            file.write(data)
        return filename
    else:
        print("Failed to fetch data", response.status_code)
        return None

if __name__ == "__main__":
    fetch_data()
