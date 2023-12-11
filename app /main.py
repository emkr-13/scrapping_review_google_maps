import time
from selenium import webdriver

def get_data(driver):
    """
    This function gets main text, score, name
    """
    print('Getting data...')
    elements = driver.find_elements('xpath', '//div[@class="Nv2PK THOPZb CpccDe "]')
    lst_data = []
    for data in elements:
        lst_data.append(data.text)
    return lst_data

if __name__ == "__main__":

    print('Starting...')

    driver = webdriver.Chrome()

    # Depending on the content you want, customize the URL
    driver.get('https://www.google.com/maps/search/kafe+jogja/@-7.7710144,110.3770161,15z/data=!4m2!2m1!6e5?entry=ttu')
    time.sleep(20)

    data = get_data(driver)

    driver.close()

    # Save data to a text file
    with open('hasil_1.txt', 'w', encoding='utf-8') as file:
        for item in data:
            file.write("%s\n" % item)

    print('Done! Data saved to output.txt')
