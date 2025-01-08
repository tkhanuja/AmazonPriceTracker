import requests
from bs4 import BeautifulSoup
import pandas as pd
import datetime
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os
import logging
import time
import csv
load_dotenv()

EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS')
EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD')
LOG_FILE = os.getenv('LOG_FILE')

logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format='%(asctime)s:%(levelname)s:%(message)s')


def get_price_components(soup, classes):
    """Extracts and combines price components from given class names."""
    price_parts = []
    for cls in classes:
        part = soup.find("span", {"class": cls})
        if part:
            price_parts.append(part.get_text(strip=True))
        
    return ''.join(price_parts) if price_parts else None


def get_amazon_price(url,retries = 5, delay = 3):
    
    headers={"accept-language": "en-US,en;q=0.9","accept-encoding": "gzip, deflate, br","User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36","accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"}
    price_classes = ["a-price-whole", "a-price-fraction"]
    
    for attempt in range(retries):
        try:
            resp = requests.get(url, headers=headers)
            print(f"HTTP Status Code: {resp.status_code}")

            if resp.status_code != 200:
                print(f"Failed to retrieve the page. Status code: {resp.status_code}")
                continue

            soup = BeautifulSoup(resp.text, 'html.parser')

    
            try:
                price_tag = soup.find("span", {"class": "a-price"})
                if price_tag:
                    price = get_price_components(price_tag, price_classes)
                    if not price:
                        # If combined price parts are empty, get text from price tag directly
                        price = price_tag.get_text(strip=True)
                    
                    print("Current price is: ", price)
                    return price
                else:
                    print("Price not found, retrying...")
                    time.sleep(delay)  # Wait before retrying

            except Exception as e:
                print(f"Exception occurred while finding price: {e}")
                time.sleep(delay)  # Wait before retrying

        except Exception as e:
            print(f"Exception occurred during request: {e}")
            time.sleep(delay)  # Wait before retrying

    print("Failed to retrieve price after multiple attempts.")
    return None



def track_price(url, csv_file, price,name, desired_price):
    # price = get_amazon_price(url)
    date = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    new_data = pd.DataFrame({"Item": name, 'Date': [date], 'Current Price': [price]})
    
    try:
        existing_data = pd.read_csv(csv_file)
        updated_data = pd.concat([existing_data, new_data])
        logging.info(f"Tracked price: {price}")
    except FileNotFoundError:
        logging.error(f"Error tracking price")
        updated_data = new_data

    updated_data.to_csv(csv_file, index=False)
    print(price)
    return price

def send_email(subject, body, to_email):
    try:
        msg = MIMEMultipart()
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body, 'plain'))

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        text = msg.as_string()
        server.sendmail(EMAIL_ADDRESS, to_email, text)
        server.quit()
        print("Message has been sent:)")
        logging.info(f"Sent email to {to_email}")
        
    except Exception as e:
        logging.error(f"Error sending email: {e}")





def main():
   
    try:
        with open('items.csv', mode='r') as file:
            reader = csv.DictReader(file)
            
            for row in reader:
                
                name = row["Item"]
                url = row['URL']
                desired_price = float(row['desired_price'])
                print(f"Checking price for URL: {name} with desired price: {desired_price}")
                
        
                current_price = get_amazon_price(url)
               
                if float(current_price.replace('$', '').replace(',', '')) < desired_price:
                    send_email(f'Price Alert For {name}', f'The price for your item is now {current_price}', EMAIL_ADDRESS)
                else:
                    print("Sorry, price is still too high:(")
                track_price(url, "price_data.csv" , current_price, name, desired_price)
                
    except Exception as e:
        logging.error(f"Error in main script: {e}")

if __name__ == "__main__":

    main()
