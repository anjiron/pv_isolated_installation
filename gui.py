import tkinter as tk

def tk_numero_dispositivos():
    main_window = tk.Tk()
    main_window.title ("------- CALCULADORA PV AISLADA -------")
    main_window.geometry ("500x400")

    lista_dispositivos = ["luminarias", "frigorificos", "ordenadores", "ventiladores", "lavdoras", "televisiones"]

    for index in lista_dispositivos:
        print(index)
        index_Stvar = tk.StringVar(main_window)
        tk.Label(main_window, text = "Número de " + index +":").pack()
        box_index = tk.Entry(main_window, textvariable=index_Stvar)
        box_index.pack()

    main_window.mainloop()


tk_numero_dispositivos()