import json
from datetime import datetime
import time

import camoufox
options = uc.ChromeOptions()
config = {
        "headless": True,    
        "os": "windows",     
        "geoip": True
    }
with camoufox.Camoufox(**config, humanize=True) as browser:
    products = set()
    for i in range(1, 9):
        page = browser.new_page()
        page.goto(f"https://ozon.ru/search/?text=блейк крауч&page={i}&limit=100", wait_until="load")
       # products = set()
        while (True):
            page.evaluate("document.body.style.zoom = '0.1'")
            page.wait_for_timeout(8000)
            page.mouse.move(0, 1000)
            page.wait_for_timeout(3000)
            print(page.locator('div[data-widget="infiniteVirtualPaginator"] div[class^="tile-root"]').count())
            if (page.locator('div[data-widget="infiniteVirtualPaginator"] div[class^="tile-root"]').count() > 12):
                    for j in page.locator('div[data-widget="infiniteVirtualPaginator"] div[class^="tile-root"]').all()[:12]:
                        products.add(j.text_content())
                        if len(products) == 100: break
                    print()
                    break

print(list(products)[:100])