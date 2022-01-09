import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import random

driver = webdriver.Chrome(executable_path='venv/chromedriver.exe')
driver.get('https://nxbkimdong.com.vn/')
class GioHang:
    def load():
        driver.maximize_window()

    def CartFirst():
        CartStart = driver.find_element(By.CLASS_NAME, 'no-bullets').text
        BillStart = driver.find_element(By.CLASS_NAME, 'qv-cart-total').text
        print("Gio hang ban dau: ", CartStart)
        print(BillStart)

    def CartLast():
        CartUpdate = driver.find_element(By.CLASS_NAME, 'no-bullets').text
        BillUpdate = driver.find_element(By.CLASS_NAME, 'qv-cart-total').text
        print(CartUpdate)
        print(BillUpdate)

    def BO0001(): #Thêm 1 sản phẩm vào giỏ hàng
        driver.find_element(By.LINK_TEXT, 'Dế mèn phiêu lưu ký').click()
        driver.find_element(By.ID, 'AddToCart').click()
        time.sleep(3)
        driver.find_element(By.ID, 'modalAddComplete-close').click()

    def BO0002(): #Kiểm tra giá trị mặc định của giỏ hàng
        driver.find_element(By.CLASS_NAME, 'hd-cart-count').click()
        status = driver.find_element(By.CLASS_NAME,'no-bullets').text
        print(status)

    def BO0003(): #Thêm 2 sản phẩm khác nhau vào giỏ hàng
        driver.find_element(By.XPATH, '//*[@id="owl-home-pro-products-slider-4"]/div[1]/div/div[3]/div/div/div[2]/div[1]/a').click()
        driver.find_element(By.ID, 'AddToCart').click()
        driver.implicitly_wait(5)
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR,'a.modalAddComplete-close').click()
        driver.find_element(By.LINK_TEXT, 'Trang chủ').click()
        driver.find_element(By.XPATH, '//*[@id="owl-home-pro-products-slider-5"]/div[1]/div/div[2]/div/div/div[2]/div[1]/a').click()
        driver.implicitly_wait(5)
        driver.find_element(By.ID, 'AddToCart').click()
        time.sleep(3)
        driver.find_element(By.ID, 'modalAddComplete-close').click()
        driver.find_element(By.CLASS_NAME, 'hd-cart-count').click()
        statusCart = driver.find_element(By.CLASS_NAME, 'no-bullets').text
        print(statusCart)

    def BO0004(): #Thêm 2 sản phẩm giống nhau vào giỏ hàng
        driver.find_element(By.XPATH,'//*[@id="owl-home-pro-products-slider-5"]/div[1]/div/div[2]/div/div/div[2]/div[1]/a').click()
        driver.find_element(By.ID, 'AddToCart').click()
        driver.implicitly_wait(5)
        time.sleep(3)
        driver.find_element(By.CSS_SELECTOR, 'a.modalAddComplete-close').click()
        driver.find_element(By.LINK_TEXT, 'Trang chủ').click()
        driver.find_element(By.XPATH,'//*[@id="owl-home-pro-products-slider-5"]/div[1]/div/div[2]/div/div/div[2]/div[1]/a').click()
        driver.implicitly_wait(5)
        driver.find_element(By.ID, 'AddToCart').click()
        time.sleep(3)
        driver.find_element(By.ID, 'modalAddComplete-close').click()
        driver.find_element(By.CLASS_NAME, 'hd-cart-count').click()
        statusCart = driver.find_element(By.CLASS_NAME, 'no-bullets').text
        print(statusCart)

    def BO0005(): #Cập nhật  số lượng sản phẩm trong giỏ hàng
        GioHang.BO0001()
        driver.find_element(By.CLASS_NAME, 'hd-cart-count').click()
        GioHang.CartFirst()
        time.sleep(2)
        driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div[1]/div/div[3]/div[3]/div/div[2]/a[1]').click()
        print('------------')
        rand = random.randint(0, 100)
        print("So luong nhap là: ",rand)
        driver.find_element(By.ID, 'updates_').clear()
        driver.find_element(By.ID, 'updates_').send_keys(rand)
        driver.find_element(By.CLASS_NAME, 'update-cart').click()
        driver.implicitly_wait(5)
        driver.find_element(By.CLASS_NAME, 'hd-cart-count').click()
        GioHang.CartLast()

    def BO0006(): #Không cập nhật số lượng rồi ấn Cập nhật
        GioHang.BO0001() #gio hang co 1 sp
        driver.find_element(By.CLASS_NAME, 'hd-cart').click()
        GioHang.CartFirst()
        driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div[1]/div/div[3]/div[3]/div/div[2]/a[1]').click()
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, 'update-cart').click()
        print("\nSau khi cap nhat khong thay doi so luong")
        driver.find_element(By.CLASS_NAME, 'hd-cart').click()
        GioHang.CartLast() #gio hang sao khi cap nhat

    def BO0007(): #Nhập số lượng sản phẩm là 0
        GioHang.BO0001()  # gio hang co 1 sp
        driver.find_element(By.CLASS_NAME, 'hd-cart').click()
        #xem gio hang
        driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div[1]/div/div[3]/div[3]/div/div[2]/a[1]').click()
        driver.find_element(By.ID, 'updates_').clear()
        driver.find_element(By.ID, 'updates_').send_keys(0)
        time.sleep(2)
        driver.find_element(By.CLASS_NAME, 'update-cart').click()
        print(driver.find_element(By.CSS_SELECTOR, 'div.inner>p').text)

    def BO0008(): #Nhập số lượng sản phẩm là chữ cái
        driver.find_element(By.XPATH, '//*[@id="owl-home-pro-products-slider-4"]/div[1]/div/div[2]/div/div/div[2]/div[1]/a').click()
        driver.find_element(By.ID, 'Quantity').clear()
        driver.find_element(By.ID, 'Quantity').send_keys('abc')
        driver.find_element(By.ID, 'AddToCart').click()

    def BO0009(): #Xóa sản phẩm
        GioHang.BO0001()
        driver.find_element(By.CLASS_NAME, 'hd-cart').click()
        GioHang.CartFirst()
        driver.find_element(By.CSS_SELECTOR, 'a.cart__remove').click()
        time.sleep(2)
        print("\nGio hang sao khi xoa")
        status = driver.find_element(By.CLASS_NAME, 'no-bullets').text
        print(status)

    def BO0010(): #Xóa sản phẩm- giỏ hàng có 1sp
        GioHang.BO0001()
        driver.find_element(By.CLASS_NAME, 'hd-cart').click()
        GioHang.CartFirst()
        # click xem gio hang
        driver.find_element(By.XPATH, '//*[@id="header"]/div[2]/div[1]/div/div[3]/div[3]/div/div[2]/a[1]').click()
        driver.find_element(By.CSS_SELECTOR, 'a.cart__remove>small').click()
        time.sleep(2)
        print("\nGio hang sao khi xoa")
        print(driver.find_element(By.CSS_SELECTOR, 'div.inner>p').text)

    def BO0011(): #Xóa sản phẩm - Giỏ hàng có 2sp
        print("Gio hang ban dau: ")
        GioHang.BO0003()
        driver.find_element(By.CLASS_NAME, 'hd-cart').click()
        driver.find_element(By.CSS_SELECTOR, 'a.cart__remove').click()
        time.sleep(2)
        print("\nGio hang sau khi xoa 1 san pham: ")
        GioHang.CartLast()

    def BO0012(): #Xem sản phẩm
        GioHang.BO0001()
        driver.find_element(By.CLASS_NAME, 'hd-cart').click()
        driver.find_element(By.CSS_SELECTOR, 'div.text-left>a').click()
        time.sleep(3)
        decription = driver.find_element(By.CSS_SELECTOR, 'div.product-content').text
        print(decription)

    def close():
        time.sleep(2)
        driver.close()

GioHang.load()
GioHang.BO0012()
GioHang.close()
