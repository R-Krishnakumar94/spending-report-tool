import tkinter as tk
from tkinter import filedialog, messagebox
import pandas as pd
import matplotlib.pyplot as plt
from openpyxl import Workbook
from openpyxl.drawing.image import Image as XLImage
from openpyxl.utils.dataframe import dataframe_to_rows
import subprocess
import os

def generate_report(filepath):
    try:
        # STEP 1: Load the CSV
        df = pd.read_csv(filepath)
        df['Date'] = pd.to_datetime(df['Date'], format='%d.%m.%Y')
        df['Turnover'] = pd.to_numeric(df['Turnover'], errors='coerce')

        # STEP 2: Extract spending (turn negatives into positive spending)
        df['Spending'] = df['Turnover'].apply(lambda x: -x if x < 0 else 0)
        daily_spending = df.groupby('Date')['Spending'].sum().reset_index()

        # STEP 3: Create a graph
        plt.figure(figsize=(10, 5))
        plt.plot(daily_spending['Date'], daily_spending['Spending'], color='red', marker='o')
        plt.title('Day-to-Day Spending')
        plt.xlabel('Date')
        plt.ylabel('Amount Spent (€)')
        plt.grid(True)

        for i in range(len(daily_spending)):
            x = daily_spending['Date'].iloc[i]
            y = daily_spending['Spending'].iloc[i]
            plt.text(x, y + 1, f"€{y:.2f}", ha='center', fontsize=8, rotation=45)

        plt.tight_layout()
        chart_path = "spending_chart.png"
        plt.savefig(chart_path)
        plt.close()

        # STEP 4: Create Excel report
        wb = Workbook()
        ws = wb.active
        ws.title = "Spending Summary"

        for row in dataframe_to_rows(daily_spending, index=False, header=True):
            ws.append(row)

        img = XLImage(chart_path)
        img.anchor = "E2"
        ws.add_image(img)

        # STEP 5: Save Excel file next to the CSV file
        output_path = os.path.join(os.path.dirname(filepath), "Spending_Report.xlsx")
        wb.save(output_path)

        messagebox.showinfo("✅ Done!", f"Excel report saved at:\n{output_path}")

        # 🟢 NEW: Open the Excel file automatically
        subprocess.Popen(['start', output_path], shell=True)

    except Exception as e:
        messagebox.showerror("Error", f"Something went wrong:\n{str(e)}")

# --- GUI SETUP ---
root = tk.Tk()
root.title("Spending Report Generator")
root.geometry("400x200")

def choose_file():
    filepath = filedialog.askopenfilename(
        title="Select Bank Statement CSV",
        filetypes=[("CSV Files", "*.csv")]
    )
    if filepath:
        generate_report(filepath)

browse_button = tk.Button(root, text="Choose Bank Statement CSV", command=choose_file, font=("Arial", 12))
browse_button.pack(pady=40)

root.mainloop()
