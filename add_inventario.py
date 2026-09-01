with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

new_nav_item = '''                <div class="relative group h-full">
                    <a href="#inventario" class="hover:text-blue-600 transition-colors block py-2">3. Inventario de Activos</a>
                </div>
'''

new_section = '''    <!-- 3. Inventario de Activos -->
    <section id="inventario" class="mt-10 py-16 bg-gray-50">
        <div class="container mx-auto px-4">
            <h2 class="text-3xl font-bold text-center mb-12 text-[#1a3e6a]">
                <i class="fas fa-boxes mr-3"></i>3. Inventario de Activos
            </h2>
            <div class="bg-white rounded-2xl shadow-xl p-8 border-l-8 border-[#1a3e6a] mb-12">
                <h3 class="text-2xl font-bold text-[#1a3e6a] mb-4">Documento de Inventario de Activos</h3>
                <div class="mb-6 flex flex-col items-center justify-center p-10 bg-gray-100 rounded-lg border-2 border-dashed border-gray-300">
                    <i class="fas fa-file-word text-6xl text-blue-600 mb-4"></i>
                    <p class="mb-6 text-gray-700 text-center max-w-lg">El inventario de activos se encuentra en un documento de Microsoft Word. Haga clic en el botón de abajo para descargarlo y visualizarlo.</p>
                    <a href="assets/docs/inventario de activos.docx" target="_blank" class="inline-block bg-[#1a3e6a] hover:bg-[#d31a1d] text-white font-bold py-3 px-8 rounded-lg shadow-lg transition-all transform hover:scale-105">
                        <i class="fas fa-download mr-2"></i>Descargar Inventario de Activos (DOCX)
                    </a>
                </div>
            </div>
        </div>
    </section>
'''

nav_2_end = 0
for i in range(len(lines)):
    if '2. Análisis Planeamiento' in lines[i]:
        for j in range(i, len(lines)):
            if '</div>' in lines[j] and '</div>' in lines[j+1] and '</nav>' in lines[j+2]:
                nav_2_end = j
                break
        break

if nav_2_end > 0:
    lines.insert(nav_2_end + 1, new_nav_item)

footer_start = 0
for i in range(len(lines)):
    if '<footer' in lines[i]:
        footer_start = i
        break

if footer_start > 0:
    lines.insert(footer_start, new_section)

with open('index.html', 'w', encoding='utf-8') as f:
    f.writelines(lines)
print('Added successfully')

