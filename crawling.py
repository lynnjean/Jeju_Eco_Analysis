import requests
import csv
import os
from datetime import datetime
import xml.etree.ElementTree as ET

def fetch_data():
    url = "http://211.184.196.130/rest/JejuSewerWaterQDataService/getJejuSewerWaterQData/"
    response = requests.get(url)
    if response.status_code == 200:
        # XML 데이터 파싱
        root = ET.fromstring(response.text)
        
        # 타임스탬프 생성
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        
        # 파일이 존재하는지 확인
        file_exists = os.path.isfile("data.csv")
        
        with open("data.csv", mode="a", newline='') as file:
            writer = csv.writer(file)
            # 파일이 존재하지 않으면 헤더 추가
            if not file_exists:
                writer.writerow(["timestamp", "PlaceCode", "MeasureTime", "Organic", "Organic_Status", 
                                 "Suspended", "Suspended_Status", "TotalP", "TotalP_Status", 
                                 "TotalN", "TotalN_Status", "CommDisorder"])
            
            # XML에서 <list> 태그에 해당하는 데이터를 추출하여 CSV에 저장
            for list_element in root.findall(".//list"):
                place_code = list_element.find("PlaceCode").text
                measure_time = list_element.find("MeasureTime").text
                organic = list_element.find("Organic").text.strip()
                organic_status = list_element.find("Organic_Status").text
                suspended = list_element.find("Suspended").text.strip()
                suspended_status = list_element.find("Suspended_Status").text
                total_p = list_element.find("TotalP").text.strip()
                total_p_status = list_element.find("TotalP_Status").text
                total_n = list_element.find("TotalN").text.strip()
                total_n_status = list_element.find("TotalN_Status").text
                comm_disorder = list_element.find("CommDisorder").text
                
                # CSV 파일에 데이터 작성
                writer.writerow([timestamp, place_code, measure_time, organic, organic_status, 
                                 suspended, suspended_status, total_p, total_p_status, 
                                 total_n, total_n_status, comm_disorder])
        
        print(f"Data appended to data.csv")
    else:
        print("Failed to fetch data", response.status_code)

if __name__ == "__main__":
    fetch_data()
