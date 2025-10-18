import requests
from bs4 import BeautifulSoup

def main():
    welcome_text()

    xula_mission_statement = scrape_university_website("https://www.xula.edu/about/mission-values.html","div","editorarea")
    utah_mission_statement = scrape_university_website("https://www.usu.edu/president/mission-statement/", "p", "lead")

    print(f"\nXULA's Mission Statement: \n'{str(xula_mission_statement)}'")
    print(f"\nUtah State's Mission Statement: \n'{str(utah_mission_statement)}'")

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

def scrape_university_website(url, element, class_name = None):
    try:
        headers = {"User-Agent":("Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")}
        
        response = requests.get(url, headers=headers)
        response.raise_for_status()  

        soup = BeautifulSoup(response.text, "html.parser")
        mission_paragraph = soup.find(element, class_=class_name) if class_name else soup.find(element)

        if mission_paragraph:
            mission_statement = mission_paragraph.get_text(strip=True)
            return mission_statement
        else:
            return "Mission statement not found."

    except Exception as e:
        return (f"An error occurred while scraping the website: {e}")

if __name__ == "__main__":
    main()