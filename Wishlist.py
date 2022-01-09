import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class BookWishListAutomationTest(unittest.TestCase):

    @classmethod
    def setUp(inst):
        service = Service(ChromeDriverManager().install())
        inst.driver = webdriver.Chrome(service=service)
        inst.driver.maximize_window()
        inst.driver.get("https://nxbkimdong.com.vn/collections/manga")

    def testWishListAdding_clickAddToWishListASpecificBook_haveThisBookInTheWishListPage(
            self):
        # Arrange
        # self.driver.set_network_conditions()

        # Step : Click one book to go to the detail page

        expected_selected_book = self.driver.find_element(By.CSS_SELECTOR,
                                                          "div.collection-body > div.grid-uniform.product-list.mg-left-15 > div:nth-child(1) > div > div.product-info > div.product-title > a")

        expected_selected_book.click()

        # Click the wish list button and store the full actual title of the current book
        adding_to_wish_list_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#onAppWishList_btn_add")))
        adding_to_wish_list_button.click()
        actual_book_title = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "div.pro-content-head.clearfix > div.header_wishlist > h1"))).text

        # Step: Redirect to the wish list page
        wish_list_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#onAppWishList_btn_page a")))
        wish_list_button.click()

        # Step: Get the first item in the wish list which is actually what we have chosen to put it to wish list recently
        expected_recent_wish_book_title = WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located((
            By.CSS_SELECTOR,
            "div.wish-list.grid-uniform.product-list.mg-left-15 > div:nth-child(1) > div > div.wish-info.product-info > div.product-title > a"))).text

        # Assert
        self.assertEqual(actual_book_title.upper(), expected_recent_wish_book_title.upper())


    def testRemoveAllWishList_clickDeleteItemWishListASpecificBook_dontContainThisBookInTheWishListPage(self):

    # Arrange
        # Step : Click one book to go to the detail page
        expected_selected_book_1 = self.driver.find_element(By.CSS_SELECTOR,
                                                          "#collection-wrapper > div > div > div > div.grid__item.large--three-quarters.medium--one-whole.small--one-whole.float-right > div > div.collection-body > div.grid-uniform.product-list.mg-left-15 > div:nth-child(1) > div > div.product-info > div.product-title > a")

        expected_selected_book_1.click()

        # Click the wish list button and store the full actual title of the current book
        adding_to_wish_list_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#onAppWishList_btn_add")))
        adding_to_wish_list_button.click()
        actual_book_title = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "div.pro-content-head.clearfix > div.header_wishlist > h1"))).text

        # Step: Redirect to the wish list page
        wish_list_button = WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, "#onAppWishList_btn_page a")))
        wish_list_button.click()
        #remove all item (book)
        # book_wishlist_list = self.driver.find_elements(By.CSS_SELECTOR, " span.current-price")
        # print("So item trong wishlist là: ", len(book_wishlist_list))

        remove_all_wish_list_button = WebDriverWait(self.driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "#onAppWishList_removeAll.btn.btn-danger")))
        remove_all_wish_list_button.click()
        time.sleep(5)
        body_Text = self.driver.find_element(By.CSS_SELECTOR,"#onAppWishList_page > div.main_content_bottom > div > div.wish-list.grid-uniform.product-list.mg-left-15 > div").text
        self.assertTrue("Không có sản phẩm trong danh sách yêu thích.",body_Text)
        print(body_Text)

    @classmethod
    def tearDown(inst):
        inst.driver.quit()


if __name__ == '__main__':
    unittest.main()
