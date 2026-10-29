import asyncio
import os
from crawl4ai import AsyncWebCrawler

async def main():
    url_file = "urls.txt"
    if not os.path.exists(url_file):
        print(f"Fehler: Die Datei {url_file} wurde nicht gefunden.")
        return

    with open(url_file, "r", encoding="utf-8") as f:
        urls = [line.strip() for line in f if line.strip()]

    if not urls:
        print("Die urls.txt ist leer.")
        return

    output_dir = "01_Quellen/Crawled"
    os.makedirs(output_dir, exist_ok=True)

    print(f"Starte Crawl für {len(urls)} URLs...")

    async with AsyncWebCrawler() as crawler:
        for url in urls:
            print(f"Crawle: {url}")
            try:
                result = await crawler.arun(url=url)
                if result.success:
                    filename = url.split("/")[-1]
                    if not filename.endswith(".md"):
                        filename += ".md"
                    filepath = os.path.join(output_dir, filename)
                    with open(filepath, "w", encoding="utf-8") as f:
                        f.write(result.markdown)
                    print(f"  -> Gespeichert als: {filename}")
                else:
                    print(f"  -> Fehler: {result.error_message}")
            except Exception as e:
                print(f"  -> Unerwarteter Fehler: {e}")

if __name__ == "__main__":
    asyncio.run(main())