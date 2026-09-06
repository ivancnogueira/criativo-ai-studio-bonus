import os
import sys
import argparse
from PIL import Image, ImageDraw, ImageFont

def get_font(size, bold=False):
    """Tenta carregar fontes elegantes do sistema Windows ou fallback para padrão."""
    font_paths = [
        r"C:\Windows\Fonts\segoeuib.ttf" if bold else r"C:\Windows\Fonts\segoeui.ttf",
        r"C:\Windows\Fonts\arialbd.ttf" if bold else r"C:\Windows\Fonts\arial.ttf",
        r"C:\Windows\Fonts\calibrib.ttf" if bold else r"C:\Windows\Fonts\calibri.ttf",
    ]
    for p in font_paths:
        if os.path.exists(p):
            try:
                return ImageFont.truetype(p, size)
            except Exception:
                pass
    return ImageFont.load_default()

def draw_badge(draw, text, x, y, font, bg_color=(20, 22, 28, 220), text_color=(240, 240, 245)):
    """Desenha um badge com fundo semitransparente ou sólido escuro para rotulagem técnica."""
    bbox = draw.textbbox((x, y), text, font=font)
    padding = 6
    rect = (bbox[0] - padding, bbox[1] - padding, bbox[2] + padding, bbox[3] + padding)
    draw.rectangle(rect, fill=bg_color)
    draw.text((x, y), text, font=font, fill=text_color)

