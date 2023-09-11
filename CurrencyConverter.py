# import all functions from the tkinter
from tkinter import *
from tkinter import Tk, ttk
from PIL import ImageTk, Image

#colors
cor0 = "#FFFFFF" # white
cor1="#333333" # black
cor2="#6c79f0" # red

window = Tk()
window.geometry('400x420')
window.title('Converter')
window.configure(bg=cor0)
window.resizable (height = FALSE, width=FALSE)

# Function to perform real time conversion
# from one currency to another currency
def RealTimeCurrencyConversion():
    # importing required libraries
    import requests, json

    currency_1 = combo1.get()
    currency_2 = combo2.get()
    amount = value.get()

    if currency_2 == 'USD':
        symbol = '$'
    elif currency_2 == 'CAD':
        symbol = '$'
    elif currency_2 == 'BRL':
        symbol = 'R$'
    elif currency_2 == 'INR':
        symbol = '₹'
    elif currency_2 =='JPY':
        symbol = '¥'
    elif currency_2 =='KRW':
        symbol = '원'
    elif currency_2 == 'EUR':
        symbol = '€'


    url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

    querystring = {"from": currency_1, "to": currency_2, "amount": amount}

    headers = {
        "X-RapidAPI-Key": "8ad055b7b9msh17f77f581d2c0c4p1803aejsn85c41ca8b0d1",
        "X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
    }

    response = requests.request("GET", url, headers=headers, params=querystring)

    data = json.loads(response.text)
    converted_amount = symbol + " " + str(round(data["result"]["convertedAmount"], 2))
    result['text'] = converted_amount



# orange frames
top = Frame(window, width=400, height=68, bg=cor2)
top.grid(row=0, column=0)
#white frame
main= Frame(window, width=400, height=290, bg=cor0)
main.grid(row=1, column=0)

# image
icon = Image.open('bitcoin_calculate_icon.ico')
icon = icon.resize((50,50))
#icon = ImageTk.PhotoImage(icon)
# placing image and text at the same time
app_name = Label(top,image = icon,compound = LEFT,text = "Currency Converter",height=5,padx=13,pady=30,anchor=CENTER,font = 'Times 18 bold',bg = cor2,fg=cor0)
app_name.place(x=35,y=0)


#main frame

result = Label(main,text = " ",width= 16,height=2,pady=7,relief='solid',anchor=CENTER,font = 'Ivy 15 bold',bg = cor0,fg=cor1)
result.place(x=94,y=30)

from_label=Label(main,text = "From",width= 8,height=1,relief='flat',anchor=NW,font = 'Ivy 11 bold',bg = cor0,fg=cor1)
from_label.place(x=94,y=110)

currency = ['CAD','BRL','INR','USD','EUR','KRW','JPY']

combo1 = ttk.Combobox(main,width=8,justify=CENTER,font = 'Ivy 11 bold')
combo1['values'] = (currency)
combo1.place(x=94,y=130)


to_label=Label(main,text = "To",width= 8,height=1,relief='flat',anchor=NW,font = 'Ivy 11 bold',bg = cor0,fg=cor1)
to_label.place(x=208,y=110)

combo2 = ttk.Combobox(main,width=8,justify=CENTER,font = 'Ivy 11 bold')
combo2['values'] = (currency)
combo2.place(x=208,y=130)

#enter amont
value = Entry(main,width=22,justify=CENTER,font ='Ivy 12 bold',relief='solid')
value.place(x=94,y=190,height=29)

btn = Button(main,text="Converter",width=21,height=2,anchor=CENTER,bg=cor2,fg=cor0,font='Ivy 11 bold',command=RealTimeCurrencyConversion)
btn.place(x=94,y=240)


window.mainloop()
