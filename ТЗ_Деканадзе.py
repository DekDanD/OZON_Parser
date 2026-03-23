import json
from datetime import datetime
import time
import re
import camoufox

config = {
        "headless": True,    
        "os": "windows",     
        "geoip": True
    }

def finding_something_in_ozon(query: str, sku_to_search: int):
    with camoufox.Camoufox(**config, humanize=True) as browser:
        products = set()
        page = browser.new_page()
        page.goto(f"https://ozon.ru/search/?text={query}&limit=100", wait_until="load")
        page.wait_for_timeout(5000)
        page.evaluate("document.body.style.zoom = '0.1'")
        page.wait_for_timeout(20000)
        print(page.locator('div[data-widget="infiniteVirtualPaginator"] div[class^="tile-root"]').count())
        for j in page.locator('div[data-widget="infiniteVirtualPaginator"] div[class^="tile-root"]').all():
            if j.text_content() in products: continue
            products.add(j.text_content())
            href = j.locator('a').first.get_attribute('href')
            match = re.search(r'.*\/product\/.*\-([1-9][0-9]+)\/', href)
            sku = 0
            if match:
                sku = match.group(1)
            if int(sku) == sku_to_search:
                return json.dumps({
                    "query": query,
                    "sku": sku,
                    "position": len(products),
                    "page": 1,
                    "total_checked": 100,
                    "timestamp": datetime.now().isoformat()
                    })
            if len(products) == 100: break
    return "not_found"

if __name__ == "__main__":
    finding_something_in_ozon('блейк крауч', 3260207120)