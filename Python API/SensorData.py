import json, os
# Open a terminal and type: pip3 install requests
import datetime as dt
import requests

# pip3 install azure-cosmosdb-table
from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity


# https://api.thecatapi.com/v1/categories
def main():
   current_date = "2021-04-19"
   response = requests.get(f"https://sensata-academy-weather-station.azurewebsites.net/api/GetSensorData?date={current_date}")
   responseDictionary = response.json()
   dataList = responseDictionary["data"]
   current_date_dt = dt.datetime.strptime("2021-05-25", "%Y-%m-%d")
   next_date_dt = current_date_dt + dt.timedelta(days=1)
   next_date = dt.datetime.strftime(next_date_dt, "%Y-%m-%d")

   for sensorData in dataList:

       saveToTable(sensorData)


def saveToTable(sensorData):
  
   table_service = TableService(account_name="belfastmetsensatastorage", account_key="0Odi9O3y3WPFml5vukufXZzb5RitwUAUO52k98b0SWOzoOtpfmWu0C81ukvPCVTQ+KO3/2NvscJ6ODzT+0mZ9Q==")

   sensorEntity = Entity()
   sensorEntity['PartitionKey'] = f"{sensorData['PartitionKey']}"
   sensorEntity['RowKey'] = f"{sensorData['RowKey']}"
   sensorEntity['latitude'] = f"{sensorData['latitude']}"
   sensorEntity['longitude'] = f"{sensorData['longitude']}"
   sensorEntity['description'] = f"{sensorData['description']}"
   sensorEntity['temperature'] = f"{sensorData['temperature']}"
   sensorEntity['pressure'] = f"{sensorData['pressure']}"
   sensorEntity['humidity'] = f"{sensorData['humidity']}"
   sensorEntity['light'] = f"{sensorData['light']}"
   sensorEntity['oxidising'] = f"{sensorData['oxidising']}"
   sensorEntity['reducing'] = f"{sensorData['reducing']}"
   sensorEntity['nh3'] = f"{sensorData['nh3']}"
   sensorEntity['pm1'] = f"{sensorData['pm1']}"
   sensorEntity['pm2_5'] = f"{sensorData['pm2_5']}"
   sensorEntity['pm10'] = f"{sensorData['pm10']}"
   sensorEntity['bst'] = f"{sensorData['bst']}"
  
    # insert row 
   try:
       table_service.insert_entity('SensorData', sensorEntity)
   except:
       print(f"FAILED to insert Sensor Data:{sensorData['PartitionKey']} / {sensorData['RowKey']}")
   else:
       print(f"SUCCESSFULLY inserted Sensor Data: {sensorData['PartitionKey']} / {sensorData['RowKey']}")


if __name__ == "__main__":
   main()