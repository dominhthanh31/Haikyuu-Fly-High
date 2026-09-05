import os
import re

haikyuu_dir = r'e:\Game\Haikyuu'
sp_dir = r'e:\Game\Haikyuu\Sp'

# Replace [Nhận thức] → [Ý thức] (toàn bộ Haikyuu)
for root, dirs, files in os.walk(haikyuu_dir):
    for fname in files:
        if not fname.endswith('.md'):
            continue
        fpath = os.path.join(root, fname)
        with open(fpath, 'r', encoding='utf-8') as f:
            content = f.read()
        content = content.replace('[Nhận thức]', '[Ý thức]')
        content = content.replace('[Giao bóng]', '[Phát bóng]')
        content = content.replace('[Phát Bóng]', '[Phát bóng]')
        with open(fpath, 'w', encoding='utf-8') as f:
            f.write(content)
        print('Fixed [Nhận thức]:', fname)

# Pattern tô đậm: [stat] ×/+/- số% nếu chưa tô đậm
bold_pattern = re.compile(
    r'(?<!\*\*)'
    r'(\[(?:Đập mạnh|Tốc công|Chuyền bóng|Phát bóng|Đỡ bóng|Cứu bóng|Chắn bóng|Ý thức|Sức mạnh|Kỹ thuật tấn công|Phản xạ|Tinh thần|Kỹ thuật phòng thủ)[^\]]*\]|chỉ số tương ứng)'
    r'(\s*[×+\-]\s*[\d?][%\d?/.]*%?)'
    r'(?!\*\*)'
)

# Tô đậm stat ×/+/- số (chỉ trong Sp)
for fname in os.listdir(sp_dir):
    if not fname.endswith('.md'):
        continue
    fpath = os.path.join(sp_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # Chuẩn hóa: [stat] × **số%** → [stat] × số% (để bold_pattern có thể match)
    content = re.sub(
        r'(\[(?:Đập mạnh|Tốc công|Chuyền bóng|Phát bóng|Đỡ bóng|Cứu bóng|Chắn bóng|Ý thức|Sức mạnh|Kỹ thuật tấn công|Phản xạ|Tinh thần|Kỹ thuật phòng thủ)[^\]]*\]|chỉ số tương ứng)'
        r'(\s*[×+\-]\s*)\*\*([\d?][^*]*)\*\*',
        r'\1\2\3', content
    )

    # Tô đậm [stat] ×/+/- số nếu chưa tô đậm
    content = bold_pattern.sub(r'**\1\2**', content)

    # Tô đậm các từ trạng thái nếu chưa tô đậm
    for word in ['Nice Play', 'BAD', 'Perfect']:
        content = re.sub(r'(?<!\*\*)' + re.escape(word) + r'(?!\*\*)', f'**{word}**', content)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Fixed [Sp]:', fname)

print('Done')
