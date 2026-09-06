# Ficha de Consistência de Persona: {{NOME_PERSONAGEM}}

> **Identificador Único:** `{{SLUG_PERSONAGEM}}`  
> **Tipo:** {{TIPO_PERSONA}} (Pessoa Real / Persona Sintética 100% IA)  
> **Data de Criação:** {{DATA_CRIACAO}}  
> **Status:** Ativo & Travado para Produção  

---

## 1. Antropometria & DNA Visual

### Características Faciais
- **Gênero & Idade Aparente:** {{GENERO}}, {{IDADE_APARENTE}} anos
- **Etnia & Tom de Pele:** {{ETNIA}}, tom de pele {{TOM_PELE}}
- **Formato do Rosto:** {{FORMATO_ROSTO}} (mandíbula, queixo, maçãs do rosto)
- **Olhos:** {{COR_OLHOS}}, formato {{FORMATO_OLHOS}}, sobrancelhas {{SOBRANCELHAS}}
- **Nariz & Boca:** Nariz {{NARIZ}}, lábios {{LABIOS}}
- **Cabelo:** Cor {{COR_CABELO}}, textura {{TEXTURA_CABELO}}, corte/estilo {{CORTE_CABELO}}
- **Pelos Faciais / Barba:** {{BARBA_DETALHES}}
- **Marcas Distintivas:** {{MARCAS_UNICAS}}

### Biotipo Corporal
- **Altura Estimada:** {{ALTURA}}
- **Porte Físico:** {{PORTE_FISICO}} (ombros, postura, compleição física)

---

## 2. Guarda-Roupa Âncora (Signature Outfits)

### Traje Principal (Signature Look)
- **Parte Superior:** {{TRAJE_PRINCIPAL_SUPERIOR}}
- **Parte Inferior:** {{TRAJE_PRINCIPAL_INFERIOR}}
- **Calçados:** {{CALCADOS_PRINCIPAIS}}
- **Acessórios Fixos:** {{ACESSORIOS_FIXOS}}

### Traje Secundário (Casual / Moderno)
- **Descrição:** {{TRAJE_SECUNDARIO}}

---

## 3. Ativos Visuais Vinculados
- **Folha Mestra de Consistência (Grid 360°):** `folha-consistencia-mestre.png`
- **Rosto Neutro de Referência:** `rosto-master.png`
- **Turnaround Anatômico:** `turnaround-corpo.png`

---

## 4. Prompts de Injeção Automática

### Prompt Positivo para Injetar em Todos os Agentes:
```text
{{POSITIVE_ANCHOR_PROMPT}}
```

### Negative Prompt Obrigatório:
```text
deformed face, asymmetrical eyes, missing fingers, extra fingers, altered hairline, changing age, deformed body proportions, blurry facial features, cartoon, distorted limbs, mutated hands, multiple heads, unrealistic skin texture.
```

---

## 5. Instruções para os Agentes do Studio
Ao produzir imagens para este personagem:
1. Sempre passe `folha-consistencia-mestre.png` no array `ImagePaths`.
2. Inclua o bloco de prompt positivo no início de cada instrução de geração.
3. Não altere o corte de cabelo ou formato da mandíbula entre os slides.
