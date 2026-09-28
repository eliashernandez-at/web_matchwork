import os

filepath = '/Users/elias/.gemini/antigravity-ide/scratch/matchwork/terminos.html'
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
                                <h1 class="text-4xl md:text-5xl font-bold mb-6 text-vibrant-lime">Términos y Condiciones de Uso</h1>
                                <p class="text-lg opacity-80">Última actualización: 10 de Agosto, 2026</p>
                        </div>
                </section>

                <!-- Terms Content -->
                <section class="py-16 md:py-24 px-margin-mobile md:px-margin-desktop bg-off-white text-dark-slate">
                        <div class="max-w-4xl mx-auto space-y-8 font-body-md">
                                <div>
                                        <p class="text-gray-600 leading-relaxed mb-4">Estos términos y condiciones regulan el uso y servicio de la aplicación móvil para iOS y Android Match Work y sitio web………… al crear una cuenta o utilizar el servicio aceptas términos y condiciones.</p>
                                        <p class="text-gray-600 leading-relaxed mb-4">Propiedad de: MatchWork SpA (RUT: 78.428.877-3)> <strong>Match Work</strong> en esta modalidad de entrada opera exclusivamente como un mural digital gratuito de contacto comunitario. La plataforma <strong>no es un proveedor laboral, agencia de empleo ni intermediario transaccional</strong>. Los usuarios son plenamente responsables de verificar la identidad, idoneidad y seguridad de las contrapartes antes de acordar o ejecutar cualquier servicio.</p>
                                </div>
                                
                                <div>
                                        <h2 class="text-2xl font-bold mb-4 text-dark-slate">1. Aceptación de los Términos y Consentimiento</h2>
                                        <p class="text-gray-600 leading-relaxed">El acceso, descarga y uso de la aplicación móvil y la plataforma web de Match Work atribuyen la condición de Usuario, ya sea en el rol de "Cliente" o "Prestador". Al presionar la casilla de marcación obligatoria durante el registro ("Acepto los Términos y Condiciones y la Política de Privacidad"), el usuario manifiesta su consentimiento expreso, informado y sin reservas a las condiciones aquí establecidas. Si no está de acuerdo con estos términos, deberá abstenerse de registrarse y utilizar la plataforma.</p>
                                </div>
                                
                                <div>
                                        <h2 class="text-2xl font-bold mb-4 text-dark-slate">2. Naturaleza del Servicio: Directorio Comunitario Gratuito</h2>
                                        <p class="text-gray-600 leading-relaxed mb-2">Match Work proporciona una plataforma tecnológica de red social basada en la geolocalización, cuyo único propósito es permitir que los Clientes visualicen de forma gráfica los perfiles de los Prestadores independientes que ofrecen oficios en su vecindad y que se encuentran en "Modo Activo".</p>
                                        <p class="text-gray-600 leading-relaxed mb-2">Prueba Gratuita: En esta fase de lanzamiento, el servicio es completamente gratuito y no exige el Rol Único Tributario (RUT) para el registro de cuentas básicas.</p>
                                        <p class="text-gray-600 leading-relaxed">Evolución del Servicio: El Usuario reconoce y acepta que la plataforma desarrollará progresivamente modelos de Marketplace con intermediación tecnológica y transaccional activa, para hacer sustentable el propósito lo cual implica la futura extensión de los alcances de estas condiciones, previo aviso oportuno en la aplicación. No obstante en compromiso a su principio social comunitario considera mantener cuentas básicas de uso gratuito durante todo su desarrollo y crecimiento.</p>
                                </div>

                                <div>
                                        <h2 class="text-2xl font-bold mb-4 text-dark-slate">3. Exclusión Estricta de Responsabilidad</h2>
                                        <p class="text-gray-600 leading-relaxed mb-2">Debido a que Match Work no realiza verificaciones de identidad, antecedentes ni certificaciones técnicas de los perfiles registrados en esta fase gratuita, se establece explícitamente que:</p>
                                        <ul class="list-disc pl-6 text-gray-600 space-y-2">
                                                <li><strong>Soporte Visual:</strong> La plataforma actúa únicamente como un soporte visual y directorio de contacto comunitario.</li>
                                                <li><strong>Inexistencia de Relación Laboral:</strong> No existe ningún tipo de vínculo laboral, subordinación, dependencia ni representación entre Match Work SpA y los Prestadores de servicios independientes.</li>
                                                <li><strong>Ausencia de Garantías:</strong> Match Work no garantiza la idoneidad, calidad, licitud, veracidad de los antecedentes, ni la conducta de los oferentes o clientes. Cualquier daño, perjuicio, estafa o disconformidad derivada de la prestación del servicio es de exclusiva responsabilidad de las partes involucradas.</li>
                                                <li><strong>Flujos Económicos Externos:</strong> Todos los acuerdos comerciales, presupuestos, negociaciones y flujos de pago se ejecutan de manera directa y exclusiva entre particulares, completamente al margen y fuera de la aplicación.</li>
                                        </ul>
                                </div>

                                <div>
                                        <h2 class="text-2xl font-bold mb-4 text-dark-slate">4. Obligaciones y Comportamiento del Usuario</h2>
                                        <p class="text-gray-600 leading-relaxed mb-2">Los usuarios se comprometen a utilizar la aplicación bajo los principios de la buena fe y el respeto comunitario. Queda estrictamente prohibido:</p>
                                        <ul class="list-disc pl-6 text-gray-600 space-y-2">
                                                <li>Suplantar la identidad de terceras personas o registrar datos falsos.</li>
                                                <li>Publicar servicios ilícitos, contenido pornográfico, violento u ofensivo.</li>
                                                <li>Utilizar los canales de mensajería interna (chat) para acosar, amenazar o realizar conductas abusivas.</li>
                                        </ul>
                                </div>

                                <div>
                                        <h2 class="text-2xl font-bold mb-4 text-dark-slate">5. Mecanismo de Denuncia y Moderación</h2>
                                        <p class="text-gray-600 leading-relaxed">Para mitigar riesgos y usos indebidos, Match Work pone a disposición de la comunidad una funcionalidad visible de "Reportar usuario o publicación" en cada perfil detallado. Tras la recepción de una alerta por comportamiento malicioso, fraudulento, ilícito o acoso, la administración se reserva el derecho de dar de baja los contenidos y suspender o eliminar el perfil infractor de forma inmediata y preventiva mediante moderación manual.</p>
                                </div>

                                <div>
                                        <h2 class="text-2xl font-bold mb-4 text-dark-slate">6. Modificaciones del servicio</h2>
                                        <p class="text-gray-600 leading-relaxed">Podemos cambiar, pausar o eliminar funcionalidades del Servicio en cualquier momento, con o sin aviso. Haremos esfuerzos razonables para notificar cambios materiales con anticipación. Si eliminamos el servicio completo, te avisaremos con al menos 30 días de anticipación.</p>
                                </div>

                                <div>
                                        <h2 class="text-2xl font-bold mb-4 text-dark-slate">7. Terminación</h2>
                                        <p class="text-gray-600 leading-relaxed">Puedes cerrar tu cuenta en cualquier momento desde la configuración de la app o escribiendo a soporte@....... Podemos suspender o cerrar tu cuenta sin aviso previo si incumples estos Términos, infringes la ley, o si tu uso del Servicio compromete su funcionamiento o el de otros usuarios.</p>
                                </div>

                                <div>
                                        <h2 class="text-2xl font-bold mb-4 text-dark-slate">8. Cambios a estos Términos</h2>
                                        <p class="text-gray-600 leading-relaxed">Si actualizamos estos Términos, cambiaremos la fecha al inicio del documento y te notificaremos dentro de la app. El uso continuado del Servicio luego del cambio implica aceptación de la versión nueva.</p>
                                </div>

                                <div>
                                        <h2 class="text-2xl font-bold mb-4 text-dark-slate">9. Ley aplicable y jurisdicción</h2>
                                        <p class="text-gray-600 leading-relaxed">Estos Términos se rigen por las leyes de la República de Chile. Cualquier controversia será resuelta por los tribunales ordinarios de justicia con asiento en la comuna de Santiago, Región Metropolitana, sin perjuicio de los derechos irrenunciables que la ley reconozca a los consumidores.</p>
                                </div>

                                <div>
                                        <h2 class="text-2xl font-bold mb-4 text-dark-slate">10. Contacto</h2>
                                        <p class="text-gray-600 leading-relaxed">Para cualquier consulta sobre estos Términos escríbenos a soporte@................</p>
                                </div>

                                <div>
                                        <h2 class="text-2xl font-bold mb-4 text-dark-slate">11. Propiedad Intelectual</h2>
                                        <p class="text-gray-600 leading-relaxed">Todos los derechos de propiedad intelectual del software, código fuente, algoritmos (incluyendo el sistema de emparejamiento exclusivo bajo "Modo Activo"), interfaces gráficas, logotipos y marcas comerciales están reservados a nombre de Match Work SpA. Queda prohibida su reproducción, explotación o ingeniería inversa sin autorización expresa.</p>
                                </div>
                        </div>
                </section>
        </main>\n"""
    lines[start_idx:end_idx+1] = [new_main]
    with open(filepath, 'w') as f:
        f.writelines(lines)
