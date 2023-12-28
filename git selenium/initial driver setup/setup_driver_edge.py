from selenium import webdriver
from selenium.webdriver.edge.service import Service as edgeservice
from webdriver_manager.microsoft import EdgeChromiumDriverManager

edge_browser = webdriver.Edge(service=edgeservice(EdgeChromiumDriverManager().install()))

edge_browser.get('https://google.com')

input()