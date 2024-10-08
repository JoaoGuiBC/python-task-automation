"""Application that automatically adds products from .csv to site"""

import time
import pyautogui
import pandas

pyautogui.PAUSE = 0.5

pyautogui.press("win")
pyautogui.write("opera")
pyautogui.press("enter")

pyautogui.write("https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")
time.sleep(2)

pyautogui.click(x=678, y=374)
pyautogui.write("johndoe@example.com")

pyautogui.press("tab")
pyautogui.write("123456")

pyautogui.press("enter")
time.sleep(2)

products_table = pandas.read_csv("products.csv")
print(products_table)

for table_line in products_table.index:
    pyautogui.click(x=608, y=257)
    product_code = products_table.loc[table_line, 'codigo']
    pyautogui.write(str(product_code))

    product_brand = products_table.loc[table_line, 'marca']
    pyautogui.press("tab")
    pyautogui.write(str(product_brand))

    product_type = products_table.loc[table_line, 'tipo']
    pyautogui.press("tab")
    pyautogui.write(str(product_type))

    product_category = products_table.loc[table_line, 'categoria']
    pyautogui.press("tab")
    pyautogui.write(str(product_category))

    product_price = products_table.loc[table_line, 'preco_unitario']
    pyautogui.press("tab")
    pyautogui.write(str(product_price))

    product_cost = products_table.loc[table_line, 'custo']
    pyautogui.press("tab")
    pyautogui.write(str(product_cost))

    product_observations = products_table.loc[table_line, 'obs']
    pyautogui.press("tab")
    if not pandas.isna(product_observations):
        pyautogui.write(str(product_observations))

    pyautogui.press("enter")
    pyautogui.scroll(1000)

print("PROCESS ENDED")
