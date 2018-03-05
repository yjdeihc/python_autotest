
from time import sleep



def wait_Text(self, text, path):
    driver = self.driver
    for i in range(10):
            try:
                if text in driver.find_element_by_xpath(path).text:
                    print(text)
                    break
            except:
                pass
            sleep(1)
    else:
        self.fail("time out")
        sleep(3)