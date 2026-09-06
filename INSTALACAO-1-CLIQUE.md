# ⚡ Instalação em 1 Clique com o Antigravity IDE

Se você adquiriu ou recebeu o pacote de **Skills Bônus do Criativo AI Studio**, você **não precisa digitar comandos complicados no terminal**. 

Você pode simplesmente **copiar e colar o prompt abaixo diretamente no chat do Antigravity IDE** aberto dentro do seu estúdio existente.

---

## 🎯 Prompt de Instalação Automática (Copie e Cole no Antigravity)

Copie todo o bloco abaixo e envie para o Antigravity no seu estúdio:

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

---

## 🛠️ O que o Antigravity fará automaticamente:

Quando você colar esse prompt, o assistente inteligente irá:
1. **Baixar o repositório bônus**: Clona `https://github.com/ivancnogueira/criativo-ai-studio-bonus.git` diretamente na sua máquina.
2. **Escanear seu projeto atual**: Detecta onde suas habilidades existentes estão instaladas (`Criativo AI Studio` ou `social-media-studio`).
3. **Copiar os arquivos**: Transporta as 3 pastas com seus códigos, modelos e instruções para o local correto sem sobrescrever nada do seu trabalho anterior.
4. **Validar o ambiente**: Testa se o gerador de PDF/Planilha e o compilador de consistência estão prontos.
5. **Atualizar a documentação**: Insere os 3 novos agentes no seu painel de controle `AGENTS.md`.
6. **Liberar os comandos**: Os 3 comandos `/gerador-de-entregaveis`, `/radar-concorrentes` e `/consistencia-personagem` passam a funcionar imediatamente em qualquer conversa do seu estúdio!

---

## 💻 Método Alternativo (Manual via Terminal PowerShell)

Caso prefira fazer a cópia manualmente via PowerShell no seu computador:

```powershell
# 1. Clonar o repositório de bônus:
git clone https://github.com/ivancnogueira/criativo-ai-studio-bonus.git temp-bonus

# 2. Defina o caminho do seu estúdio existente:
$MeuStudio = "CAMINHO_DO_SEU_STUDIO"  # Ex: "C:\PROJETOS\meu-social-media-studio"

# 3. Copiar as 3 skills bônus para a pasta de habilidades do seu studio:
Copy-Item -Path "temp-bonus\gerador-de-entregaveis", "temp-bonus\engenharia-reversa-concorrentes", "temp-bonus\consistencia-personagem" -Destination "$MeuStudio\habilidades\" -Recurse -Force

# 4. (Opcional) Copiar também para o Antigravity global:
Copy-Item -Path "temp-bonus\gerador-de-entregaveis", "temp-bonus\engenharia-reversa-concorrentes", "temp-bonus\consistencia-personagem" -Destination "$HOME\.gemini\config\skills\" -Recurse -Force

# 5. Limpar pasta temporária:
Remove-Item -Path "temp-bonus" -Recurse -Force
```
