import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException  # Import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import json


class JobSearch:
    def __init__(self, data) -> None:
        """parameter initialization"""
        self.email = data["email"]
        self.password = data["password"]
        self.keyword = data["keyword"]
        self.city = data["city"]
        self.application = []
        self.driver = webdriver.Chrome()

    def login(self):
        self.driver.get("https://www.linkedin.com/login")
        try:
            email = self.driver.find_element(By.ID, "username")
            email.clear()
            email.send_keys(self.email)
            password = self.driver.find_element(By.ID, "password")
            password.clear()
            password.send_keys(self.password)
            password.send_keys(Keys.RETURN) 
            time.sleep(2)
            self.driver.get("https://www.linkedin.com/jobs")
            time.sleep(2)
            print("Successfuly Logged In")
        except Exception as e:
            print("Error occurred during login:", e)

    def search_jobs(self):
        search_box = self.driver.find_element(By.XPATH,"//*[contains(@id,'jobs-search-box-keyword-id')]")
        search_box.click()
        search_box.send_keys(self.keyword)
        search_box. send_keys(Keys.RETURN)
        #To search city
        time.sleep(2)
        search_city = self.driver.find_element(By.XPATH,"//*[contains(@id,'jobs-search-box-location-id')]")
        search_city.clear()
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(@id,'jobs-search-box-location-id')]"))
        ).click()
        search_city.clear()
        WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//*[contains(@id,'jobs-search-box-location-id')]"))
        ).send_keys(self.city)
        search_city.send_keys(Keys.RETURN)
        time.sleep(3)



    def find_jobs(self):
    
        parent_container = WebDriverWait(self.driver, 10).until(
            EC.presence_of_element_located((By.CLASS_NAME, "scaffold-layout__list-container"))
        )
        
        # Find all 'a' elements within the parent container
        a_elements = parent_container.find_elements(By.XPATH, ".//a[contains(@class, 'job-card-container__link')]")
        
        # Find all 'div' elements with class 'artdeco-entity-lockup__subtitle' within the parent container
        company_name_div_elements = parent_container.find_elements(By.CLASS_NAME, 'artdeco-entity-lockup__subtitle')

        # Find all 'div' elements with class 'class="artdeco-entity-lockup__caption' within the parent container
        location_div_elements = parent_container.find_elements(By.CLASS_NAME,'artdeco-entity-lockup__caption')

        with open('python_job_applications.json', 'a') as json_file:
            json_file.write("[")  # Write opening square bracket
            try:
                # Iterate through both lists simultaneously to extract the information 
                for i, (a_element, company_name_div_element, location_div_element) in enumerate(zip(a_elements, company_name_div_elements, location_div_elements)):
                    try:
                        # Find the 'span' tag within the current div element
                        company_name_span_tag = company_name_div_element.find_element(By.CLASS_NAME, "job-card-container__primary-description")
                        company_name = company_name_span_tag.text
                        
                        # Find the 'strong' tag within the 'a' tag to extract the job name
                        job_name_element = a_element.find_element(By.XPATH, ".//strong")
                        job_name = job_name_element.text

                        # Find the 'span' tag within the current div element
                        company_location_ul = location_div_element.find_element(By.CLASS_NAME, "job-card-container__metadata-item ")
                        company_location = company_location_ul.text

                        job_link = a_element.get_attribute("href")
                        
                        print("Job Name:", job_name)
                        print("Company Name:", company_name)
                        print("Location:", company_location)
                        print("URL:", job_link)
                        
                        # Write job details to the JSON file
                        data = {
                            "Title": job_name,
                            "Company name": company_name,
                            "Location": company_location,
                            "URL": job_link
                        }
                        json.dump(data, json_file, indent=4)
                        
                        # Add a comma and newline if it's not the last entry
                        if i != len(a_elements) - 1:
                            json_file.write(",\n")
                        else:
                            json_file.write("\n")  # Write newline after the last entry
                        
                        print("---")                   
                        
                    except NoSuchElementException:
                        print("Company name not found in the current 'a' element")

            finally:
                json_file.write("]")  # Write closing square bracket


    
    def close_session(self):
        try:
            self.driver.quit()  # Close the browser session
            print("Browser session closed successfully.")
        except Exception as e:
            print("Error occurred while closing the browser session:", e)




    def fetch_jobs(self):
        self.driver.maximize_window()
        try:
            self.login()
        except:
            self.driver.get("https://www.linkedin.com")
        self.search_jobs()
        time.sleep(5)
        self.find_jobs()
        time.sleep(2)
        self.close_session()




if __name__ == "__main__":
    try:
        with open("config.json") as config_file:
            data = json.load(config_file)
    except FileNotFoundError:
        print("Config file not found.")
    except json.JSONDecodeError:
        print("Error decoding JSON data.")
    else:
        bot = JobSearch(data)
        bot.fetch_jobs()

