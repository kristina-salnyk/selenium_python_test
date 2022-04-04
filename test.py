import test_case

driver_params = {'webdriver': './chromedriver.exe', 'lang': '--lang=en', 'login': 'kristina.salnyk.test.acc@gmail.com',
                 'password': 'test.password'}
test = test_case.Test(driver_params)

test.open_page('https://mail.google.com/')
test.auth()

email_count = 10
test.send_email(email_count)
email_data = test.read_email(email_count)

test.send_report(email_data)
test.delete_email(email_data)

del test
