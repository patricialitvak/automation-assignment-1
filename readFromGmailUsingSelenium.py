from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By


def print_all_mail():
    for n in range(3, len(List), +4):
        print("Sender: " + List[n][0])
        print("Subject: " + List[n + 1][0])
        print("\n")


def print_nth_mail(num):
    print("Sender: " + List[3 + (4 * num)][0])
    print("Subject: " + List[3 + (4 * num) + 1][0])
    print("\n")


if __name__ == '__main__':
    try:
        gmail_username = 'litvakpatricia@gmail.com'
        gmail_password = 'p@ssword01!'

        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        driver.get(r'https://accounts.google.com/signin/v2/identifier?continue=' + \
                   'https%3A%2F%2Fmail.google.com%2Fmail%2F&service=mail&sacu=1&rip=1' + \
                   '&flowName=GlifWebSignIn&flowEntry = ServiceLogin')

        driver.implicitly_wait(60)
        driver.find_element("id", 'identifierId').send_keys(gmail_username)
        driver.find_element("id", 'identifierNext').click()

        driver.implicitly_wait(60)
        driver.find_element("name", 'password').send_keys(gmail_password)
        driver.find_element("id", 'passwordNext').click()

        rms = driver.find_elements(By.CLASS_NAME, "yW")

        titles = driver.find_elements(By.TAG_NAME, "td")
        List = []
        for i in range(0, len(titles), +1):
            if titles[i].text:
                List.append(titles[i].text.strip().split("-"))

        print("Total count of mails is: " + str(len(rms)))

        print_nth_mail(4)

        print_all_mail()

    except TimeoutException as e:
        print(str(e))
