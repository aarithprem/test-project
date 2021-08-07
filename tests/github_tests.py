
from utils.app_utils import AppUtils
from utils.driver_setup import DriverSetup
from utils.selenium_utils import SeleniumUtils


class GitHubTests(DriverSetup, SeleniumUtils, AppUtils):

    def test_01_github_search(self):
        language = "JavaScript"
        stars = ">45"
        followers = ">50"
        name = "Boost Software License 1.0"
        keyword = "react"

        self.enter(keyword)
        self.select_keyword()
        self.choose_advanced_search()
        self.set_params_and_submit(language, stars, followers, name)

        # Verify expected count should be 1
        exp_result_count = "1"
        assert self.get_search_results().text == "{} repository result".format(exp_result_count)

        # Verify repo name matches
        exp_repo = "mvoloskov/decider"
        actual_repo = self.get_repo_text()
        assert actual_repo == exp_repo, "actual repo {} not matching with exp repo {}".format(actual_repo, exp_repo)

        # Click on the repo link
        self.click_on_repo()
        read_me_content = self.get_read_me_text()

        # printing first 300 characters
        if len(read_me_content) == 0:
            print("No content present")
        else:
            print(read_me_content[:300])


