import customtkinter as ctk

# ---------------------------------------------------------------
# Apariencia general
# ---------------------------------------------------------------
ctk.set_appearance_mode("dark")          # "light", "dark" o "system"
ctk.set_default_color_theme("blue")      # "blue", "green" o "dark-blue"


# ---------------------------------------------------------------
# FUNCIONES PROPORCIONADAS POR EL DOCENTE
# (Reemplace el contenido de estas dos funciones por las del docente
#  si tienen otro nombre o comportamiento; la conexión con los
#  botones ya está hecha más abajo.)
# ---------------------------------------------------------------
def registrar_producto():
    producto = entry_producto.get().strip()
    precio = entry_precio.get().strip()

    if not producto or not precio:
        lbl_resultado.configure(text="⚠ Complete todos los campos", text_color="#F5A623")
        return

    try:
        precio_num = float(precio)
    except ValueError:
        lbl_resultado.configure(text="⚠ El precio debe ser un número", text_color="#F5A623")
        return

    lbl_resultado.configure(
        text=f"✔ Producto registrado\n{producto} — Q {precio_num:,.2f}",
        text_color="#2ECC71",
    )


def limpiar_campos():
    entry_producto.delete(0, "end")
    entry_precio.delete(0, "end")
    lbl_resultado.configure(text="", text_color="white")
    entry_producto.focus()


# ---------------------------------------------------------------
# Ventana principal
# ---------------------------------------------------------------
app = ctk.CTk()
app.title("Registro de Producto")
app.geometry("420x520")
app.resizable(False, False)

# Tarjeta contenedora
marco = ctk.CTkFrame(app, corner_radius=20)
marco.pack(padx=25, pady=25, fill="both", expand=True)
marco.grid_columnconfigure((0, 1), weight=1)

# Título
lbl_titulo = ctk.CTkLabel(
    marco, text="📦 Registro de Producto",
    font=ctk.CTkFont(family="Segoe UI", size=24, weight="bold"),
)
lbl_titulo.grid(row=0, column=0, columnspan=2, pady=(30, 5))

lbl_sub = ctk.CTkLabel(
    marco, text="Ingrese los datos del producto",
    font=ctk.CTkFont(size=13), text_color="gray70",
)
lbl_sub.grid(row=1, column=0, columnspan=2, pady=(0, 20))

# Campo Producto
lbl_producto = ctk.CTkLabel(marco, text="Producto", font=ctk.CTkFont(size=14, weight="bold"))
lbl_producto.grid(row=2, column=0, columnspan=2, padx=35, sticky="w")

entry_producto = ctk.CTkEntry(
    marco, placeholder_text="Ej. Laptop", height=40, corner_radius=10,
)
entry_producto.grid(row=3, column=0, columnspan=2, padx=35, pady=(5, 15), sticky="ew")

# Campo Precio
lbl_precio = ctk.CTkLabel(marco, text="Precio", font=ctk.CTkFont(size=14, weight="bold"))
lbl_precio.grid(row=4, column=0, columnspan=2, padx=35, sticky="w")

entry_precio = ctk.CTkEntry(
    marco, placeholder_text="Ej. 2500.00", height=40, corner_radius=10,
)
entry_precio.grid(row=5, column=0, columnspan=2, padx=35, pady=(5, 25), sticky="ew")

# Botones
btn_registrar = ctk.CTkButton(
    marco, text="Registrar", height=40, corner_radius=10,
    font=ctk.CTkFont(size=14, weight="bold"),
    fg_color="#2ECC71", hover_color="#27AE60", text_color="black",
    command=registrar_producto,
)
btn_registrar.grid(row=6, column=0, padx=(35, 8), sticky="ew")

btn_limpiar = ctk.CTkButton(
    marco, text="Limpiar", height=40, corner_radius=10,
    font=ctk.CTkFont(size=14, weight="bold"),
    fg_color="#E74C3C", hover_color="#C0392B",
    command=limpiar_campos,
)
btn_limpiar.grid(row=6, column=1, padx=(8, 35), sticky="ew")

# Etiqueta de resultado
lbl_resultado = ctk.CTkLabel(
    marco, text="", font=ctk.CTkFont(size=15), wraplength=300, justify="center",
)
lbl_resultado.grid(row=7, column=0, columnspan=2, padx=35, pady=30)

app.mainloop()
