import gspread
from oauth2client.service_account import ServiceAccountCredentials


scope = ['https://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('creds.json',scope)

client = gspread.authorize(creds)

sheet = client.open("sheet1").sheet1

#data = sheet.get_all_records()
#print(data)

row = sheet.row_values(4)
#print(row)

col = sheet.col_values(2)
#print(col)

cell = sheet.cell(1,2).value
#print(cell)

"""
row = ["test4", "3", "uk", "cc", "2", "alyan@noon.com"]
#sheet.clear()
sheet.append_row(row)
print(" tha row has been added")

"""
"""
cell_row = 1
cell_column = 1
image_url = "https://z.nooncdn.com/rn/emails/afs-return-01.png"  # Replace with your direct image URL
image_formula = f'=IMAGE("{image_url}")'
sheet.update_cell(cell_row, cell_column, image_formula)
print("yess")
"""

#data = sheet.delete_rows(1)
#print(data)
#print("tha row has been deleted")


"""
data = [
    ['Name', 'phone', 'email'],
    ['Al', '984843', 'al@gmail.com'],
    ['Bob', '2822232', 'b@js.com'],
    ['aryan', '94380943098', 'aryn@g.com']
]

# Clear existing data (optional)
#sheet.clear()


# Append new data
sheet.append_rows(data)
print(" Data sent to Google Sheet successfully.")

"""
