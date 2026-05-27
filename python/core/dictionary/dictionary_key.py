if __name__ == '__main__':
    employees = {
        "name": "Meenakshi",
        "department": "Software Engineering",
        "age": 30,
        "salary": 120000,
        "gender": "Male"
    }

    print(employees)

    user = {
        17: "Alia",
        21: "Genelia"
    }

    print(user)

    orders = ("Mobile 1", 25, "TV", 17.8)

    print(orders)

    order_details = {
        orders: "electronics"
    } # tuple is immutable so it can be used as key in dictionary

    print(order_details)

    list_data = [27, "name_data"]

    print(list_data)

  #  list_as_key_in_dictionary = {
  #      list_data: "collects all data"
  #  } # list is mutable so it can not be used as key in dictionary

  #  print(list_as_key_in_dictionary)