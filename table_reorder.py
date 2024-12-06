import pandas as pd
import requests

def try_connect(url):
    try:
        response = requests.get(url, )
        return "Yes" if response.status_code == 200 else "No"
    except Exception as e:
        print(e)
        return "Unknown"


if __name__ == '__main__':
    ls = """Animals
    Anime
    Anti-Malware
    Art & Design
    Authentication & Authorization
    Blockchain
    Books
    Business
    Calendar
    Cloud Storage & File Sharing
    Continuous Integration
    Cryptocurrency
    Currency Exchange
    Data Validation
    Development
    Dictionaries
    Documents & Productivity
    Email
    Entertainment
    Environment
    Events
    Finance
    Food & Drink
    Games & Comics
    Geocoding
    Government
    Health
    Jobs
    Machine Learning
    Music
    News
    Open Data
    Open Source Projects
    Patent
    Personality
    Phone
    Photography
    Programming
    Science & Math
    Security
    Shopping
    Social
    Sports & Fitness
    Test Data
    Text Analysis
    Tracking
    Transportation
    URL Shorteners
    Vehicle
    Video
    Weather""".split("\n")

    tables = pd.read_html("https://github.com/public-apis/public-apis")
    tables_with_links = pd.read_html("https://github.com/public-apis/public-apis", extract_links="body")

    output = ""
    for inum, v in enumerate(tables[2:]):
        k = ls[inum]

        output += f"### {k}\n"
        v["API"] = tables_with_links[inum+2]["API"].apply(lambda x:f"[{x[0]}]({x[1]})")

        v["Available"] = tables_with_links[inum + 2]["API"].apply(lambda x: try_connect(x[1]))
        tables[2+inum] = v

    for inum, v in enumerate(tables[2:]):
        v["cn_Available"] = tables_with_links[inum + 2]["API"].apply(lambda x: try_connect(x[1]))

        v = v.sort_values(by=["cn_Available", "Available", "Auth", "HTTPS", "CORS", "API"], ascending=[False, True, False, False, True])
        v = v.reset_index(drop=True)
        v.index += 1
        # v["available"] = "Unknown"
        output += f"{v.to_markdown()}\n\n"
        output += """**[⬆ Back to Index](#index)**\n<br >\n<br >\n\n"""

    print()