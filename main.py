#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  9 17:25:12 2022

@author: Apostolos Tsetoglou
@github: https://github.com/atsetoglou
"""
import os
from time import sleep
from datetime import datetime
from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.common.by import By
import smtplib

def sendEmail(link):
    message = "Dear customer,\n\nWe have the pleasure to announce you that the product you love that much ( "+link+" ) is finally available.\n\nPlease order as soon as possible.\n\nYours sincerely,\nAvailability Bot"
    
    email = "availability.bot@gmail.com"    # Replace email
    password = "password"                   # Replace password
    # set up the SMTP server
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)        # Personally I am using gmail but you can use whatever you want
    server.login(email, password)
    
    # Prepare the mail
    mailTo = ["mailTo@gmail.com"]           # Replace email | You can add more than one email addresses in the list
    subject = "Product AVAILABLE"           # Change subject if you want

    message = "subject: "+subject+"\n"+message    
    
    # Send the mail
    server.sendmail(email, mailTo, message)
    server.quit()

# the list of links you want to verify
links = ["https://www.amazon.fr/dp/B084DWG2VQ/ref=cm_sw_em_r_mt_dp_QRA607JJVGMV1Z5N52HD"]

# isAvailable is an element in the source page indicating that our
# product is available (see the README to learn more on its selection)
isAvailable = "En stock."

while len(links)!=0:
    for link in links:
        service = Service(os.path.join(os.getcwd(),"resources/geckodriver"))
        browser = webdriver.Firefox(service=service)
        browser.get(link)
        
        cookies_button = browser.find_element(By.ID, "sp-cc-accept") # We need to find the cookies button in order
        cookies_button.click()                                       # to accept and continue.

        availability = browser.find_element(By.ID, "availability") # Find the availability section in the page source

        if isAvailable in availability.text:
            print(datetime.now().strftime("%d/%m/%Y %H:%M:%S")+"\tProduct Available")
            links.pop(links.index(link))
            sendEmail(link)
        else:
            print(datetime.now().strftime("%d/%m/%Y %H:%M:%S")+"\tNot Available")

        browser.close()

    if len(links)!=0:
        sleep(3600) # Wait for one hour until the next try 
