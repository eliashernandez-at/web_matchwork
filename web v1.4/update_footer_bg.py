import os

files = [
    '/Users/elias/.gemini/antigravity-ide/scratch/matchwork/index.html',
    '/Users/elias/.gemini/antigravity-ide/scratch/matchwork/terminos.html',
    '/Users/elias/.gemini/antigravity-ide/scratch/matchwork/privacidad.html'
]

target = '<footer class="relative bg-off-white text-dark-slate pt-16">'
replacement = '<footer class="relative bg-[#F5ECD5] text-dark-slate pt-16">'

for filepath in files:
    with open(filepath, 'r') as f:
        content = f.read()

    if target in content:
        content = content.replace(target, replacement)
        with open(filepath, 'w') as f:
            f.write(content)
