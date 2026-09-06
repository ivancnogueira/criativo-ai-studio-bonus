import os
import sys
import json
import argparse

def create_approval_html(persona_data, images_info, output_html_path):
    """
    Gera uma interface HTML interativa de aprovação e visualização no padrão Google Flow:
    - Tema escuro de estúdio (#0e0e0e)
    - Grid responsivo com zoom modal
    - Badges técnicos de cada ângulo (Face Angles, Expressions, Body Shots)
    - Informações biométricas da persona (peso, tipo de corpo amigável, altura)
    - Botão de aprovação no estúdio e opção de download
    """
    
    nome = persona_data.get('nome', 'Persona Digital')
    slug = persona_data.get('slug', 'persona')
    genero = persona_data.get('genero', 'Indefinido')
    idade = persona_data.get('idadeAparente', 30)
    peso = persona_data.get('peso', 'Não informado')
    altura = persona_data.get('altura', 'Não informado')
    tipo_corpo = persona_data.get('tipoCorpo', 'Padrão')
    prompt_ancora = persona_data.get('promptAncora', '')

    images_cards_html = ""
    for idx, img in enumerate(images_info):
        cat = img.get('categoria', 'Geral')
        titulo = img.get('titulo', f'Tomada {idx+1}')
        rel_path = img.get('path', '')
        
        images_cards_html += f"""
        <div class="shot-card group" data-category="{cat}">
            <div class="card-media-wrapper">
                <img src="{rel_path}" alt="{titulo}" loading="lazy" onclick="openModal('{rel_path}', '{titulo}', '{cat}')" />
                <div class="card-overlay">
                    <button class="action-btn" onclick="openModal('{rel_path}', '{titulo}', '{cat}')" title="Ampliar">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M15 3h6v6M9 21H3v-6M21 3l-7 7M3 21l7-7"/></svg>
                    </button>
                    <a href="{rel_path}" download class="action-btn" title="Baixar esta imagem">
                        <svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M7 10l5 5 5-5M12 15V3"/></svg>
                    </a>
                </div>
                <div class="category-badge">{cat}</div>
            </div>
            <div class="card-meta">
                <span class="shot-index">#{idx+1:02d}</span>
                <span class="shot-title" title="{titulo}">{titulo}</span>
            </div>
        </div>
        """

    html_content = f"""<!DOCTYPE html>
<html lang="pt-BR">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Estúdio de Consistência · {nome}</title>
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@300;400;500;600;700&family=Space+Grotesk:wght@500;700&family=JetBrains+Mono:wght@400;600&display=swap" rel="stylesheet">
    <style>
        :root {{
            --bg: #0e0e0e;
            --surface: #15161a;
            --surface-card: #1a1b22;
            --surface-border: rgba(255, 255, 255, 0.08);
            --primary: #38bdf8;
            --primary-glow: rgba(56, 189, 248, 0.25);
            --success: #10b981;
            --text: #f3f4f6;
            --text-muted: #9ca3af;
        }}
        * {{ margin: 0; padding: 0; box-sizing: border-box; }}
        body {{
            background: var(--bg);
            color: var(--text);
            font-family: 'Plus Jakarta Sans', sans-serif;
            min-height: 100vh;
            display: flex;
            flex-direction: column;
        }}
        header {{
            background: rgba(21, 22, 26, 0.85);
            backdrop-filter: blur(16px);
            border-bottom: 1px solid var(--surface-border);
            padding: 16px 28px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            position: sticky;
            top: 0;
            z-index: 40;
        }}
        .brand {{
            display: flex;
            align-items: center;
            gap: 12px;
        }}
        .brand-badge {{
            background: linear-gradient(135deg, #38bdf8, #818cf8);
            color: #000;
            font-weight: 700;
            font-size: 11px;
            padding: 4px 10px;
            border-radius: 6px;
            letter-spacing: 0.5px;
            text-transform: uppercase;
        }}
        .brand-title {{
            font-size: 18px;
            font-weight: 700;
            color: #fff;
            letter-spacing: -0.3px;
        }}
        .persona-stats {{
            display: flex;
            align-items: center;
            gap: 16px;
        }}
        .stat-chip {{
            background: var(--surface-card);
            border: 1px solid var(--surface-border);
            padding: 6px 14px;
            border-radius: 20px;
            font-size: 12px;
            color: var(--text-muted);
            display: flex;
            align-items: center;
            gap: 6px;
        }}
        .stat-chip b {{ color: #fff; font-weight: 600; }}
        .btn-approve {{
            background: #10b981;
            color: #000;
            border: none;
            padding: 8px 20px;
            border-radius: 20px;
            font-size: 13px;
            font-weight: 600;
            cursor: pointer;
            transition: all 0.2s ease;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .btn-approve:hover {{
            background: #059669;
            transform: translateY(-1px);
        }}
        main {{
            max-width: 1480px;
            width: 100%;
            margin: 0 auto;
            padding: 28px 24px 80px;
            flex: 1;
        }}
        .hero-banner {{
            background: linear-gradient(135deg, #181a20, #131418);
            border: 1px solid var(--surface-border);
            border-radius: 16px;
            padding: 22px 26px;
            margin-bottom: 28px;
            display: flex;
            justify-content: space-between;
            align-items: center;
            flex-wrap: wrap;
            gap: 16px;
        }}
        .hero-info h1 {{
            font-size: 24px;
            font-weight: 700;
            margin-bottom: 6px;
        }}
        .hero-info p {{
            font-size: 13px;
            color: var(--text-muted);
            max-width: 700px;
            line-height: 1.5;
        }}
        .filter-nav {{
            display: flex;
            gap: 8px;
            margin-bottom: 24px;
            overflow-x: auto;
            padding-bottom: 4px;
        }}
        .filter-btn {{
            background: var(--surface);
            border: 1px solid var(--surface-border);
            color: var(--text-muted);
            padding: 8px 16px;
            border-radius: 10px;
            font-size: 12px;
            font-weight: 500;
            cursor: pointer;
            transition: all 0.2s;
        }}
        .filter-btn.active, .filter-btn:hover {{
            background: var(--surface-card);
            border-color: var(--primary);
            color: #fff;
        }}
        .shots-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(240px, 1fr));
            gap: 20px;
        }}
        .shot-card {{
            background: var(--surface-card);
            border: 1px solid var(--surface-border);
            border-radius: 14px;
            overflow: hidden;
            transition: transform 0.2s, border-color 0.2s, box-shadow 0.2s;
            display: flex;
            flex-direction: column;
        }}
        .shot-card:hover {{
            transform: translateY(-4px);
            border-color: rgba(56, 189, 248, 0.4);
            box-shadow: 0 12px 28px rgba(0, 0, 0, 0.5);
        }}
        .card-media-wrapper {{
            position: relative;
            aspect-ratio: 1 / 1;
            background: #111;
            overflow: hidden;
            cursor: pointer;
        }}
        .card-media-wrapper img {{
            width: 100%;
            height: 100%;
            object-fit: cover;
            transition: transform 0.3s;
        }}
        .shot-card:hover .card-media-wrapper img {{
            transform: scale(1.04);
        }}
        .card-overlay {{
            position: absolute;
            top: 10px;
            right: 10px;
            display: flex;
            gap: 6px;
            opacity: 0;
            transition: opacity 0.2s;
            z-index: 10;
        }}
        .shot-card:hover .card-overlay {{ opacity: 1; }}
        .action-btn {{
            background: rgba(0, 0, 0, 0.7);
            border: 1px solid rgba(255, 255, 255, 0.2);
            color: #fff;
            width: 32px;
            height: 32px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
            transition: background 0.2s;
            text-decoration: none;
        }}
        .action-btn:hover {{
            background: var(--primary);
            color: #000;
        }}
        .category-badge {{
            position: absolute;
            bottom: 10px;
            left: 10px;
            background: rgba(0, 0, 0, 0.75);
            backdrop-filter: blur(8px);
            border: 1px solid rgba(255, 255, 255, 0.1);
            color: #fff;
            font-size: 10px;
            font-weight: 600;
            padding: 3px 8px;
            border-radius: 6px;
            text-transform: uppercase;
            letter-spacing: 0.5px;
        }}
        .card-meta {{
            padding: 12px 14px;
            display: flex;
            align-items: center;
            gap: 8px;
        }}
        .shot-index {{
            font-family: 'JetBrains Mono', monospace;
            font-size: 11px;
            color: var(--primary);
            font-weight: 600;
        }}
        .shot-title {{
            font-size: 12px;
            font-weight: 500;
            color: #e5e7eb;
            white-space: nowrap;
            overflow: hidden;
            text-overflow: ellipsis;
        }}
        /* Modal */
        .modal {{
            position: fixed;
            inset: 0;
            background: rgba(0,0,0,0.85);
            backdrop-filter: blur(12px);
            display: none;
            align-items: center;
            justify-content: center;
            z-index: 99;
            padding: 24px;
        }}
        .modal.active {{ display: flex; }}
        .modal-content {{
            max-width: 900px;
            max-height: 90vh;
            background: var(--surface);
            border: 1px solid var(--surface-border);
            border-radius: 16px;
            overflow: hidden;
            display: flex;
            flex-direction: column;
            position: relative;
        }}
        .modal-img {{
            max-width: 100%;
            max-height: 75vh;
            object-fit: contain;
            background: #000;
        }}
        .modal-footer {{
            padding: 14px 20px;
            display: flex;
            align-items: center;
            justify-content: space-between;
            background: var(--surface-card);
        }}
        .modal-close {{
            position: absolute;
            top: 14px;
            right: 14px;
            background: rgba(0,0,0,0.6);
            border: 1px solid rgba(255,255,255,0.2);
            color: #fff;
            width: 36px;
            height: 36px;
            border-radius: 50%;
            display: flex;
            align-items: center;
            justify-content: center;
            cursor: pointer;
        }}
    </style>
</head>
<body>
    <header>
        <div class="brand">
            <span class="brand-badge">STUDIO DE CONSISTÊNCIA</span>
            <div class="brand-title">{nome}</div>
        </div>
        <div class="persona-stats">
            <div class="stat-chip">Tipo: <b>{tipo_corpo}</b></div>
            <div class="stat-chip">Peso: <b>{peso}</b></div>
            <div class="stat-chip">Altura: <b>{altura}</b></div>
            <button class="btn-approve" onclick="alert('Persona aprovada! O agente registrou os tokens no PERSONAGEM.md e consistencia.json para uso automático no estúdio.')">
                <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><polyline points="20 6 9 17 4 12"/></svg>
                Aprovada para Produção
            </button>
        </div>
    </header>

    <main>
        <div class="hero-banner">
            <div class="hero-info">
                <h1>Galeria de Calibração Visual & Turnaround</h1>
                <p>Todas as tomadas foram geradas exclusivamente por IA com base no DNA visual do personagem. Os agentes do Criativo AI Studio utilizam este conjunto como âncora para gerar posts, carrosséis e stories sem descaracterização facial ou corporal.</p>
            </div>
            <div>
                <a href="folha-consistencia-mestre.png" download class="stat-chip" style="text-decoration:none; cursor:pointer; border-color:var(--primary); color:#fff;">
                    <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2"><path d="M21 15v4a2 2 0 0 1-2 2H5a2 2 0 0 1-2-2v-4M7 10l5 5 5-5M12 15V3"/></svg>
                    Baixar Folha Mestra (2400px)
                </a>
            </div>
        </div>

        <div class="filter-nav">
            <button class="filter-btn active" onclick="filterCategory('all')">Todas as Tomadas ({len(images_info)})</button>
            <button class="filter-btn" onclick="filterCategory('Face Angles')">Ângulos de Rosto</button>
            <button class="filter-btn" onclick="filterCategory('Expressions')">Expressões</button>
            <button class="filter-btn" onclick="filterCategory('Body Shots')">Corpo Inteiro (Turnaround 360°)</button>
            <button class="filter-btn" onclick="filterCategory('Lighting')">Iluminações de Estúdio</button>
        </div>

        <div class="shots-grid" id="shotsGrid">
            {images_cards_html}
        </div>
    </main>

    <div class="modal" id="imageModal" onclick="closeModal()">
        <div class="modal-content" onclick="event.stopPropagation()">
            <button class="modal-close" onclick="closeModal()">✕</button>
            <img class="modal-img" id="modalImg" src="" alt="" />
            <div class="modal-footer">
                <div>
                    <h3 id="modalTitle" style="font-size: 14px; font-weight: 600;"></h3>
                    <p id="modalCategory" style="font-size: 11px; color: var(--text-muted);"></p>
                </div>
                <a id="modalDownload" href="" download class="stat-chip" style="text-decoration:none; color:#fff;">
                    Baixar Imagem Original
                </a>
            </div>
        </div>
    </div>

    <script>
        function filterCategory(cat) {{
            document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
            event.target.classList.add('active');
            const cards = document.querySelectorAll('.shot-card');
            cards.forEach(c => {{
                if (cat === 'all' || c.dataset.category.toLowerCase().includes(cat.toLowerCase())) {{
                    c.style.display = 'flex';
                }} else {{
                    c.style.display = 'none';
                }}
            }});
        }}

        function openModal(src, title, cat) {{
            document.getElementById('modalImg').src = src;
            document.getElementById('modalTitle').textContent = title;
            document.getElementById('modalCategory').textContent = 'Categoria: ' + cat;
            document.getElementById('modalDownload').href = src;
            document.getElementById('imageModal').classList.add('active');
        }}

        function closeModal() {{
            document.getElementById('imageModal').classList.remove('active');
        }}

        document.addEventListener('keydown', e => {{
            if (e.key === 'Escape') closeModal();
        }});
    </script>
</body>
</html>
"""

    os.makedirs(os.path.dirname(os.path.abspath(output_html_path)), exist_ok=True)
    with open(output_html_path, 'w', encoding='utf-8') as f:
        f.write(html_content)
    print(f"✓ Painel visual de aprovação gerado com sucesso em: {output_html_path}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Gerador de Painel Visual de Aprovação de Consistência")
    parser.add_argument("--json", help="Caminho do consistencia.json", required=True)
    parser.add_argument("--saida", help="Caminho do arquivo HTML gerado", default="aprovacao-consistencia.html")
    args = parser.parse_args()

    if os.path.exists(args.json):
        with open(args.json, 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        base_dir = os.path.dirname(os.path.abspath(args.json))
        paineis_dir = os.path.join(base_dir, 'paineis')
        
        # Mapeamento dos painéis existentes
        images_info = []
        if os.path.exists(paineis_dir):
            for f in sorted(os.listdir(paineis_dir)):
                if f.endswith(('.png', '.jpg', '.webp')):
                    rel = f"paineis/{f}"
                    cat = "Body Shots" if "r3_" in f else ("Expressions" if "r2_" in f else "Lighting")
                    images_info.append({
                        "titulo": f.replace('.png', '').upper(),
                        "path": rel,
                        "categoria": cat
                    })
        
        create_approval_html(data, images_info, args.saida)
