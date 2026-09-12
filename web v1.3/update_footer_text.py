import os

files = [
    '/Users/elias/.gemini/antigravity-ide/scratch/matchwork/index.html',
    '/Users/elias/.gemini/antigravity-ide/scratch/matchwork/terminos.html',
    '/Users/elias/.gemini/antigravity-ide/scratch/matchwork/privacidad.html'
]

target = '<p>© <span id="currentYear">2026</span> Match Work. Todos los derechos reservados.</p>'
replacement = '<p>© <span id="currentYear">2026</span> <span class="font-bold">Match<span class="text-vibrant-lime">Work</span></span>. Todos los derechos reservados.</p>'

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()

    if target in content:
        content = content.replace(target, replacement)
        with open(filepath, 'w') as f:
            f.write(content)
