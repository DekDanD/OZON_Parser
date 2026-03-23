# Ozon Parser (Camoufox)

Скрипт для поиска конкретного товара (SKU) в поисковой выдаче Ozon на глубину до 100 позиций. Использует библиотеку Camoufox для обхода защиты.

## Приготовления

Для работы требуется **Python 3.10+**.

1.  **Установите зависимости:**
    ```bash
    pip install camoufox
    ```

2.  **Установите браузер:**
    Библиотека Camoufox требует скачивания своего ядра (на базе Firefox):
    ```bash
    camoufox fetch
    ```

## Запуск

Просто запустите файл через терминал:
```bash
python main.py

Можно также через IDE: Visual Studio, Visual Studio Code или PyCharm.

