# ram-monitor

A lightweight terminal utility for monitoring system RAM usage in real time.

## Features

* Real-time memory monitoring
* Displays total, used, and available RAM
* Live RAM usage percentage
* Color-coded status indicators
* Automatic terminal refresh
* Supports both Linux and Windows
* Lightweight and easy to use

## Requirements

* Python 3.x
* psutil

## Installation

```bash
git clone https://github.com/MohssineX/ram-monitor.git
cd ram-monitor
```

Install the required dependency:

```bash
pip install psutil
```

## Usage

Run the program:

```bash
python ram-monitor.py
```

If your system uses `python3`:

```bash
python3 ram-monitor.py
```

The monitor updates automatically and displays:

* Total RAM
* Used RAM
* Available RAM
* Memory usage percentage
* Current memory status

Stop the monitor at any time with:

```text
Ctrl + C
```

## Status Levels

| RAM Usage | Status    |
| --------- | --------- |
| Below 60% | Very Good |
| 60% – 79% | Good      |
| 80%+      | Bad       |

## Platform Support

* Linux
* Windows

ANSI color support is enabled automatically on Windows.

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
