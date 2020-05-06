from Prac8.car import Car
from Prac8.taxi import Taxi
from Prac8.silver_taxi_service import SilverServiceTaxi

Menu = "Q: Quit, C: Choose taxi, D: Drive"


def main():

    total_bill = 0
    taxis = [Taxi("Prius", 100), SilverServiceTaxi("Limo", 100, 2), SilverServiceTaxi("Hummer", 200, 4)]

    print("Lets drive!")
    print(Menu)
    choice = input(">>> ").upper()
    while choice != "Q":
        if choice == "C":
            print("Taxis available:")
            display_taxis(taxis)
            taxi_choice = int(input("Choose taxi:"))
            current_taxi = taxis[taxi_choice]
        elif choice == "D":
            current_taxi.start_fare()
            distance_to_drive = float(input("How far?"))
            current_taxi.drive(distance_to_drive)
            trip_cost = current_taxi.get_fare()
            print("You {} trip cost you ${:2f}".format(current_taxi.name, trip_cost))
            total_bill += trip_cost
        else:
            print("Invalid option")
        print("Bill to date: ${:2f}".format(total_bill))
        print(Menu)
        choice = input(">>> ").upper()

    print("Total trip cost: ${:2f}".format(total_bill))
    print("Current taxis are now:")
    display_taxis(taxis)


def display_taxis(taxis):
    for i, taxi in enumerate(taxis):
        print("{} - {}".format(i, taxi))


def run_tests():
    bus = Car("Datsun", 180)
    bus.drive(30)
    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    bus.drive(55)
    print("fuel =", bus.fuel)
    print("odo =", bus.odometer)
    print(bus)

    distance = int(input("How far?"))
    while distance > 0:
        travelled = bus.drive(distance)
        print("{} travelled {}".format(str(bus), travelled))
        distance = int(input("How far?"))

    t = Taxi("Prius 1", 100)
    print(t)
    t.drive(25)
    print(t, t.get_fare())
    t.start_fare()
    t.drive(40)
    print(t, t.get_fare())

    sst = SilverServiceTaxi("Limo", 100, 2)
    print(sst, sst.get_fare())
    sst.drive(10)
    print(sst, sst.get_fare())


main()
