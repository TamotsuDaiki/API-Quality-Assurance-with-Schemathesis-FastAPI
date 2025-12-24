# API Quality Assurance with Schemathesis & FastAPI

## Opis projektu
Projekt demonstruje wykorzystanie nowoczesnych technik testowania opartego na właściwościach (**Property-Based Testing**) w celu automatycznej weryfikacji poprawności implementacji API względem specyfikacji **OpenAPI 3.1**.

Sercem projektu jest narzędzie **Schemathesis**, które parsuje schemat wygenerowany przez framework **FastAPI** i generuje setki przypadków testowych, w tym scenariusze brzegowe (edge cases), których nie obejmują tradycyjne testy jednostkowe.

## Stack Technologiczny
* **Backend:** Python 3.x, FastAPI, Uvicorn
* **QA Tool:** Schemathesis (Hypothesis-based engine)
* **Specyfikacja:** OpenAPI / Swagger

## Instrukcja uruchomienia
1. Zainstaluj zależności:
   ```
   pip install fastapi uvicorn schemathesis requests
   ```
2. Uruchom serwer API:
    ```
    python -m uvicorn app:app --reload --port 8080
    ```
3. W osobnym terminalu uruchom pakiet testowy:
```
python -m schemathesis.cli run --checks all [http://127.0.0.1:8080/openapi.json](http://
```
