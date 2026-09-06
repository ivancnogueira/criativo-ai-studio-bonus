# ⚡ Instalação em 1 Clique com o Antigravity IDE

Se você adquiriu ou recebeu o pacote de **Skills Bônus do Criativo AI Studio**, você **não precisa digitar comandos complicados no terminal**. 

Você pode simplesmente **copiar e colar o prompt abaixo diretamente no chat do Antigravity IDE** aberto dentro do seu estúdio.

---

## 🎯 Prompt de Instalação Automática (Copie e Cole no Antigravity)

Copie todo o bloco abaixo e envie para o Antigravity:

```text
Atue como Engenheiro de Instalação do Criativo AI Studio.

Identifiquei que tenho um pacote de 3 SKILLS BÔNUS que quero integrar ao meu projeto do Criativo AI Studio existente:
1. gerador-de-entregaveis (/gerador-de-entregaveis)
2. engenharia-reversa-concorrentes (/radar-concorrentes)
3. consistencia-personagem (/consistencia-personagem)

Por favor, execute a instalação completa e autônoma seguindo este roteiro:

1. Localize a pasta onde minhas habilidades/skills principais do Studio estão instaladas (verifique a pasta 'habilidades/', '.agents/skills/' ou o diretório de skills do Antigravity em '~/.gemini/config/skills').
2. Copie as pastas das 3 skills bônus para o mesmo local das outras habilidades do meu studio, mantendo todos os arquivos (SKILL.md, scripts e templates).
3. Verifique se as dependências necessárias (Node.js e Python com Pillow) estão operacionais.
4. Atualize o arquivo 'AGENTS.md' ou índice de habilidades do meu estúdio, registrando os 3 novos agentes de elite e seus respectivos comandos.
5. Finalize me apresentando um resumo amigável confirmando que a instalação foi concluída com sucesso e demonstrando um exemplo de como acionar cada uma das 3 novas skills.
```

---

## 🛠️ O que o Antigravity fará automaticamente:

Quando você colar esse prompt, o assistente inteligente irá:
1. **Escanear seu projeto atual**: Ele detecta a estrutura do seu estúdio ativo (`Criativo AI Studio` ou `social-media-studio`).
2. **Copiar os arquivos**: Ele transporta as 3 pastas com seus códigos, modelos e instruções para o local correto sem sobrescrever nada do seu trabalho.
3. **Validar o ambiente**: Testa se o gerador de PDF/Planilha e o compilador de consistência estão prontos.
4. **Atualizar a documentação**: Insere os 3 novos agentes no seu painel de controle de habilidades.
5. **Liberar os comandos**: Os 3 comandos `/gerador-de-entregaveis`, `/radar-concorrentes` e `/consistencia-personagem` passam a funcionar imediatamente em qualquer conversa do seu estúdio!

---

## 💻 Método Alternativo (Manual via Terminal PowerShell)

Caso prefira fazer a cópia manualmente via PowerShell no seu computador:

```powershell
# 1. Defina o caminho do seu estúdio existente:
$MeuStudio = "CAMINHO_DO_SEU_STUDIO"  # Ex: "C:\PROJETOS\meu-social-media-studio"

# 2. Copiar as 3 skills bônus para a pasta de habilidades do seu studio:
Copy-Item -Path "gerador-de-entregaveis", "engenharia-reversa-concorrentes", "consistencia-personagem" -Destination "$MeuStudio\habilidades\" -Recurse -Force

# 3. (Opcional) Copiar também para o Antigravity global:
Copy-Item -Path "gerador-de-entregaveis", "engenharia-reversa-concorrentes", "consistencia-personagem" -Destination "$HOME\.gemini\config\skills\" -Recurse -Force
```
