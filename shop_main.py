import sqlite3
import PySimpleGUI as sg
from datetime import datetime
from shop_db import connector, cursor
from typing import Any

sg.theme("dark")
sg.set_options(font="ariel 20")

def get_items_list(
        connector: sqlite3.Connection = connector,
        cursor: sqlite3.Cursor = cursor,
    ) -> list[Any]:
    with connector:
        cursor.execute("SELECT * FROM products")
        products_list = cursor.fetchall()
    return products_list

main_layout = [
    [
        sg.Button("Sell your stuff", key="-SELL-", size=15),
        sg.Button("Check all sales", key="-SALES-", size=15),
    ],
    [
        sg.Button("Sold items list", key="-RECENTLY-", size=20),
    ],
    [
        sg.Button("Exit", key="-EXIT-", size=20)
    ],
]

main_window = sg.Window(
    "PROPER SHOPPER SHOP FOR SHOPPING",
    main_layout,
    element_justification="center",
    element_padding=10,
    finalize=True
)

while True:
    event, values = main_window.read(timeout=0.1)
    if event in [sg.WIN_CLOSED, "-EXIT-"]:
        break
    if event == "-SELL-":
        input_order(connector, cursor)
    if event == "-SALES-":
        show_items(main_window)
    if event == "-RECENTLY-":
        pass
connector.close()