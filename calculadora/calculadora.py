import tkinter as tk
from tkinter import ttk, messagebox
import numpy as np

class SustainabilityCalculatorGUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Calculadora de Operadores de Agregación - Sostenibilidad")
        self.root.geometry("700x600")
        self.root.configure(bg='#f0f8ff')
        
        # Variables para los valores de entrada
        self.valor1_var = tk.StringVar()
        self.valor2_var = tk.StringVar()
        self.valor3_var = tk.StringVar()
        self.valor4_var = tk.StringVar()
        
        # Variables para los resultados
        self.resultado_minimo = tk.StringVar()
        self.resultado_maximo = tk.StringVar()
        self.resultado_promedio = tk.StringVar()
        self.resultado_owa = tk.StringVar()
        
        self.create_widgets()
        
    def create_widgets(self):
        # Título principal
        title_frame = tk.Frame(self.root, bg='#f0f8ff')
        title_frame.pack(pady=20)
        
        title_label = tk.Label(
            title_frame,
            text="Calculadora de Operadores de Agregación",
            font=("Arial", 18, "bold"),
            bg='#f0f8ff',
            fg='#2c3e50'
        )
        title_label.pack()
        
        subtitle_label = tk.Label(
            title_frame,
            text="T-normas, S-normas, Promedio",
            font=("Arial", 12),
            bg='#f0f8ff',
            fg='#7f8c8d'
        )
        subtitle_label.pack()
        
        # Frame principal
        main_frame = tk.Frame(self.root, bg='#f0f8ff')
        main_frame.pack(pady=20, padx=20, fill='both', expand=True)
        
        # Frame de entrada
        input_frame = tk.LabelFrame(
            main_frame,
            text="Valores de Actividades de Sostenibilidad (0-10)",
            font=("Arial", 12, "bold"),
            bg='#ecf0f1',
            fg='#2c3e50',
            padx=20,
            pady=20
        )
        input_frame.pack(fill='x', pady=(0, 20))
        
        # Campos de entrada
        self.create_input_field(input_frame, "Actividad 1:", self.valor1_var, 0)
        self.create_input_field(input_frame, "Actividad 2:", self.valor2_var, 1)
        self.create_input_field(input_frame, "Actividad 3:", self.valor3_var, 2)
        self.create_input_field(input_frame, "Actividad 4:", self.valor4_var, 3)
        
        # Botón de cálculo
        calc_button = tk.Button(
            input_frame,
            text="CALCULAR OPCIONES",
            command=self.calcular_opciones,
            font=("Arial", 12, "bold"),
            bg='#3498db',
            fg='white',
            activebackground='#2980b9',
            activeforeground='white',
            relief='raised',
            borderwidth=2,
            padx=20,
            pady=10
        )
        calc_button.grid(row=4, column=0, columnspan=3, pady=20)
        
        # Frame de resultados
        result_frame = tk.LabelFrame(
            main_frame,
            text="Los 3 Operadores de Agregación Calculados",
            font=("Arial", 12, "bold"),
            bg='#ecf0f1',
            fg='#2c3e50',
            padx=20,
            pady=20
        )
        result_frame.pack(fill='both', expand=True)
        
        # Crear frame horizontal para los 3 operadores
        operadores_frame = tk.Frame(result_frame, bg='#ecf0f1')
        operadores_frame.pack(fill='x', expand=True)
        
        # Operador 1: T-normas
        op1_frame = tk.Frame(operadores_frame, bg='#ecf0f1', relief='solid', borderwidth=1)
        op1_frame.pack(side='left', fill='both', expand=True, padx=(0, 5))
        
        tk.Label(
            op1_frame,
            text="1. T-normas (del Mínimo):",
            font=("Arial", 11, "bold"),
            bg='#ecf0f1',
            fg='#e74c3c'
        ).pack(pady=(10, 5))
        
        result1_label = tk.Label(
            op1_frame,
            textvariable=self.resultado_minimo,
            font=("Arial", 16, "bold"),
            bg='white',
            fg='#e74c3c',
            relief='solid',
            borderwidth=1,
            padx=10,
            pady=8,
            width=8
        )
        result1_label.pack(pady=5)
        
        tk.Label(
            op1_frame,
            text="Operador lógico básico\nSe enfoca en la práctica\nmás deficiente",
            font=("Arial", 9, "italic"),
            bg='#ecf0f1',
            fg='#7f8c8d',
            justify='center'
        ).pack(pady=(5, 10))
        
        # Operador 2: S-normas
        op2_frame = tk.Frame(operadores_frame, bg='#ecf0f1', relief='solid', borderwidth=1)
        op2_frame.pack(side='left', fill='both', expand=True, padx=5)
        
        tk.Label(
            op2_frame,
            text="2. S-normas (del Máximo):",
            font=("Arial", 11, "bold"),
            bg='#ecf0f1',
            fg='#27ae60'
        ).pack(pady=(10, 5))
        
        result2_label = tk.Label(
            op2_frame,
            textvariable=self.resultado_maximo,
            font=("Arial", 16, "bold"),
            bg='white',
            fg='#27ae60',
            relief='solid',
            borderwidth=1,
            padx=10,
            pady=8,
            width=8
        )
        result2_label.pack(pady=5)
        
        tk.Label(
            op2_frame,
            text="Operador lógico básico\nSe enfoca en la\nmejor práctica",
            font=("Arial", 9, "italic"),
            bg='#ecf0f1',
            fg='#7f8c8d',
            justify='center'
        ).pack(pady=(5, 10))
        
        # Operador 3: Promedio/OWA
        op3_frame = tk.Frame(operadores_frame, bg='#ecf0f1', relief='solid', borderwidth=1)
        op3_frame.pack(side='left', fill='both', expand=True, padx=(5, 0))
        
        tk.Label(
            op3_frame,
            text="3. Promedio/OWA uniforme:",
            font=("Arial", 11, "bold"),
            bg='#ecf0f1',
            fg='#f39c12'
        ).pack(pady=(10, 5))
        
        result3_label = tk.Label(
            op3_frame,
            textvariable=self.resultado_promedio,
            font=("Arial", 16, "bold"),
            bg='white',
            fg='#f39c12',
            relief='solid',
            borderwidth=1,
            padx=10,
            pady=8,
            width=8
        )
        result3_label.pack(pady=5)
        
        tk.Label(
            op3_frame,
            text="Operador compensatorio\nPromedio de todas\nlas prácticas",
            font=("Arial", 9, "italic"),
            bg='#ecf0f1',
            fg='#7f8c8d',
            justify='center'
        ).pack(pady=(5, 10))
        
        # Frame de ejemplo
        example_frame = tk.LabelFrame(
            main_frame,
            text="Información de los Operadores",
            font=("Arial", 10, "bold"),
            bg='#ecf0f1',
            fg='#2c3e50',
            padx=15,
            pady=10
        )
        example_frame.pack(fill='x', pady=(20, 0))
        
        example_text = tk.Label(
            example_frame,
            text="T-normas y S-normas: Operadores lógicos básicos | Promedio: Operador compensatorio | OWA: Método adaptable",
            font=("Arial", 9),
            bg='#ecf0f1',
            fg='#7f8c8d'
        )
        example_text.pack(pady=2)
        
        scale_text = tk.Label(
            example_frame,
            text="Escala: Excelente (9-10) | Bueno (7-8) | Regular (5-6) | Deficiente (2-4)",
            font=("Arial", 9),
            bg='#ecf0f1',
            fg='#7f8c8d'
        )
        scale_text.pack()
        
    def create_input_field(self, parent, label_text, variable, row):
        # Etiqueta
        label = tk.Label(
            parent,
            text=label_text,
            font=("Arial", 11),
            bg='#ecf0f1',
            fg='#2c3e50'
        )
        label.grid(row=row, column=0, sticky='w', pady=5)
        
        # Campo de entrada
        entry = tk.Entry(
            parent,
            textvariable=variable,
            font=("Arial", 11),
            width=10,
            justify='center',
            relief='solid',
            borderwidth=1
        )
        entry.grid(row=row, column=1, padx=(10, 5), pady=5)
        
        # Validación visual
        def validate_input(event):
            try:
                value = float(variable.get())
                if 0 <= value <= 10:
                    entry.configure(bg='white')
                else:
                    entry.configure(bg='#ffcccb')
            except ValueError:
                if variable.get() == '':
                    entry.configure(bg='white')
                else:
                    entry.configure(bg='#ffcccb')
        
        entry.bind('<KeyRelease>', validate_input)
        
        # Etiqueta /10
        scale_label = tk.Label(
            parent,
            text="/10",
            font=("Arial", 11),
            bg='#ecf0f1',
            fg='#7f8c8d'
        )
        scale_label.grid(row=row, column=2, sticky='w', pady=5)
        
    def create_result_field(self, parent, label_text, description, variable, color, row):
        # Frame para cada resultado
        result_item_frame = tk.Frame(parent, bg='#ecf0f1')
        result_item_frame.pack(fill='x', pady=8)
        
        # Etiqueta principal
        main_label = tk.Label(
            result_item_frame,
            text=label_text,
            font=("Arial", 11, "bold"),
            bg='#ecf0f1',
            fg=color
        )
        main_label.pack(anchor='w')
        
        # Resultado
        result_label = tk.Label(
            result_item_frame,
            textvariable=variable,
            font=("Arial", 14, "bold"),
            bg='white',
            fg=color,
            relief='solid',
            borderwidth=1,
            padx=10,
            pady=5
        )
        result_label.pack(anchor='w', pady=(2, 2))
        
        # Descripción
        desc_label = tk.Label(
            result_item_frame,
            text=description,
            font=("Arial", 9, "italic"),
            bg='#ecf0f1',
            fg='#7f8c8d'
        )
        desc_label.pack(anchor='w')
        
    def calcular_opciones(self):
        try:
            # Obtener valores
            valores = [
                float(self.valor1_var.get()) if self.valor1_var.get() else 0,
                float(self.valor2_var.get()) if self.valor2_var.get() else 0,
                float(self.valor3_var.get()) if self.valor3_var.get() else 0,
                float(self.valor4_var.get()) if self.valor4_var.get() else 0
            ]
            
            # Validar que todos los valores estén entre 0 y 10
            if not all(0 <= v <= 10 for v in valores):
                messagebox.showerror("Error", "Todos los valores deben estar entre 0 y 10")
                return
            
            # Validar que al menos un valor sea diferente de 0
            if all(v == 0 for v in valores):
                messagebox.showwarning("Advertencia", "Ingrese al menos un valor mayor a 0")
                return
            
            # Filtrar valores 0 para el cálculo (opcional, dependiendo de tu lógica)
            valores_validos = [v for v in valores if v > 0]
            if not valores_validos:
                valores_validos = valores  # Si todos son 0, usar todos
            
            # Calcular operadores de agregación
            minimo = min(valores_validos)
            maximo = max(valores_validos)
            promedio = sum(valores_validos) / len(valores_validos)
            
            # Actualizar resultados
            self.resultado_minimo.set(f"{minimo:.1f}/10")
            self.resultado_maximo.set(f"{maximo:.1f}/10")
            self.resultado_promedio.set(f"{promedio:.2f}/10")
            
            # Mostrar mensaje de éxito
            messagebox.showinfo(
                "Cálculo Completado",
                f"Valores ingresados: {valores}\n\n"
                f"1. T-normas (Mínimo): {minimo:.1f}/10\n"
                f"2. S-normas (Máximo): {maximo:.1f}/10\n"
                f"3. Promedio/OWA uniforme: {promedio:.2f}/10"
            )
            
        except ValueError:
            messagebox.showerror(
                "Error de Entrada",
                "Por favor, ingrese valores numéricos válidos entre 0 y 10"
            )
        except Exception as e:
            messagebox.showerror("Error", f"Ha ocurrido un error: {str(e)}")
    
    def limpiar_campos(self):
        """Función para limpiar todos los campos"""
        self.valor1_var.set("")
        self.valor2_var.set("")
        self.valor3_var.set("")
        self.valor4_var.set("")
        self.resultado_minimo.set("")
        self.resultado_maximo.set("")
        self.resultado_promedio.set("")
        self.resultado_owa.set("")
    
    def run(self):
        # Agregar botón de limpiar
        clear_button = tk.Button(
            self.root,
            text="Limpiar Campos",
            command=self.limpiar_campos,
            font=("Arial", 10),
            bg='#95a5a6',
            fg='white',
            activebackground='#7f8c8d',
            relief='raised',
            borderwidth=1,
            padx=15,
            pady=5
        )
        clear_button.pack(pady=10)
        
        # Centrar ventana
        self.root.update_idletasks()
        width = self.root.winfo_width()
        height = self.root.winfo_height()
        x = (self.root.winfo_screenwidth() // 2) - (width // 2)
        y = (self.root.winfo_screenheight() // 2) - (height // 2)
        self.root.geometry(f'{width}x{height}+{x}+{y}')
        
        self.root.mainloop()


# Función principal para ejecutar la aplicación
def main():
    app = SustainabilityCalculatorGUI()
    app.run()

if __name__ == "__main__":
    main()