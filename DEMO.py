import customtkinter as ctk
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

import sympy as sp
from sympy import Symbol, limit, zoo, nan, sympify

# ============================================================
# NAMESPACE MATEMÁTICO
# ============================================================
NAMESPACE_MATEMATICO = {
    "x"    : Symbol("x"),
    "sin"  : sp.sin,
    "cos"  : sp.cos,
    "tan"  : sp.tan,
    "asin" : sp.asin,
    "acos" : sp.acos,
    "atan" : sp.atan,
    "exp"  : sp.exp,
    "log"  : sp.log,
    "ln"   : sp.log,
    "sqrt" : sp.sqrt,
    "Abs"  : sp.Abs,
    "abs"  : sp.Abs,
    "pi"   : sp.pi,
    "e"    : sp.E,
    "E"    : sp.E,
    "oo"   : sp.oo,
    "inf"  : sp.oo,
}

# Tabla completa — igual al popout original, más ejemplos completos
TABLA_SINTAXIS = [
    ("OPERADORES BÁSICOS",                   None,                    None),
    ("Suma",                                 "x + 2",                 "x + 2"),
    ("Resta",                                "x - 5",                 "x - 5"),
    ("Multiplicación",                       "3*x  ó  3 * x",         "3·x"),
    ("División",                             "x / 2",                 "x / 2"),
    ("Potencia",                             "x**2  ó  x**3",         "x², x³"),
    ("Paréntesis",                           "(x + 1) / (x - 1)",     "(x+1)/(x−1)"),

    ("FUNCIONES TRIGONOMÉTRICAS",            None,                    None),
    ("Seno",                                 "sin(x)",                "sin(x)"),
    ("Coseno",                               "cos(x)",                "cos(x)"),
    ("Tangente",                             "tan(x)",                "tan(x)"),
    ("Arcoseno",                             "asin(x)",               "arcsin(x)"),
    ("Arcocoseno",                           "acos(x)",               "arccos(x)"),
    ("Arcotangente",                         "atan(x)",               "arctan(x)"),

    ("FUNCIONES EXPONENCIALES Y LOGARÍTMICAS", None,                  None),
    ("Euler  eˣ",                            "exp(x)",                "eˣ"),
    ("Logaritmo natural",                    "log(x)  ó  ln(x)",      "ln(x)"),
    ("Logaritmo base 10",                    "log(x, 10)",            "log₁₀(x)"),
    ("Logaritmo base b",                     "log(x, b)",             "logᵦ(x)"),
    ("Raíz cuadrada",                        "sqrt(x)",               "√x"),
    ("Raíz n-ésima",                         "x**(1/n)",              "ⁿ√x  (ej: x**(1/3))"),

    ("CONSTANTES",                           None,                    None),
    ("Número π",                             "pi",                    "3.14159…"),
    ("Número e",                             "e  ó  E",               "2.71828…"),
    ("Infinito (+)",                         "inf  ó  oo",            "+∞  (solo campo h)"),
    ("Infinito (−)",                         "-inf  ó  -oo",          "-∞  (solo campo h)"),

    ("VALOR ABSOLUTO",                       None,                    None),
    ("Valor absoluto",                       "Abs(x)  ó  abs(x)",     "|x|"),

    ("EJEMPLOS COMPLETOS",                   None,                    None),
    ("Límite removible",                     "(x**2 - 1)/(x - 1)",    "(x²−1)/(x−1)  →  h=1"),
    ("Límite trigonométrico",                "sin(x)/x",              "sin(x)/x  →  h=0"),
    ("Número e (definición)",                "(1 + 1/x)**x",          "(1+1/x)^x  →  h=inf"),
    ("Límite con raíz",                      "(sqrt(x)-1)/(x-1)",     "(√x−1)/(x−1)  →  h=1"),
    ("Límite logarítmico",                   "log(x+1)/x",            "ln(x+1)/x  →  h=0"),
    ("Límite exponencial",                   "(exp(x)-1)/x",          "(eˣ−1)/x  →  h=0"),
    ("Polinomio cúbico",                     "(x**3 - 8)/(x - 2)",    "(x³−8)/(x−2)  →  h=2"),
    ("Trig. con cuadrado",                   "sin(x)**2 / x",         "sin²(x)/x  →  h=0"),
    ("Arcotangente en inf",                  "atan(x)",               "arctan(x)  →  h=inf"),
    ("Compuesta exp/log",                    "log(exp(x)/x)",         "ln(eˣ/x)  →  h=inf"),
]

