import PySimpleGUI as sg

def gui():
    """
    Agrega una interfaz gráfica sencilla a este script para que usuarios no técnicos puedan ejecutarlo.
    :return: None
    """
    sg.theme("Dark Teal 7")
    layout = [
        [sg.Text("¡Hola! Para ejecutar este programa, solo haz clic en 'Ejecutar' :-)", size=(120, 1))],
        [sg.Submit('Ejecutar'), sg.Cancel()]
    ]

    window = sg.Window("Mi programa genial", layout)
    event, values = window.read() # Esto es importante: window.read() devuelve dos valores
    window.close()

    if event == 'Ejecutar': # Comparamos el evento con el texto del botón 'Ejecutar'
        # y ejecutamos algunas funciones
        print("El programa se está ejecutando correctamente en Chile 🇨🇱.")

if __name__ == '__main__':
    gui()