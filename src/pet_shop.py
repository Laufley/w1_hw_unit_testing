
def get_pet_shop_name(shop_name):
    return(shop_name["name"])


def get_total_cash(pet_shop):
    return(pet_shop["admin"]["total_cash"])
# This solution is an improvement of my initial attempt as follows:

    # def get_total_cash(pet_shop):
    #     sum = pet_shop["admin"]["total_cash"]
    #     return(sum)

def add_or_remove_cash(pet_shop, new_money):
    (pet_shop["admin"]["total_cash"]) = (pet_shop["admin"]["total_cash"]) + new_money
# with this exercise i learnt how to update a list!


def add_or_remove_cash(pet_shop, new_cash):
    (pet_shop["admin"]["total_cash"]) = (pet_shop["admin"]["total_cash"]) + new_cash


def get_pets_sold(pet_shop):
    return(pet_shop["admin"]["pets_sold"])
#QUESTION:
#For this function, if i PRINT instead of RETURN, the end result is different. Why?
# when I print it, the error is: AssertionError: 0 != None


def increase_pets_sold(pet_shop, new_number):
    (pet_shop["admin"]["pets_sold"]) = (pet_shop["admin"]["pets_sold"]) + new_number

def get_stock_count(pet_shop):
    stock_count = 0
    for pet in pet_shop["pets"]:
        stock_count += pet
    print(stock_count)

def get_stock_count(pet_shop):
    stock_count = 0
    for pet in pet_shop["pets"]:
        stock_count += 1
    return stock_count

def get_pets_by_breed(pet_shop, breed_name):
    breed_type = []
    for pet in pet_shop["pets"]:
        if pet["breed"] == breed_name:
            print(breed_type.append(pet))
    return(breed_type)


def find_pet_by_name(pet_shop, pet_name):
    for pet in pet_shop["pets"]:
        if pet["name"] == pet_name:
            return(pet)

def remove_pet_by_name(pet_shop, pet_name):
    pet = find_pet_by_name(pet_shop, pet_name)
    print(pet_shop["pets"].remove(pet))


def add_pet_to_stock(pet_shop, new_pet):
    print(pet_shop["pets"].append(new_pet))


def get_customer_cash(customers):
    return(customers["cash"])


def remove_customer_cash(customer, cash):
    (customer["cash"]) -= cash


def get_customer_pet_count(customer):
    return(len(customer["pets"]))

def test_add_pet_to_customer(self):
        customer = self.customers[0]
        add_pet_to_customer(customer, self.new_pet)
        self.assertEqual(1, get_customer_pet_count(customer))


def add_pet_to_customer(customers, new_pet):
    (customers["pets"].append(new_pet))



