# Internet-Speed-Test-with-Python
This project is a Python-based Internet Speed Test tool with a graphical user interface (GUI) built using Tkinter. It allows users to test their internet speed and view historical speed test results as a graph with dual y-axes for download and upload speeds. Whether you're curious about your connection or want to monitor changes over time, this app has you covered.

# Features
- **Test Internet Speed**: Perform download and upload speed tests.
- **Save Results**: Automatically save speed test results along with the date and time to a CSV file.
- **View Historical Data**: Display a line graph showing historical download and upload speeds, each with its own y-axis for better visualisation.

# Technologies Used
- Python: Core programming language.
- Tkinter: GUI framework.
- Speedtest: Used for internet speed tests.
- Matplotlib: Used for plotting historical data.
- CSV: For storing historical test results.

# File Structure
- main.py: Main script containing the GUI and logic.
- speedtest_results.csv: CSV file that stores the historical speed test data.

# CSV Format
The results are saved in speedtest_results.csv with the following structure:

| Date & Time | Download Speed (Mbps) | Upload Speed (Mbps) |
| ----------- | --------------------- | --------------------| 
| 2024-11-13 13:43:16 | 67.18 | 2.13 |
| 2024-11-13 13:43:42 | 55.17 | 1.98 |

This file grows as you keep testing, giving you a reliable historical record.

# Why You’ll Love It
Ever wondered how your internet speed fluctuates throughout the day or over weeks? This tool not only gives you instant results but also helps you track your connection’s performance over time. Perfect for identifying patterns or proving to your provider that your speeds aren't up to par!

# Why I Built This
I wanted a way to better understand my internet performance and showcase my programming skills. This project combines useful functionality with a clean, interactive interface—and it’s a great way to demonstrate my ability to work with data, GUIs, and visualisation.

https://github.com/user-attachments/assets/09c3e412-b765-4b74-be1e-afd131d51698
