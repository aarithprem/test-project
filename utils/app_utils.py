from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select


class AppUtils:
    def enter(self, keyword):
        self.driver.find_element(By.NAME, "q").send_keys(keyword)

    def select_keyword(self):
        global_suggestion = "//*[@id='jump-to-suggestion-search-global']/a"
        element = (By.XPATH, global_suggestion)
        self.wait_until_element_found(element)
        self.driver.find_element_by_xpath(global_suggestion).click()

    def choose_advanced_search(self):
        self.driver.find_element(By.LINK_TEXT, "Advanced search").click()

    def search_language(self, language):
        search_language = Select(self.driver.find_element(By.ID, "search_language"))
        search_language.select_by_value(language)

    def set_stars(self, stars):
        self.driver.find_element(By.ID, "search_stars").send_keys(stars)

    def set_followers(self, followers):
        self.driver.find_element(By.ID, "search_followers").send_keys(followers)

    def search_license(self, license_name):
        select_license = Select(self.driver.find_element(By.XPATH, "//select[@id='search_license']"))
        select_license.select_by_visible_text(license_name)

    def click_submit(self):
        self.driver.find_element(By.XPATH, "//button[@type='submit']").click()

    def get_search_results(self):
        return self.driver.find_element(By.XPATH, "//*[@id='js-pjax-container']//div[2]/h3")

    def get_repo_text(self):
        return self.driver.find_element(By.XPATH, "//div[@class='f4 text-normal']/a").text

    def click_on_repo(self):
        self.driver.find_element(By.XPATH, "//div[@class='f4 text-normal']/a").click()

    def get_read_me_text(self):
        return self.driver.find_element(By.XPATH, "//div[@data-target='readme-toc.content']").text

    def set_params_and_submit(self, language, stars, followers, name):
        self.search_language(language)
        self.set_stars(stars)
        self.set_followers(followers)
        self.search_license(name)
        self.click_submit()


