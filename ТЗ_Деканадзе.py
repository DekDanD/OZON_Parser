import json
from datetime import datetime
import time

import camoufox

config = {
        "headless": True,    
        "os": "windows",     
        "geoip": True
    }

def finding_something_in_ozon(query: str, sku_to_search: int):
    with camoufox.Camoufox(**config, humanize=True) as browser:
        products = set()
        for i in range(1, 9):
            page = browser.new_page()
            page.goto(f"https://ozon.ru/search/?text=блейк крауч&page={i}&limit=100", wait_until="load")
            while (True):
                page.evaluate("document.body.style.zoom = '0.1'")
                page.mouse.move(0, 1000)
                page.wait_for_timeout(5000)
                if (page.locator('div[data-widget="infiniteVirtualPaginator"] div[class^="tile-root"]').count() > 12):
                        for j in page.locator('div[data-widget="infiniteVirtualPaginator"] div[class^="tile-root"]').all()[:12]:
                            if j in products: continue
                            sub = browser.new_page()
                            href = j.locator('a').first.get_attribute('href')
                            sub.goto(f"https://ozon.ru/{href[1:]}")
                            sub.wait_for_timeout(2000)
                            content = sub.content()
                            start = content.index('Артикул: ') + 9
                            end = start
                            products.add(j)
                            while content[end].isdigit():
                                end += 1
                            sku = content[start:end]
                            if int(sku) == sku_to_search:
                                return json.dumps({
                                    "query": query,
                                    "sku": sku,
                                    "position": len(products),
                                    "page": i,
                                    "total_checked": 100,
                                    "timestamp": datetime.now().isoformat()
                                    })
                            if len(products) == 100: break
                        break
    return "not_found"
