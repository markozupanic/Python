def input_car_values():
    make = input("make: ")
    model = input("model: ")
    horse_power = int(input("hp: "))
    torque = int(input("torque: "))
    weight = int(input("weight: "))
    top_speed = int(input("top speed: "))
    mileage = int(input("mileage: "))
    price = int(input("price: "))
    age = int(input("age: "))
    keys = ["make", "model", "horse_power", "torque", "weight", "top_speed", "mileage", "price", "age"]
    values = [make, model, horse_power, torque, weight, top_speed, mileage, price, age]
    car_dict = dict(zip(keys, values))
    return car_dict


def print_car_stats():
    print(f'make: {car_dict["make"]}, model: {car_dict["model"]}, horse_power: {car_dict["horse_power"]}, '
          f'torque: {car_dict["torque"]}, weight: {car_dict["weight"]}, top_speed: {car_dict["top_speed"]}, '
          f'mileage: {car_dict["mileage"]}, price: {car_dict["price"]}, age: {car_dict["age"]}')
    print(f'starting price: {car_dict["price"]}')
    print(f"acceleration: {get_car_acceleration()} m/s")
    print(f"inspection fee: {get_inspection_fee_price()} novaca")
    print_time_to_reach_top_speed()


def calculate_depreciation_price():
    mileage_depreciation = car_dict["price"] * (car_dict["mileage"] / 10000) * (1 / 100)
    age_depreciation = car_dict["price"] * car_dict["age"] * (2 / 100)
    depreciation_price = mileage_depreciation + age_depreciation
    return depreciation_price


def get_car_acceleration():
    return (car_dict["torque"] + car_dict["horse_power"]) / car_dict["weight"] * 3.6


def get_inspection_fee_price():
    return car_dict["horse_power"] + car_dict["torque"] + car_dict["weight"] + (get_car_acceleration()) * 10


def add_car_to_inspection():
    with open(INSPECTION_FILE_PATH, "a") as f:
        string_to_write = car_dict["make"], car_dict["model"], car_dict["horse_power"], car_dict["torque"], car_dict[
            "weight"], car_dict["top_speed"], car_dict["mileage"], car_dict["price"], car_dict["age"]
        f.write(str(string_to_write))
        f.write("\n")


def print_time_to_reach_top_speed():
    time = car_dict["top_speed"] / get_car_acceleration()
    print(f"time to reach top: {time}")


def depreciate_car():
    car_dict["price"] -= calculate_depreciation_price()


def add_age_mileage(age, mileage):
    car_dict["age"] += age
    car_dict["mileage"] += mileage


car_dict = {}
INSPECTION_FILE_PATH = "inspection.txt"
while True:
    option = input("\nunesi broj: 1-unos\n2-ispis\n3-izlaz\n")
    if option == "1":
        car_dict = input_car_values()
        print_car_stats()
        add_age_mileage(5, 10000)
        add_car_to_inspection()
        print_car_stats()

    elif option == "2":
        with open(INSPECTION_FILE_PATH, "r") as f:
            print(f.read())
    else:
        break