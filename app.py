import os
import tkinter as tk
from tkinter import filedialog, messagebox
import zipfile


def descomprimir_zip():
    # Seleccionar el archivo ZIP
    archivo_zip = filedialog.askopenfilename(
        title="Seleccionar archivo ZIP", filetypes=[("Archivos ZIP", "*.zip")]
    )

    if not archivo_zip:
        return

    # Seleccionar la carpeta de destino
    carpeta_destino = filedialog.askdirectory(
        title="Seleccionar carpeta de destino"
    )

    if not carpeta_destino:
        return

    try:
        with zipfile.ZipFile(archivo_zip, "r") as zip_ref:
            zip_ref.extractall(carpeta_destino)
        messagebox.showinfo(
            "Éxito", "El archivo ZIP se ha descomprimido correctamente."
        )
    except Exception as e:
        messagebox.showerror(
            "Error", f"No se pudo descomprimir el archivo:\n{e}"
        )


def comprimir_a_zip():
    # Seleccionar la carpeta o archivos a comprimir
    carpeta_origen = filedialog.askdirectory(
        title="Seleccionar carpeta para comprimir"
    )

    if not carpeta_origen:
        return

    # Seleccionar dónde guardar el ZIP resultante
    archivo_salida = filedialog.asksaveasfilename(
        title="Guardar archivo ZIP como...",
        defaultextension=".zip",
        filetypes=[("Archivos ZIP", "*.zip")],
    )

    if not archivo_salida:
        return

    try:
        with zipfile.ZipFile(archivo_salida, "w", zipfile.ZIP_DEFLATED) as zipf:
            for raiz, dirs, archivos in os.walk(carpeta_origen):
                for archivo in archivos:
                    ruta_completa = os.path.join(raiz, archivo)
                    # Mantener la estructura relativa de carpetas dentro del ZIP
                    ruta_relativa = os.path.relpath(
                        ruta_completa, carpeta_origen
                    )
                    zipf.write(ruta_completa, ruta_relativa)
        messagebox.showinfo("Éxito", "La carpeta se ha comprimido correctamente.")
    except Exception as e:
        messagebox.showerror("Error", f"No se pudo comprimir la carpeta:\n{e}")


# Configuración de la Ventana Principal
ventana = tk.Tk()
ventana.title("Mi Gestor ZIP")
ventana.geometry("400x200")
ventana.resizable(False, False)

label = tk.Label(
    ventana, text="¿Qué deseas hacer?", font=("Arial", 14), pady=20
)
label.pack()

btn_descomprimir = tk.Button(
    ventana,
    text="Descomprimir archivo ZIP",
    command=descomprimir_zip,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 11),
    padx=10,
    pady=5,
)
btn_descomprimir.pack(pady=5)

btn_comprimir = tk.Button(
    ventana,
    text="Comprimir carpeta a ZIP",
    command=comprimir_a_zip,
    bg="#2196F3",
    fg="white",
    font=("Arial", 11),
    padx=10,
    pady=5,
)
btn_comprimir.pack(pady=5)

ventana.mainloop()
