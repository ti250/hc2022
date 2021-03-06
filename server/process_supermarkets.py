import pandas as pd
import numpy as np
import math

class PricesHelper():

    def __init__(self, csv_loc):
        self.prices = pd.read_csv(csv_loc).set_index('Store name')

    def calculate_distance(self, current_place, latitude, longitude):
        x = current_place[0]["latitude"] - latitude
        y = current_place[0]["longitude"] - longitude
        z = x * x
        w = y * y
        return np.sqrt(z + w) * 111 * 1000

    def get_recommendations(self, current_place, items):
        locations_list = []
        not_existed_item_list = self.calculate_cost_of_items(items, self.prices.index[0])[1]
        for i in range(len(self.prices.index)):
            price = self.calculate_cost_of_items(items, self.prices.index[i])[0]
            if math.isnan(self.prices.loc[self.prices.index[i], "Longitude"]):
                locations_list.append({
                    'locationName': self.prices.index[i],
                    'locationType': self.prices.loc[self.prices.index[i], "storeType"],
                    'deliveryDate': "25/Jan/2022",
                    'estimatedPrice': price,
                    'isOnline': True})
            else:
                x = self.prices.loc[self.prices.index[i], "Longitude"]
                y = self.prices.loc[self.prices.index[i], "Latitude"]
                distance = self.calculate_distance(current_place, y, x)
                locations_list.append({'location': {'longitude': x, 'latitude': y},
                            'locationName': self.prices.index[i],
                            'locationType': self.prices.loc[self.prices.index[i], "storeType"],
                            'distance': distance,
                            'estimatedPrice': price,
                            'isOnline': False})
        sorted_list = sorted(locations_list, key=lambda x: x["estimatedPrice"])
        return sorted_list, not_existed_item_list

    def calculate_cost_of_items(self, items, supermarket_name):
        x = 0
        not_existed_item_list = []
        for item in items:
            if self.check_the_existance_in_database(item):
                price = self.prices.loc[supermarket_name, item["name"]]
                x += price * item["quantity"]
            else:
                not_existed_item_list.append(item["name"])
        return (x, not_existed_item_list)

    def check_the_existance_in_database(self, item):
        for col_name in self.prices.columns:
            if col_name == item["name"]:
                return True
        return False

