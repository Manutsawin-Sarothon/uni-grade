from pathlib import Path
from zipfile import ZipFile, ZIP_DEFLATED

base = Path(__file__).resolve().parent.parent
repo = base / 'uni-grade'
out = base / 'outputs' / 'uni-grade-redesign.zip'
files = [
    'index.html', 'redesign.css', 'manifest.webmanifest',
    'app-icon.svg', 'app-icon-maskable.svg',
    'favicon-32.png', 'apple-touch-icon.png', 'icon-192.png',
    'icon-512.png', 'icon-maskable-512.png',
    'README.md', 'PRODUCT.md', 'DESIGN.md',
    '.impeccable/design.json', '.impeccable/surfaces/index-html.md',
]
with ZipFile(out, 'w', ZIP_DEFLATED) as archive:
    for name in files:
        archive.write(repo / name, arcname=f'uni-grade/{name}')
print(out)
with ZipFile(out) as archive:
    print('entries:', len(archive.namelist()), 'integrity:', archive.testzip())
