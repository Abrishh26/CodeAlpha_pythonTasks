import requests
import re

urls = [
    "https://www.wikipedia.org",
    "https://www.python.org",
    "https://github.com"
]

output_file = "Task3_Automation/scraped_titles.txt"

print("=== Web Title Scraper ===\n")

with open(output_file, "w") as f:
    f.write("Scraped Website Titles\n")
    f.write("=" * 30 + "\n\n")

    for url in urls:
        try:
            response = requests.get(url, timeout=5)
            match = re.search(r'<title>(.*?)</title>', response.text, re.IGNORECASE)
            if match:
                title = match.group(1).strip()
                print(f"URL: {url}")
                print(f"Title: {title}\n")
                f.write(f"URL: {url}\n")
                f.write(f"Title: {title}\n\n")
            else:
                print(f"URL: {url}")
                print("Title: Not found\n")
        except Exception as e:
            print(f"Failed to fetch {url}: {e}\n")

print(f"Results saved to {output_file}")