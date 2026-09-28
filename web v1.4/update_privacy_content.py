import os

filepath = '/Users/elias/.gemini/antigravity-ide/scratch/matchwork/privacidad.html'
with open(filepath, 'r') as f:
    lines = f.readlines()

start_idx = -1
end_idx = -1
for i, line in enumerate(lines):
    if '<main>' in line and start_idx == -1:
        start_idx = i
    if '</main>' in line:
        end_idx = i

if start_idx != -1 and end_idx != -1:
    new_main = """        <main>
                <!-- Hero-like Header for Navigation to work -->
                <section class="relative pt-32 pb-16 px-margin-mobile md:px-margin-desktop bg-dark-slate text-off-white" id="hero-section">
                        <div class="max-w-4xl mx-auto text-center">
                                <h1 class="text-4xl md:text-5xl font-bold mb-6 text-vibrant-lime">Política de Privacidad de Match Work</h1>
                                <p class="text-lg opacity-80">Última actualización: 30 de julio, 2026</p>
                        </div>
                </section>

                <!-- Privacy Policy Content -->
                <section class="py-16 md:py-24 px-margin-mobile md:px-margin-desktop bg-off-white text-dark-slate">
                        <div class="max-w-4xl mx-auto space-y-8 font-body-md">
                                <div>
                                        <p class="text-gray-600 leading-relaxed mb-4">Propiedad de: MatchWork SpA (RUT: 78.428.877-3)> <strong>Compromiso de Privacidad</strong> <strong>Match Work</strong> opera bajo el principio estricto de minimización de datos en su fase comunitaria. Para proteger la seguridad e integridad física de los Prestadores, la plataforma <strong>nunca exhibirá coordenadas geográficas exactas ni direcciones domiciliarias en el mapa público</strong>, sustituyéndolas por radios aproximados de visualización.</p>
                                </div>
                                
                                <div>
                                        <h2 class="text-2xl font-bold mb-4 text-dark-slate">1. Marco Normativo y Responsable del Tratamiento</h2>
                                        <p class="text-gray-600 leading-relaxed">La presente Política de Privacidad regula el tratamiento de datos personales recopilados a través de la aplicación móvil y la plataforma web de Match Work. Este instrumento ha sido diseñado en cumplimiento de la Ley de Protección de Datos Personales local y los estándares del Reglamento General de Protección de Datos (RGPD). El responsable legal del resguardo y almacenamiento de sus datos es MatchWork SpA.</p>
                                </div>
                                
                                <div>
                                        <h2 class="text-2xl font-bold mb-4 text-dark-slate">2. Datos Recopilados y Principio de Minimización</h2>
                                        <p class="text-gray-600 leading-relaxed mb-2">En conformidad con el principio de minimización de datos, durante esta fase de lanzamiento y prueba gratuita, Match Work solo recopila la información estrictamente necesaria para el funcionamiento del directorio comunitario:</p>
                                        <ul class="list-disc pl-6 text-gray-600 space-y-2">
                                                <li><strong>Información de Identidad Básica:</strong> Nombre completo proporcionado de forma voluntaria por el usuario durante el registro (no se solicita RUT en esta etapa).</li>
                                                <li><strong>Datos de Contacto y Acceso:</strong> Dirección de correo electrónico activa bajo verificación y contraseña encriptada. (recomendación activar validación por OTP código verificación / account confirmation/ magic link o simil)</li>
                                                <li><strong>Datos de Navegación Operativa:</strong> Rol seleccionado dentro de la plataforma (Cliente o Prestador) e historial de mensajes dentro del chat interno.</li>
                                                <li><strong>Datos de Localización (Geolocalización):</strong> Coordenadas geográficas capturadas mediante el sistema GPS del dispositivo móvil o navegador web.</li>
                                        </ul>
                                </div>

                                <div>
                                        <h2 class="text-2xl font-bold mb-4 text-dark-slate">3. Principio de Finalidad del Tratamiento</h2>
                                        <p class="text-gray-600 leading-relaxed mb-2">Los datos recolectados se tratarán única y exclusivamente para los fines operativos autorizados por el Usuario al momento de su registro:</p>
                                        <ul class="list-disc pl-6 text-gray-600 space-y-2">
                                                <li>Habilitar la creación, autenticación y gestión técnica de la cuenta de usuario.</li>
                                                <li>Permitir a los Clientes buscar y visualizar gráficamente la disponibilidad de profesionales independientes en su vecindad.</li>
                                                <li>Habilitar el canal de mensajería (chat interno) en tiempo real para coordinar de forma privada los presupuestos y detalles de los oficios requeridos.</li>
                                                <li>Gestionar y procesar el sistema de retroalimentación bidireccional (calificaciones y comentarios) tras finalizar los servicios.</li>
                                        </ul>
                                </div>

                                <div>
                                        <h2 class="text-2xl font-bold mb-4 text-dark-slate">4. Geolocalización y Seguridad</h2>
                                        <ul class="list-disc pl-6 text-gray-600 space-y-2 mb-4">
                                                <li><strong>Ubicación:</strong> El backend procesa la coordenada exacta provista por el Smartphone del Prestador.</li>
                                                <li><strong>Control del Estado Operativo:</strong> El envío de datos geográficos se restringe exclusivamente a los períodos en que la aplicación está abierta y el Prestador mantiene el interruptor de disponibilidad en "Modo Activo". Si el usuario cambia a "Modo Fuera de Servicio" o cierra la aplicación, el sistema suspenderá la actualización geográfica y ocultará el perfil del mapa.</li>
                                        </ul>
                                        <p class="text-gray-600 leading-relaxed italic">** A la consulta realizada (esto es suficiente y aplica en la voluntad de no estar visible como prestador) No requiere función o botón especial para tal efecto.</p>
                                </div>

                                <div>
                                        <h2 class="text-2xl font-bold mb-4 text-dark-slate">5. Ejercicio de Derechos ARCO y Mecanismo de Eliminación</h2>
                                        <p class="text-gray-600 leading-relaxed mb-2">El Usuario mantiene el control total sobre su información personal y podrá ejercer en cualquier momento sus derechos de Acceso, Rectificación, Cancelación y Oposición (ARCO).</p>
                                        <ul class="list-disc pl-6 text-gray-600 space-y-2">
                                                <li><strong>Modificación y Ocultación:</strong> El usuario puede ingresar a la sección de Configuración del Perfil dentro de la barra lateral para actualizar sus datos o desactivar su visibilidad inmediata en el mapa geográfico.</li>
                                                <li><strong>Eliminación Definitiva:</strong> Se garantiza un mecanismo directo dentro del perfil de usuario para dar de baja la cuenta. Al ejecutar esta acción, Match Work procederá al borrado permanente e irreversible de los datos de identidad, registros de ubicación e historial de la base de datos de producción (Cloud Firestore) de manera automática.</li>
                                        </ul>
                                </div>

                                <div>
                                        <h2 class="text-2xl font-bold mb-4 text-dark-slate">6. Destinatarios de los Datos y Transferencia</h2>
                                        <ul class="list-disc pl-6 text-gray-600 space-y-2">
                                                <li><strong>No Comercialización:</strong> La base de datos de los usuarios no se vende, arrienda, cede ni comercializa con agencias publicitarias ni terceras empresas bajo ningún concepto.</li>
                                                <li><strong>Intercambio Interno Mínimo:</strong> Los únicos datos que se transfieren internamente entre usuarios son el nombre, el oficio ofertado, la foto de perfil y la distancia en kilómetros, con el propósito exclusivo de concretar el sistema de conexión ("match").</li>
                                        </ul>
                                </div>

                                <div>
                                        <h2 class="text-2xl font-bold mb-4 text-dark-slate">7. Evolución de las Políticas y Consentimiento Futuro</h2>
                                        <p class="text-gray-600 leading-relaxed">El Usuario reconoce que Match Work se encuentra en una etapa de maduración técnica. Con la futura evolución en paralelo hacia un modelo comercial de Marketplace integral con pasarelas de pago e intermediación financiera activa, el volumen y tratamiento de datos. Cualquier cambio estructural en esta Política de Privacidad será notificado oportunamente mediante alertas dentro de la interfaz de la aplicación, requiriendo una nueva aceptación expresa para la continuidad del servicio.</p>
                                </div>
                        </div>
                </section>
        </main>\n"""
    lines[start_idx:end_idx+1] = [new_main]
    with open(filepath, 'w') as f:
        f.writelines(lines)
