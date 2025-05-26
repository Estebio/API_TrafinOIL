import requests
import pytest

BASE_URL = "https://to-barrel-monitor.azurewebsites.net/measurements"

def test_ziskani_vsech_mereni():
    # 1. Odeslání GET požadavku
    response = requests.get(BASE_URL)

    # 2. Ověření status kódu
    print(f"Status kód odpovědi: {response.status_code}")
    assert response.status_code == 200, f"Očekáván kód 200, ale byl {response.status_code}"

    # 3. Parsování JSON odpovědi
    data = response.json()
    print(f"Počet měření: {len(data)}")

    # 4. Ověření, že se jedná o seznam
    assert isinstance(data, list), "Odpověď není seznam (list)"

    # 5. Ověření struktury každého záznamu (nebo jen prvního)
    if data:
        for i, measurement in enumerate(data):
            print(f"Měření č. {i + 1}: {measurement}")
            assert "id" in measurement, "Chybí pole 'id'"
            assert "barrelId" in measurement, "Chybí pole 'barrelId'"
            assert "dirtLevel" in measurement, "Chybí pole 'dirtLevel'"
            assert "weight" in measurement, "Chybí pole 'weight'"

            # Typové kontroly (volitelné)
            assert isinstance(measurement["id"], str), "'id' není string"
            assert isinstance(measurement["barrelId"], str), "'barrelId' není string"
            assert isinstance(measurement["dirtLevel"], (int, float)), "'dirtLevel' není číslo"
            assert isinstance(measurement["weight"], (int, float)), "'weight' není číslo"
