import os
from fpdf import FPDF

class PDF(FPDF):
    def header(self):
        self.set_font("Helvetica", "B", 16)
        self.set_x(25.4)
        self.cell(165, 10, "Practica 3 - Robot Framework", align="C", new_x="LMARGIN", new_y="NEXT")
        self.set_y(self.get_y() + 5)

def main():
    pdf = PDF(format="letter")
    pdf.set_margins(left=25.4, top=25.4, right=25.4)
    pdf.add_page()
    w_seguro = 165
    
    # Repositorio Git
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_x(25.4)
    pdf.cell(w_seguro, 10, "Ruta de GIT del Proyecto:", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", size=11)
    pdf.set_x(25.4)
    pdf.multi_cell(w_seguro, 8, text="https://github.com/AlejandroDev77/practica-3-robot-framework", align="L", new_x="LMARGIN", new_y="NEXT")
    pdf.set_y(pdf.get_y() + 5)
    
    # Descripción de Estructura
    pdf.set_font("Helvetica", "B", 12)
    pdf.set_x(25.4)
    pdf.cell(w_seguro, 10, "Estructura del Proyecto:", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", size=11)
    pdf.set_x(25.4)
    pdf.multi_cell(w_seguro, 6, text="El proyecto esta divido en las carpetas recomendadas:\n- tests/: Archivos .robot con los Test Cases.\n- keywords/: Keywords personalizados (ej. Abrir Navegador, Tomar Captura).\n- variables/: Variables globales (URL, BROWSER).\n- screenshots/: Salida de las capturas de imagen.\n- reports/: Resultados log.html y output.xml.", align="L", new_x="LMARGIN", new_y="NEXT")
    pdf.set_y(pdf.get_y() + 5)

    # Ejercicio 2
    pdf.set_font("Helvetica", "B", 14)
    pdf.set_x(25.4)
    pdf.cell(w_seguro, 10, "Ejercicio 2 - Login Incorrecto", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", size=11)
    pdf.set_x(25.4)
    pdf.multi_cell(w_seguro, 6, text="Explicacion: Inicio de sesion automatizado con datos falsos.\nValidaciones implementadas:\n1) Element Text Should Be (css:.login-form h2) -> 'Login to your account'\n2) Element Text Should Be (xpath://form/p) -> 'Your email or password is incorrect!'", align="L", new_x="LMARGIN", new_y="NEXT")
    
    if os.path.exists("screenshots/ej2_error_login.png"):
        pdf.set_y(pdf.get_y() + 2)
        pdf.image("screenshots/ej2_error_login.png", x=25.4, w=w_seguro)
        pdf.set_y(pdf.get_y() + 5)
        
    # Ejercicio 3
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 14)
    pdf.set_x(25.4)
    pdf.cell(w_seguro, 10, "Ejercicio 3 - Busqueda de Productos", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", size=11)
    pdf.set_x(25.4)
    pdf.multi_cell(w_seguro, 6, text="Explicacion: Busqueda del termino 'tshirt' usando Keywords.\nValidaciones implementadas:\n1) Element Should Contain -> 'ALL PRODUCTS'\n2) Element Should Contain -> 'SEARCHED PRODUCTS'", align="L", new_x="LMARGIN", new_y="NEXT")
    
    if os.path.exists("screenshots/ej3_searched_products.png"):
        pdf.set_y(pdf.get_y() + 2)
        pdf.image("screenshots/ej3_searched_products.png", x=25.4, w=w_seguro)
        pdf.set_y(pdf.get_y() + 5)
        
    # Ejercicio 6
    pdf.add_page()
    pdf.set_font("Helvetica", "B", 14)
    pdf.set_x(25.4)
    pdf.cell(w_seguro, 10, "Ejercicio 6 - Suscripcion", new_x="LMARGIN", new_y="NEXT")
    pdf.set_font("Helvetica", size=11)
    pdf.set_x(25.4)
    pdf.multi_cell(w_seguro, 6, text="Explicacion: Scroll hacia el final de la pagina y suscripcion.\nValidaciones implementadas:\n1) Element Should Contain -> 'SUBSCRIPTION'\n2) Element Should Contain -> 'You have been successfully subscribed!'", align="L", new_x="LMARGIN", new_y="NEXT")
    
    if os.path.exists("screenshots/ej6_subscription_success.png"):
        pdf.set_y(pdf.get_y() + 2)
        pdf.image("screenshots/ej6_subscription_success.png", x=25.4, w=w_seguro)

    pdf.output("Practica3_Entregable.pdf")
    print("PDF generado con exito: Practica3_Entregable.pdf")

if __name__ == "__main__":
    main()
