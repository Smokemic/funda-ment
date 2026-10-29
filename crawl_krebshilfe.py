import asyncio
import os
from crawl4ai import AsyncWebCrawler

async def main():
    # Die URLs der Webseiten, die gecrawlt werden sollen
    urls = [
        "https://www.krebshilfe.de/infomaterial/Blaue_Ratgeber/leberkrebs",
        "https://www.krebshilfe.de/infomaterial/Blaue_Ratgeber/bauchspeicheldruesenkrebs",
        "https://www.krebshilfe.de/infomaterial/Blaue_Ratgeber/magenkrebs",
        "https://www.krebshilfe.de/infomaterial/Blaue_Ratgeber/lungenkrebs",
        "https://www.krebshilfe.de/infomaterial/Blaue_Ratgeber/darmkrebs",
        "https://www.krebshilfe.de/infomaterial/Blaue_Ratgeber/brustkrebs",
        "https://www.krebshilfe.de/infomaterial/Blaue_Ratgeber/prostatakrebs",
        "https://www.krebshilfe.de/infomaterial/Blaue_Ratgeber/hautkrebs",
        "https://www.krebshilfe.de/infomaterial/Blaue_Ratgeber/blasenkrebs",
        "https://www.krebshilfe.de/infomaterial/Blaue_Ratgeber/nierenkrebs"
    ]

    # Zielordner erstellen, falls nicht vorhanden
    output_dir = r"C:\Projekte\FundaMent\01_Quellen\Crawled"
    os.makedirs(output_dir, exist_ok=True)

    print("Starte Crawl... Das kann ein paar Minuten dauern.")
    
    async with AsyncWebCrawler() as crawler:
        for url in urls:
            print(f"Crawle: {url}")
            result = await crawler.arun(url=url)
            
            if result.success:
                # Dateinamen aus der URL ableiten
                filename = url.split("/")[-1] + ".md"
                filepath = os.path.join(output_dir, filename)
                
                with open(filepath, "w", encoding="utf-8") as f:
                    f.write(result.markdown)
                print(f"  -> Gespeichert als: {filename}")
            else:
                print(f"  -> Fehler: {result.error_message}")

if __name__ == "__main__":
    asyncio.run(main())