# ============================================================
# PALETA — más clara y contrastada
# ============================================================
C = {
    "bg":        "#1c2333",   # azul-gris profundo (antes casi negro)
    "panel":     "#243047",   # panel lateral más visible
    "card":      "#2d3d5c",   # tarjetas con más contraste
    "card2":     "#354a6e",   # hover/card secundaria
    "acento":    "#818cf8",   # indigo claro (más luminoso)
    "acento_h":  "#6366f1",
    "acento2":   "#38bdf8",   # celeste brillante
    "acento2_h": "#0ea5e9",
    "exito":     "#34d399",   # verde esmeralda claro
    "warn":      "#fbbf24",   # ámbar claro
    "error":     "#fb7185",   # rosa-rojo suave
    "txt":       "#f8fafc",   # blanco suave
    "txt2":      "#b8c9e0",   # gris azulado claro (antes muy opaco)
    "borde":     "#3d5478",
    "entrada":   "#1a2744",
    "sint_bg":   "#1e2e45",   # fondo panel sintaxis
    "sint_row_a":"#243552",
    "sint_row_b":"#1e2e45",
    "sint_sec":  "#6366f1",   # cabecera sección
    "graf_bg":   "#1a2236",   # fondo del gráfico matplotlib
    "graf_grid": "#2a3a55",
}

FONT_LBL   = ("Segoe UI", 13, "bold")
FONT_ENTRY = ("Consolas",  13)
FONT_RES   = ("Consolas",  16, "bold")
FONT_SM    = ("Segoe UI",  11)
FONT_CODE  = ("Consolas",  11)
FONT_TINY  = ("Segoe UI",  10)


# ============================================================
# LÓGICA MATEMÁTICA
# ============================================================
def parsear_funcion(texto):
    try:
        return sympify(texto, locals=NAMESPACE_MATEMATICO)
    except Exception:
        raise ValueError(
            f"La función '{texto}' no es válida.\n"
            "Usa sintaxis Python: x**2, sin(x), exp(x), log(x), sqrt(x), etc."
        )

def parsear_h(texto):
    normalizado = texto.strip().lower().replace("infinity", "oo").replace("∞", "oo")
    mapa = {
        "inf": sp.oo, "+inf": sp.oo, "oo": sp.oo, "+oo": sp.oo,
        "-inf": -sp.oo, "-oo": -sp.oo,
    }
    if normalizado in mapa:
        return mapa[normalizado]
    try:
        return sympify(normalizado)
    except Exception:
        raise ValueError(
            f"El valor '{texto}' no es válido.\n"
            "Ingresa un número (ej: 1, -2, 0.5) o 'inf' / '-inf'."
        )

def calcular_limite(funcion_str, h_str):
    x = Symbol("x")
    f_sym = parsear_funcion(funcion_str)
    h_val = parsear_h(h_str)
    try:
        resultado = limit(f_sym, x, h_val)
    except Exception as e:
        raise ValueError(f"No se pudo calcular el límite:\n{e}")
    if resultado == zoo:         resultado_str = "No existe (indeterminado)"
    elif resultado == sp.oo:     resultado_str = "+∞"
    elif resultado == -sp.oo:    resultado_str = "-∞"
    elif resultado == nan:       resultado_str = "No existe"
    else:                        resultado_str = str(resultado)
    return resultado, resultado_str, f_sym

def generar_puntos(f_sym, x_sym, x_inicio, x_fin, n_puntos=300):
    paso = (x_fin - x_inicio) / (n_puntos - 1)
    xs = [x_inicio + i * paso for i in range(n_puntos)]
    ys = []
    for xi in xs:
        try:
            yi = float(f_sym.subs(x_sym, xi))
            ys.append(yi if abs(yi) < 1e6 else float("nan"))
        except Exception:
            ys.append(float("nan"))
    return xs, ys

