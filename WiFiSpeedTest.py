import speedtest
import time

def main_menu():
    print("--- WiFi Speed Test ---\n")
    print("1. Test Download Speed")
    print("2. Test Upload Speed")
    print("3. Test Latency")
    print("4. Test Ping")
    print("5. Test Jitter")
    print("6. Test Max Speed")
    print("7. Exit")
    choice = int(input("Enter your choice: "))
    return choice

def download_speed():
    st = speedtest.Speedtest()
    download_speed = st.download() / 10**6
    print("\nDownload speed: {:.2f} Mbps".format(download_speed))
    time.sleep(2)

def upload_speed():
    st = speedtest.Speedtest()
    upload_speed = st.upload() / 10**6
    print("\nUpload speed: {:.2f} Mbps".format(upload_speed))
    time.sleep(2)

def latency():
    st = speedtest.Speedtest()
    server = st.get_best_server()
    latency = server['latency']
    print("\nLatency: {:.2f} ms".format(latency))
    time.sleep(2)

def ping():
    st = speedtest.Speedtest()
    server = st.get_best_server()
    ping = server['latency']
    print("\nPing: {:.2f} ms".format(ping))
    time.sleep(2)

def jitter():
    st = speedtest.Speedtest()
    server = st.get_best_server()
    jitter = server['jitter']
    print("\nJitter: {:.2f} ms".format(jitter))
    time.sleep(2)

def max_speed():
    st = speedtest.Speedtest()
    st.get_best_server()
    max_speed = st.download() / 10**6
    print("\nMax Speed: {:.2f} Mbps".format(max_speed))
    time.sleep(2)

while True:
    choice = main_menu()
    if choice == 1:
        download_speed()
    elif choice == 2:
        upload_speed()
    elif choice == 3:
        latency()
    elif choice == 4:
        ping()
    elif choice == 5:
        jitter()
    elif choice == 6:
        max_speed()
    elif choice == 7:
        print("Exiting...")
        break
    else:
        print("Invalid choice. Try again.")
