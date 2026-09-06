# 🎁 Skills & Agentes Bônus Exclusivos — Criativo AI Studio

Este repositório contém o pacote com as **3 Skills Bônus de Alta Performance** desenvolvidas para expandir o seu estúdio do **Criativo AI Studio**.

---

## ⚡ Como Instalar no seu Studio Existente (Prompt 1-Clique)

Não precisa mexer em terminal nem configurar nada manualmente. **Basta abrir o Antigravity no seu Studio existente e colar o prompt abaixo no chat:**

```text
Atue como Engenheiro de Instalação do Criativo AI Studio.

Quero instalar e integrar as 3 SKILLS BÔNUS oficiais ao meu projeto existente do Criativo AI Studio.

Repositório Oficial dos Bônus:
https://github.com/ivancnogueira/criativo-ai-studio-bonus.git

As 3 skills bônus que quero instaladas são:
1. gerador-de-entregaveis (comando: /gerador-de-entregaveis)
2. engenharia-reversa-concorrentes (comandos: /radar-concorrentes ou /engenharia-reversa-concorrentes)
3. consistencia-personagem (comando: /consistencia-personagem)

Por favor, execute a instalação completa e autônoma seguindo este roteiro:

1. Clone temporariamente ou baixe os arquivos do repositório 'https://github.com/ivancnogueira/criativo-ai-studio-bonus.git' em uma pasta temporária.
2. Localize a pasta onde minhas habilidades/skills principais do Studio estão instaladas no meu projeto ativo (verifique 'habilidades/', '.agents/skills/' ou o diretório global de skills do Antigravity em '~/.gemini/config/skills').
3. Copie as pastas completas das 3 skills bônus ('gerador-de-entregaveis', 'engenharia-reversa-concorrentes' e 'consistencia-personagem') para o mesmo local das outras habilidades do meu studio, mantendo todos os arquivos (SKILL.md, scripts e templates).
4. Verifique se as dependências necessárias do ambiente (Node.js e Python com Pillow) estão operacionais.
5. Atualize o arquivo 'AGENTS.md' ou índice de habilidades do meu estúdio, registrando os 3 novos agentes de elite e seus respectivos comandos.
6. Exclua a pasta temporária do clone após a cópia.
7. Finalize me apresentando um resumo confirmando que a instalação foi concluída com sucesso e demonstrando um exemplo prático de como acionar cada uma das 3 novas skills.
```

O Antigravity identificará o seu estúdio, baixará os arquivos do repositório, copiará para as pastas corretas, atualizará o `AGENTS.md` e deixará os comandos prontos para uso imediato!

*(Para instruções detalhadas ou método alternativo via PowerShell, consulte o guia [INSTALACAO-1-CLIQUE.md](INSTALACAO-1-CLIQUE.md)).*

---

## 📦 As 3 Habilidades Bônus Incluídas

### 1. 📄 Gerador de Entregáveis (`/gerador-de-entregaveis`)
- **Pasta:** `gerador-de-entregaveis/`
- **Função:** Empacota posts, carrosséis, stories e calendários em produtos finais prontos para validação e entrega ao cliente ou equipe.
- **Entregáveis Suportados:**
  - **PDF Executivo / Deck de Apresentação:** Layout A4 paisagem de luxo (`deck-aprovacao-template.html`), mockups de Instagram em escala real lado a lado, legenda diagramada e checklist com campo de assinatura formal de aprovação.
  - **Planilha Editorial Completa:** Formato `.csv` compatível com Excel e Google Sheets com colunas de data, horário, pilar, gancho, legenda e status.
  - **Showcase Web Interativo:** Landing page responsiva (`showcase-aprovacao-template.html`) com slider mobile, botão de cópia de legenda em 1 clique e botões de aprovação/ajustes.
  - **Dossiê Estratégico:** Documento completo em Markdown/DOCX com o racional criativo da campanha.
- **Automação Inclusa:** Script `scripts/compilar-entregavel.mjs` que processa uma pasta e compila tudo automaticamente.

---

### 2. 🕵️ Engenharia Reversa de Concorrentes (`/radar-concorrentes`)
- **Pasta:** `engenharia-reversa-concorrentes/`
- **Gatilhos:** `/radar-concorrentes` ou `/engenharia-reversa-concorrentes`
- **Função:** Inteligência de mercado forense para mapear exatamente o que funciona no nicho e superar a concorrência.
- **Destaques:**
  - **Engenharia Reversa de Ganchos (Hooks):** Desmonta as fórmulas psicológicas dos posts virais dos concorrentes e gera versões 10x mais magnéticas.
  - **Autópsia Estrutural de Carrosséis:** Mapeia quantidade ideal de slides, pontos de retenção e chamadas para ação.
  - **Brechas Estéticas:** Identifica onde o concorrente é esteticamente fraco para entrar com design superior.
  - **Rastreamento de Funis Ocultos:** Mapeia a esteira de produtos e a máquina de vendas no direct dos perfis analisados.
  - **Dossiê de Contra-Ataque:** Entrega de 10 a 15 pautas prontas para execução imediata no Studio.

---

### 3. 👤 Criador de Consistência de Personagem (`/consistencia-personagem`)
- **Pasta:** `consistencia-personagem/`
- **Gatilho:** `/consistencia-personagem`
- **Função:** Elimina o maior problema de modelos de imagem de IA: a variação de rosto e corpo entre slides e posts.
- **Destaques:**
  - **Entrevista Antropométrica Guiada:** Coleta biotipo, altura, mandíbula, olhos, corte de cabelo, tom de pele e guarda-roupa assinatura.
  - **Folha Mestra de Consistência (Grid de 13 Painéis):**
    - *Linha 1:* 4 contextos e iluminações (estúdio neutro, luz natural em parque, pôr do sol, luz noturna/vela).
    - *Linha 2:* 4 expressões faciais vivas e perfil estrito de 90°.
    - *Linha 3:* Turnaround corporal 360° em 5 ângulos alinhados (0°, 45°, 90°, 135°, 180°).
  - **Tokens Âncora & Injeção Automática:** Gera o manual `PERSONAGEM.md` e o arquivo `consistencia.json` consumidos automaticamente pelos agentes de geração de imagem (`criar-carrossel`, `criar-post-individual`, `gerar-stories` e `criar-post-anuncio`).
  - **Script de Compilação:** `scripts/montar-folha-consistencia.py` monta a folha mestra em alta definição (`2048x2048px`).

---

## 🎯 Como Usar no Dia a Dia

Uma vez instalado no seu estúdio, basta digitar no chat do Antigravity:
- `/gerador-de-entregaveis` — Para empacotar qualquer post em PDF, planilha ou showcase web.
- `/radar-concorrentes` — Para espionar um perfil ou mapear o que está em alta no seu nicho.
- `/consistencia-personagem` — Para cadastrar uma nova pessoa ou avatar e gerar sua folha mestre de consistência.
