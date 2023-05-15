from selenium import webdriver
options = webdriver.FirefoxOptions()
options.headless = True
browser = webdriver.Firefox(executable_path=r"C:\Users\corp1\OneDrive\Masaüstü\geckodriver.exe",firefox_profile=r"C:\Users\corp1\AppData\Roaming\Mozilla\Firefox\Profiles\kfbwpp0c.dev-edition-default")
browser.fullscreen_window()