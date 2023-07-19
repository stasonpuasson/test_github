import pytest

from main import calculate_tariff_payment


def test_calculate_tariff1000_used800():
    res = calculate_tariff_payment(1000, 800)
    assert res == 20

def test_calculate_tariff1000_used1200():
    res = calculate_tariff_payment(1000, 1200)
    assert res == 30

def test_calculate_tariff1000_used2200():
    res = calculate_tariff_payment(1000, 2200)
    assert res == 80

def test_calculate_tariff1000_used5200():
    res = calculate_tariff_payment(1000, 5200)
    assert res == 230

def test_calculate_tariff2000_used800():
    res = calculate_tariff_payment(2000, 800)
    assert res == 35

def test_calculate_tariff2000_used2200():
    res = calculate_tariff_payment(2000, 2200)
    assert res == 43

def test_calculate_tariff2000_used5200():
    res = calculate_tariff_payment(2000, 5200)
    assert res == 163

def test_calculate_tariff5000_used800():
    res = calculate_tariff_payment(5000, 800)
    assert res == 75

def test_calculate_tariff5000_used5200():
    res = calculate_tariff_payment(5000, 5200)
    assert res == 79

def test_calculate_tariff10000_used5200():
    with pytest.raises(ValueError, match="Tariff does not exist!"):
        calculate_tariff_payment(10000, 5200)
