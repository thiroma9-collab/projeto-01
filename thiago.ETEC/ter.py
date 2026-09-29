void main() {
  Map<String, dynamic> programador = {
    "nome": "João",
    "celular": "11999999999",
    "linguagens": ["Dart", "Python", "Java"],
  };

  print(programador);

  programador["linguagens"].add("JavaScript");

  print("\nProgramador atualizado:");
  print(programador);

  List<Map<String, dynamic>> programadores = [
    {
      "nome": "João",
      "celular": "11999999999",
      "linguagens": ["Dart", "Python"],
    },
    {
      "nome": "Maria",
      "celular": "11888888888",
      "linguagens": ["Java", "C#"],
    },
    {
      "nome": "Carlos",
      "celular": "11777777777",
      "linguagens": ["JavaScript", "PHP"],
    },
  ];

  programadores.add({
    "nome": "Ana",
    "celular": "11666666666",
    "linguagens": ["C++", "Python"],
  });

  programadores.last["linguagens"].add("Dart");

  print("\nProgramadores:");

  for (var programador in programadores) {
    print(
      "Nome: ${programador["nome"]} - "
      "Primeira linguagem: ${programador["linguagens"][0]}",
    );
  }
}