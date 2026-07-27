import re
import os

sp_dir = r'e:\Game\Haikyuu\Sp'

for fname in os.listdir(sp_dir):
    if not fname.endswith('.md'):
        continue
    fpath = os.path.join(sp_dir, fname)
    with open(fpath, 'r', encoding='utf-8') as f:
        content = f.read()

    # 1. Convert markdown image syntax (old path) → <img> with ../
    content = re.sub(
        r'!\[([^\]]+)\]\(Ảnh/Tiềm%20năng/([^)]+)\)',
        r'<img src="../Ảnh/Tiềm%20năng/\2" alt="\1" width="75">',
        content
    )

    # 2. Fix any <img> that still uses old path without ../
    content = re.sub(
        r'<img src="Ảnh/Tiềm%20năng/',
        '<img src="../Ảnh/Tiềm%20năng/',
        content
    )

    # 3. Ensure blank line BEFORE <img> tag
    content = re.sub(r'([^\n])\n(<img )', r'\1\n\n\2', content)

    # 4. Ensure blank line AFTER <img> tag (before next content)
    content = re.sub(r'(width="\d+">)\n([^\n])', r'\1\n\n\2', content)

    with open(fpath, 'w', encoding='utf-8') as f:
        f.write(content)
    print('Fixed:', fname)

print('Done')