def create_character_sheet(
    row1_imgs, 
    row2_imgs, 
    row3_imgs, 
    output_path, 
    character_name="PERSONA DIGITAL", 
    biometrics="ALTURA: 1.80m | PESO: 80kg | MESOMORFO"
):
    """
    Compila a folha mestra de consistência visual em alta definição (2400px):
    - Cabeçalho executivo de calibração
    - Linha 1: 4 imagens quadradas (Cenários e Iluminações)
    - Linha 2: 4 imagens quadradas (Expressões, Look Casual e Perfil 90°)
    - Linha 3: 5 imagens verticais de corpo inteiro (Turnaround Anatômico 360°)
    """
    TARGET_WIDTH = 2400
    MARGIN = 24
    GAP = 12
    HEADER_HEIGHT = 160
    SECTION_HEADER_HEIGHT = 44

    # Largura útil interna
    usable_w = TARGET_WIDTH - (2 * MARGIN)

    # Dimensões da Linha 1 e 2 (4 colunas quadradas)
    col_w_4 = (usable_w - (3 * GAP)) // 4
    h_row1 = col_w_4
    h_row2 = col_w_4

    # Dimensões da Linha 3 (5 colunas verticais)
    col_w_5 = (usable_w - (4 * GAP)) // 5
    h_row3 = int(col_w_5 * 1.68) # Proporção anatômica 9:15+

    TOTAL_HEIGHT = (
        HEADER_HEIGHT +
        SECTION_HEADER_HEIGHT + h_row1 + GAP +
        SECTION_HEADER_HEIGHT + h_row2 + GAP +
        SECTION_HEADER_HEIGHT + h_row3 + MARGIN
    )

    # Canvas principal em tom Studio Dark Grafite
    BG_COLOR = (14, 16, 20)
    sheet = Image.new('RGB', (TARGET_WIDTH, TOTAL_HEIGHT), BG_COLOR)
    draw = ImageDraw.Draw(sheet)

    # Fontes
    font_title = get_font(36, bold=True)
    font_sub = get_font(20, bold=False)
    font_sec = get_font(18, bold=True)
    font_badge = get_font(14, bold=True)

    # 1. Renderizar Cabeçalho Executivo
    draw.rectangle([(MARGIN, MARGIN), (TARGET_WIDTH - MARGIN, HEADER_HEIGHT - 10)], fill=(22, 25, 33))
    # Borda decorativa sutil
    draw.rectangle([(MARGIN, MARGIN), (TARGET_WIDTH - MARGIN, HEADER_HEIGHT - 10)], outline=(40, 45, 60), width=2)
    
    # Tag no canto
    draw.rectangle([(MARGIN + 20, MARGIN + 20), (MARGIN + 250, MARGIN + 48)], fill=(56, 189, 248))
    draw.text((MARGIN + 30, MARGIN + 24), "CONSISTÊNCIA MASTER 360°", font=font_badge, fill=(10, 15, 25))

    # Título Principal
    draw.text((MARGIN + 20, MARGIN + 60), f"DNA VISUAL & ANATOMIA: {character_name.upper()}", font=font_title, fill=(255, 255, 255))
    draw.text((MARGIN + 20, MARGIN + 110), f"CALIBRAÇÃO BIOMÉTRICA: {biometrics.upper()}", font=font_sub, fill=(160, 170, 190))

    # Labels técnicos para os 13 painéis
    labels_r1 = [
        "01 · ESTÚDIO NEUTRO (FACE MASTER)",
        "02 · EXTERNA / LUZ NATURAL",
        "03 · GOLDEN HOUR (ADEREÇO)",
        "04 · NOTURNO / CHIAROSCURO"
    ]

    labels_r2 = [
        "05 · LOOK CASUAL SECUNDÁRIO",
        "06 · EXPRESSÃO VIVA / SORRISO",
        "07 · PERFIL RÍGIDO 90°",
        "08 · AUTORIDADE EXECUTIVA"
    ]

    labels_r3 = [
        "09 · 0° FRONTAL COMPLETO",
        "10 · 45° TRÊS-QUARTOS",
        "11 · 90° PERFIL LATERAL",
        "12 · 135° TRÊS-QUARTOS COSTAS",
        "13 · 180° COSTAS COMPLETAS (DORSAL)"
    ]

    current_y = HEADER_HEIGHT + 10

    # Função auxiliar para desenhar título de seção
    def draw_section_bar(title, y_pos):
        draw.text((MARGIN + 4, y_pos + 10), title, font=font_sec, fill=(140, 190, 255))
        draw.line([(MARGIN + 4, y_pos + 36), (TARGET_WIDTH - MARGIN, y_pos + 36)], fill=(32, 36, 48), width=2)
        return y_pos + SECTION_HEADER_HEIGHT

    # --- LINHA 1 ---
    current_y = draw_section_bar("LINHA 01: CALIBRAÇÃO DE ILUMINAÇÃO & AMBIENTES (1:1)", current_y)
    for i in range(4):
        x = MARGIN + i * (col_w_4 + GAP)
        panel_box = [(x, current_y), (x + col_w_4, current_y + h_row1)]
        if i < len(row1_imgs) and os.path.exists(row1_imgs[i]):
            im = Image.open(row1_imgs[i]).convert('RGB')
            im_resized = im.resize((col_w_4, h_row1), Image.Resampling.LANCZOS)
            sheet.paste(im_resized, (x, current_y))
        else:
            sheet.paste(Image.new('RGB', (col_w_4, h_row1), (26, 29, 38)), (x, current_y))
            draw.text((x + 20, current_y + h_row1 // 2 - 10), "[PAINEL EM ESPERA]", font=font_badge, fill=(100, 110, 130))

        # Moldura e Badge
        draw.rectangle(panel_box, outline=(40, 46, 60), width=2)
        draw_badge(draw, labels_r1[i], x + 12, current_y + 16, font_badge)

    current_y += h_row1 + GAP + 10

    # --- LINHA 2 ---
    current_y = draw_section_bar("LINHA 02: EXPRESSÕES, LOOK SECUNDÁRIO & PERFIL 90° (1:1)", current_y)
    for i in range(4):
        x = MARGIN + i * (col_w_4 + GAP)
        panel_box = [(x, current_y), (x + col_w_4, current_y + h_row2)]
        if i < len(row2_imgs) and os.path.exists(row2_imgs[i]):
            im = Image.open(row2_imgs[i]).convert('RGB')
            im_resized = im.resize((col_w_4, h_row2), Image.Resampling.LANCZOS)
            sheet.paste(im_resized, (x, current_y))
        else:
            sheet.paste(Image.new('RGB', (col_w_4, h_row2), (26, 29, 38)), (x, current_y))
            draw.text((x + 20, current_y + h_row2 // 2 - 10), "[PAINEL EM ESPERA]", font=font_badge, fill=(100, 110, 130))

        draw.rectangle(panel_box, outline=(40, 46, 60), width=2)
        draw_badge(draw, labels_r2[i], x + 12, current_y + 16, font_badge)

    current_y += h_row2 + GAP + 10

    # --- LINHA 3 ---
    current_y = draw_section_bar("LINHA 03: TURNAROUND ANATÔMICO 360° EM CORPO INTEIRO (ALINHADO CABEÇA AOS PÉS)", current_y)
    for i in range(5):
        x = MARGIN + i * (col_w_5 + GAP)
        # Ajusta largura do último painel se necessário
        cur_w = col_w_5 if i < 4 else (usable_w - (4 * (col_w_5 + GAP)))
        panel_box = [(x, current_y), (x + cur_w, current_y + h_row3)]

        if i < len(row3_imgs) and os.path.exists(row3_imgs[i]):
            im = Image.open(row3_imgs[i]).convert('RGB')
            im_resized = im.resize((cur_w, h_row3), Image.Resampling.LANCZOS)
            sheet.paste(im_resized, (x, current_y))
        else:
            sheet.paste(Image.new('RGB', (cur_w, h_row3), (26, 29, 38)), (x, current_y))
            draw.text((x + 15, current_y + h_row3 // 2 - 10), "[PAINEL EM ESPERA]", font=font_badge, fill=(100, 110, 130))

        draw.rectangle(panel_box, outline=(40, 46, 60), width=2)
        draw_badge(draw, labels_r3[i], x + 10, current_y + 16, font_badge)

    # Salvar resultado final
    os.makedirs(os.path.dirname(os.path.abspath(output_path)), exist_ok=True)
    sheet.save(output_path, 'PNG', quality=95)
    print(f"✓ Folha Mestra de Consistência Premium gerada com sucesso em: {output_path}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Compilador da Folha Mestra de Consistência de Personagem Premium")
    parser.add_argument("--pasta", help="Pasta com as imagens (r1_1..4, r2_1..4, r3_1..5)", required=True)
    parser.add_argument("--saida", help="Caminho do arquivo PNG final", default="folha-consistencia-mestre.png")
    parser.add_argument("--nome", help="Nome da Persona", default="PERSONA DIGITAL")
    parser.add_argument("--biotipo", help="Resumo biométrico", default="ALTURA: 1.80m | PESO: 80kg | MESOMORFO")
    args = parser.parse_args()

    p = args.pasta
    row1 = [os.path.join(p, f"r1_{i}.png") for i in range(1, 5)]
    row2 = [os.path.join(p, f"r2_{i}.png") for i in range(1, 5)]
    row3 = [os.path.join(p, f"r3_{i}.png") for i in range(1, 6)]

    create_character_sheet(row1, row2, row3, args.saida, args.nome, args.biotipo)
