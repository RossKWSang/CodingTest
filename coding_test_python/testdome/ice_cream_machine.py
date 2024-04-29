class IceCreamMachine:
    def __init__(self, ingredients, toppings):
        self.ingredients = ingredients
        self.toppings = toppings

    def scoops(self):
        if not self.ingredients or not self.toppings:
            return []

        result = []
        for ingredient in self.ingredients:
            for topping in self.toppings:
                result.append([ingredient, topping])

        return result


if __name__ == '__main__':
    ice_cream_machine = IceCreamMachine(
        ["vanilla", "chocolate"],
        ["chocolate sauce"]
    ).scoops()

    print(ice_cream_machine)
