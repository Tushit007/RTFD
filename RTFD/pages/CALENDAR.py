# /PAGES/CALENDAR.PY
# IMPORTING THE REQUIRED MODULES IN THE WORK SPACE 
import streamlit as stream
import calendar
import time

# PAGE CONFIGURATION
stream.set_page_config(page_title="CALENDAR", page_icon=":eye", layout="wide")

def get_reminders():
      if "reminders" not in stream.session_state:
            stream.session_state.reminders = []
      return stream.session_state.reminders

def main():
      stream.title("STUDENT CALENDAR")

      # Get user input for year and month
      year = stream.number_input("ENTER YEAR:", min_value=2024, max_value=2100, step=1)
      month = stream.selectbox("SELECT MONTH:", list(calendar.month_name)[1:])

      # Get the calendar for the specified month and year
      cal = calendar.monthcalendar(year, list(calendar.month_name).index(month))

      # Display the weekdays
      weekdays = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]

      # Create table data
      table_data = [weekdays] + cal

      # Display the calendar in tabular format
      stream.table(table_data)


# MAIN
if __name__ == "__main__":
      main()
