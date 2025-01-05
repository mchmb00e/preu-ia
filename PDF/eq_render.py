import subprocess
from PIL import Image
import os

def render_latex_to_image(latex_code, output_image_path='output.png'):
    # Escribir el código LaTeX en un archivo temporal
    with open('temp.tex', 'w') as f:
        f.write(r'''
        \documentclass{standalone}
        \usepackage{amsmath}
        \begin{document}
        % Aquí va el código LaTeX
        % Lo reemplazamos con la entrada
        ''' + latex_code + r'''
        \end{document}
        ''')

    # Ejecutar pdflatex para generar el archivo .pdf
    subprocess.run(['pdflatex', 'temp.tex'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Convertir el archivo .pdf a .png usando pdftoppm (parte de la instalación de LaTeX)
    subprocess.run(['pdftoppm', 'temp.pdf', 'temp', '-png', '-r', '150'])  # Resolución más baja


    # Abrir la imagen generada
    img = Image.open('temp-1.png')

    # Guardar la imagen
    img.save(output_image_path)

    # Limpiar archivos temporales
    os.remove('temp.tex')
    os.remove('temp.pdf')
    os.remove('temp-1.png')

    return img

# Texto LaTeX de entrada
latex_text = r'El resultado de sumar $\frac{2}{3}$ y $\frac{1}{3}$ es $1$'

# Llamada a la función para renderizar LaTeX y guardar la imagen
img = render_latex_to_image(latex_text)
img.show()  # Muestra la imagen generada
