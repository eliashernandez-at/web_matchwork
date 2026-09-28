import os

files = ['/Users/elias/.gemini/antigravity-ide/scratch/matchwork/terminos.html', '/Users/elias/.gemini/antigravity-ide/scratch/matchwork/privacidad.html']

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()

    # Logo Link
    content = content.replace('<a class="flex items-center gap-2 relative" href="#">', '<a class="flex items-center gap-2 relative" href="./index.html">')
    
    # Menu Links
    content = content.replace('href="#hero-section"', 'href="./index.html#hero-section"')
    content = content.replace('href="#solucion-section"', 'href="./index.html#solucion-section"')
    content = content.replace('href="#team-section"', 'href="./index.html#team-section"')
    content = content.replace('href="#preguntas-section"', 'href="./index.html#preguntas-section"')
    content = content.replace('href="#contacto-section"', 'href="./index.html#contacto-section"')
    
    with open(filepath, 'w') as f:
        f.write(content)
