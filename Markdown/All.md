# Iniciando na programação com Python ( Lógica de programação básica )

📅 **06/05/2025**

O professor vai abordar tudo do básico em Python, com foco em lógica de programação.

---

## Aula 1 - Criando meu primeiro módulo Python

Para começar a programar em Python, criamos **um arquivo `.py`** ( extensão de arquivos Python ) dentro de uma **pasta do projeto**.

**Passos:**
1. Abra o **VSCode**.
2. Clique em **"File" > "New Folder"** para criar uma pasta do projeto.
3. Dentro da pasta, clique em **"New File"** e salve como `Class01`.
4. Pronto! Você já pode começar a digitar seus códigos em Python.

---

## Aula 2 - Criando comentários em Python

Comentários são ignorados pelo Python, e servem apenas para anotações no código.

- Para escrever um comentário de uma única linha, use a cerquilha ( `#` ).

## Aula 2.1 - Docstrings como comentários

Docstrings são textos entre três aspas ( `'''` ou `"""` ) usados geralmente para **documentar funções, classes ou módulos.** Porém, algumas pessoas também os usam como comentários de múltiplas linhas.

## Aula 2.2 - A função `print`

A função `print()` serve para mostrar informações na tela, geralmente no terminal. É usada o tempo todo em programas Python.

---

## Aula 3 - Tipos de string ( Introdução aos tipos de dados )

Strings são textos em Python, e podem ser representadas de diferentes formas:

- **Aspas simples.**
- **Aspas duplas.**
- **Escape de caracteres** ( Quando você quer usar aspas dentro de aspas ).
- **Uso misto de aspas** ( Mais simples que o escape ).
- **Prefixo `r` ( raw string )** Impede que o Python interprete os caracteres especiais.

## Aula 3.1 - Tipos int e float ( Números )

Além de textos, o Python também trabalha com números.

- **Inteiros** ( `int` ): números sem casas decimais.
- **Ponto flutuante** ( `float` ): números com casas decimais.

## Aula 3.2 - Tipo bool ( Boolean )

O tipo `bool` representa os **valores lógicos**: `True` ( verdadeiro ) e `False` ( falso ).

---

## Aula 4 - Variáveis

**Variáveis**, são usadas para armazenar valores que podemos usar depois no código. Também conhecemos a **f-string**, uma forma prática de montar frases com variáveis dentro do `print()`.

### O que é uma variável?

Uma variável é como uma "caixa" com um nome, onde você guarda um valor. Esse valor pode ser alterado ou utilizado em outras partes do programa.

### f-string ( formatação de string )

A f-string permite inserir valores de variáveis dentro de uma string com muita facilidade. Basta colocar um `f` antes das aspas e usar `{}` para incluir a variável.

---

## Aula 5 - Introdução aos operadores aritméticos (matemática)

Nessa aula, falamos os principais **operadores aritméticos** do Python. Eles são usados para realizar **cálculos matemáticos**.

### Adição (`+`)
Soma dois valores.

### Subtração (`-`)
Subtrai um valor do outro.

### Multiplicação (`*`)
Multiplica dois valores.

### Divisão (`/`)
Divide um valor pelo outro. Sempre retorna float.

### Divisão inteira (`//`)
Divide e retorna somente a parte inteira do resultado.

### Exponenciação (`**`)
Potência — eleva um número a outro.

### Módulo (`%`)
Resto da divisão.

## Aula 5.1 - Precedência entre os operadores aritméticos

Nessa aula, falamos sobre a **ordem de precedência** entre os operadores aritméticos em Python. Assim como na matemática, algumas operações são feitas antes de outras, a não ser que a gente use parênteses para alterar essa ordem.

### Ordem de precedência dos operadores em Python:

1. **Parênteses** `()`
2. **Exponenciação** `**`
3. **Multiplicação**, **Divisão**, **Divisão inteira**, **Módulo** `* / // %`
4. **Adição** e **Subtração** `+ -`

---

## Aula 6 - Usando a função input()

Nesta aula, usamos a função `input()` para **receber dados do usuário** durante a execução do programa.

### O que é a função `input()`?

A função `input()` **espera que o usuário digite algo** no terminal e aperte Enter. O valor digitado é **sempre retornado como uma string ( `str` )**, mesmo que o usuário digite um número.

