import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException


driver = webdriver.Chrome(executable_path='venv/chromedriver.exe')
driver.get('https://nxbkimdong.com.vn/')

class DatHang():
    def load():
        driver.maximize_window()

    def BO0013(): #Đặt hàng đầy với đầy đủ thông tin
        try:
            driver.find_element(By.LINK_TEXT, 'Dế mèn phiêu lưu ký').click()
            driver.find_element(By.ID, 'buy-now').click()
            driver.implicitly_wait(10)
            driver.find_element(By.ID, 'billing_address_full_name').send_keys('huyen')
            driver.find_element(By.ID, 'checkout_user_email').send_keys('abc@gmail.com')
            driver.find_element(By.ID, 'billing_address_phone').send_keys('0348498153')
            driver.find_element(By.ID, 'billing_address_address1').send_keys('Nguyễn Kiệm')
            tinh = Select(driver.find_element(By.ID, 'customer_shipping_province'))
            tinh.select_by_visible_text('Hồ Chí Minh')
            time.sleep(3)
            huyen = Select(driver.find_element(By.ID, 'customer_shipping_district'))
            huyen.select_by_visible_text('Quận Gò Vấp')
            time.sleep(5)
            xa = Select(driver.find_element(By.ID, 'customer_shipping_ward'))
            xa.select_by_visible_text('Phường 03')
            driver.find_element(By.XPATH, '//*[@id="form_next_step"]/button/i').click()
            driver.find_element(By.NAME, 'payment_method_id').click()
            ''' #click dat hang
            driver.find_element(By.XPATH, '//*[@id="form_next_step"]/button/i').click()
            '''
            print("Đặt hàng thành công")
        except:
            print("Lỗi")

    def BO0014(): #Họ và tên: nhập thiếu
        try:
            driver.find_element(By.LINK_TEXT, 'Dế mèn phiêu lưu ký').click()
            driver.find_element(By.ID, 'buy-now').click()
            driver.implicitly_wait(10)
            driver.find_element(By.ID, 'checkout_user_email').send_keys('abc@gmail.com')
            driver.find_element(By.ID, 'billing_address_phone').send_keys('0348498153')
            driver.find_element(By.ID, 'billing_address_address1').send_keys('Nguyễn Kiệm')
            tinh = Select(driver.find_element(By.ID, 'customer_shipping_province'))
            tinh.select_by_visible_text('Hồ Chí Minh')
            time.sleep(3)
            huyen = Select(driver.find_element(By.ID, 'customer_shipping_district'))
            huyen.select_by_visible_text('Quận Gò Vấp')
            time.sleep(5)
            xa = Select(driver.find_element(By.ID, 'customer_shipping_ward'))
            xa.select_by_visible_text('Phường 03')
            driver.find_element(By.XPATH, '//*[@id="form_next_step"]/button/i').click()
            driver.find_element(By.NAME, 'payment_method_id').click()
            ''' #click dat hang
            driver.find_element(By.XPATH, '//*[@id="form_next_step"]/button/i').click()
            '''
            print("Đặt hàng thành công")
        except:
            print("Lỗi: ",  driver.find_element(By.XPATH, '//*[@class="field-message field-message-error"]').text)

    def BO0015(): #Họ và tên: có kí tự đặc biệt
        try:
            driver.find_element(By.LINK_TEXT, 'Dế mèn phiêu lưu ký').click()
            driver.find_element(By.ID, 'buy-now').click()
            driver.implicitly_wait(10)
            driver.find_element(By.ID, 'billing_address_full_name').send_keys('huyen 12 @!#_ ')
            driver.find_element(By.ID, 'checkout_user_email').send_keys('abc@gmail.com')
            driver.find_element(By.ID, 'billing_address_phone').send_keys('0348498153')
            driver.find_element(By.ID, 'billing_address_address1').send_keys('Nguyễn Kiệm')
            tinh = Select(driver.find_element(By.ID, 'customer_shipping_province'))
            tinh.select_by_visible_text('Hồ Chí Minh')
            time.sleep(3)
            huyen = Select(driver.find_element(By.ID, 'customer_shipping_district'))
            huyen.select_by_visible_text('Quận Gò Vấp')
            time.sleep(5)
            xa = Select(driver.find_element(By.ID, 'customer_shipping_ward'))
            xa.select_by_visible_text('Phường 03')
            driver.find_element(By.XPATH, '//*[@id="form_next_step"]/button/i').click()
            driver.find_element(By.NAME, 'payment_method_id').click()
            ''' #click dat hang
            driver.find_element(By.XPATH, '//*[@id="form_next_step"]/button/i').click()
            '''
            print("Đặt hàng thành công")
        except:
            print("Lỗi tên không hợp lệ")

    def BO0016(): #Email: bỏ trống
        try:
            driver.find_element(By.LINK_TEXT, 'Dế mèn phiêu lưu ký').click()
            driver.find_element(By.ID, 'buy-now').click()
            driver.implicitly_wait(10)
            driver.find_element(By.ID, 'billing_address_full_name').send_keys('huyen')
            driver.find_element(By.ID, 'billing_address_phone').send_keys('0348498153')
            driver.find_element(By.ID, 'billing_address_address1').send_keys('Nguyễn Kiệm')
            tinh = Select(driver.find_element(By.ID, 'customer_shipping_province'))
            tinh.select_by_visible_text('Hồ Chí Minh')
            time.sleep(3)
            huyen = Select(driver.find_element(By.ID, 'customer_shipping_district'))
            huyen.select_by_visible_text('Quận Gò Vấp')
            time.sleep(5)
            xa = Select(driver.find_element(By.ID, 'customer_shipping_ward'))
            xa.select_by_visible_text('Phường 03')
            driver.find_element(By.XPATH, '//*[@id="form_next_step"]/button/i').click()
            driver.find_element(By.NAME, 'payment_method_id').click()
            ''' #click dat hang
            driver.find_element(By.XPATH, '//*[@id="form_next_step"]/button/i').click()
            '''
            print("Đặt hàng thành công")
        except:
            print("Lỗi:", driver.find_element(By.XPATH, '//*[@class="field-message field-message-error"]').text)

    def BO0017(): #Email: nhập sai
        try:
            driver.find_element(By.LINK_TEXT, 'Dế mèn phiêu lưu ký').click()
            driver.find_element(By.ID, 'buy-now').click()
            driver.implicitly_wait(10)
            driver.find_element(By.ID, 'billing_address_full_name').send_keys('huyen')
            driver.find_element(By.ID, 'checkout_user_email').send_keys('abcde')
            driver.find_element(By.ID, 'billing_address_phone').send_keys('0348498153')
            driver.find_element(By.ID, 'billing_address_address1').send_keys('Nguyễn Kiệm')
            tinh = Select(driver.find_element(By.ID, 'customer_shipping_province'))
            tinh.select_by_visible_text('Hồ Chí Minh')
            time.sleep(3)
            huyen = Select(driver.find_element(By.ID, 'customer_shipping_district'))
            huyen.select_by_visible_text('Quận Gò Vấp')
            time.sleep(5)
            xa = Select(driver.find_element(By.ID, 'customer_shipping_ward'))
            xa.select_by_visible_text('Phường 03')
            driver.find_element(By.XPATH, '//*[@id="form_next_step"]/button/i').click()
            driver.find_element(By.NAME, 'payment_method_id').click()
            ''' #click dat hang
            driver.find_element(By.XPATH, '//*[@id="form_next_step"]/button/i').click()
            '''
            print("Đặt hàng thành công")
        except:
            print("Lỗi:", driver.find_element(By.XPATH, '//*[@class="field-message field-message-error"]').text)

    def BO0018(): #Email: nhập email có khoảng trắng
        try:
            driver.find_element(By.LINK_TEXT, 'Dế mèn phiêu lưu ký').click()
            driver.find_element(By.ID, 'buy-now').click()
            driver.implicitly_wait(10)
            driver.find_element(By.ID, 'billing_address_full_name').send_keys('huyen')
            driver.find_element(By.ID, 'checkout_user_email').send_keys('abc de  @g mail.com')
            driver.find_element(By.ID, 'billing_address_phone').send_keys('0348498153')
            driver.find_element(By.ID, 'billing_address_address1').send_keys('Nguyễn Kiệm')
            tinh = Select(driver.find_element(By.ID, 'customer_shipping_province'))
            tinh.select_by_visible_text('Hồ Chí Minh')
            time.sleep(3)
            huyen = Select(driver.find_element(By.ID, 'customer_shipping_district'))
            huyen.select_by_visible_text('Quận Gò Vấp')
            time.sleep(5)
            xa = Select(driver.find_element(By.ID, 'customer_shipping_ward'))
            xa.select_by_visible_text('Phường 03')
            driver.find_element(By.XPATH, '//*[@id="form_next_step"]/button/i').click()
            driver.find_element(By.NAME, 'payment_method_id').click()
            ''' #click dat hang
            driver.find_element(By.XPATH, '//*[@id="form_next_step"]/button/i').click()
            '''
            print("Đặt hàng thành công")
        except:
            print("Lỗi:", driver.find_element(By.XPATH, '//*[@class="field-message field-message-error"]').text)

    def BO0019(): #Email: nhập email có dấu
        try:
            driver.find_element(By.LINK_TEXT, 'Dế mèn phiêu lưu ký').click()
            driver.find_element(By.ID, 'buy-now').click()
            driver.implicitly_wait(10)
            driver.find_element(By.ID, 'billing_address_full_name').send_keys('huyen')
            driver.find_element(By.ID, 'checkout_user_email').send_keys(' nguyễn@gmail.com')
            driver.find_element(By.ID, 'billing_address_phone').send_keys('0348498153')
            driver.find_element(By.ID, 'billing_address_address1').send_keys('Nguyễn Kiệm')
            tinh = Select(driver.find_element(By.ID, 'customer_shipping_province'))
            tinh.select_by_visible_text('Hồ Chí Minh')
            time.sleep(3)
            huyen = Select(driver.find_element(By.ID, 'customer_shipping_district'))
            huyen.select_by_visible_text('Quận Gò Vấp')
            time.sleep(5)
            xa = Select(driver.find_element(By.ID, 'customer_shipping_ward'))
            xa.select_by_visible_text('Phường 03')
            driver.find_element(By.XPATH, '//*[@id="form_next_step"]/button/i').click()
            driver.find_element(By.NAME, 'payment_method_id').click()
            ''' #click dat hang
            driver.find_element(By.XPATH, '//*[@id="form_next_step"]/button/i').click()
            '''
            print("Đặt hàng thành công")
        except:
            print("Lỗi:", driver.find_element(By.XPATH, '//*[@class="field-message field-message-error"]').text)

    def BO0020():  #Số điện thoại: bỏ trống
        try:
            driver.find_element(By.LINK_TEXT, 'Dế mèn phiêu lưu ký').click()
            driver.find_element(By.ID, 'buy-now').click()
            driver.implicitly_wait(10)
            driver.find_element(By.ID, 'billing_address_full_name').send_keys('huyen')
            driver.find_element(By.ID, 'checkout_user_email').send_keys(' abc@gmail.com')
            driver.find_element(By.ID, 'billing_address_address1').send_keys('Nguyễn Kiệm')
            tinh = Select(driver.find_element(By.ID, 'customer_shipping_province'))
            tinh.select_by_visible_text('Hồ Chí Minh')
            time.sleep(3)
            huyen = Select(driver.find_element(By.ID, 'customer_shipping_district'))
            huyen.select_by_visible_text('Quận Gò Vấp')
            time.sleep(5)
            xa = Select(driver.find_element(By.ID, 'customer_shipping_ward'))
            xa.select_by_visible_text('Phường 03')
            driver.find_element(By.XPATH, '//*[@id="form_next_step"]/button/i').click()
            driver.find_element(By.NAME, 'payment_method_id').click()
            ''' #click dat hang
            driver.find_element(By.XPATH, '//*[@id="form_next_step"]/button/i').click()
            '''
            print("Đặt hàng thành công")
        except:
            print("Lỗi:", driver.find_element(By.XPATH, '//*[@class="field-message field-message-error"]').text)

    def BO0021():  #Số điện thoại: có kí tự đặc biệt ngoài số
        try:
            driver.find_element(By.LINK_TEXT, 'Dế mèn phiêu lưu ký').click()
            driver.find_element(By.ID, 'buy-now').click()
            driver.implicitly_wait(10)
            driver.find_element(By.ID, 'billing_address_full_name').send_keys('huyen')
            driver.find_element(By.ID, 'checkout_user_email').send_keys(' abc@gmail.com')
            driver.find_element(By.ID, 'billing_address_phone').send_keys('03@grk5769')
            driver.find_element(By.ID, 'billing_address_address1').send_keys('Nguyễn Kiệm')
            tinh = Select(driver.find_element(By.ID, 'customer_shipping_province'))
            tinh.select_by_visible_text('Hồ Chí Minh')
            time.sleep(3)
            huyen = Select(driver.find_element(By.ID, 'customer_shipping_district'))
            huyen.select_by_visible_text('Quận Gò Vấp')
            time.sleep(5)
            xa = Select(driver.find_element(By.ID, 'customer_shipping_ward'))
            xa.select_by_visible_text('Phường 03')
            driver.find_element(By.XPATH, '//*[@id="form_next_step"]/button/i').click()
            driver.find_element(By.NAME, 'payment_method_id').click()
            ''' #click dat hang
            driver.find_element(By.XPATH, '//*[@id="form_next_step"]/button/i').click()
            '''
            print("Đặt hàng thành công")
        except:
            print("Lỗi:", driver.find_element(By.XPATH, '//*[@class="field-message field-message-error"]').text)

    def BO0022():  #Địa chỉ: rỗng
        try:
            driver.find_element(By.LINK_TEXT, 'Dế mèn phiêu lưu ký').click()
            driver.find_element(By.ID, 'buy-now').click()
            driver.implicitly_wait(10)
            driver.find_element(By.ID, 'billing_address_full_name').send_keys('huyen')
            driver.find_element(By.ID, 'checkout_user_email').send_keys(' abc@gmail.com')
            driver.find_element(By.ID, 'billing_address_phone').send_keys('0348498153')
            #driver.find_element(By.ID, 'billing_address_address1').send_keys('Nguyễn Kiệm')
            tinh = Select(driver.find_element(By.ID, 'customer_shipping_province'))
            tinh.select_by_visible_text('Hồ Chí Minh')
            time.sleep(3)
            huyen = Select(driver.find_element(By.ID, 'customer_shipping_district'))
            huyen.select_by_visible_text('Quận Gò Vấp')
            time.sleep(5)
            xa = Select(driver.find_element(By.ID, 'customer_shipping_ward'))
            xa.select_by_visible_text('Phường 03')
            driver.find_element(By.XPATH, '//*[@id="form_next_step"]/button/i').click()
            driver.find_element(By.NAME, 'payment_method_id').click()
            ''' #click dat hang
            driver.find_element(By.XPATH, '//*[@id="form_next_step"]/button/i').click()
            '''
            print("Đặt hàng thành công")
        except:
            print("Lỗi:", driver.find_element(By.XPATH, '//*[@class="field-message field-message-error"]').text)

    def BO0023():  #Địa chỉ không tìm thấy
        try:
            driver.find_element(By.LINK_TEXT, 'Dế mèn phiêu lưu ký').click()
            driver.find_element(By.ID, 'buy-now').click()
            driver.implicitly_wait(10)
            driver.find_element(By.ID, 'billing_address_full_name').send_keys('huyen')
            driver.find_element(By.ID, 'checkout_user_email').send_keys(' abc@gmail.com')
            driver.find_element(By.ID, 'billing_address_phone').send_keys('0348498153')
            driver.find_element(By.ID, 'billing_address_address1').send_keys('thôn a')
            tinh = Select(driver.find_element(By.ID, 'customer_shipping_province'))
            tinh.select_by_visible_text('Đắk Lắk')
            time.sleep(3)
            huyen = Select(driver.find_element(By.ID, 'customer_shipping_district'))
            huyen.select_by_visible_text('Huyện Krông Năng')
            time.sleep(5)
            xa = Select(driver.find_element(By.ID, 'customer_shipping_ward'))
            xa.select_by_visible_text('xã Dlieya')
            driver.find_element(By.XPATH, '//*[@id="form_next_step"]/button/i').click()
            driver.find_element(By.NAME, 'payment_method_id').click()
            ''' #click dat hang
            driver.find_element(By.XPATH, '//*[@id="form_next_step"]/button/i').click()
            '''
            print("Đặt hàng thành công")
        except NoSuchElementException:
            print("Lỗi không tìm thấy")

    def close():
        time.sleep(2)
        driver.close()

DatHang.load()
DatHang.BO0023()
DatHang.close()
