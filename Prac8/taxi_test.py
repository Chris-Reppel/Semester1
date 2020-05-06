from Prac8.taxi import Taxi


def main():
    test_taxi = Taxi("Prius 1", 100)
    test_taxi.drive(40)
    print(test_taxi)
    test_taxi.start_fare()
    test_taxi.drive(100)
    print(test_taxi)


main()
