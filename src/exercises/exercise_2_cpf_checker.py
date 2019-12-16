""""
=[Enunciado]============================================================================================================
Desenvolver e testar uma função que valide se um número de CPF é válido.

Condições:

 - Deve conter 11 dígitos.
 - Deve ser uma entrada de dígitos exclusivamente, sem texto.
 - Os números não podem ser todos repetidos.
 - Os dígitos devem ser cálculados corretamente, pelo cálculo oficial.

=[Cálculo do dígito verificador do CPF]=================================================================================

O CPF (Cadastro de Pessoas Físicas), emitido pela Receita Federal, é caracterizado por uma função entre o conjunto das
pessoas físicas cadastradas e o conjunto dos documentos emitidos.

Ou seja, o fato de um número de CPF ser autenticado pelos seus dígitos verificadores, não o torna um CPF válido, pois é
necessário que ele esteja cadastrado no banco de dados da Receita Federal. Assim, um número válido de CPF nem sempre
será um documento já emitido. Porém, os dígitos verificadores servem para alertar que o número foi escrito de forma
inadequada, sem precisar acessar o banco de dados da Receita Federal.

- Regra Prática ------------

O número de um CPF tem 9 algarismos e mais dois dígitos verificadores, que são indicados após uma barra. Logo, um CPF
tem 11 algarismos. O número do CPF é escrito na forma ABCDEFGHI/JK ou diretamente como ABCDEFGHIJK, onde os algarismos
não podem ser todos iguais entre si.

O J é chamado 1° dígito verificador do número do CPF.
O K é chamado 2° dígito verificador do número do CPF.

- Primeiro Dígito -----------

Para obter J multiplicamos A, B, C, D, E, F, G, H e I pelas constantes correspondentes:

|  A|  B|  C|  D|  E|  F|  G|  H|  I|
|x10| x9| x8| x7| x6| x5| x4| x3| x2|

O resultado da soma, 10A + 9B + 8C + 7D + 6E + 5F + 4G + 3H + 2I, é dividido por 11.

Analisamos então o RESTO dessa divisão:

Se for 0 ou 1, o dígito J é [0] (zero). Se for 2, 3, 4, 5, 6, 7, 8, 9 ou 10, o dígito J é [11 - RESTO]

- Segundo Dígito ------------

Já temos J. Para obter K multiplicamos A, B, C, D, E, F, G, H, I e J pelas constantes correspondentes:

|  A|  B|  C|  D|  E|  F|  G|  H|  I|  J|
|x11|x10| x9| x8| x7| x6| x5| x4| x3| x2|

O resultado da soma, 11A + 10B + 9C + 8D + 7E + 6F + 5G + 4H + 3I + 2J, é dividido por 11.

Verificamos então o RESTO dessa divisão:

Se for 0 ou 1, o dígito K é [0] (zero). Se for 2, 3, 4, 5, 6, 7, 8, 9 ou 10, o dígito K é [11 - RESTO].
"""


class CPF:
    def __init__(self, value=None):
        self.value = value

    def __str__(self):
        return str(self.value)

    def Is_Valid(self):

        cpf = self.value

        if (not cpf) or (len(cpf) != 11):
            return False

        if not cpf.isdigit():
            return False

        verifying_digit_1 = cpf[10]
        verifying_digit_2 = cpf[11]


# The main program.
while True:
    print("Informe o CPF a ser validado, somente números (use <CTRL + C> para sair): ")
    input_cpf = int(input())

    cpf = CPF(input_cpf)
    print(str(cpf) + " é um CPF " + ("válido" if cpf.Is_Valid else "inválido") + ".\n")
