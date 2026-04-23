def formato_nombre(name, lastname):
    """
    Devuelve el nombre de usuario en el formato apellido, Nombre.

    Argumentos:
        name (str): Primer nombre del usuario.
        lastname (str):Apellido paterno del usuario.

    Retorno:
        (str): El nombre completo en formato Apellido, nombre.
    """
    return f"{lastname}, {name}"

#funcion main para la ejecucion del codigo.
def main():
    # Entrada de datos.
    print("--- Registro del usuario ---")
    nombre = input("introduce tu nombre: ")
    apellido = input("introduce tu apellido: ")

    #llama a tu funcion logica
    print(formato_nombre(nombre, apellido))


#El punto de entrada oficial del script
if __name__== "__main__":
    main()