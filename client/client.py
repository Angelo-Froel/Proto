import requests
import time

url = 'http://load_balancer'

# Function to send a packet and calculate RTT
def send_packet():
    start_time = time.time()
    response = requests.get(url)
    end_time = time.time()
    rtt = end_time - start_time
    print("Response from server:", response.text)
    print("Round trip time:", rtt)

# Send packets continuously
while True:
    send_packet()
    time.sleep(1)  # Adjust the interval between packets as needed
