# 🧾 Spending Report Tool

This is a simple Python desktop tool built with Tkinter that lets you generate an Excel spending report from a CSV file — complete with a daily chart, data labels, and automatic file output.

---

## 📂 Project Overview

This tool reads a bank statement in CSV format with just two columns:

1. `Date` – in any format
2. `Turnover` – positive numbers for income, negative numbers for spending

It then:
- Calculates your total daily spending
- Turns spending into positive values
- Creates a line chart with labeled values in euros (€)
- Outputs a clean Excel file with both the data and the chart
- Automatically opens the report when done ✅

---

## 📄 Included Dummy File

A sample file named `Master.csv` is included. You can open it in Excel and fill in:
- Dates in the first column (e.g., `03.06.2025`)
- Spending or income in the second column (e.g., `-15.75` for spending or `200` for income)

| Date       | Turnover |
|------------|----------|
| 01.04.2025 | -25.50   |
| 02.04.2025 | 100.00   |
| 03.04.2025 | -40.75   |

---

## 🚀 How to Use It

1. Clone this repository or download the ZIP
2. Install required Python libraries (refer to requirements)
3. Run the script

🧠 Skills Demonstrated
This project highlights key skills in:

🐍 Python scripting for automation

🖼 Tkinter GUI design for desktop apps

📊 Data visualization using Matplotlib

📋 Data processing and transformation using Pandas

⚙️ File system operations and subprocess handling

🧪 Error handling and clean user interaction

🛠 Packaging small tools for non-technical users


