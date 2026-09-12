import os

src_file = '/Users/elias/.gemini/antigravity-ide/scratch/matchwork/terminos.html'
dest_file = '/Users/elias/.gemini/antigravity-ide/scratch/matchwork/privacidad.html'
index_file = '/Users/elias/.gemini/antigravity-ide/scratch/matchwork/index.html'

# 1. Create privacidad.html
with open(src_file, 'r') as f:
    privacidad_html = f.read()

# Replace Title and Date
privacidad_html = privacidad_html.replace('Términos y Condiciones de Uso', 'Política de Privacidad de Match Work')
privacidad_html = privacidad_html.replace('10 de Agosto, 2026', '30 de julio, 2026')

with open(dest_file, 'w') as f:
    f.write(privacidad_html)

# 2. Update Footer in all 3 files
footer_target = '''                                        <div class="flex flex-col gap-2">
                                                <a class="w-max text-gray-500 text-sm duration-200 hover:text-vibrant-lime hover:underline"
                                                        href="#">Sobre Nosotros</a>
                                                <a class="w-max text-gray-500 text-sm duration-200 hover:text-vibrant-lime hover:underline"
                                                        href="./terminos.html">Términos y Condiciones de Uso</a>
                                        </div>'''

footer_replacement = '''                                        <div class="flex flex-col gap-2">
                                                <a class="w-max text-gray-500 text-sm duration-200 hover:text-vibrant-lime hover:underline"
                                                        href="#">Sobre Nosotros</a>
                                                <a class="w-max text-gray-500 text-sm duration-200 hover:text-vibrant-lime hover:underline"
                                                        href="./privacidad.html">Política de Privacidad</a>
                                                <a class="w-max text-gray-500 text-sm duration-200 hover:text-vibrant-lime hover:underline"
                                                        href="./terminos.html">Términos y Condiciones de Uso</a>
                                        </div>'''

for filepath in [index_file, src_file, dest_file]:
    with open(filepath, 'r') as f:
        content = f.read()
    
    # We replace the specific footer block
    if footer_target in content:
        content = content.replace(footer_target, footer_replacement)
        with open(filepath, 'w') as f:
            f.write(content)
