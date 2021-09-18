import json, os
# Open a terminal and type: pip3 install requests
import requests

# pip3 install azure-cosmosdb-table
from azure.cosmosdb.table.tableservice import TableService
from azure.cosmosdb.table.models import Entity


# https://api.thecatapi.com/v1/categories
def main():
  
   response = requests.get("https://api.thecatapi.com/v1/categories")
   categoriesList = response.json()

   for category in categoriesList:
       print(category["PartitionKey"])
       print(category["temperature"])

       #saveToTable(category)


def saveToTable(category):
  
   table_service = TableService(account_name="sensordatakyle", account_key="yES88dXHaHGHrALrk1juJcYvwDk3gKgL329QppScUkGpB9yYGz6LlXmnXn/DSm6HcnICzKVW4BwQN1qV579PMg==")

   categoryEntity = Entity()
   categoryEntity['PartitionKey'] = f"{category['PartitionKey']}"
   categoryEntity['RowKey'] = f"{category['temperature']}"
  
    # insert row 
   try:
       table_service.insert_entity('SensorData', categoryEntity)
   except:
       print(f"FAILED to insert CATEGORY: {category['name']}")
   else:
       print(f"SUCCESSFULLY inserted CATEGORY: {category['name']}")
  


if __name__ == "__main__":
   main()
