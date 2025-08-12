# Lab Sample Integration Plugin (Python Demo)

This is a demo Python script that simulates a lightweight SLIMS integration plugin.

It:
- Reads sample data from a CSV file (like instrument output)
- Filters and cleans the data
- Formats each entry into JSON
- Sends each sample to a mock API endpoint
- Logs activity to a file (`plugin_log.txt`)
- Prints progress to the console

---

## Files

| File | Description |
|------|-------------|
| `lab_samples.csv` | Sample input data (CSV) |
| `lab_data_plugin.py` | Python script for reading, cleaning, and sending data |
| `plugin_log.txt` | Log file created automatically after running the script |
| `README.md` | You're reading it! |

---

## Requirements

You need Python 3 installed and the following packages:

```bash
pip install pandas requests
```

---

## How to Run

1. Make sure you're in the folder with the script and CSV file
2. Run the script:

```bash
python lab_data_plugin.py
```

You’ll see output in the terminal showing the data processing and sending.

Logs are also saved to `plugin_log.txt`.

---

##  Sample Output (console)

```
 Loaded CSV file.
 Cleaned data. 3 valid samples found.
 Sent sample S001 successfully.
 Sent sample S004 successfully.
 Sent sample S005 successfully.
```

---

##  Mock API

The script uses this mock API for demo purposes:
> https://jsonplaceholder.typicode.com/posts

No real data is stored — it's just for testing.

---

##  Customization Ideas

You can expand the script to:
- Read from Excel or instrument-generated files
- Connect to a real API or database
- Add email or retry logic
- Trigger the script on file drop (automation)

---
