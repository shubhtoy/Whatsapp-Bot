import PySimpleGUI as sg
import threading
import json
from itertools import *
import sys
import os
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from PIL import Image, ImageDraw, ImageFont
import gspread
from oauth2client.service_account import ServiceAccountCredentials

import time
import os

#
# fnt = ImageFont.truetype("./program/Comfortaa-Bold.ttf", 43)


def sender(lis):
    options = Options()
    options.add_argument("--user-data-dir=./Data")
    driver = webdriver.Chrome(
        executable_path="./program/chromedriver.exe", options=options
    )

    driver.get("https://web.whatsapp.com")
    for name in lis:
        element = WebDriverWait(driver, 100).until(
            EC.element_to_be_clickable((By.XPATH, "//div[@contenteditable='true']"))
        )
        element.send_keys(name)
        element.send_keys(Keys.ENTER)
        # img='C:\\Users\\shivam sethi\\Desktop\\test.jpg'
        # img2='C:\\Users\\shivam sethi\\Desktop\\pil_text.png'
        element = WebDriverWait(driver, 100).until(
            EC.element_to_be_clickable((By.XPATH, "//span[@data-testid='clip']"))
        )
        element.click()
        element = driver.find_element_by_css_selector("input[type='file']")
        element.send_keys(
            "D:\\Shared drives\\Shubh Data\\Everything Python\\Pending\\Temp\\test.jpg"
        )
        element = WebDriverWait(driver, 100).until(
            EC.element_to_be_clickable(
                (
                    By.XPATH,
                    "/html/body/div[1]/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/div[1]/span/div/div[2]/div/div[3]/div[1]/div[2]",
                )
            )
        )
        # /html/body/div[1]/div/div/div[4]/div/div[3]/div/div/div[3]/div[9]/div/div/div/div/div[1]/div[1]/div/div[2]

        # maximize_window()
        # element = driver.find_element_by_xpath(
        #     "//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/span[1]/div[1]/span[1]/div[1]/div[1]/div[2]/input[1]"
        # )
        element.send_keys(Keys.ENTER)

        while True:
            try:

                element = WebDriverWait(driver, 3).until(
                    EC.presence_of_element_located(
                        (
                            By.XPATH,
                            "/html/body/div[1]/div/div/div[4]/div/div[3]/div/div/div[3]/div[9]/div/div/div/div/div[1]/div[1]/div/div[2]",
                        )
                    )
                )
            except Exception as e:
                print(f"Message sent:{name}")
                break

    # element = WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable(
    #         (
    #             By.XPATH,
    #             "//body/div[@id='app']/div[1]/div[1]/div[2]/div[2]/span[1]/div[1]/span[1]/div[1]/div[1]/div[2]/span[1]/div[1]/div[1]",
    #         )
    #     )
    # )
    # element.click()
    # time.sleep(7)
    # driver.minimize_window()
    # print("=========================================")
    # print("-Completed-")
    # time.sleep(10000000000)


# def long_function(patient, patient_wa, driver):
#     print("=========================================")
#     print("-Starting-")
#     threading.Thread(
#         target=long_function_thread, args=(patient, patient_wa, driver), daemon=True
#     ).start()


# sg.theme("DarkBlack")

# # fin__ = "\u0332".join(text__)
# layout = [
#     [sg.Output(size=(70, 10))],
#     [sg.Text("Diet Sender", font=("Helvetica", 25))],
#     [
#         sg.Text("Enter Patient Name:\t", font=("Arial", 10)),
#         sg.Input(key="patient", font=("Arial", 10)),
#     ],
#     [
#         sg.Text("Enter Whatsapp Name:        ", font=("Arial", 10)),
#         sg.Input(key="patient-wa", font=("Arial", 10)),
#     ],
#     [sg.Submit("Enter", key="Submit"), sg.Cancel("Exit", key="Exit")],
# ]

# # layout = [[sg.Output(size=(60,10))],
# #           [sg.Button('Go'), sg.Button('Nothing'), sg.Button('Exit')]  ]

# window = sg.Window("Dietitian Bhawana", layout, icon="Program/Python.ico")
# options = Options()
# options.add_argument("--user-data-dir=./Data")
# driver = webdriver.Chrome(executable_path="./program/chromedriver.exe", options=options)

# driver.get("https://web.whatsapp.com")
# driver.minimize_window()

# while True:  # Event Loop
#     try:
#         event, values = window.read()
#         patient = values["patient"]
#         patient_wa = values["patient-wa"]
#         if event == "Submit":
#             if len(patient) != 0 and len(patient_wa) != 0:
#                 long_function(patient, patient_wa, driver)
#             else:
#                 pass
#         elif event == "Exit":
#             break
#         # if event == sg.WIN_CLOSED or event == 'Exit':
#         #     break
#         # if event == 'Go':
#         #     print('About to go to call my long function')
#         #     long_function()
#         #     print('Long function has returned from starting')
#         # elif event == '-THREAD DONE-':
#         #     print('Your long operation completed')
#     except Exception as e:
#         print(e)
#         driver.close()
#         window.close()

import csv

with open("fin.txt", "r+") as f:
    a = f.readlines()
    a = [i.replace("\n", "") for i in a]
    # print(len(*a))?
sender(a)
# with open("contact2.csv", "r+") as f:
#     a = csv.reader(f)
#     # print(len(*a))?
#     # list1 = []
#     for i in a:
#         print(i)
# print(type(lis1))
# A = "ss"
# sender(A)