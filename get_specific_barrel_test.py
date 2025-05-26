import requests
import pytest

BASE_URL = "https://to-barrel-monitor.azurewebsites.net/barrels"
TEST_ID = "3fa85f64-5717-4562-b3fc-2c963f66afa6"  # nahraď ID podle potřeby

def test_ziskani_konkretniho_barelu():
    # Vytvoření URL pro konkrétní barel
    url = f"{BASE_URL}/{TEST_ID}"

    # Odeslání GET požadavku
    response = requests.get(url)

    # Výpis status kódu do konzole
    print(f"Status kód: {response.status_code}")

    # Ověření odpovědi
    assert response.status_code == 200, f"Očekáván kód 200, ale byl {response.status_code}"

    # Výpis obsahu odpovědi
    response_data = response.json()
    print("Získaný barel:")
    print(response_data)
