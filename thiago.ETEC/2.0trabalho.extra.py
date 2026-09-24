def ler_numero(msg, tipo=float, minimo=None, maximo=None):
    while True:
        try:
            valor = tipo(input(msg))
            if minimo is not None and valor <= minimo:
                print(f"Valor deve ser maior que {minimo}.")
            elif maximo is not None and valor > maximo:
                print(f"Valor deve ser menor ou igual a {maximo}.")
            else:
                return valor
        except:
            print("Entrada inválida! Tente novamente.")


def classificar(nota):
    if nota >= 7:
        return "Aprovado"
    elif nota >= 5:
        return "Recuperação"
    return "Reprovado"


alunos = []

while True:
    nome = input("Nome: ")
    idade = ler_numero("Idade: ", int, minimo=0)
    nota = ler_numero("Nota: ", float, minimo=-1, maximo=10)

    #Validação de entrada (idade e nota)
    alunos.append({
        "nome": nome,
        "idade": idade,
        "nota": nota,
        "situacao": classificar(nota)
    })

    if input("Outro aluno? (s/n): ").lower() != 's':
        break


print("\n--- RESULTADO ---")

for a in alunos:
    print(f"{a['nome']} | {a['idade']} | {a['nota']:.1f} | {a['situacao']}")

media = sum(a["nota"] for a in alunos) / len(alunos)

aprov = sum(a["situacao"] == "Aprovado" for a in alunos)
recup = sum(a["situacao"] == "Recuperação" for a in alunos)
reprov = sum(a["situacao"] == "Reprovado" for a in alunos)

print(f"\nMédia: {media}")
print(f"Aprovados: {aprov}")
print(f"Recuperação: {recup}")
print(f"Reprovados: {reprov}")

maior = max(alunos, key=lambda x: x["nota"])
menor = min(alunos, key=lambda x: x["nota"])

print(f"\nMaior nota: {maior['nome']} - {maior['nota']}")
print(f"Menor nota: {menor['nome']} - {menor['nota']}")