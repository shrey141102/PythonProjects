from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from datetime import datetime
from tabulate import tabulate
from selenium.webdriver.chrome.options import Options as ChromeOptions


def scrape(tags):
    # driver setup and initialization
    chrome_options = ChromeOptions()
    chrome_options.add_argument('--headless')
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    date = "20" + datetime.now().strftime("%y-%m-%d")

    # class name for scraping
    class_div = "ipc-metadata-list-summary-item"
    # connecting to the site in headful mode
    driver.minimize_window()
    # driver.set_window_size(1920, 1080)
    driver.get(f"https://www.imdb.com/search/title/?title_type=feature&genres={tags}&release_date=,{date}")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.CLASS_NAME, class_div))
    )

    elements = driver.find_elements(By.CLASS_NAME, class_div)

    # collecting results
    recommendations = []
    for i in elements:
        text = i.text.split("\n")
        recommendations.append(text)
    # stopping web driver
    driver.quit()
    return recommendations


def display_recommendations(recommendations):
    if not recommendations:
        print("No recommendations found.")
        return
    headers = ["Title", "Year", "Runtime"]
    table_data = [[item[0], item[1], item[2]] for item in recommendations]
    table = tabulate(table_data, headers, tablefmt="pretty")
    return table


def main():
    try:
        print("Make sure you have internet.")
        print("Type valid tags separated by space.")
        tags = input("Enter movie genre tags (e.g., thriller): ").split()
        actual_tags = ""
        for i in tags:
            actual_tags += i + ","
        print("\nLoading results.....")
        print("please wait.\n")

        final_recommendations = scrape(actual_tags[:-1])
        print("Results - ")
        print(display_recommendations(final_recommendations))
    except:
        print("There was error.")
        print("Few things you can check are - ")
        print("1. Tags should be separated by space.")
        print("2. Spelling errors.")
        print("3. Network connection.")
        print("4. Tags should be valid i.e. only use generally used tags like action, adventure, thriller etc.")


if __name__ == "__main__":
    main()
