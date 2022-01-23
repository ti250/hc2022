import pandas as pd


class InformationManager():
    def __init__(self, prices):
        self.prices = prices

    def add_new_product(self, product_name, price):
        new_product_name = product_name.lower()
        new_list = []
        for i in range(len(self.prices.index)):
            new_list.append(price)
        self.prices[new_product_name] = new_list
        pass

    def change_price(self, supermarket_name, product_name, new_price):
        self.prices[product_name][supermarket_name] = new_price
        pass

    def check_price(self, new_price, old_price):
        if new_price == old_price:
            return True
        else:
            return False

    def extract_old_price(self, supermarket_name, product_name):
        return self.prices.loc[supermarket_name, product_name]

    def extract_list_of_column_name(self):
        columnsNamesArr = self.prices.columns.values
        return list(columnsNamesArr)

    def add_reciept(self, items, supermarket_name):
        product_name_list = self.extract_list_of_column_name()
        for item in items:
            print(item)
            product_name = item["description"].lower()
            new_price = item["total"] / item["quantity"]
            if product_name not in product_name_list:
                self.add_new_product(product_name, new_price)
            else:
                old_price = self.extract_old_price(supermarket_name, product_name)
                if self.check_price(new_price, old_price):
                    pass
                else:
                    self.change_price(supermarket_name, product_name, new_price)
        return (self.prices)
