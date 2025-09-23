from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import anthropic
from bs4 import BeautifulSoup
from utils.config import Config

from dotenv import load_dotenv
load_dotenv()

class DOMXPathLocator:
    def __init__(self, driver,page_url):
        self.client = anthropic.Anthropic(api_key=Config.get_anthropic_api_key())
        self.driver =  driver
        self.page_url = page_url
    
    def get_page_dom(self, url):
        try:
            self.driver.get(url)
            
            # Wait for page to load
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, "body"))
            )
            
            page_source = self.driver.page_source
            
            # Use BeautifulSoup to remove script and style elements to reduce noise
            soup = BeautifulSoup(page_source, 'html.parser')

            for script in soup(["script", "style"]):
                script.extract()
            
            return str(soup)
            
        except Exception as e:
            raise Exception(f"Error loading page: {str(e)}")
    
    def get_xpath(self, dom_content, element_description):
        prompt = f"""You are a webpage XPath extraction AI assistant. 
        
Given the following HTML DOM and a description of the element to locate, return ONLY the exact XPath selector as plain text with no additional formatting, explanations, or code blocks.

DOM:
{dom_content}

Element to locate: {element_description}

Return only the XPath selector:"""

        try:
            response = self.client.messages.create(
                model="claude-3-7-sonnet-20250219",
                max_tokens=100,
                messages=[
                    {
                        "role": "user",
                        "content": prompt
                    }
                ]
            )
            
            # Extract the XPath from response
            xpath = response.content[0].text.strip()
            
            # Clean up any potential formatting
            if xpath.startswith('```'):
                xpath = xpath.split('\n')[1]
            if xpath.endswith('```'):
                xpath = xpath.replace('```', '')
            
            return xpath.strip()
            
        except Exception as e:
            raise Exception(f"Error calling Anthropic API: {str(e)}")
    
    def validate_xpath(self, xpath):
        try:
            elements = self.driver.find_elements(By.XPATH, xpath)
            return len(elements) > 0, len(elements)
        except Exception as e:
            return False, 0
        
    def find_element_by_xpath(self, element_description):
        try:
            dom = self.get_page_dom(self.page_url)
            xpath = self.locator.get_xpath(dom, element_description)
            is_valid = self.locator.validate_xpath(xpath)
            
            if is_valid:
                return self.driver.find_element(By.XPATH, xpath)
        except Exception as e:
            raise Exception(f"Error finding element by XPath - {xpath}: {str(e)}")