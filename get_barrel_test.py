import requests
import pytest

BASE_URL = "https://to-barrel-monitor.azurewebsites.net/barrels"

def test_vypsani_barelu():
    # Odeslání GET požadavku
    response = requests.get(BASE_URL)

    # Výpis status kódu do konzole
    print(f"Status kód: {response.status_code}")

    # Ověření kódu odpovědi
    assert response.status_code == 200, f"Očekáván kód 200, ale byl {response.status_code}"

    # Zpracování odpovědi
    response_data = response.json()

    # Výpis počtu záznamů
    print(f"Počet vrácených barelů: {len(response_data)}")

    # Výpis prvního barelu (pokud nějaký existuje)
    if response_data:
        print("První barel:")
        print(response_data[0])
    else:
        print("Žádné barely nebyly nalezeny.")

    # Ověření typu
    assert isinstance(response_data, list), "Odpověď není seznam (list)"

    # Volitelná kontrola obsahu
    for barrel in response_data:
        assert "id" in barrel, "Chybí 'id' v barelu"
        assert "qr" in barrel, "Chybí 'qr' v barelu"
        assert "rfid" in barrel, "Chybí 'rfid' v barelu"
        assert "nfc" in barrel, "Chybí 'nfc' v barelu"