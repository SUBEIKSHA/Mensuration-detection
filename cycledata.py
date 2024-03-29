import pandas as pd
import openpyxl

# Get the inputs from the user
age = input("Enter the patient's age: ")
days_since_last_period = input("Enter the number of days since the patient's last period: ")
cycle_length = input("Enter the patient's cycle length: ")

# Create a Pandas DataFrame
data = pd.DataFrame({
    "age": [age],
    "days_since_last_period": [days_since_last_period],
    "cycle_length": [cycle_length]
})

# Save the DataFrame to an Excel file
file_path = "C:\\Users\\magdaline suganthi\\Desktop\\prd\\MenstruatioNN\\menstruation_data.xlsx"

data.to_excel(file_path)

print("Data saved to menstruation_data.xlsx")
