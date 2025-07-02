import re

def eh_palindromo(frase: str) -> str:
  frase_limpa = re.sub(r'[^a-zA-Z0-9]', '', frase).lower()

  if frase_limpa == frase_limpa[::-1]:
    return "Sim"
  else:
    return "Não"

print(f"'Ovo' é um palíndromo? {eh_palindromo('Ovo')}")
print(f"'Anotaram a data da maratona' é um palíndromo? {eh_palindromo('Anotaram a data da maratona')}")
print(f"'BRSAO' é um palíndromo? {eh_palindromo('Gemini')}")