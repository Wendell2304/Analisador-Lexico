import re

# 1. Definir as regras léxicas (padrões regex para cada token)
TOKEN_REGEX = [
    ("KEYWORD", r"\b(if|else|while|return)\b"),
    ("IDENTIFIER", r"[a-zA-Z_][a-zA-Z0-9_]*"),
    ("NUMBER", r"\b\d+\b"),
    ("OPERATOR", r"[\+\-\*/=]"),
    ("PAREN", r"[\(\)]"),
    ("BRACE", r"[{}]"),
    ("SEMICOLON", r";"),
    ("WHITESPACE", r"\s+"),  # Ignorar depois
]

# 2. Função para tokenizar o código-fonte
def tokenize(code):
    tokens = []
    pos = 0
    while pos < len(code):
        match = None
        for token_type, pattern in TOKEN_REGEX:
            regex = re.compile(pattern)
            match = regex.match(code, pos)
            if match:
                if token_type != "WHITESPACE":  # Ignorar espaços em branco
                    tokens.append({"type": token_type, "value": match.group(), "position": pos})
                pos = match.end()
                break
        if not match:
            raise SyntaxError(f"Caractere inesperado: {code[pos]} na posição {pos}")
    return tokens

# 3. Função principal para executar o analisador
def main():
    print("=== Analisador Léxico ===")
    code = input("Digite o código: ")
    try:
        tokens = tokenize(code)
        print("\nTokens:")
        for token in tokens:
            print(token)
    except SyntaxError as e:
        print(f"Erro: {e}")

# 4. Executar o programa
if __name__ == "__main__":
    main()

# Exemplos de código para testar:
# if (x == 10) return x + 1;
# while (y != 0) y = y - 1;
# else { x = x * 2; }

# O programa tokeniza o código digitado na entrada.
