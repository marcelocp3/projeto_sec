# Demonstração — Headers MVP

## Projeto e resultados

CLI Python com httpx e Rich que busca uma URL, avalia sete cabeçalhos
HTTP de segurança e retorna pontuação normalizada, nota e recomendações.
O MVP inclui Cross-Origin-Opener-Policy, JSON puro e verbose com todos
os cabeçalhos brutos da resposta, inclusive os que não são avaliados.

Validação realizada: 26 testes passaram; Ruff aprovado; Mypy com
`--strict` aprovado; Pylint 10/10. O `just` não está instalado no ambiente
usado para esta validação; os executáveis equivalentes da `.venv` foram usados.
O justfile teve os delimitadores Markdown removidos para ser utilizável.

Demonstração reproduzível: `demo_mvp.py` chama a CLI real e intercepta
HTTP com respx. Não acessa um servidor real nem valida TLS na internet.
Resposta completa: 100 pontos, nota A, código 0. Com `--weak`: CSP ausente,
COOP fraco, 69 pontos, nota D, código 1. O verbose mostra também `x-demo`.
Os testes cobrem as notas A/B (código 0), C/D (1), F e erro de rede (2),
JSON com verbose e os estados correto/fraco/ausente do sétimo cabeçalho.

A pontuação usa pesos high=30, medium=15 e low=5; cabeçalho fraco ganha
metade do peso. A soma máxima é 105, normalizada para 100. Limites:
A >=90, B >=80, C >=70, D >=60, F <60. É uma rubrica local inspirada
no Observatory; não equivale à nota oficial nem garante segurança do site.
A análise de CSP neste MVP verifica presença, sem analisar suas diretivas.

## O que é o `demo_mvp.py`?

É um arquivo auxiliar para executar o scanner em um cenário controlado,
sem depender da internet. Ele importa a função `main()` de
`http_headers_scanner.py`, que é o mesmo ponto de entrada usado ao analisar
um site real.

A biblioteca `respx` intercepta a requisição feita pelo `httpx` à URL
fictícia `https://demo.test/` e entrega uma resposta HTTP 200 com os
cabeçalhos definidos no arquivo. A partir daí, o scanner executa sua lógica
normal: avalia cada cabeçalho, calcula a pontuação e a nota e monta a saída.
A tabela e os resultados são calculados nessa execução; o arquivo de demo
não contém uma tabela pronta para imprimir.

Com `--weak`, a demo remove o CSP e muda o COOP para `unsafe-none` antes
de entregar a resposta ao scanner. Essas mudanças fazem o resultado cair
de A/100 para D/69 e geram recomendações. Você pode comparar os dois casos:

```bash
python demo_mvp.py
python demo_mvp.py --weak
```

Essa execução demonstra a análise e a saída da ferramenta. A conexão com
um servidor real e o TLS devem ser demonstrados usando
`python http_headers_scanner.py https://SEU-SITE-AUTORIZADO`.

Uma frase curta para explicar no vídeo: “Esse arquivo simula a resposta de
um site e passa os cabeçalhos para o scanner real, que calcula a nota na
hora. Se eu remover uma proteção, a nota cai e ele mostra a recomendação.”

## Gravação — no máximo 1 minuto

Deixe o terminal aberto na pasta do projeto, com fonte grande e a `.venv`
ativada. Escolha uma URL sua ou autorizada e teste antes de gravar.

```bash
cd /home/cuzo/Projetos/projects/Individual/Headers
source .venv/bin/activate
```

### Roteiro direto

- **0–10 segundos:** “Esse é o Headers, um scanner em Python que verifica
  sete cabeçalhos de segurança de um site e dá uma nota com recomendações.”
- **10–35 segundos:** execute o comando abaixo com a URL escolhida:

  ```bash
  python http_headers_scanner.py https://SEU-SITE-AUTORIZADO
  ```

  Enquanto roda: “Ele faz a requisição e verifica quais cabeçalhos estão
  corretos, fracos ou ausentes.”
- **35–50 segundos:** aponte a tabela, a nota e a pontuação. Diga: “Aqui está
  o resultado da análise e, se houver problemas, ele sugere como corrigir.”
- **50–60 segundos:** “Também tem saída JSON para automação e modo verbose
  para ver os cabeçalhos recebidos. É isso, valeu!”

Não precisa mostrar código, testes nem todas as flags nesse vídeo.
Se preferir a demonstração offline, rode `python demo_mvp.py` e diga
“Vou mostrar com uma resposta simulada”: o resultado será nota A, 100 pontos.

## Vídeo da entrega

Pendente: gravar, publicar e inserir aqui o link do vídeo.
O roteiro e a demonstração estão preparados; a gravação não foi realizada.
