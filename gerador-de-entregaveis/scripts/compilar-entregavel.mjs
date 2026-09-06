import fs from 'fs';
import path from 'path';

/**
 * compilar-entregavel.mjs
 * Script utilitário do Gerador de Entregáveis.
 * Uso: node compilar-entregavel.mjs --origem <caminho_da_pasta_do_conteudo>
 */

function parseArgs() {
  const args = process.argv.slice(2);
  let origem = '';
  for (let i = 0; i < args.length; i++) {
    if (args[i] === '--origem' && args[i + 1]) {
      origem = args[i + 1];
    }
  }
  return { origem };
}

async function run() {
  const { origem } = parseArgs();
  if (!origem) {
    console.error('❌ Erro: informe a pasta de origem usando --origem <caminho>');
    process.exit(1);
  }

  const absOrigem = path.resolve(origem);
  if (!fs.existsSync(absOrigem)) {
    console.error(`❌ Pasta não encontrada: ${absOrigem}`);
    process.exit(1);
  }

  console.log(`📦 Processando entregáveis para: ${absOrigem}`);

  // Tentar carregar metadados (briefing.json ou publicacao.json)
  let briefing = {};
  let publicacao = {};

  const briefingPath = path.join(absOrigem, 'briefing.json');
  if (fs.existsSync(briefingPath)) {
    try { briefing = JSON.parse(fs.readFileSync(briefingPath, 'utf8')); } catch (e) {}
  }

  const publicacaoPath = path.join(absOrigem, 'publicacao.json');
  if (fs.existsSync(publicacaoPath)) {
    try { publicacao = JSON.parse(fs.readFileSync(publicacaoPath, 'utf8')); } catch (e) {}
  }

  // Buscar imagens de slides
  const files = fs.readdirSync(absOrigem);
  const slideImages = files
    .filter(f => /slide-\d+\.(png|webp|jpg)$/i.test(f) || /Camada \d+\.(png|webp|jpg)$/i.test(f) || /^\d+\.(png|webp|jpg)$/i.test(f))
    .sort((a, b) => a.localeCompare(b, undefined, { numeric: true, sensitivity: 'base' }));

  const titulo = briefing.titulo || publicacao.titulo || path.basename(absOrigem).replace(/-/g, ' ').toUpperCase();
  const legenda = briefing.legenda || publicacao.legenda || 'Confira este conteúdo completo produzido com o Criativo AI Studio.';
  const hashtags = briefing.hashtags || publicacao.hashtags || '#criativoaistudio #marketingdigital #inteligenciaartificial';
  const nomeMarca = briefing.marca || publicacao.marca || 'Criativo AI Studio';
  const dataCriacao = new Date().toLocaleDateString('pt-BR');

  // Criar pasta de saída entregavel/
  const outDir = path.join(absOrigem, 'entregavel');
  if (!fs.existsSync(outDir)) {
    fs.mkdirSync(outDir, { recursive: true });
  }

  // 1. Gerar Planilha Editorial CSV (com BOM UTF-8 para Excel)
  const csvContent = '\uFEFF' + [
    'ID,Data Sugerida,Horário Ideal,Formato,Pilar Editorial,Tema / Título,Gancho,Legenda Completa,CTA,Hashtags,Status',
    `1,"${dataCriacao}","18:30","Carrossel","Autoridade & Conversão","${titulo}","${titulo}","${legenda.replace(/"/g, '""')}","Arraste para o lado e salve","${hashtags}","Aguardando Aprovação"`
  ].join('\n');

  const csvFile = path.join(outDir, 'calendario-editorial.csv');
  fs.writeFileSync(csvFile, csvContent, 'utf8');
  console.log(`✓ Planilha gerada: ${csvFile}`);

  // 2. Gerar Showcase HTML de Aprovação
  const templateShowcasePath = path.resolve(path.dirname(import.meta.url.replace('file:///', '')), '../templates/showcase-aprovacao-template.html');
  let showcaseTemplate = '';
  if (fs.existsSync(templateShowcasePath)) {
    showcaseTemplate = fs.readFileSync(templateShowcasePath, 'utf8');
  }

  if (showcaseTemplate) {
    const slideElements = slideImages.map((s, idx) => {
      const imgPath = path.relative(outDir, path.join(absOrigem, s)).replace(/\\/g, '/');
      return `<img src="${imgPath}" alt="Slide ${idx + 1}" class="slide-img ${idx === 0 ? 'active' : ''}">`;
    }).join('\n        ');

    let htmlShowcase = showcaseTemplate
      .replace(/\{\{TITULO_CONTEUDO\}\}/g, titulo)
      .replace(/\{\{DESCRICAO_BREVE\}\}/g, `Carrossel estratégico diagramado em ${slideImages.length || 1} slides para máxima retenção.`)
      .replace(/\{\{NOME_MARCA\}\}/g, nomeMarca)
      .replace(/\{\{QTD_SLIDES\}\}/g, slideImages.length.toString())
      .replace(/\{\{DATA_CRIACAO\}\}/g, dataCriacao)
      .replace(/\{\{FORMATO_PECA\}\}/g, 'Carrossel Instagram (1080x1350)')
      .replace(/\{\{LEGENDA_COMPLETA\}\}/g, legenda)
      .replace(/\{\{HASHTAGS\}\}/g, hashtags)
      .replace('{{ELEMENTOS_SLIDES_IMG}}', slideElements);

    const showcaseFile = path.join(outDir, 'showcase-aprovacao.html');
    fs.writeFileSync(showcaseFile, htmlShowcase, 'utf8');
    console.log(`✓ Showcase Web gerado: ${showcaseFile}`);
  }

  // 3. Gerar Apresentação / Deck PDF HTML
  const templateDeckPath = path.resolve(path.dirname(import.meta.url.replace('file:///', '')), '../templates/deck-aprovacao-template.html');
  let deckTemplate = '';
  if (fs.existsSync(templateDeckPath)) {
    deckTemplate = fs.readFileSync(templateDeckPath, 'utf8');
  }

  if (deckTemplate) {
    // Dividir slides em páginas de 3 slides
    const slidesPerPage = 3;
    const slidePages = [];
    for (let i = 0; i < slideImages.length; i += slidesPerPage) {
      const chunk = slideImages.slice(i, i + slidesPerPage);
      const cardsHtml = chunk.map((s, idx) => {
        const slideIndex = i + idx + 1;
        const imgPath = path.relative(outDir, path.join(absOrigem, s)).replace(/\\/g, '/');
        const role = slideIndex === 1 ? 'Capa & Gancho' : (slideIndex === slideImages.length ? 'CTA & Fechamento' : 'Desenvolvimento');
        return `
        <div class="slide-card">
          <div class="slide-preview-wrapper">
            <span class="slide-number-badge">SLIDE ${slideIndex}</span>
            <img src="${imgPath}" alt="Slide ${slideIndex}" class="slide-preview-img">
          </div>
          <div class="slide-info">
            <span class="slide-role">${role}</span>
            <span class="slide-desc">Slide estratégico #${slideIndex} focado na narrativa.</span>
          </div>
        </div>`;
      }).join('\n');

      slidePages.push(`
      <section class="page">
        <div class="page-header">
          <div class="brand-area">
            <span class="brand-title">${nomeMarca}</span>
          </div>
          <div class="header-badge">SLIDES ${i + 1} A ${Math.min(i + slidesPerPage, slideImages.length)}</div>
        </div>

        <div class="slides-grid">
          ${cardsHtml}
        </div>

        <div class="page-footer">
          <span>${titulo} • Exibição Visual</span>
          <span>Página ${slidePages.length + 2}</span>
        </div>
      </section>`);
    }

    const totalPaginas = 1 + slidePages.length + 2; // Capa + Slides + Legenda + Aprovação
    let htmlDeck = deckTemplate
      .replace(/\{\{TITULO_PROJETO\}\}/g, titulo)
      .replace(/\{\{TITULO_CONTEUDO\}\}/g, titulo)
      .replace(/\{\{DESCRICAO_BREVE\}\}/g, `Dossiê visual de aprovação para postagem oficial no Instagram.`)
      .replace(/\{\{NOME_MARCA\}\}/g, nomeMarca)
      .replace(/\{\{LOGO_URL\}\}/g, '')
      .replace(/\{\{FORMATO_PECA\}\}/g, 'Carrossel Instagram')
      .replace(/\{\{QTD_SLIDES\}\}/g, slideImages.length.toString())
      .replace(/\{\{DATA_CRIACAO\}\}/g, dataCriacao)
      .replace(/\{\{TOTAL_PAGINAS\}\}/g, totalPaginas.toString())
      .replace(/\{\{BLOCOS_PAGINAS_SLIDES\}\}/g, slidePages.join('\n'))
      .replace(/\{\{LEGENDA_COMPLETA\}\}/g, legenda)
      .replace(/\{\{OBJETIVO_ESTRATEGICO\}\}/g, 'Parar o scroll, reter a atenção por mais de 45 segundos e direcionar para o CTA.')
      .replace(/\{\{CTA_DETALHADO\}\}/g, 'Comente a palavra-chave ou envie mensagem no Direct para receber o link exclusivo.')
      .replace(/\{\{HASHTAGS\}\}/g, hashtags)
      .replace(/\{\{NUM_PAG_LEGENDA\}\}/g, (totalPaginas - 1).toString());

    const deckFile = path.join(outDir, 'deck-aprovacao.html');
    fs.writeFileSync(deckFile, htmlDeck, 'utf8');
    console.log(`✓ Deck de Apresentação (Pronto para PDF) gerado: ${deckFile}`);
  }

  console.log('\n🎉 Todos os entregáveis foram gerados com sucesso na pasta:');
  console.log(`📁 ${outDir}\n`);
}

run().catch(console.error);
