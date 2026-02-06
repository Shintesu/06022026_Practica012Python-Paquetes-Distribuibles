# Curso de Python. Paquetes distribuibles. Vídeo 36
# paso a paso en OneNote
# archivo con nombre setup.py en la carpeta de PYTHON PRÁCTICAS


from setuptools import setup # importamos setup de setuptools

setup( # el comando setup espera que se le añada una dirección 
    name="Paquete Distribuible de Calculos",
    version="1.0",
    description="Paquete de operaciones de redondeo y potencia",
    author="Shintesu",
    author_email="leisberth.an24@gmail.com",
    url="www.miDirecciónPrivada.com",
    packages=["PaqueteCalculos","PaqueteCalculos.Modulo_RedondeoPotencia"] # packages indexa la dirección del paquete

)