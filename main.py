import PySimpleGUI as sg
import os

fileLocal = "cadastros.txt"

open(fileLocal,"a")

sg.theme("DarkAmber")

app = [
    [sg.Text("Nome da pessoa: "),sg.Input(key="name")],
    [sg.Text("Número de telefone: "),sg.Input(key="number")],
    [sg.Button("Cadastrar"),sg.Button("Ver cadastros"),sg.Button("Limpar cadastros"),sg.Button("Sair")]
]

window = sg.Window("Gerenciador de pessoas",app)

while True:
    event,value = window.read()
    if event == sg.WIN_CLOSED or event == "Sair":
        break
    if event == "Cadastrar":
        with open(fileLocal,"a") as file:
            file.write(f"Nome: {value['name']} | Telefone: {value['number']}\n\n")
    if event == "Ver cadastros":
        with open(fileLocal,"r") as file:
            app2 = [
                [sg.Column(layout=[[sg.Text(file.read())]],scrollable=True,size=(300,100))],
                [sg.Button("Voltar")]
            ]
            window2 = sg.Window("Lista cadastros",app2)
            while True:
                event,value = window2.read()
                if event == sg.WIN_CLOSED or event == "Voltar":
                    break
            window2.close()
    if event == "Limpar cadastros":
        app3 = [
            [sg.Text("Tem certeza que quer apagar todos os dados dos cadastros ?")],
            [sg.Button("Não"),sg.Button("Sim")]
        ]
        window3 = sg.Window("Confirmação de limpza",app3)
        while True:
            event,value = window3.read()
            if event == sg.WIN_CLOSED or event == "Não":
                break
            if event == "Sim":
                with open(fileLocal,"w") as file:
                    file.write("")
                    break
        window3.close()
window.close()