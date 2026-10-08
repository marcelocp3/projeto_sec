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

## Preparação da gravação

Grave a tela e sua voz. Deixe o terminal com fonte grande e feche janelas
que exibam informações pessoais. Faça um ensaio dos comandos abaixo antes.
Duração sugerida pelo repositório: 5–10 minutos.

```bash
cd /home/cuzo/Projetos/projects/Individual/Headers
source .venv/bin/activate
```

Se precisar preparar o ambiente em outra máquina: `uv sync --all-extras`.
Os comandos a seguir usam a `.venv` ativada e dispensam o just.

## Roteiro de vídeo (aproximadamente 8 minutos)

1. **Contexto — 45 segundos.** Explique: “O projeto verifica cabeçalhos
   de segurança HTTP. Cabeçalhos ausentes ou fracos podem reduzir proteções
   do navegador. A ferramenta ajuda a identificar essas configurações.”
2. **Construção — 1 minuto.** Abra `http_headers_scanner.py`. Mostre `RULES`,
   `evaluate_header`, `scan` e `main`. Explique o fluxo: URL → requisição →
   avaliação → pontuação → tabela ou JSON. Mostre a regra COOP adicionada.
3. **Execução — 3 minutos.** Execute um comando por vez:

   ```bash
   python demo_mvp.py
   python demo_mvp.py --verbose
   python demo_mvp.py --json
   python demo_mvp.py --weak
   echo $?
   ```

   Diga explicitamente: “Esta primeira demonstração usa uma resposta HTTPS
   simulada, para tornar os resultados reproduzíveis.” Mostre os sete
   cabeçalhos, nota A/100 e COOP correto. No verbose, destaque `x-demo` antes
   da tabela. No JSON, explique `score`, `grade` e `findings`. No cenário
   fraco, destaque CSP ausente, COOP fraco, as recomendações e código 1.

   Para a execução real pedida pelo padrão da demo, use um site seu ou
   autorizado. Substitua a URL abaixo antes de executar:

   ```bash
   python http_headers_scanner.py https://SEU-SITE-AUTORIZADO --verbose
   echo $?
   ```

   Explique que a nota depende da resposta atual do servidor; não prometa A.
4. **Decisões — 1 minuto.** Explique por que as regras são dados e a avaliação
   é separada da rede: novas regras são fáceis de adicionar e os testes ficam
   independentes da disponibilidade de sites. Explique o peso maior de HSTS
   e CSP e a normalização para 100. JSON serve para automações; verbose ajuda
   a conferir os valores enviados pelo servidor.
5. **Validação — 1 minuto.** Execute:

   ```bash
   python -m pytest -q
   ruff check http_headers_scanner.py test_http_headers_scanner.py demo_mvp.py
   mypy --strict http_headers_scanner.py
   pylint http_headers_scanner.py
   ```

   Com just instalado, os atalhos são `just test` e `just lint`.
6. **Aprendizado e próximos passos — 30 segundos.** Explique o que aprendeu
   sobre HTTP, testes de rede simulada e CLI. Cite análise aprofundada de CSP
   ou múltiplas URLs como extensões e V_Scanner como próximo projeto da trilha.

## Vídeo da entrega

Pendente: gravar, publicar e inserir aqui o link do vídeo.
O roteiro e a demonstração estão preparados; a gravação não foi realizada.
