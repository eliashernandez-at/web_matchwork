import os

files = [
    '/Users/elias/.gemini/antigravity-ide/scratch/matchwork/index.html',
    '/Users/elias/.gemini/antigravity-ide/scratch/matchwork/terminos.html',
    '/Users/elias/.gemini/antigravity-ide/scratch/matchwork/privacidad.html'
]

new_footer = """        <!-- FOOTER -->
        <footer class="flex flex-col md:flex-row gap-6 items-center justify-around w-full py-8 text-sm bg-dark-slate text-off-white border-t border-gray-800">
                <div class="flex flex-col md:flex-row items-center gap-4">
                        <p>© <span id="currentYear">2026</span> Match Work. Todos los derechos reservados.</p>
                        <div class="flex items-center gap-4 text-vibrant-lime">
                                <!-- Facebook -->
                                <a class="hover:opacity-80 transition-opacity duration-200" target="_blank" href="#">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                                <path d="M18 2h-3a5 5 0 0 0-5 5v3H7v4h3v8h4v-8h3l1-4h-4V7a1 1 0 0 1 1-1h3z" />
                                        </svg>
                                </a>
                                <!-- Instagram -->
                                <a class="hover:opacity-80 transition-opacity duration-200" target="_blank" href="#">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                                <rect width="20" height="20" x="2" y="2" rx="5" ry="5" />
                                                <path d="M16 11.37A4 4 0 1 1 12.63 8 4 4 0 0 1 16 11.37z" />
                                                <line x1="17.5" x2="17.51" y1="6.5" y2="6.5" />
                                        </svg>
                                </a>
                                <!-- LinkedIn -->
                                <a class="hover:opacity-80 transition-opacity duration-200" target="_blank" href="#">
                                        <svg xmlns="http://www.w3.org/2000/svg" width="20" height="20" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round">
                                                <path d="M16 8a6 6 0 0 1 6 6v7h-4v-7a2 2 0 0 0-2-2 2 2 0 0 0-2 2v7h-4v-7a6 6 0 0 1 6-6z" />
                                                <rect width="4" height="12" x="2" y="9" />
                                                <circle cx="4" cy="4" r="2" />
                                        </svg>
                                </a>
                        </div>
                </div>
                <div class="flex items-center gap-4">
                        <a href="./privacidad.html" class="hover:text-vibrant-lime transition-colors">Política de Privacidad</a>
                        <div class="h-4 w-px bg-off-white/20"></div>
                        <a href="./terminos.html" class="hover:text-vibrant-lime transition-colors">Términos y Condiciones de Uso</a>
                </div>
        </footer>"""

for filepath in files:
    with open(filepath, 'r') as f:
        lines = f.readlines()
    
    start_idx = -1
    end_idx = -1
    
    for i, line in enumerate(lines):
        if '<footer' in line and start_idx == -1:
            start_idx = i
        if '</footer>' in line:
            end_idx = i
            
    if start_idx != -1 and end_idx != -1:
        lines[start_idx:end_idx+1] = [new_footer + '\n']
        with open(filepath, 'w') as f:
            f.writelines(lines)
