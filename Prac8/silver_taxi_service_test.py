from Prac8.silver_taxi_service import SilverServiceTaxi


def main():
    taxi = SilverServiceTaxi("Test Fancy Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())


main()
