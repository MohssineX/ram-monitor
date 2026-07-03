# ram-monitor

A lightweight terminal-based RAM monitoring tool written in Python.
Displays real-time memory usage with color-coded status indicators.

---

## Overview

ram-monitor continuously tracks system memory usage and displays it in the terminal with color-coded output based on consumption levels. It is designed to be simple, cross-platform, and dependency-minimal.

---

## Features

- Real-time RAM usage monitoring
- Color-coded output based on usage thresholds
- Cross-platform support: Windows and Linux
- Lightweight with minimal dependencies
- Clean terminal display with automatic refresh

---

## Requirements

- Python 3.6 or higher
- psutil

---

## Installation

**Clone the repository:**

```bash
git clone https://github.com/MohssineX/ram-monitor
cd ram-monitor
```

**Install dependencies:**

```bash
pip install psutil
```
---

## Usage

```bash
python ram-monitor.py
```
> **Tip:** If `python` does not work, try:
> ```bash
> python3 ram-monitor.py
> ```

To stop the monitor, press `Ctrl+C`. A goodbye message will be displayed before exiting.

---

## Status Thresholds

| RAM Usage     | Status      | Color  |
|---------------|-------------|--------|
| Below 60%     | Very Good   | Green  |
| 60% to 79%    | Good        | Orange |
| 80% and above | Bad         | Red    |

---

## Platform Notes

- **Linux**: Full support including terminal clear via ANSI escape codes.
- **Windows**: Full support. ANSI escape codes are enabled automatically at startup.

---

## License

This project is licensed under the **[GNU General Public License v3.0](https://www.gnu.org/licenses/gpl-3.0.html)** 

---

## Author

**Mohssine :**
[ https://github.com/MohssineX](https://github.com/MohssineX)

---

## 🐱 Special Thanks

A special thanks to mimi — the legendary, the great, the gentle cat. 
