# from instabot import Bot

# user=Bot()

# user.login(username="chipmunk.3986088",password="Neeraj@1234")
# print("Login Successfully")

# from instagrapi import Client

# cl = Client()
# cl.login("chipmunk.3986088", "Neeraj@1234")
# print("Login Successful!")

# from instabot import Bot
# bot = Bot()
# bot.login(username="chipmunk.3986088", password="Neeraj@1234")

# import instaloader

# # Create an instance
# L = instaloader.Instaloader()

# # Login (It's better to use session files for repeated logins)
# USER = "chipmunk.3986088"
# PASSWORD = "Neeraj@1234"
# L.login(USER, PASSWORD) 

# # Get profile
# profile = instaloader.Profile.from_username(L.context, "target_username")

# # Print follower count
# print(f"Followers: {profile.followers}")

# from selenium import webdriver
# from selenium.webdriver.common.by import By
# from selenium.webdriver.chrome.service import Service
# from webdriver_manager.chrome import ChromeDriverManager
# import time

# # Setup Chrome
# driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

# def insta_login(username, password):
#     driver.get("https://instagram.com")
#     time.sleep(3) # Wait for page load
    
#     # Fill credentials
#     driver.find_element(By.NAME, "username").send_keys(username)
#     driver.find_element(By.NAME, "password").send_keys(password)
    
#     # Click Login
#     driver.find_element(By.XPATH, "//button[@type='submit']").click()
#     time.sleep(5)

# # Example usage
# insta_login("chipmunk.3986088", "Neeraj@1234")

