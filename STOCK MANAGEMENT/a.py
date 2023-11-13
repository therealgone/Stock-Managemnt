import psutil
import time

def get_cpu_usage():
    return psutil.cpu_percent(interval=1)

def get_ram_usage():
    return psutil.virtual_memory().percent

def get_disk_usage():
    return psutil.disk_usage('/').percent

def get_network_usage():
    return psutil.net_io_counters().bytes_sent, psutil.net_io_counters().bytes_recv

def monitor_resources(interval=5):
    try:
        while True:
            cpu_usage = get_cpu_usage()
            ram_usage = get_ram_usage()
            disk_usage = get_disk_usage()
            sent, received = get_network_usage()

            print(f"CPU Usage: {cpu_usage}% | RAM Usage: {ram_usage}% | Disk Usage: {disk_usage}%")
            print(f"Network - Sent: {sent} bytes | Received: {received} bytes\n")

            time.sleep(interval)

    except KeyboardInterrupt:
        print("Monitoring stopped.")

if __name__ == "__main__":
    monitor_resources()
