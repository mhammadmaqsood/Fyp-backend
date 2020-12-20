from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import requests
from selenium.webdriver import ActionChains
import csv
import time

driver = webdriver.Chrome(executable_path="E:\Instafol\Instagram\chromedriver.exe")
driver.get("https://www.instagram.com/")
driver.maximize_window()

# Login to Instagram Page
def login():
    try:
        username = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input"))
        )
        password = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input"))
        )
        login = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located(
                (By.XPATH, "//*[@id='loginForm']/div/div[3]/button")))
        username.send_keys("_motivation_with_stonescave_")
        password.send_keys("hd739145852")
        login.click()
        not_now = wait(
            find_element(
                (By.XPATH, "//*[@id='react-root']/section/main/div/div/div/div/button"))
        )
        if not_now.is_displayed():
            not_now.click()
            not_now_final = wait(
                find_element(
                    (By.XPATH, "/html/body/div[4]/div/div/div/div[3]/button[2]")))
            if not_now_final.is_displayed():
                not_now_final.click()
    finally:
            search(index)

# Like posts and comments on pages
def postLike(index, account, comment):
        try:
            time.sleep(10)
            post = wait(
                find_element(
                    (By.XPATH,
                     "//*[@id='react-root']/section/main/div/div[3]/article/div[1]/div/div[1]/div[1]/a/div/div[2]"))
            )
            # driver.execute_script("arguments[0].scrollIntoView();", post)
            # time.sleep(2)
            post.click()
            time.sleep(2)
            like = wait(
                find_element((By.XPATH, "/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button/div/span")))
            like.click()
            next_post = wait(find_element((By.XPATH,
                                           "/html/body/div[5]/div[1]/div/div/a")))
            for postLike in range(0, 2):
                next_post.click()
                time.sleep(2)
                like = wait(
                    find_element(
                        (By.XPATH, "/html/body/div[5]/div[2]/div/article/div[3]/section[1]/span[1]/button/div/span"))
                )
                like.click()
                time.sleep(2)
                if comment:
                    comment = wait(
                        find_element(
                            (By.XPATH, "/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea"))
                    )
                    comment.click()
                    # comment.clear()
                    write_comment = wait(
                        find_element(
                            (By.XPATH, "/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/textarea"))
                    )
                    write_comment.send_keys(cmnt)
                    time.sleep(2)
                    post_comment = wait(
                        find_element(
                            (By.XPATH, "/html/body/div[5]/div[2]/div/article/div[3]/section[3]/div/form/button"))
                    )
                    post_comment.click()
                    time.sleep(3)
            close_post = wait(find_element((By.XPATH, "/html/body/div[5]/div[3]/button/div")))
            close_post.click()
            index = index + 1
            if index < len(account):
                search(index)
            else:
                print("Done with posts likes and comments")
        except Exception as e:
            print(e)
        finally:
            # driver.close()
            print("Posts Liked")
def followAccounts():
    try:
        followers = wait(find_element((By.XPATH, "//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a")))
        followers.click()
        for i in range(4):
            for j in range(0,10):
                # j = 0
                follow_btn = wait(
                    EC.presence_of_all_elements_located((By.CSS_SELECTOR, ".sqdOP.L3NKy.y3zKF     ")))
                follow_btn[j].click()
                time.sleep(2)

    except Exception as e:
        print(e)
    finally:
        # driver.close()
        print("Accounts Followed")

# Account Search
def search(index):
    try:
        search = wait(find_element((By.XPATH, "//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")))
        search.send_keys(account[index])
        acc_one = wait(find_element((By.XPATH,
                                     "//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/div[3]/div[2]/div/a[1]/div")))
        acc_one.click()
    finally:
        if post_like:
            postLike(index, account, comment)
        if follow:
            followAccounts()
        else:
            # driver.close()
            print("Done")


if __name__ == '__main__':
    wait = WebDriverWait(driver, 30).until
    find_element = EC.presence_of_element_located
    # Set post_like, comment and follow true if you want to like posts,comments and follow otherwise mark them as false
    post_like = True
    comment = True
    follow = True
    index = 0
    # Add account names you want to like posts
    account = ['hubtosucceedd']
    cmnt = "Awesome content"
    login()

