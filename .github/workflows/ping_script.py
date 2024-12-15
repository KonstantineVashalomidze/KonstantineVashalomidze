import requests
import schedule
import time
import logging

def ping_endpoints():
    endpoints = [
        "https://financial-instruments-platform-backend.onrender.com/swagger-ui/index.html",  
        "https://mock-data-generation-service.onrender.com/swagger-ui/index.html",
        "https://financial-instruments-platform-frontend.onrender.com/dashboard"
    ]
    
    for url in endpoints:
        try:
            response = requests.get(url, timeout=10)
            logging.info(f"Pinged {url}. Status code: {response.status_code}")
        except Exception as e:
            logging.error(f"Error pinging {url}: {e}")

def main():
    logging.basicConfig(level=logging.INFO)
    ping_endpoints()

if __name__ == "__main__":
    main()
