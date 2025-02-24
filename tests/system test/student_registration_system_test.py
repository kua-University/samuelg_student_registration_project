from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


class SystemTest(LiveServerTestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.driver = (
            webdriver.Chrome()
        )  # Or specify the path: webdriver.Chrome(executable_path='/path/to/chromedriver')
        cls.driver.implicitly_wait(10)  # Wait up to 10 seconds for elements to appear

    @classmethod
    def tearDownClass(cls):
        cls.driver.quit()
        super().tearDownClass()

    def test_user_registration_and_login(self):
        self.driver.get(self.live_server_url + "/users/register/")

        # Fill the registration form
        self.driver.find_element(By.NAME, "username").send_keys("testuser")
        self.driver.find_element(By.NAME, "password1").send_keys("testpass123")
        self.driver.find_element(By.NAME, "password2").send_keys("testpass123")
        self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        # Assert registration success
        assert "Login" in self.driver.title

        # Navigate to login page
        self.driver.get(self.live_server_url + "/users/login/")

        # Fill login form
        self.driver.find_element(By.NAME, "username").send_keys("testuser")
        self.driver.find_element(By.NAME, "password").send_keys("testpass123")
        self.driver.find_element(By.CSS_SELECTOR, 'button[type="submit"]').click()

        # Assert successful login (check if redirected to courses page)
        assert "Courses" in self.driver.page_source

    def test_course_registration(self):
        self.test_user_registration_and_login()  # Ensure logged in

        # Navigate to courses list
        self.driver.get(self.live_server_url + "/courses/list/")

        # Register for a course (assuming course ID 1 is present)
        self.driver.find_element(By.LINK_TEXT, "Register for Course 1").click()

        # Assert successful course registration
        assert "Registration Successful" in self.driver.page_source
