import requests
from bs4 import BeautifulSoup
from csv import writer
import random
from datetime import datetime

def main():
    welcome_text()

    print(f"\nXULA's Mission Statement:")
    strip_text(scrape_website("https://www.xula.edu/about/mission-values.html","div","editorarea"))
    
    print(f"\nUtah State's Mission Statement:")
    strip_text(scrape_website("https://www.usu.edu/president/mission-statement/", "p", "lead"))

    scraped_jobs = scrape_website("https://realpython.github.io/fake-jobs/", "div", "card-content")
    add_jobs_to_csv(scraped_jobs, "fake_jobs.csv")
    
def add_jobs_to_csv (jobs_data, job_file):
    with open(job_file, "w") as f:
        csv_writer = writer(f)
        csv_writer.writerow(["Title", " Company", " Location", " Date Posted"])

        for job in jobs_data:
            title = job.find("h2", class_="title").get_text(strip=True)
            company = job.find("h3", class_="company").get_text(strip=True)
            location = job.find("p", class_="location").get_text(strip=True)
            date_posted = random_date()
            csv_writer.writerow([title, company, location, date_posted])

def scrape_website(url, element, class_name = None):
    try:
        headers = {"User-Agent":("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/120.0.0.0 Safari/537.36")}
        
        response = requests.get(url, headers=headers)
        response.raise_for_status()  

        soup = BeautifulSoup(response.content, "lxml")
        scraped_text = soup.find_all(element, class_=class_name) if class_name else soup.find(element)

        if scraped_text:
            return scraped_text
        else:
            return "Nothing found."

    except Exception as e:
        return (f"An error occurred while scraping the website: {e}")
    
def strip_text(scraped_text):
    for text in scraped_text:
        print(text.get_text(strip=True))

def random_date():
    random_year = random.randint(1999, datetime.now().year)
    random_month = random.randint(1, 12)
    random_day = random.randint(1, 31)
    return f"{random_year}-{random_month:02d}-{random_day:02d}"
    
def welcome_text():
    underscores = "_" * len(">> This is a program or tool that automatically extracts data from websites by parsing the underlying HTML code <<")
    print(underscores)
    print(
        "\t\t   _      _      _      _      _      _      _      _      _      _   \n"
        "\t\t _( )_  _( )_  _( )_  _( )_  _( )_  _( )_  _( )_  _( )_  _( )_  _( )_ \n"
        "\t\t(_ o _)(_ o _)(_ o _)(_ o _)(_ o _)(_ o _)(_ o _)(_ o _)(_ o _)(_ o _)\n"
        "\t\t (_,_)  (_,_)  (_,_)  (_,_)  (_,_)  (_,_)  (_,_)  (_,_)  (_,_)  (_,_) \n"
        "\t\t   _                                                              _   \n"
        "\t\t _( )_                                                          _( )_ \n"
        "\t\t(_ o _)                                                        (_ o _)\n"
        "\t\t (_,_)       __        __   _                          _        (_,_) \n"
        "\t\t   _         \\ \\      / /__| | ___ ___  _ __ ___   ___| |         _   \n"
        "\t\t _( )_        \\ \\ /\\ / / _ \\ |/ __/ _ \\| '_ ` _ \\ / _ \\ |       _( )_ \n"
        "\t\t(_ o _)        \\ V  V /  __/ | (_| (_) | | | | | |  __/_|      (_ o _)\n"
        "\t\t (_,_)          \\_/\\_/ \\___|_|\\___\\___/|_| |_| |_|\\___(_)       (_,_) \n"
        "\t\t   _                                                              _   \n"
        "\t\t _( )_                                                          _( )_ \n"
        "\t\t(_ o _)                                                        (_ o _)\n"
        "\t\t (_,_)                                                          (_,_) \n"
        "\t\t   _      _      _      _      _      _      _      _      _      _   \n"
        "\t\t _( )_  _( )_  _( )_  _( )_  _( )_  _( )_  _( )_  _( )_  _( )_  _( )_ \n"
        "\t\t(_ o _)(_ o _)(_ o _)(_ o _)(_ o _)(_ o _)(_ o _)(_ o _)(_ o _)(_ o _)\n"
        "\t\t (_,_)  (_,_)  (_,_)  (_,_)  (_,_)  (_,_)  (_,_)  (_,_)  (_,_)  (_,_) \n"
    )
    print(f">> This is a program or tool that automatically extracts data from websites by parsing the underlying HTML code << \n{underscores}")

if __name__ == "__main__":
    main()