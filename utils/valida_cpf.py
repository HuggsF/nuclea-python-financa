from validate_docbr import CPF

def valida_cpf():

    cpf_validador = CPF()

    while True:
        cpf = input("CPF: ")
        resultado_validacao = cpf_validador.validate(cpf)

        if (resultado_validacao):
            cpf_formatado = cpf

            if len(cpf) == 11:
                cpf_formatado= f"{cpf[0:3]}.{cpf[3:6]}.{cpf[6:9]}-{cpf[9:11]}"

            return cpf_formatado
        else:
            print("CPF inválido. Tente novamente: ")

def gera_cpf():
    cpf = CPF()
    cpf_gerado = cpf.generate()
    return cpf_gerado



