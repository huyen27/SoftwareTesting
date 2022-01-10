import time
import unittest

from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager


class BookFilteringAutomationTest(unittest.TestCase):

    @classmethod
    def setUp(inst):
        service = Service(ChromeDriverManager().install())
        inst.driver = webdriver.Chrome(service=service)
        inst.driver.maximize_window()
        # inst.driver.get("https://nxbkimdong.com.vn/collections/manga")

    # Loc theo khoang gia
    def testfilterByPriceRange_clickThePriceRangeFrom100000To200000_haveNonEmptyListAndTheFirstBookPriceIsInTheRange(
            self):
        # Arrange
        self.driver.get("https://nxbkimdong.com.vn/collections/manga")
        time.sleep(15)
        # Act
        # Step: click on the price option
        price_option = self.driver.find_element(By.CSS_SELECTOR, "input[data-price='100000:200000']")
        price_option.click()
        time.sleep(5)

        # Step: get the first item (book) in the filtered list
        book_price_web_element_list = self.driver.find_elements(By.CSS_SELECTOR,
                                                                "div.product-price span.current-price")
         #lấy 1 phần tử đầu tiên trong list
        first_book_price_text = book_price_web_element_list[1]
        first_product_price_value = self.transformThePriceTextToNumber(first_book_price_text)

        # Assert
        self.assertGreaterEqual(len(book_price_web_element_list), 1)
        self.assertGreaterEqual(first_product_price_value, 100000)
        self.assertLessEqual(first_product_price_value, 200000)
     # Lọc theo nhiều khoảng giá cung luc
    def test_selectmultiplefiltersbypricerange(self):
        self.driver.get("https://nxbkimdong.com.vn/collections/100-sach-ban-chay")
        time.sleep(10)
        self.driver.find_element(By.CSS_SELECTOR, ".filter-price > li:nth-child(4) input").click()
        self.driver.find_element(By.CSS_SELECTOR, ".filter-price > li:nth-child(3) input").click()
        assert (self.driver.find_element(By.CSS_SELECTOR, ".filter-price > li:nth-child(4) input")).is_selected() is True
        assert (self.driver.find_element(By.CSS_SELECTOR, ".filter-price > li:nth-child(3) input")).is_selected() is True



     # Lọc theo 1 The Loai
    def testfilterByCategory_clickWingsBook_haveNonEmptyListAndTheFirstBookPriceIsInTheRange(
            self):
        # Arrange
        self.driver.get("https://nxbkimdong.com.vn/collections/100-sach-ban-chay")
        time.sleep(10)
        # Act
        # Step: click on the category option
        category_option = self.driver.find_element(By.CSS_SELECTOR, "#collection-wrapper > div > div > div > div.grid__item.large--one-quarter.medium--one-whole.small--one-whole > div > div > div:nth-child(3) > div > div > ul > li:nth-child(3) > label > span")
        category_option_name = category_option.text
        category_option.click()
        time.sleep(5)

        # Step: get the first item (book) in the filtered list
        book_category_web_element = self.driver.find_element(By.CSS_SELECTOR,
                                                                "#collection-wrapper > div > div > div > div.grid__item.large--three-quarters.medium--one-whole.small--one-whole.float-right > div > div.collection-body > div > div:nth-child(1) > div > div.product-info > div.product-title > a")
        book_category_web_element.click()
        category_name_web_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#breadcrumb-wrapper > div.breadcrumb-content > div > div > div.breadcrumb-small > a:nth-child(3)")))

        # assert
        self.assertEqual(category_option_name.upper(), category_name_web_element.text.upper())

     #loc theo nhieu the loai
    def testFilterByMultipleCategory_clickWingsBookAndVhvn_haveNonEmptyListAndTheFirstBookCategoryIsInTheRange(
            self):
        # Arrange
        self.driver.get("https://nxbkimdong.com.vn/collections/100-sach-ban-chay")
        # Act
        # Step: click on the category option
        time.sleep(8)
        category_option_wb = self.driver.find_element(By.CSS_SELECTOR, "#collection-wrapper > div > div > div > div.grid__item.large--one-quarter.medium--one-whole.small--one-whole > div > div > div:nth-child(3) > div > div > ul > li:nth-child(3) > label > span")
        category_option_name_wb = category_option_wb.text
        category_option_wb.click()

        category_option_vhvn = self.driver.find_element(By.CSS_SELECTOR,
                                                      "#collection-wrapper > div > div > div > div.grid__item.large--one-quarter.medium--one-whole.small--one-whole > div > div > div:nth-child(3) > div > div > ul > li:nth-child(2) > label > span")
        category_option_name_vhvn = category_option_vhvn.text
        category_option_vhvn.click()

        time.sleep(5)

        # Step: get the first item (book) in the filterd list
        book_category_web_element_1 = self.driver.find_element(By.CSS_SELECTOR,
                                                                "#collection-wrapper > div > div > div > div.grid__item.large--three-quarters.medium--one-whole.small--one-whole.float-right > div > div.collection-body > div > div:nth-child(4) > div > div.product-info > div.product-title > a")
        book_category_web_element_1.click()
        category_name_web_element_1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#breadcrumb-wrapper > div.breadcrumb-content > div > div > div.breadcrumb-small > a:nth-child(3)")))

        # assert
        self.assertEqual(category_name_web_element_1.text.upper(), category_option_name_wb.upper())

        # book_category_web_element = self.driver.find_element(By.CSS_SELECTOR,
        #                                                      "#collection-wrapper > div > div > div > div.grid__item.large--three-quarters.medium--one-whole.small--one-whole.float-right > div > div.collection-body > div > div:nth-child(14) > div > div.product-info > div.product-title > a")
        self.driver.get("https://nxbkimdong.com.vn/collections/100-sach-ban-chay?type=V%C4%83n%20h%E1%BB%8Dc%20Vi%E1%BB%87t%20Nam,Wings%20Books")
        time.sleep(5)
        book_category_web_element_2 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#collection-wrapper > div > div > div > div.grid__item.large--three-quarters.medium--one-whole.small--one-whole.float-right > div > div.collection-body > div > div:nth-child(1) > div > div.product-info > div.product-title > a")))
        book_category_web_element_2.click()
        category_name_web_element_2 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                                                     "#breadcrumb-wrapper > div.breadcrumb-content > div > div > div.breadcrumb-small > a:nth-child(3)")))

        # assert
        self.assertEqual(category_option_name_vhvn.upper(), category_name_web_element_2.text.upper())


     # xoa loc mot The Loai
    def testRemoveFilterByCategory_removeVhvn_haveNoneVhvnCategoryInList(self):

        # Arrange
        self.driver.get("https://nxbkimdong.com.vn/collections/100-sach-ban-chay")
        time.sleep(10)
        # Act
        # Step: click on the category option
        category_option_wb = self.driver.find_element(By.CSS_SELECTOR, "#collection-wrapper > div > div > div > div.grid__item.large--one-quarter.medium--one-whole.small--one-whole > div > div > div:nth-child(3) > div > div > ul > li:nth-child(3) > label > span")
        category_option_name_wb = category_option_wb.text
        category_option_wb.click()

        category_option_vhvn = self.driver.find_element(By.CSS_SELECTOR,
                                                          "#collection-wrapper > div > div > div > div.grid__item.large--one-quarter.medium--one-whole.small--one-whole > div > div > div:nth-child(3) > div > div > ul > li:nth-child(2) > label > span")
        category_option_name_vhvn = category_option_vhvn.text
        category_option_vhvn.click()
        # Wait for the page has loaded fully
        time.sleep(5)

        # Step: get the first item (book) in the filterd list
        book_category_web_element_1 = self.driver.find_element(By.CSS_SELECTOR,
                                                                    "#collection-wrapper > div > div > div > div.grid__item.large--three-quarters.medium--one-whole.small--one-whole.float-right > div > div.collection-body > div > div:nth-child(4) > div > div.product-info > div.product-title > a")
        book_category_web_element_1.click()
        category_name_web_element_1 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, "#breadcrumb-wrapper > div.breadcrumb-content > div > div > div.breadcrumb-small > a:nth-child(3)")))

        # assert
        self.assertEqual(category_option_name_wb.upper(), category_name_web_element_1.text.upper())

        # get the second item (book) in the filtered list
        self.driver.get("https://nxbkimdong.com.vn/collections/100-sach-ban-chay?type=V%C4%83n%20h%E1%BB%8Dc%20Vi%E1%BB%87t%20Nam,Wings%20Books")
        time.sleep(7)
        book_category_web_element_2 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#collection-wrapper > div > div > div > div.grid__item.large--three-quarters.medium--one-whole.small--one-whole.float-right > div > div.collection-body > div > div:nth-child(1) > div > div.product-info > div.product-title > a")))
        book_category_web_element_2.click()
        category_name_web_element_2 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                                                         "#breadcrumb-wrapper > div.breadcrumb-content > div > div > div.breadcrumb-small > a:nth-child(3)")))



            # assert
        self.assertEqual(category_option_name_vhvn.upper(), category_name_web_element_2.text.upper())

            # remove one option
        self.driver.get("https://nxbkimdong.com.vn/collections/100-sach-ban-chay?type=V%C4%83n%20h%E1%BB%8Dc%20Vi%E1%BB%87t%20Nam,Wings%20Books")
        time.sleep(6)
        category_option_unclickvhvn = self.driver.find_element(By.CSS_SELECTOR, "#collection-wrapper > div > div > div > div.grid__item.large--one-quarter.medium--one-whole.small--one-whole > div > div > div:nth-child(3) > div > div > ul > li:nth-child(2) > label > span")
        category_option_name_unclickvhvn = category_option_unclickvhvn.text
        category_option_unclickvhvn.click()
        time.sleep(4)
            # get item in the filtered list

        book_category_web_element_3 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                                                       "#collection-wrapper > div > div > div > div.grid__item.large--three-quarters.medium--one-whole.small--one-whole.float-right > div > div.collection-body > div > div:nth-child(8) > div > div.product-info > div.product-title > a")))
        book_category_web_element_3.click()

        category_name_web_element_3 = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,"#breadcrumb-wrapper > div.breadcrumb-content > div > div > div.breadcrumb-small > a:nth-child(3)")))
        self.assertNotEqual(category_option_name_unclickvhvn, category_name_web_element_3.text.upper())
    # Loc dong thoi theo Khoang gia va The loai
    def testFilterByPriceAndCategory_Click100to200andvhvn_listbook (self):
        # Arrange
        self.driver.get("https://nxbkimdong.com.vn/collections/100-sach-ban-chay")
        time.sleep(10)
        # Act
        # Step: click on the price option
        price_option = self.driver.find_element(By.CSS_SELECTOR, "input[data-price='100000:200000']")
        price_option.click()
        category_option = self.driver.find_element(By.CSS_SELECTOR, "#collection-wrapper > div > div > div > div.grid__item.large--one-quarter.medium--one-whole.small--one-whole > div > div > div:nth-child(3) > div > div > ul > li:nth-child(2) > label > span")

        category_option_name = category_option.text
        category_option.click()
        time.sleep(5)

        # Step: get the first item (book) in the filtered list
        book_price_web_element_list = self.driver.find_elements(By.CSS_SELECTOR,
                                                                "div.product-price span.current-price")
        # lấy 1 phần tử đầu tiên trong list de kiem tra gia
        first_book_price_text = book_price_web_element_list[1]
        first_product_price_value = self.transformThePriceTextToNumber(first_book_price_text)
        self.assertGreaterEqual(len(book_price_web_element_list), 1)
        self.assertGreaterEqual(first_product_price_value, 100000)
        self.assertLessEqual(first_product_price_value, 200000)
        # click vào chi tiết sp: kiem tra the loai
        book_category_web_element = self.driver.find_element(By.CSS_SELECTOR,
                                                             "#collection-wrapper > div > div > div > div.grid__item.large--three-quarters.medium--one-whole.small--one-whole.float-right > div > div.collection-body > div > div > div > div.product-info > div.product-title > a")
        book_category_web_element.click()
        category_name_web_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                                                     "#breadcrumb-wrapper > div.breadcrumb-content > div > div > div.breadcrumb-small > a:nth-child(3)")))

        # assert
        self.assertEqual(category_option_name.upper(), category_name_web_element.text.upper())


    # loc theo tac gia
    def testFilterByAuther_ClickOnlyOption_haveTrueAutherList(self):
        self.driver.get("https://nxbkimdong.com.vn/collections/100-sach-ban-chay")
        time.sleep(10)
        # Step: click on the auther option
        auther_option = self.driver.find_element(By.CSS_SELECTOR,
                                                   "#collection-wrapper > div > div > div > div.grid__item.large--one-quarter.medium--one-whole.small--one-whole > div > div > div:nth-child(2) > div > div > ul > li > label > span")
        auther_option_name = auther_option.text
        auther_option.click()
        time.sleep(5)

        # Step: get the first item (book) in the filtered list

        book_auther_web_element = self.driver.find_element(By.CSS_SELECTOR,
                                                               "#collection-wrapper > div > div > div > div.grid__item.large--three-quarters.medium--one-whole.small--one-whole.float-right > div > div.collection-body > div > div:nth-child(1) > div > div.product-info > div.product-title > a")
        book_auther_web_element.click()
        auther_name_web_element = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR,
                                                                                                       "#product-wrapper > div > div > div > div.grid.product-single > div.grid__item.large--seven-twelfths.medium--one-whole.small--one-whole > div > div.grid > div:nth-child(1) > div > ul > li:nth-child(2) > a")))

        # assert
        self.assertEqual(auther_option_name.upper(), auther_name_web_element.text.upper())


    @staticmethod
    def transformThePriceTextToNumber(html_element):
        price_text = html_element.get_attribute("innerHTML").strip()
        processed_text = price_text[0:(len(price_text) - 1)].replace(",", "")
        actual_price = int(processed_text)
        return actual_price

    @classmethod
    def tearDown(inst):
        inst.driver.quit()


if __name__ == '__main__':
    unittest.main()
