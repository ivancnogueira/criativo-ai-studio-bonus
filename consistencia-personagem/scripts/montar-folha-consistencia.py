import os
import sys
import argparse
from PIL import Image, ImageDraw, ImageFont

def create_character_sheet(row1_imgs, row2_imgs, row3_imgs, output_path, title="MASTER CHARACTER CONSISTENCY SHEET"):
    """
    Compila a folha mestra de consistência de personagem no formato:
    Linha 1: 4 imagens (Cenários e Iluminações)
    Linha 2: 4 imagens (Expressões e Poses)
    Linha 3: 5 imagens (Turnaround Anatômico 360° de corpo inteiro)
    """
    TARGET_WIDTH = 2048
    
    # Alturas das linhas
    # Linha 1 e 2 são quadradas (largura da coluna = TARGET_WIDTH / 4 = 512px)
    col_w_r12 = TARGET_WIDTH // 4
    h_row1 = col_w_r12
    h_row2 = col_w_r12
    
    # Linha 3 são 5 painéis verticais de corpo inteiro (largura = TARGET_WIDTH / 5 = ~409px)
    # Proporção típica de corpo inteiro ~ 409 x 680
    col_w_r3 = TARGET_WIDTH // 5
    h_row3 = int(col_w_r3 * 1.66)
    
    TOTAL_HEIGHT = h_row1 + h_row2 + h_row3
    
    sheet = Image.new('RGB', (TARGET_WIDTH, TOTAL_HEIGHT), (240, 240, 245))
    
    # Processar Linha 1 (4 painéis)
    for i in range(4):
        x = i * col_w_r12
        y = 0
        if i < len(row1_imgs) and os.path.exists(row1_imgs[i]):
            im = Image.open(row1_imgs[i]).convert('RGB')
            im_resized = im.resize((col_w_r12, h_row1), Image.Resampling.LANCZOS)
            sheet.paste(im_resized, (x, y))
        else:
            # Placeholder cinza
            ph = Image.new('RGB', (col_w_r12, h_row1), (220, 220, 225))
            sheet.paste(ph, (x, y))
            
    # Processar Linha 2 (4 painéis)
    for i in range(4):
        x = i * col_w_r12
        y = h_row1
        if i < len(row2_imgs) and os.path.exists(row2_imgs[i]):
            im = Image.open(row2_imgs[i]).convert('RGB')
            im_resized = im.resize((col_w_r12, h_row2), Image.Resampling.LANCZOS)
            sheet.paste(im_resized, (x, y))
        else:
            ph = Image.new('RGB', (col_w_r12, h_row2), (210, 210, 218))
            sheet.paste(ph, (x, y))
            
    # Processar Linha 3 (5 painéis de corpo inteiro)
    for i in range(5):
        x = i * col_w_r3
        y = h_row1 + h_row2
        # Para o último painel, ajustar largura restante para fechar exatamente em TARGET_WIDTH
        cur_w = col_w_r3 if i < 4 else (TARGET_WIDTH - x)
        if i < len(row3_imgs) and os.path.exists(row3_imgs[i]):
            im = Image.open(row3_imgs[i]).convert('RGB')
            im_resized = im.resize((cur_w, h_row3), Image.Resampling.LANCZOS)
            sheet.paste(im_resized, (x, y))
        else:
            ph = Image.new('RGB', (cur_w, h_row3), (200, 200, 210))
            sheet.paste(ph, (x, y))
            
    # Salvar resultado final
    os.makedirs(os.path.dirname(output_path), exist_ok=True)
    sheet.save(output_path, 'PNG', quality=95)
    print(f"✓ Folha mestra de consistência gerada em: {output_path}")

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Compilador da Folha Mestra de Consistência de Personagem")
    parser.add_argument("--pasta", help="Pasta com as imagens numeradas (r1_1..4, r2_1..4, r3_1..5)", required=True)
    parser.add_argument("--saida", help="Caminho do arquivo PNG final", default="folha-consistencia-mestre.png")
    args = parser.parse_args()
    
    p = args.pasta
    row1 = [os.path.join(p, f"r1_{i}.png") for i in range(1, 5)]
    row2 = [os.path.join(p, f"r2_{i}.png") for i in range(1, 5)]
    row3 = [os.path.join(p, f"r3_{i}.png") for i in range(1, 6)]
    
    create_character_sheet(row1, row2, row3, args.saida)
