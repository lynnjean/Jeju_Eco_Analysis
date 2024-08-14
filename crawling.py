# import requests
# import csv
# import os
# from datetime import datetime

# def fetch_data():
#     url = "http://211.184.196.130/rest/JejuSewerWaterQDataService/getJejuSewerWaterQData/"
#     response = requests.get(url)
#     if response.status_code == 200:
#         data = response.text
#         timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

#         # 파일이 존재하지 않으면 헤더를 추가
#         file_exists = os.path.isfile("data.csv")
        
#         with open("data.csv", mode="a", newline='') as file:
#             writer = csv.writer(file)
#             if not file_exists:
#                 # CSV 파일에 헤더 작성 (필요에 따라 수정)
#                 writer.writerow(["timestamp", "data"])
#             # 데이터와 타임스탬프를 CSV 파일에 추가
#             writer.writerow([timestamp, data])
        
#         print(f"Data appended to data.csv")
#     else:
#         print("Failed to fetch data", response.status_code)

# if __name__ == "__main__":
#     fetch_data()
print('Hello')
