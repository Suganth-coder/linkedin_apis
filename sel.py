from selenium import webdriver as web
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from pyvirtualdisplay import Display
import pickle
import json
from linkedin_api import Linkedin

def func(user,passw):
    
    # display = Display(visible=0, size=(800, 600))
    # display.start()

    # Authenticate using any Linkedin account credentials
    api = Linkedin(user,passw)

    # GET a profile
    profile = api.get_profile('billy-g')

    # GET a profiles contact info
    contact_info = api.get_profile_contact_info('billy-g')

    # GET all connected profiles (1st, 2nd and 3rd degree) of a given profile
    connections = api.get_profile_connections('1234asc12304', max_connections=200)
    print(connections)