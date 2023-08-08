def retornar_menu_principal():
    retornar_menu_principal = input("Deseja retornar ao menu principal? ")
    while True:
        if retornar_menu_principal == "sim":
            retorna_menu = True
        elif retornar_menu_principal == "não":
            retorna_menu = False
        else:
            retornar_menu_principal = input("Deseja retornar ao menu principal? (sim/não): ")
        return retorna_menu

def formata_texto(texto):
    texto_formatado = texto.title()
    return texto_formatado
