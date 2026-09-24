def classificar_aluno(nota):
    if nota >= 7:
        return "Aprovado"
    elif nota >= 5:
        return "Recuperação"
    else:
        return "Reprovado"


#
def calcular_media(alunos):
    if len(alunos) == 0:
        return 0
    soma = sum(aluno["nota"] for aluno in alunos)
    return soma / len(alunos)


alunos = []

#Loop principal (cadastro):permite cadastrar vários alunos de forma repetida
while True:
    # Entrada do nome
    nome = input("Digite o nome do aluno: ")

    # Idade (validação)
    while True:
        try:
            idade = int(input("Digite a idade: "))
            if idade <= 0:
                print("Idade inválida! Deve ser maior que 0.")
                continue
            break
        except:
            print("Erro: digite um número válido para idade.")

    # Nota (validação)
    while True:
        try:
            nota = float(input("Digite a nota: "))
            if nota < 0 or nota > 10:
                print("Nota inválida! Deve estar entre 0 e 10.")
                continue
            break
        except:
            print("Erro: digite um número válido para nota.")

    situacao = classificar_aluno(nota)

    #Lista
    alunos.append({
        "nome": nome,
        "idade": idade,
        "nota": nota,
        "situacao": situacao
    })
    #Controle de continuidade: O sistema solicita ao usuário se deseja continuar o cadastro.
    continuar = input("Deseja cadastrar outro aluno? (s/n): ").lower()
    if continuar != 's':
        break

# Esse trecho prepara o programa para contar quantos alunos estão em cada situação.
print("\n--- RESULTADO ---")

aprovados = 0
recuperacao = 0
reprovados = 0

# exibe informações de cada aluno e conta quantos estão em cada situação
for aluno in alunos:
    print(f"Aluno: {aluno['nome']} | Idade: {aluno['idade']} | Nota: {aluno['nota']:.1f} | Situação: {aluno['situacao']}")
    
    if aluno["situacao"] == "Aprovado":
        aprovados += 1
    elif aluno["situacao"] == "Recuperação":
        recuperacao += 1
    else:
        reprovados += 1

#É calculada a média geral das notas da turma por meio da função definida anteriormente.
media = calcular_media(alunos)

print(f"\nMédia da turma: {media}")
print(f"Aprovados: {aprovados}")
print(f"Recuperação: {recuperacao}")
print(f"Reprovados: {reprovados}")

#Identificação de extremos (maior e menor nota):A comparação é realizada com base no valor da chave "nota".
if alunos:
    maior = max(alunos, key=lambda x: x["nota"])
    menor = min(alunos, key=lambda x: x["nota"])

    print(f"\nAluno com maior nota: {maior['nome']} - {maior['nota']}")
    print(f"Aluno com menor nota: {menor['nome']} - {menor['nota']}")