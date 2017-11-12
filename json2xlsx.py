import json
from openpyxl import Workbook
categories = json.loads(open("menu.json").read())

wb = Workbook()
ws = wb.create_sheet("categories")
for category in categories:
    categoryName = category['menuName']
    row = [categoryName]
    sheet = wb.get_sheet_by_name('categories')
    sheet.append(row)
    ws = wb.create_sheet(title=categoryName)
    for menuItem in category['menuItems']:
        row = [menuItem['menuItemName'], menuItem['menuItemDescription']]
        ws.append(row)
wb.save('menu.xlsx')