def ventana_grafico(h_float, margen=4.0):
    return h_float - margen, h_float + margen


# ============================================================
# APLICACIÓN PRINCIPAL
# ============================================================
class LimiteApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("MATE1133 · Analizador y Visualizador de Límites")
        self.geometry("1420x800")
        self.minsize(1100, 640)
        self.configure(fg_color=C["bg"])
        ctk.set_appearance_mode("dark")
        ctk.set_default_color_theme("dark-blue")

        self._figura    = None
        self._canvas_tk = None
        self._ultima_funcion = None
        self._ultimo_h = None

        self._construir_layout()

    # --------------------------------------------------------
    # LAYOUT
    # --------------------------------------------------------
    def _construir_layout(self):
        self.columnconfigure(0, weight=0, minsize=310)   # inputs
        self.columnconfigure(1, weight=1)                 # gráfico
        self.columnconfigure(2, weight=0, minsize=390)   # sintaxis (más ancha)
        self.rowconfigure(0, weight=1)
        self._panel_izquierdo()
        self._panel_grafico()
        self._panel_sintaxis()

    # --------------------------------------------------------
    # PANEL IZQUIERDO — inputs
    # --------------------------------------------------------
    def _panel_izquierdo(self):
        panel = ctk.CTkFrame(self, fg_color=C["panel"], corner_radius=0, width=310)
        panel.grid(row=0, column=0, sticky="nsew")
        panel.grid_propagate(False)
        panel.columnconfigure(0, weight=1)
        fila = 0

        # Título
        ft = ctk.CTkFrame(panel, fg_color=C["card"], corner_radius=12)
        ft.grid(row=fila, column=0, padx=14, pady=(18, 8), sticky="ew"); fila += 1
        ctk.CTkLabel(ft, text="∫  Límites",
                     font=("Segoe UI", 26, "bold"), text_color=C["acento"]).pack(pady=(12, 0))
        ctk.CTkLabel(ft, text="MATE1133 · UCTemuco",
                     font=FONT_SM, text_color=C["txt2"]).pack(pady=(0, 12))

        # f(x)
        ff = ctk.CTkFrame(panel, fg_color=C["card"], corner_radius=12)
        ff.grid(row=fila, column=0, padx=14, pady=5, sticky="ew"); fila += 1
        ff.columnconfigure(0, weight=1)
        ctk.CTkLabel(ff, text="Función  f(x)", font=FONT_LBL,
                     text_color=C["txt"]).grid(row=0, column=0, padx=12, pady=(12, 4), sticky="w")
        self.entry_funcion = ctk.CTkEntry(
            ff, placeholder_text="Ej: (x**2 - 1)/(x - 1)",
            font=FONT_ENTRY, fg_color=C["entrada"],
            border_color=C["acento"], border_width=2,
            text_color=C["txt"], height=38)
        self.entry_funcion.grid(row=1, column=0, sticky="ew", padx=12, pady=(0, 12))
        self.entry_funcion.bind("<Return>", lambda e: self._accion_calcular())

        # h
        fh = ctk.CTkFrame(panel, fg_color=C["card"], corner_radius=12)
        fh.grid(row=fila, column=0, padx=14, pady=5, sticky="ew"); fila += 1
        ctk.CTkLabel(fh, text="Valor  h  (x tiende a…)", font=FONT_LBL,
                     text_color=C["txt"]).pack(anchor="w", padx=12, pady=(12, 4))
        self.entry_h = ctk.CTkEntry(
            fh, placeholder_text="Ej: 1   o   inf   o   -inf",
            font=FONT_ENTRY, fg_color=C["entrada"],
            border_color=C["acento"], border_width=2,
            text_color=C["txt"], height=38)
        self.entry_h.pack(fill="x", padx=12, pady=(0, 12))
        self.entry_h.bind("<Return>", lambda e: self._accion_calcular())

        # Botones
        fb = ctk.CTkFrame(panel, fg_color="transparent")
        fb.grid(row=fila, column=0, padx=14, pady=(6, 4), sticky="ew"); fila += 1
        fb.columnconfigure((0, 1), weight=1)
        ctk.CTkButton(fb, text="▶  Calcular",
                      font=("Segoe UI", 13, "bold"),
                      fg_color=C["acento"], hover_color=C["acento_h"],
                      text_color="#ffffff", height=40, corner_radius=10,
                      command=self._accion_calcular,
                      ).grid(row=0, column=0, padx=(0, 4), sticky="ew")
        ctk.CTkButton(fb, text="✕  Limpiar",
                      font=("Segoe UI", 13, "bold"),
                      fg_color=C["card"], hover_color=C["card2"],
                      text_color=C["txt2"], height=40, corner_radius=10,
                      command=self._accion_limpiar,
                      ).grid(row=0, column=1, padx=(4, 0), sticky="ew")

        # Resultado
        fr = ctk.CTkFrame(panel, fg_color=C["card"], corner_radius=12)
        fr.grid(row=fila, column=0, padx=14, pady=5, sticky="ew"); fila += 1
        ctk.CTkLabel(fr, text="Resultado", font=FONT_LBL,
                     text_color=C["txt"]).pack(anchor="w", padx=12, pady=(12, 4))
        self.lbl_resultado = ctk.CTkLabel(
            fr, text="—", font=("Consolas", 17, "bold"),
            text_color=C["exito"], wraplength=270, justify="center")
        self.lbl_resultado.pack(padx=12, pady=(0, 12))

        # Límites laterales
        fl = ctk.CTkFrame(panel, fg_color=C["card"], corner_radius=12)
        fl.grid(row=fila, column=0, padx=14, pady=5, sticky="ew"); fila += 1
        fl.columnconfigure((0, 1), weight=1)
        ctk.CTkLabel(fl, text="x → h⁻  (izquierdo)",
                     font=FONT_SM, text_color=C["txt2"]).grid(row=0, column=0, padx=8, pady=(10, 2))
        ctk.CTkLabel(fl, text="x → h⁺  (derecho)",
                     font=FONT_SM, text_color=C["txt2"]).grid(row=0, column=1, padx=8, pady=(10, 2))
        self.lbl_izq = ctk.CTkLabel(fl, text="—", font=FONT_RES, text_color=C["warn"])
        self.lbl_izq.grid(row=1, column=0, padx=8, pady=(0, 10))
        self.lbl_der = ctk.CTkLabel(fl, text="—", font=FONT_RES, text_color=C["warn"])
        self.lbl_der.grid(row=1, column=1, padx=8, pady=(0, 10))

        # Estado
        self.lbl_estado = ctk.CTkLabel(
            panel, text="Ingresa una función y presiona Calcular.",
            font=FONT_SM, text_color=C["txt2"], wraplength=285, justify="left")
        self.lbl_estado.grid(row=fila, column=0, padx=16, pady=(4, 6), sticky="w"); fila += 1

        # Ejemplos rápidos por categoría
        fe = ctk.CTkFrame(panel, fg_color=C["card"], corner_radius=12)
        fe.grid(row=fila, column=0, padx=14, pady=(4, 18), sticky="nsew")
        fe.columnconfigure(0, weight=1)
        fe.rowconfigure(1, weight=1)
        panel.rowconfigure(fila, weight=1)

        ctk.CTkLabel(fe, text="Ejemplos rápidos",
                     font=FONT_LBL, text_color=C["txt"]).grid(
                     row=0, column=0, padx=12, pady=(10, 4), sticky="w")

        scroll_ej = ctk.CTkScrollableFrame(
            fe, fg_color="transparent",
            scrollbar_button_color=C["acento"],
            scrollbar_button_hover_color=C["acento_h"],
        )
        scroll_ej.grid(row=1, column=0, sticky="nsew", padx=4, pady=(0, 8))
        scroll_ej.columnconfigure(0, weight=1)

        CATEGORIAS_EJ = [
            ("Límites removibles / algebraicos", C["acento"], [
                ("(x**2 - 1)/(x - 1)",          "1",    "(x²−1)/(x−1)"),
                ("(x**3 - 8)/(x - 2)",           "2",    "(x³−8)/(x−2)"),
                ("(x**2 - 5*x + 6)/(x - 2)",    "2",    "(x²−5x+6)/(x−2)"),
            ]),
            ("Límites trigonométricos", "#a78bfa", [
                ("sin(x)/x",                     "0",    "sin(x)/x"),
                ("(1 - cos(x))/x",               "0",    "(1−cos x)/x"),
                ("tan(x)/x",                     "0",    "tan(x)/x"),
            ]),
            ("Límites al infinito  (+∞)", C["acento2"], [
                ("(1 + 1/x)**x",                 "inf",  "(1+1/x)^x  →  e"),
                ("(3*x**2 + 1)/(x**2 - 2)",      "inf",  "(3x²+1)/(x²−2)"),
                ("atan(x)",                       "inf",  "arctan(x)  →  π/2"),
            ]),
            ("Límites al infinito  (−∞)", "#f472b6", [
                ("(2*x**3 - x)/(x**3 + 1)",      "-inf", "(2x³−x)/(x³+1)"),
                ("exp(x)",                        "-inf", "eˣ  →  0"),
                ("atan(x)",                       "-inf", "arctan(x)  →  −π/2"),
            ]),
            ("Límites con raíces", C["exito"], [
                ("(sqrt(x) - 1)/(x - 1)",        "1",    "(√x−1)/(x−1)"),
                ("(sqrt(x+4) - 2)/x",            "0",    "(√(x+4)−2)/x"),
                ("(sqrt(x**2+1) - 1)/x",         "0",    "(√(x²+1)−1)/x"),
            ]),
            ("Límites exponenciales / logarítmicos", C["warn"], [
                ("(exp(x) - 1)/x",               "0",    "(eˣ−1)/x  →  1"),
                ("log(x + 1)/x",                 "0",    "ln(x+1)/x  →  1"),
                ("log(x)/x",                     "inf",  "ln(x)/x  →  0"),
            ]),
            ("Límites laterales (verifica h⁻ y h⁺)", C["error"], [
                ("Abs(x)/x",                     "0",    "|x|/x  (no existe)"),
                ("1/(x - 2)",                    "2",    "1/(x−2)  (→ ±∞)"),
                ("(x**2 - 4)/(x - 2)",           "2",    "(x²−4)/(x−2)"),
            ]),
        ]

        fila_s = 0
        for cat_nombre, cat_color, items in CATEGORIAS_EJ:
            # Cabecera de categoría
            cab = ctk.CTkFrame(scroll_ej, fg_color=cat_color, corner_radius=5, height=22)
            cab.grid(row=fila_s, column=0, sticky="ew", padx=2, pady=(8, 2), ipady=1)
            cab.columnconfigure(0, weight=1)
            cab.grid_propagate(False)
            ctk.CTkLabel(cab, text=f"  {cat_nombre}",
                         font=("Segoe UI", 9, "bold"),
                         text_color="#ffffff", anchor="w",
                         ).grid(row=0, column=0, sticky="ew", padx=6)
            fila_s += 1

            for func_ej, h_ej, etiqueta in items:
                ctk.CTkButton(
                    scroll_ej,
                    text=f"  {etiqueta}   →   h={h_ej}",
                    font=("Consolas", 10),
                    fg_color=C["card2"], hover_color=C["acento_h"],
                    text_color=C["txt2"], height=24, corner_radius=5, anchor="w",
                    command=lambda f=func_ej, h=h_ej: self._cargar_ejemplo(f, h),
                ).grid(row=fila_s, column=0, sticky="ew", padx=2, pady=1)
                fila_s += 1

    # --------------------------------------------------------
    # PANEL CENTRAL — gráfico (sin toolbar/pan)
    # --------------------------------------------------------
    def _panel_grafico(self):
        self.frame_grafico = ctk.CTkFrame(self, fg_color=C["bg"], corner_radius=0)
        self.frame_grafico.grid(row=0, column=1, sticky="nsew", padx=2)
        self.frame_grafico.columnconfigure(0, weight=1)
        self.frame_grafico.rowconfigure(0, weight=1)

        self.lbl_placeholder = ctk.CTkLabel(
            self.frame_grafico,
            text="El gráfico aparecerá aquí\ndespués de calcular un límite",
            font=("Segoe UI", 16), text_color=C["txt2"])
        self.lbl_placeholder.grid(row=0, column=0)

    # --------------------------------------------------------
    # PANEL DERECHO — sintaxis completa siempre visible
    # --------------------------------------------------------
    def _panel_sintaxis(self):
        panel = ctk.CTkFrame(self, fg_color=C["panel"], corner_radius=0, width=390)
        panel.grid(row=0, column=2, sticky="nsew")
        panel.grid_propagate(False)
        panel.columnconfigure(0, weight=1)
        panel.rowconfigure(1, weight=1)

        # Encabezado
        enc = ctk.CTkFrame(panel, fg_color=C["card2"], corner_radius=0)
        enc.grid(row=0, column=0, sticky="ew")
        enc.columnconfigure(0, weight=1)
        ctk.CTkLabel(enc, text="📖  Guía de Sintaxis  —  f(x)",
                     font=("Segoe UI", 13, "bold"), text_color=C["txt"],
                     ).grid(row=0, column=0, padx=14, pady=(12, 2), sticky="w")
        ctk.CTkLabel(enc,
                     text="Escribe las funciones tal como aparece en la columna 'f(x)'",
                     font=FONT_TINY, text_color=C["acento2"],
                     ).grid(row=1, column=0, padx=14, pady=(0, 10), sticky="w")

        # Tabla scrollable — 3 columnas
        scroll = ctk.CTkScrollableFrame(
            panel,
            fg_color=C["sint_bg"],
            corner_radius=0,
            scrollbar_button_color=C["acento"],
            scrollbar_button_hover_color=C["acento_h"],
        )
        scroll.grid(row=1, column=0, sticky="nsew")
        scroll.columnconfigure(0, weight=3)   # nombre
        scroll.columnconfigure(1, weight=4)   # código
        scroll.columnconfigure(2, weight=3)   # equivalente matemático

        # Cabeceras de columna
        for col, titulo in enumerate(["Operación", "Escribir en f(x)", "Equivalente"]):
            ctk.CTkLabel(
                scroll, text=titulo,
                font=("Segoe UI", 10, "bold"),
                text_color=C["acento2"],
                fg_color=C["card"],
                anchor="w",
            ).grid(row=0, column=col, sticky="ew", padx=2, pady=(4, 2), ipady=6)

        fila = 1
        alternado = False

        for nombre, sintaxis, equivalente in TABLA_SINTAXIS:
            if sintaxis is None:
                # Cabecera de sección — ocupa las 3 columnas
                sec = ctk.CTkFrame(scroll, fg_color=C["sint_sec"], corner_radius=5, height=26)
                sec.grid(row=fila, column=0, columnspan=3,
                         sticky="ew", padx=4, pady=(10, 2), ipady=2)
                sec.columnconfigure(0, weight=1)
                sec.grid_propagate(False)
                ctk.CTkLabel(sec, text=f"  {nombre}",
                             font=("Segoe UI", 10, "bold"),
                             text_color="#ffffff", anchor="w",
                             ).grid(row=0, column=0, sticky="ew", padx=6)
                fila += 1
                alternado = False
                continue

            bg = C["sint_row_a"] if alternado else C["sint_row_b"]
            alternado = not alternado

            ctk.CTkLabel(scroll, text=f"  {nombre}", font=FONT_TINY,
                         text_color=C["txt"], fg_color=bg,
                         anchor="w", corner_radius=3,
                         ).grid(row=fila, column=0, sticky="ew", padx=(4, 1), pady=1, ipady=5)

            ctk.CTkLabel(scroll, text=sintaxis, font=("Consolas", 10, "bold"),
                         text_color=C["acento2"], fg_color=bg,
                         anchor="w", corner_radius=3,
                         ).grid(row=fila, column=1, sticky="ew", padx=1, pady=1, ipady=5)

            ctk.CTkLabel(scroll, text=equivalente, font=FONT_TINY,
                         text_color=C["exito"], fg_color=bg,
                         anchor="w", corner_radius=3,
                         ).grid(row=fila, column=2, sticky="ew", padx=(1, 4), pady=1, ipady=5)
            fila += 1

    # --------------------------------------------------------
    # ACCIONES
    # --------------------------------------------------------
    def _accion_calcular(self):
        funcion_str = self.entry_funcion.get().strip()
        h_str       = self.entry_h.get().strip()
        if not funcion_str:
            self._mostrar_error("Por favor ingresa una función f(x).")
            return
        if not h_str:
            self._mostrar_error("Por favor ingresa el valor h.")
            return

        if funcion_str == self._ultima_funcion and h_str == self._ultimo_h:
            self._mostrar_estado("Los datos no han cambiado.", C["warn"])
            return

        self._mostrar_estado("Calculando…", C["txt2"])
        self.update()

        try:
            resultado_sym, resultado_str, f_sym = calcular_limite(funcion_str, h_str)
        except ValueError as e:
            self._mostrar_error(str(e))
            self.lbl_resultado.configure(text="Error", text_color=C["error"])
            self.lbl_izq.configure(text="—")
            self.lbl_der.configure(text="—")
            return

        self.lbl_resultado.configure(text=f"lím = {resultado_str}", text_color=C["exito"])

        x = Symbol("x")
        h_norm = h_str.strip().lower().replace("infinity", "oo").replace("∞", "oo")
        es_infinito = h_norm in ("inf", "+inf", "oo", "+oo", "-inf", "-oo")

        if not es_infinito:
            try:
                h_sym = sympify(h_norm)
                def _fmt(v):
                    if v == sp.oo:      return "+∞"
                    if v == -sp.oo:     return "-∞"
                    if v in (zoo, nan): return "∄"
                    return str(v)
                self.lbl_izq.configure(text=_fmt(limit(f_sym, x, h_sym, dir="-")))
                self.lbl_der.configure(text=_fmt(limit(f_sym, x, h_sym, dir="+")))
            except Exception:
                self.lbl_izq.configure(text="—")
                self.lbl_der.configure(text="—")
        else:
            self.lbl_izq.configure(text="N/A")
            self.lbl_der.configure(text="N/A")

        self._ultima_funcion = funcion_str
        self._ultimo_h = h_str
        self._graficar(f_sym, x, h_str, resultado_str, funcion_str)
        self._mostrar_estado("Cálculo completado correctamente.", C["exito"])

    def _accion_limpiar(self):
        self.entry_funcion.delete(0, "end")
        self.entry_h.delete(0, "end")
        self.lbl_resultado.configure(text="—", text_color=C["exito"])
        self.lbl_izq.configure(text="—")
        self.lbl_der.configure(text="—")
        self._mostrar_estado("Campos limpiados.", C["txt2"])
        if self._canvas_tk is not None:
            self._canvas_tk.get_tk_widget().destroy()
            self._canvas_tk = None
        self._ultima_funcion = None
        self._ultimo_h = None
        if self._figura is not None:
            plt.close(self._figura)
            self._figura = None
        self.lbl_placeholder = ctk.CTkLabel(
            self.frame_grafico,
            text="El gráfico aparecerá aquí\ndespués de calcular un límite",
            font=("Segoe UI", 16), text_color=C["txt2"])
        self.lbl_placeholder.grid(row=0, column=0)

    # --------------------------------------------------------
    # GRÁFICO — sin toolbar ni pan
    # --------------------------------------------------------
    def _graficar(self, f_sym, x_sym, h_str, resultado_str, funcion_str):
        h_norm = h_str.strip().lower().replace("infinity", "oo").replace("∞", "oo")
        es_infinito = h_norm in ("inf", "+inf", "oo", "+oo", "-inf", "-oo")

        if es_infinito:
            x_ini, x_fin = (-20.0, -1.0) if "-" in h_norm else (0.5, 20.0)
            h_float = None
        else:
            try:
                h_float = float(sympify(h_norm))
            except Exception:
                h_float = 0.0
            x_ini, x_fin = ventana_grafico(h_float, margen=4.0)

        xs, ys = generar_puntos(f_sym, x_sym, x_ini, x_fin, n_puntos=300)

        plt.style.use("dark_background")
        if self._figura is not None:
            plt.close(self._figura)

        fig, ax = plt.subplots(figsize=(6.5, 4.8), facecolor=C["graf_bg"])
        ax.set_facecolor(C["graf_bg"])

        # Curva principal
        ax.plot(xs, ys, color=C["acento2"], linewidth=2.3,
                label=f"f(x) = {funcion_str}", zorder=3)

        # Anotaciones del límite
        if not es_infinito and h_float is not None:
            ax.axvline(x=h_float, color=C["acento"], linewidth=1.4,
                       linestyle="--", alpha=0.85, label=f"x → {h_str}", zorder=2)
            try:
                lim_float = float(sympify(resultado_str.replace("∞", "oo")))
                ax.plot(h_float, lim_float, "o", markersize=9,
                        markerfacecolor=C["graf_bg"],
                        markeredgecolor=C["exito"],
                        markeredgewidth=2.2, zorder=5,
                        label=f"lím = {resultado_str}")
                ax.axhline(y=lim_float, color=C["exito"], linewidth=1.0,
                           linestyle=":", alpha=0.6, zorder=1)
                ax.annotate(f"  lím = {resultado_str}",
                            xy=(h_float, lim_float),
                            fontsize=10, color=C["exito"], va="bottom")
            except Exception:
                pass

        # Estilo
        ax.set_title(f"lím  f(x)  cuando  x → {h_str}",
                     color=C["txt"], fontsize=12, pad=10)
        ax.set_xlabel("x", color=C["txt2"], fontsize=11)
        ax.set_ylabel("f(x)", color=C["txt2"], fontsize=11)
        ax.tick_params(colors=C["txt2"], labelsize=9)
        for spine in ax.spines.values():
            spine.set_edgecolor(C["borde"])
        ax.grid(True, color=C["graf_grid"], linewidth=0.8, alpha=0.9)
        ax.legend(fontsize=9, facecolor=C["graf_bg"],
                  edgecolor=C["borde"], labelcolor=C["txt"])
        fig.tight_layout(pad=1.2)

        # Reemplazar canvas (sin toolbar)
        if self._canvas_tk is not None:
            self._canvas_tk.get_tk_widget().destroy()
        try:
            self.lbl_placeholder.grid_forget()
        except Exception:
            pass

        self._figura    = fig
        self._canvas_tk = FigureCanvasTkAgg(fig, master=self.frame_grafico)
        # Deshabilitar interacciones de teclado/ratón de matplotlib
        self._canvas_tk.mpl_disconnect(
            self._canvas_tk.mpl_connect("key_press_event", lambda e: None))
        self._canvas_tk.draw()
        self._canvas_tk.get_tk_widget().grid(
            row=0, column=0, sticky="nsew", padx=8, pady=8)

    # --------------------------------------------------------
    # HELPERS
    # --------------------------------------------------------
    def _mostrar_error(self, msg):
        self.lbl_estado.configure(text=f"⚠  {msg}", text_color=C["error"])

    def _mostrar_estado(self, msg, color=None):
        self.lbl_estado.configure(text=msg, text_color=color or C["txt2"])

    def _cargar_ejemplo(self, funcion, h):
        self.entry_funcion.delete(0, "end")
        self.entry_funcion.insert(0, funcion)
        self.entry_h.delete(0, "end")
        self.entry_h.insert(0, h)
        self._accion_calcular()


# ============================================================
if __name__ == "__main__":
    app = LimiteApp()
    app.mainloop()