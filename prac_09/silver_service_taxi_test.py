"""CP1404 Programming 2 - prac 09 - silver service taxi
Estimate: 30 minutes combined with test
Start: 9:35
Finish: 9:55
Total: 20 minutes
"""

from prac_09.silver_service_taxi import SilverServiceTaxi


def main():
    """Test SilverServiceTaxi."""
    taxi = SilverServiceTaxi("Test Fancy Taxi", 100, 2)
    taxi.drive(18)
    print(taxi)
    print(taxi.get_fare())

main()