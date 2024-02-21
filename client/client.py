import requests
import time

def main():
    start_time = time.time()
    response = requests.get('http://load_balancer')
    end_time = time.time()
    print("Response:", response.text)
    print("Round Trip Time:", end_time - start_time)

if __name__ == "__main__":
    main()
