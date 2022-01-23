class FeedbackGenerator():
    def __init__(self, information_manager):
        self.information = information_manager
        self.prices = information_manager.prices

    def read_the_date(self, item):
        if item["date"] != "":
            return item["date"]
        else:
            return False

    def read_the_product_name(self, item):
        return item["description"].lower()

    def read_the_total_price(self, item):
        if item["total"] != "":
            return item["total"]
        else:
            return item["price"] * item["quantity"]

    def read_the_quantity(self, item):
        if item["quantity"] != '':
            return item["quantity"]
        else:
            return item["total"] / item["price"]

    def read_the_each_price(self, item):
        if item["price"] != '':
            return item["price"]
        else:
            return item["total"] / item["quantity"]

    #this is for home page
    def make_list(self, items):
        reciept_list = [{'time': 0, 'product': {}}]
        resultant_price = 0
        resultant_quantity = 0
        n = 0
        for item in items:
            if reciept_list[0]["time"] == 0:
                if self.read_the_date(item):
                    reciept_list[0]["time"] = self.read_the_date(item)
            name = self.read_the_product_name(item)
            price = self.read_the_each_price(item)
            quantity = self.read_the_quantity(item)
            total_price = self.read_the_total_price(item)
            reciept_list[0]['product'][n] = {}
            reciept_list[0]['product'][n]['name'] = name
            reciept_list[0]['product'][n]['quantity'] = quantity
            reciept_list[0]['product'][n]['price'] = price
            reciept_list[0]['product'][n]['total price'] = total_price
            resultant_price += total_price
            resultant_quantity += quantity
            n += 1
        reciept_list[0]['total'] = {}
        reciept_list[0]['total']['quantity'] = resultant_quantity
        reciept_list[0]['total']['price'] = resultant_price
        return reciept_list

    def make_predicted_price(self, supermarket, items):
        resultant_price = 0
        reciept = self.make_list(items)
        for i in range(len(reciept[0]["product"])):
            name = reciept[0]["product"][i]["name"]
            quantity = reciept[0]["product"][i]["quantity"]
            price = self.information.extract_old_price(supermarket, name)
            total_price = price * quantity
            resultant_price += total_price
        return resultant_price

    def calculate_net_benefit(self, supermarket, items):
        paid_price = self.make_list(items)[0]["total"]["price"]
        predicted_price = self.make_predicted_price(supermarket, items)
        benefit = predicted_price - paid_price
        return benefit

    #this is to get list
    def net_benefit(self, bought_supermarket, items):
        benefit_list = []
        for supermarket in self.prices.index:
            if bought_supermarket != supermarket:
                # net_benefit = self.calculate_net_benefit(supermarket, items)
                predicted_price = self.make_predicted_price(supermarket, items)
                benefit_list.append({"name": supermarket,
                                     "predictedPrice": predicted_price,
                                     "locationType": self.prices.loc[supermarket, "storeType"],
                                     })
        sorted_list = sorted(benefit_list, key=lambda x: x["predictedPrice"])
        return sorted_list









