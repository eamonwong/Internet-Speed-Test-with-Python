import tkinter as tk
from tkinter import messagebox
import csv
import os
from datetime import datetime
import matplotlib.pyplot as plt
import speedtest


# Function to run the speed test and save the results
def test_internet_speed():
    try:
        st = speedtest.Speedtest()
        download_speed = st.download() / 1000000  # Convert to Mbps
        upload_speed = st.upload() / 1000000  # Convert to Mbps

        save_results(download_speed, upload_speed)

        result_label.config(text=f"Download Speed: {download_speed:.2f} Mbps\nUpload Speed: {upload_speed:.2f} Mbps")
    except speedtest.SpeedtestException as e:
        messagebox.showerror("Error", f"An error occurred: {str(e)}")


# Function to save results with timestamp
def save_results(download_speed, upload_speed):
    file_exists = os.path.isfile('speedtest_results.csv')
    with open('speedtest_results.csv', 'a', newline='') as file:
        writer = csv.writer(file)
        if not file_exists:
            writer.writerow(["Date & Time", "Download Speed (Mbps)", "Upload Speed (Mbps)"])  # Header
        current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        writer.writerow([current_time, download_speed, upload_speed])


# Function to plot historical results with two y-axes
def plot_results():
    if not os.path.isfile('speedtest_results.csv'):
        messagebox.showinfo("No Data", "No historical data available.")
        return

    dates, download, upload = [], [], []

    # Read data from the CSV file
    with open('speedtest_results.csv', 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            dates.append(row["Date & Time"])
            download.append(float(row["Download Speed (Mbps)"]))
            upload.append(float(row["Upload Speed (Mbps)"]))

    # Create the figure and the first axis
    fig, ax1 = plt.subplots(figsize=(10, 6))

    # Plot download speed on the first y-axis
    ax1.plot(dates, download, label="Download Speed (Mbps)", color="tab:blue", marker="o")
    ax1.set_xlabel('Date & Time')
    ax1.set_ylabel('Download Speed (Mbps)', color="tab:blue")
    ax1.tick_params(axis='y', labelcolor="tab:blue")
    ax1.tick_params(axis='x', rotation=45)

    # Create a second y-axis for upload speed
    ax2 = ax1.twinx()
    ax2.plot(dates, upload, label="Upload Speed (Mbps)", color="tab:orange", marker="o")
    ax2.set_ylabel('Upload Speed (Mbps)', color="tab:orange")
    ax2.tick_params(axis='y', labelcolor="tab:orange")

    # Add title and legend
    plt.title('Internet Speed Over Time')
    fig.tight_layout()

    # Display the plot
    plt.show()

root = tk.Tk()
root.title("Internet Speed Test")

frame = tk.Frame(root)
frame.pack(pady=20)

result_label = tk.Label(frame, text="Click 'Start Test' to begin", font=("Helvetica", 12))
result_label.pack(pady=10)

start_button = tk.Button(frame, text="Start Test", command=test_internet_speed, height=1)
start_button.pack(side=tk.LEFT, padx=10)

history_button = tk.Button(frame, text="Show History", command=plot_results, height=1)
history_button.pack(side=tk.LEFT, padx=10)

root.mainloop()