### Convertendo o input para números

Como tudo que vem do `input()` é uma string, precisamos converter quando queremos fazer operações matemáticas. Para isso usamos:

- `int()` → para converter para inteiro.
- `float()` → para converter para número com casas decimais.

---

## Aula 7 - Introdução as Condicionais

Nesta aula falamos sobre estruturas condicionais no Python: `if`, `elif` e `else`.

- `if` é usado para **verificar uma condição**.
- `elif` (else if) serve como uma **segunda ou mais alternativas**.
- `else` é o **caminho final**, caso nenhuma das condições anteriores seja verdadeira.

---

## Aula 8 - Operadores relacionais

Nesta aula usamos os **operadores relacionais**, que são usados para **comparar valores**. Eles retornam um valor do tipo **booleano** ( `True` ou `False` ), e são muito usados em condicionais.

| Operador | Significado    | Exemplo  | Resultado |
| -------- | -------------- | -------- | --------- |
| `>`      | Maior que      | `2 > 1`  | `True`    |
| `<`      | Menor que      | `1 < 2`  | `True`    |
| `>=`     | Maior ou igual | `2 >= 1` | `True`    |
| `<=`     | Menor ou igual | `1 <= 2` | `True`    |
| `==`     | Igual a        | `2 == 2` | `True`    |
| `!=`     | Diferente de   | `1 != 2` | `True`    |

---

## Aula 9 - Operadores Lógicos ( And, Or, Not e In )

Nesta aula usamos os **operadores lógicos**, que são usados para combinar expressões booleanas e retornar `True` ou `False`.

## Aula 9.1 - Operador Lógico `And`

O operador `and` só retorna `True` **se todas as condições forem verdadeiras**. Se uma das condições for falsa, o resultado já será `False`.

## Aula 9.2 - Operador Lógico `Or`

O operador `or` retorna `True` **se pelo menos uma das condições for verdadeira**. Ele só retorna `False` se todas as condições forem falsas.

## Aula 9.3 - Operador Lógico `Not`

O operador `not` **inverte** o valor lógico de uma condição. Se a condição for `True`, ele transforma em `False`, e se for False, ele transforma em `True`.

## Aula 9.4 - Operador Lógico `In`

O operador `in` é usado para verificar se **um valor está contido dentro de uma sequência**.

### Aula 9.4.1 - `In` e `Not in`

O operador `not in` faz o oposto **verifica se um valor não está contido dentro da sequência**.

---

## Aula 10 - Fatiamento de Strings e a Função `len()`

O fatiamento permite pegar partes de uma string utilizando a notação `[início:fim:passo]`.

- `"Python"[0:3]` → `'Pyt'` ( pega do índice 0 até o 2 )
- `"Python"[::2]` → `'Pto'` ( pula de 2 em 2 )
- `"Python"[::-1]` → `'nohtyP'` ( string invertida )

## Aula 10.1 - Função `len()`

A função `len()` retorna o número de caracteres de uma string. Ela é útil para saber onde um fatiamento pode terminar ou para validar o tamanho de um texto.

--- 

## Aula 11 - Introdução ao `try` e `except`

Nesta aula aprendemos como lidar com erros que podem ocorrer durante a execução do programa, utilizando os blocos try e except. O bloco `try` serve para **testar** um trecho de código que **pode causar erro**. Se acontecer algum erro, o programa **não trava**, ele pula para o bloco `except` e executa o que estiver lá.

--- 

## Aula 12 - Flags, `is`, `is not` e `None`

Nesta aula aprendemos sobre **controle de estado** usando *flags*, e também sobre os operadores de identidade `is`, `is not` e o valor especial `None`, muito usado para representar ausência de valor.

## Aula 12.1 - Flag

Uma *flag* é uma variável que usamos para **controlar o fluxo** do programa, geralmente começando como `False` ou `None`, e sendo alterada durante a execução.

## Aula 12.2 - `Is` e `Is not`

São operadores de **identidade**, usados para saber se duas variáveis apontam para o **mesmo objeto na memória**.

- `a is b` → retorna `True` se `a` e `b` são o mesmo objeto.
- `a is not b` → retorna `True` se `a` e `b` são objetos diferentes.