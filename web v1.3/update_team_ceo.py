import os

filepath = '/Users/elias/.gemini/antigravity-ide/scratch/matchwork/index.html'

with open(filepath, 'r') as f:
    content = f.read()

target = '''                                                <p
                                                        class="text-vibrant-lime bg-dark-slate rounded-full px-3 py-1 inline-block font-semibold uppercase tracking-wider text-sm mt-1">
                                                        CEO MatchWork</p>'''

replacement = '''                                                <p
                                                        class="inline-flex items-center rounded-full border border-vibrant-lime text-dark-slate px-3 py-1 text-xs font-semibold bg-vibrant-lime/10 uppercase mt-1">
                                                        CEO MATCHWORK</p>'''

content = content.replace(target, replacement)

with open(filepath, 'w') as f:
    f.write(content)
