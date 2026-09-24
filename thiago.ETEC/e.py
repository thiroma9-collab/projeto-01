def classificar(nota):
    return "Aprovado" if nota >= 7 else "Recuperação" if nota >= 5 else "Reprovado"


def media_turma(alunos):
    return sum(a["nota"] for a in alunos) / len(alunos) if alunos else 0


alunos = []

while True:
    nome = input("Nome: ")

    while True:
        try:
            idade = int(input("Idade: "))
            if idade > 0:
                break
            print("Idade inválida!")
        except ValueError:
            print("Digite um número válido.")

    while True:
        try:
            nota = float(input("Nota: "))
            if 0 <= nota <= 10:
                break
            print("Nota deve estar entre 0 e 10.")
        except ValueError:
            print("Digite um número válido.")

    alunos.append({
        "nome": nome,
        "idade": idade,
        "nota": nota,
        "situacao": classificar(nota)
    })

    if input("Continuar? (s/n): ").lower() != "s":
        break

print("\n--- RESULTADO ---")

aprovados = sum(a["situacao"] == "Aprovado" for a in alunos)
recuperacao = sum(a["situacao"] == "Recuperação" for a in alunos)
reprovados = len(alunos) - aprovados - recuperacao

for a in alunos:
    print(f"{a['nome']} | {a['idade']} | {a['nota']:.1f} | {a['situacao']}")

print(f"\nMédia: {media_turma(alunos):.2f}")
print(f"Aprovados: {aprovados}")
print(f"Recuperação: {recuperacao}")
print(f"Reprovados: {reprovados}")

if alunos:
    maior = max(alunos, key=lambda a: a["nota"])
    menor = min(alunos, key=lambda a: a["nota"])

    print(f"\nMaior nota: {maior['nome']} - {maior['nota']}")
    print(f"Menor nota: {menor['nome']} - {menor['nota']}")