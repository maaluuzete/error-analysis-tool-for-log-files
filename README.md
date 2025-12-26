# LogFinder  
*(Based on the exercise [LogFinder](https://example.com) inspired by common system administration tasks)*

This project was developed as a **command-line tool in Python** to analyze log files and identify periods with the highest concentration of errors.  
It focuses on efficient **file processing**, **timestamp handling**, and the use of a **sliding window algorithm** to optimize error detection in large log files.

---

## Features
- Process large log files line by line without loading the entire file into memory;
- Identify log entries containing the keyword `ERROR`;
- Convert timestamps (`HH:MM:SS`) to seconds for arithmetic operations;
- Use a **sliding window** approach to find the busiest error periods;
- Print the start and end times of the window with the highest number of errors along with the total error count.

> **Note**  
> This tool focuses on **log analysis** and does not modify or interact with live systems.

---

## Data Structures Used

- **Deque (`collections.deque`)**  
  Maintains the timestamps of errors inside the active window efficiently. Allows **O(1)** insertion and removal from both ends.

- **Integer arithmetic**  
  Converts timestamps to seconds to facilitate quick comparisons and window calculations.

---

## How to Run

Follow the steps below to run the project locally:

```bash
git clone https://github.com/your-username/logfinder.git
cd logfinder
python logfinder.py <path_to_log_file> <window_size_in_seconds>
```
## Project Structure

```
logfinder/
│── logfinder.py
│── events.log
│── README.md
```
