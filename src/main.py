# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

def calculate_tariff_payment(tariff_name: int, used_mb: float) -> float:
    if tariff_name == 5000:
        return 75 if used_mb <= 5000 else 75 + (used_mb - tariff_name) * 0.02
    elif tariff_name == 2000:
        return 35 if used_mb <= 2000 else 35 + (used_mb - tariff_name) * 0.04
    elif tariff_name == 1000:
        return 20 if used_mb <= 1000 else 20 + (used_mb - tariff_name) * 0.05
    else:
        raise ValueError("Tariff does not exist!")

if __name__ == '__main__':
    tariff = 1000
    used_traffic = 800
    calculate_tariff_payment(tariff, used_traffic)

