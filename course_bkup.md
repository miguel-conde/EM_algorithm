Omitir e ir al contenido
Historial del chat




Tú dijiste:
necesito aprender sobre "EM (Excpectations Maximization) Algorithm". necesito centrarlo sobre un ejemplo en el que tenemos HCPs disctribuidos en bricks, conocemos las ventas totales de cada brick y necesitamos atribuirselas a los hcps
Data Science Mentor dijo:
Perfecto, el Algoritmo EM (Expectation–Maximization) encaja muy bien con el problema que describes 👍.
Antes de empezar formalmente el minicurso, necesito cumplir el Paso 1 y afinar el enfoque para que sea exactamente útil para ti.

🔍 Paso 1 — Aclaraciones necesarias
Por favor dime:

1️⃣ Tu nivel actual
¿Con cuál te identificas más?

🔰 Principiante: conoces estadística básica (media, probabilidad) pero no modelos latentes

📊 Intermedio: conoces MLE, distribuciones (Normal, Poisson), clustering (K-means)

🚀 Avanzado: ya has visto EM, modelos de mezcla, Bayesian inference

2️⃣ Herramientas
¿Quieres que el ejemplo se desarrolle principalmente en:

🐍 Python

📈 R

📐 Solo conceptual / matemático, con algo de pseudo-código

3️⃣ Dominio del problema
Para el caso de negocio:

¿Los HCPs pertenecen a un único brick o pueden influir en varios?

¿Las ventas son continuas (euros) o conteos (unidades)?

¿Dispones de alguna información previa por HCP?
(por ejemplo: especialidad, histórico parcial, potencial, visitas)

No hace falta que sea perfecto, solo “aproximadamente cierto”.

🧠 Adelanto (para alinear expectativas)
El problema que describes es clásico de variables latentes:

🔹 Observado:

Ventas totales por brick

🔹 No observado (latente):

Contribución individual de cada HCP

🔹 Objetivo:

Inferir probabilísticamente esas contribuciones

👉 EM es ideal porque:

No observamos directamente las ventas por HCP

Pero podemos modelar cómo se generan las ventas agregadas

➡️ Próximo paso (Paso 2)
Cuando me confirmes lo anterior, te propondré un mini-curso estructurado, por ejemplo:

Intuición del algoritmo EM (sin matemáticas duras)

Formulación del problema HCP–Brick como modelo latente

Definición de likelihood y variables ocultas

Paso E aplicado al caso de ventas

Paso M y actualización de parámetros

Ejemplo numérico paso a paso

Implementación en código

Interpretación de resultados y pitfalls reales (overfitting, identifiability)

Lo revisarás, lo ajustamos si quieres, y solo entonces empezamos el capítulo 1.

Espero tus respuestas 👨‍🏫📊

Tú dijiste:
1. Soy data scientist senior 2. Python 3. Pueden pertenecer a varios, las ventas son en unidades pero quiero saber que pasa si son en euros, se dispone de info sobre hcps (demografica, especialidad, visitas, etc.) 
Necesitaré que usemos datos mock porque no tengo reales
Data Science Mentor dijo:
Excelente, gracias por el contexto — con ese perfil podemos ir directo a un EM “de verdad”, bien formulado y cercano a producción 👍
Paso entonces al Paso 2: propuesta del mini-curso, centrado exactamente en tu caso HCP–Brick, con datos mock y código en Python.

📘 Mini-curso propuesto
Expectation–Maximization aplicado a atribución de ventas HCP–Brick
🎯 Objetivo general
Construir un modelo EM para atribuir ventas agregadas por brick a HCPs, cuando:

Los HCPs pueden contribuir a varios bricks

Las ventas están agregadas

Existen features observables por HCP

Queremos comparar:

🔢 Ventas en unidades (conteos)

💶 Ventas en euros (continuas)

🧠 Estructura del mini-curso
Capítulo 1 — El problema como modelo de variables latentes
Reformulación del business problem en términos estadísticos

Qué es observado vs latente

Por qué EM (y no regresión directa, SHAP, etc.)

Relación con:

Mixture Models

Ecological inference

Credit attribution

✔️ Salida: definición clara del modelo generativo

Capítulo 2 — Modelo probabilístico base (sin covariables)
Notación:

HCPs, Bricks, Ventas

Variable latente:

contribución individual 
z
h
,
b
z 
h,b
​
 

Supuestos iniciales:

Unidades → Poisson

Euros → Gamma / Lognormal

Likelihood completa vs marginal

✔️ Salida: likelihood formal del problema

Capítulo 3 — EM paso a paso en este contexto
E-step:

Cálculo de contribución esperada de cada HCP al total del brick

M-step:

Actualización de parámetros de productividad HCP

Interpretación probabilística del “share” de ventas

✔️ Salida: ecuaciones EM totalmente explícitas

Capítulo 4 — Ejemplo numérico pequeño (a mano)
2 bricks, 4 HCPs

Ventas conocidas por brick

Iteraciones EM manuales

Qué aprende el modelo realmente

✔️ Salida: intuición fuerte del algoritmo

Capítulo 5 — Incorporando features de HCP (modelo realista)
Productividad como función de covariables:

λ
h
=
exp
⁡
(
X
h
β
)
λ 
h
​
 =exp(X 
h
​
 β)
EM + GLM (Poisson / Gamma)

Regularización e identificabilidad

Qué pasa cuando un HCP está en muchos bricks

✔️ Salida: modelo listo para datos reales

Capítulo 6 — Mock data generation
Simulación realista:

HCPs con especialidad, visitas, seniority

Bricks con composición heterogénea

Ground truth conocido

Cómo evaluar si EM recupera la verdad

✔️ Salida: dataset sintético reutilizable

Capítulo 7 — Implementación completa en Python
Código EM desde cero (no sklearn)

Vectorización

Convergencia y criterios de parada

Debugging típico de EM

✔️ Salida: notebook funcional end-to-end

Capítulo 8 — Unidades vs Euros
Diferencias conceptuales:

Poisson vs Gamma / Lognormal

Impacto en:

Interpretación

Estabilidad

Sesgo por outliers

Cuándo conviene cada uno

✔️ Salida: guía práctica de model choice

Capítulo 9 — Pitfalls reales y extensiones
Identifiability

Overfitting silencioso

Cold start HCPs

EM vs Bayesian Hierarchical Models

Cuándo pasar a variational inference

✔️ Salida: criterio de senior data scientist

🧪 Estilo del curso
100% aplicado

Matemática solo cuando aporta

Código claro y extensible

Siempre conectando con decisiones de negocio

✅ Siguiente paso
¿Te parece bien esta estructura?

Opciones:

✔️ La aprobamos tal cual → empezamos Capítulo 1

✏️ Ajustamos:

Más foco en euros

Más matemática

Más comparación con modelos alternativos

Menos código / más código

Cuando me confirmes, arrancamos y no avanzamos de capítulo sin tu OK 👨‍🏫📊

Tú dijiste:
adelante con Capítulo 1 — El problema como modelo de variables latentes

Reformulación del business problem en términos estadísticos

Qué es observado vs latente

Por qué EM (y no regresión directa, SHAP, etc.)

Relación con:

Mixture Models

Ecological inference

Credit attribution

✔️ Salida: definición clara del modelo generativo
Data Science Mentor dijo:
Perfecto. Empezamos entonces Capítulo 1 con nivel senior, rigor estadístico y foco absoluto en tu caso HCP–Brick.
No habrá código todavía: aquí construimos el modelo mental y generativo que hará que EM sea inevitable (y defendible ante negocio).

📘 Capítulo 1 — El problema como modelo de variables latentes
1️⃣ Reformulación del business problem (de negocio → estadística)
🔹 Formulación de negocio
Tenemos HCPs distribuidos en bricks

Cada brick reporta ventas totales agregadas

No observamos ventas por HCP

Queremos atribuir esas ventas a HCPs individuales

Disponemos de features por HCP (especialidad, visitas, demografía…)

🔹 Reformulación estadística
Esto no es un problema de predicción directa, sino de inferir una descomposición no observada.

“Las ventas de cada brick son la suma de contribuciones latentes de los HCPs que lo componen.”

Formalmente:

Existe un proceso generativo no observado:

Cada HCP genera ventas

Parte de esas ventas se manifiestan en cada brick

Solo observamos el resultado agregado

👉 Esto es exactamente un problema de variables latentes + datos incompletos.

2️⃣ Qué está observado y qué es latente
🔍 Observado (datos)
y
b
y 
b
​
 : ventas totales del brick 
b
b

X
h
X 
h
​
 : covariables del HCP 
h
h

M
h
,
b
∈
{
0
,
1
}
M 
h,b
​
 ∈{0,1}: pertenencia HCP–brick
(o peso si la pertenencia no es binaria)

👻 Latente (no observado)
z
h
,
b
z 
h,b
​
 : contribución de ventas del HCP 
h
h al brick 
b
b

con la restricción:

∑
h
∈
b
z
h
,
b
=
y
b
h∈b
∑
​
 z 
h,b
​
 =y 
b
​
 
📌 Este 
z
h
,
b
z 
h,b
​
  es la variable oculta clave.

3️⃣ Por qué esto NO es una regresión directa
❌ Regresión naïve
Podrías intentar algo como:

y
b
=
∑
h
∈
b
f
(
X
h
)
y 
b
​
 = 
h∈b
∑
​
 f(X 
h
​
 )
Problemas:

No puedes identificar contribuciones individuales

No hay likelihood bien definida

No hay forma natural de repartir 
y
b
y 
b
​
 

Mal planteado para inferencia

❌ SHAP / Attribution post-hoc
SHAP asume:

Predicción individual

Función conocida

Observaciones independientes

Aquí:

El target es agregado

La unidad de decisión (HCP) no tiene label

El problema es estructuralmente inverso

👉 SHAP responde “por qué el modelo predijo”,
no “cómo se generaron los datos”.

4️⃣ Por qué EM es el algoritmo natural
🔑 Observación clave
Si conociéramos 
z
h
,
b
z 
h,b
​
 :

Podríamos estimar fácilmente productividad de HCPs

Podríamos ajustar un GLM estándar

Si conociéramos la productividad de HCPs:

Podríamos repartir las ventas esperadas entre ellos

👉 EM alterna exactamente entre estas dos cosas.

🧠 EM en una frase (en este contexto)
EM alterna entre atribuir probabilísticamente ventas a HCPs (E-step)
y actualizar el modelo de productividad de HCPs (M-step)

5️⃣ Relación con modelos conocidos
🔹 Mixture Models
Cada venta del brick proviene de un “componente” HCP:

p
(
venta
∣
b
)
=
∑
h
∈
b
π
h
,
b
 
p
h
p(venta∣b)= 
h∈b
∑
​
 π 
h,b
​
 p 
h
​
 
HCPs = componentes

π
h
,
b
π 
h,b
​
  = peso del HCP en el brick

z
h
,
b
z 
h,b
​
  = responsabilidades

📌 Es un mixture model con labels parcialmente observados.

🔹 Ecological Inference
Clásico problema:

Datos agregados

Inferencia a nivel individual

Múltiples soluciones posibles

EM:

Impone un modelo generativo

Regulariza vía covariables

Evita soluciones arbitrarias

🔹 Credit Attribution
Muy similar a:

Multi-touch attribution en marketing

Reparto de revenue entre canales

Diferencia clave:

Aquí las “touches” no se observan

Solo vemos el revenue final agregado

6️⃣ Definición clara del modelo generativo (SALIDA)
Este es el modelo conceptual que usaremos:

🔹 Nivel HCP
Cada HCP tiene una productividad latente:

θ
h
=
f
(
X
h
;
β
)
θ 
h
​
 =f(X 
h
​
 ;β)
Ejemplos:

Unidades → 
θ
h
=
λ
h
θ 
h
​
 =λ 
h
​
  (Poisson)

Euros → media Gamma / Lognormal

🔹 Nivel Brick
Las ventas del brick se generan como:

y
b
=
∑
h
∈
b
z
h
,
b
y 
b
​
 = 
h∈b
∑
​
 z 
h,b
​
 
con:

z
h
,
b
∼
Distribuci
o
ˊ
n
(
θ
h
,
w
h
,
b
)
z 
h,b
​
 ∼Distribuci 
o
ˊ
 n(θ 
h
​
 ,w 
h,b
​
 )
donde:

w
h
,
b
w 
h,b
​
 : exposición / peso del HCP en el brick
(visitas, tiempo, overlap geográfico…)

🔹 Lo que hace EM
E-step:

E
[
z
h
,
b
∣
y
b
,
θ
]
E[z 
h,b
​
 ∣y 
b
​
 ,θ]
M-step:

arg
⁡
max
⁡
β
∑
h
,
b
E
[
z
h
,
b
]
log
⁡
p
(
z
h
,
b
∣
X
h
)
arg 
β
max
​
  
h,b
∑
​
 E[z 
h,b
​
 ]logp(z 
h,b
​
 ∣X 
h
​
 )
📌 Todo lo demás del curso es implementar esto bien.

✅ Checkpoint
Antes de pasar al Capítulo 2 (modelo probabilístico concreto: Poisson vs Gamma), dime:

1️⃣ ¿Esta formulación refleja exactamente tu problema real?
2️⃣ ¿Quieres:

más formalismo matemático

o avanzar ya al modelo concreto?

Cuando me confirmes, seguimos 👨‍🏫📊

Tú dijiste:
perfecto asi. tengo 2 preguntas: 1) En Mixture Models explicas 𝑧
ℎ
,
𝑏
z
h,b
	​

 = responsabilidades

pero no aprece en la formula (aparece p_h) 2) En pocas lineas, dime sobre credit attribution y relacion con MTA en marketing - solo para entender, no entraremos mas en este curso
Data Science Mentor dijo:
Muy buenas preguntas — ambas van al núcleo conceptual del modelo. Las respondo con precisión y sin desviar el curso.

1️⃣ Mixture Models: ¿dónde están exactamente las responsabilidades 
z
h
,
b
z 
h,b
​
 ?
Tienes razón: tal como estaba escrita, la fórmula era incompleta / implícita. Vamos a corregirla y dejarla canónica.

🔹 Mixture model estándar (recordatorio)
En un mixture clásico:

p
(
y
)
=
∑
k
=
1
K
π
k
 
p
(
y
∣
θ
k
)
p(y)= 
k=1
∑
K
​
 π 
k
​
 p(y∣θ 
k
​
 )
y la variable latente es:

z
i
k
∈
{
0
,
1
}
,
∑
k
z
i
k
=
1
z 
ik
​
 ∈{0,1}, 
k
∑
​
 z 
ik
​
 =1
Las responsabilidades son:

γ
i
k
=
E
[
z
i
k
∣
y
i
]
γ 
ik
​
 =E[z 
ik
​
 ∣y 
i
​
 ]
🔹 Mixture reinterpretado en tu problema HCP–Brick
Aquí:

Un brick genera ventas

Cada venta/unidad proviene de un HCP

El HCP es el “componente” del mixture

Variable latente correcta
z
h
,
b
≡
n
u
ˊ
mero de unidades del brick 
b
 atribuibles al HCP 
h
z 
h,b
​
 ≡n 
u
ˊ
 mero de unidades del brick b atribuibles al HCP h
No es binaria, es conteo latente.

🔹 Modelo correctamente escrito
Para un brick 
b
b:

y
b
=
∑
h
∈
b
z
h
,
b
y 
b
​
 = 
h∈b
∑
​
 z 
h,b
​
 
y la probabilidad marginal:

p
(
y
b
∣
θ
)
=
∑
{
z
h
,
b
}
:
∑
z
=
y
b
∏
h
∈
b
[
π
h
,
b
z
h
,
b
⋅
p
(
z
h
,
b
∣
θ
h
)
]
p(y 
b
​
 ∣θ)= 
{z 
h,b
​
 }:∑z=y 
b
​
 
∑
​
  
h∈b
∏
​
 [π 
h,b
z 
h,b
​
 
​
 ⋅p(z 
h,b
​
 ∣θ 
h
​
 )]
👉 Esto es un mixture con datos agregados.

🔹 Responsabilidades (E-step real)
Las responsabilidades NO aparecen directamente en la likelihood, sino en el E-step:

γ
h
,
b
  
≡
  
E
[
z
h
,
b
∣
y
b
,
θ
]
γ 
h,b
​
 ≡E[z 
h,b
​
 ∣y 
b
​
 ,θ]
Intuición:

p
h
p 
h
​
  describe cómo genera ventas un HCP

γ
h
,
b
γ 
h,b
​
  dice qué fracción del brick le pertenece

En Poisson, por ejemplo:

γ
h
,
b
=
y
b
⋅
λ
h
w
h
,
b
∑
h
′
∈
b
λ
h
′
w
h
′
,
b
γ 
h,b
​
 =y 
b
​
 ⋅ 
∑ 
h 
′
 ∈b
​
 λ 
h 
′
 
​
 w 
h 
′
 ,b
​
 
λ 
h
​
 w 
h,b
​
 
​
 
📌 Conclusión

p
h
p 
h
​
  = distribución del componente

z
h
,
b
z 
h,b
​
  = variable latente

γ
h
,
b
=
E
[
z
h
,
b
]
γ 
h,b
​
 =E[z 
h,b
​
 ] = responsabilidades

Gracias por señalarlo: es una distinción crítica.

2️⃣ Credit attribution y relación con MTA (en pocas líneas)
🔹 Credit attribution (idea general)
Problema:

Un resultado final (venta, revenue) es consecuencia de múltiples agentes, pero solo observamos el total.

Objetivo:

Repartir el crédito entre agentes de forma consistente y explicable.

🔹 Multi-Touch Attribution (Marketing)
En marketing digital:

Agentes = canales (Search, Display, Email…)

Observado = conversión final

Latente = contribución de cada touch

Modelos MTA modernos:

Usan mixture models

Usan EM o Bayesian inference

Estiman responsabilidades por canal

🔹 Analogía exacta con tu problema
Marketing MTA	HCP–Brick
Canales	HCPs
Touches	Presencia en brick
Conversión	Ventas del brick
Attribution	
z
h
,
b
z 
h,b
​
 
📌 Conceptualmente idéntico, solo cambia la semántica del dominio.

✅ Checkpoint final
Si estás de acuerdo:
➡️ pasamos al Capítulo 2 — Modelo probabilístico base
(donde fijamos Poisson vs Gamma, likelihood formal y supuestos).

Confírmame y arrancamos.

Tú dijiste:
adelante Capítulo 2 — Modelo probabilístico base (sin covariables)

Notación:

HCPs, Bricks, Ventas

Variable latente:

contribución individual 
𝑧
ℎ
,
𝑏
z
h,b
	​


Supuestos iniciales:

Unidades → Poisson

Euros → Gamma / Lognormal

Likelihood completa vs marginal

✔️ Salida: likelihood formal del problema
Data Science Mentor dijo:
Perfecto. Entramos en Capítulo 2.
Aquí fijamos el modelo probabilístico base, aún sin covariables, para que el EM quede matemáticamente bien definido y auditable.

📘 Capítulo 2 — Modelo probabilístico base (sin covariables)
1️⃣ Notación formal (dejamos esto fijo para todo el curso)
Índices
h
=
1
,
…
,
H
h=1,…,H → HCPs

b
=
1
,
…
,
B
b=1,…,B → Bricks

Conjuntos
H
b
⊂
{
1
,
…
,
H
}
H 
b
​
 ⊂{1,…,H}: HCPs que pertenecen al brick 
b
b

Variables observadas
y
b
∈
R
+
y 
b
​
 ∈R 
+
 : ventas totales del brick 
b
b

w
h
,
b
≥
0
w 
h,b
​
 ≥0: exposición del HCP 
h
h en el brick 
b
b
(por ahora puede ser 1 si hay pertenencia)

Parámetros (a estimar)
θ
h
θ 
h
​
 : productividad latente del HCP 
h
h

2️⃣ Variable latente clave
Definimos:

z
h
,
b
≡
ventas atribuibles al HCP 
h
 en el brick 
b
z 
h,b
​
 ≡ventas atribuibles al HCP h en el brick b
con la restricción estructural:

∑
h
∈
H
b
z
h
,
b
=
y
b
h∈H 
b
​
 
∑
​
 z 
h,b
​
 =y 
b
​
 
📌 Esta restricción es lo que hace el problema no trivial.

3️⃣ Caso A — Ventas en unidades (Poisson)
🔹 Supuesto generativo
Cada HCP genera ventas de forma independiente:

z
h
,
b
∼
Poisson
(
λ
h
 
w
h
,
b
)
z 
h,b
​
 ∼Poisson(λ 
h
​
 w 
h,b
​
 )
donde:

λ
h
>
0
λ 
h
​
 >0: tasa base del HCP

w
h
,
b
w 
h,b
​
 : exposición en el brick

🔹 Propiedad clave (aditividad)
La suma de Poisson independientes es Poisson:

y
b
=
∑
h
∈
b
z
h
,
b
⇒
y
b
∼
Poisson
(
∑
h
∈
b
λ
h
w
h
,
b
)
y 
b
​
 = 
h∈b
∑
​
 z 
h,b
​
 ⇒y 
b
​
 ∼Poisson( 
h∈b
∑
​
 λ 
h
​
 w 
h,b
​
 )
📌 Esta propiedad justifica EM y simplifica enormemente el E-step.

🔹 Likelihood marginal (observada)
L
obs
(
λ
)
=
∏
b
=
1
B
Poisson
(
y
b
  
|
  
∑
h
∈
b
λ
h
w
h
,
b
)
L 
obs
​
 (λ)= 
b=1
∏
B
​
 Poisson(y 
b
​
  
​
  
h∈b
∑
​
 λ 
h
​
 w 
h,b
​
 )
🔹 Likelihood completa (con latentes)
L
comp
(
λ
)
=
∏
b
=
1
B
∏
h
∈
b
Poisson
(
z
h
,
b
∣
λ
h
w
h
,
b
)
L 
comp
​
 (λ)= 
b=1
∏
B
​
  
h∈b
∏
​
 Poisson(z 
h,b
​
 ∣λ 
h
​
 w 
h,b
​
 )
📌 EM optimiza la esperanza del log de esta expresión.

4️⃣ Caso B — Ventas en euros (continuas)
Aquí ya no podemos usar Poisson. Dos opciones realistas:

🔹 Opción 1: Gamma (mi favorita en este contexto)
Supuesto
z
h
,
b
∼
Gamma
(
k
,
θ
h
w
h
,
b
)
z 
h,b
​
 ∼Gamma(k,θ 
h
​
 w 
h,b
​
 )
Media: 
E
[
z
h
,
b
]
=
k
θ
h
w
h
,
b
E[z 
h,b
​
 ]=kθ 
h
​
 w 
h,b
​
 

Varianza proporcional a la media

Soporta asimetría

📌 Muy usada en revenue modeling.

Suma
Si todos los 
k
k son iguales:

y
b
=
∑
h
∈
b
z
h
,
b
∼
Gamma
(
k
∣
H
b
∣
,
∑
h
∈
b
θ
h
w
h
,
b
)
y 
b
​
 = 
h∈b
∑
​
 z 
h,b
​
 ∼Gamma(k∣H 
b
​
 ∣, 
h∈b
∑
​
 θ 
h
​
 w 
h,b
​
 )
🔹 Opción 2: Lognormal (más frágil)
log
⁡
z
h
,
b
∼
N
(
μ
h
+
log
⁡
w
h
,
b
,
σ
2
)
logz 
h,b
​
 ∼N(μ 
h
​
 +logw 
h,b
​
 ,σ 
2
 )
Problemas:

La suma no es lognormal

EM requiere aproximaciones

Sensible a outliers

📌 Útil si hay colas muy pesadas, pero más compleja.

5️⃣ Likelihood completa vs marginal (el corazón de EM)
🔹 Likelihood completa
La que queremos maximizar:

log
⁡
p
(
{
y
b
,
z
h
,
b
}
∣
θ
)
=
∑
b
,
h
log
⁡
p
(
z
h
,
b
∣
θ
h
)
logp({y 
b
​
 ,z 
h,b
​
 }∣θ)= 
b,h
∑
​
 logp(z 
h,b
​
 ∣θ 
h
​
 )
pero no podemos porque 
z
h
,
b
z 
h,b
​
  no se observa.

🔹 Likelihood marginal (observada)
log
⁡
p
(
{
y
b
}
∣
θ
)
=
∑
b
log
⁡
∫
∏
h
∈
b
p
(
z
h
,
b
∣
θ
h
)
 
δ
(
∑
z
−
y
b
)
d
z
logp({y 
b
​
 }∣θ)= 
b
∑
​
 log∫ 
h∈b
∏
​
 p(z 
h,b
​
 ∣θ 
h
​
 )δ(∑z−y 
b
​
 )dz
📌 Integral intratable → EM.

6️⃣ Qué hará EM exactamente (preview)
E-step
Calcula:

E
[
z
h
,
b
∣
y
b
,
θ
(
t
)
]
E[z 
h,b
​
 ∣y 
b
​
 ,θ 
(t)
 ]
M-step
Actualiza:

θ
h
(
t
+
1
)
=
arg
⁡
max
⁡
θ
h
∑
b
E
[
z
h
,
b
]
log
⁡
p
(
z
h
,
b
∣
θ
h
)
θ 
h
(t+1)
​
 =arg 
θ 
h
​
 
max
​
  
b
∑
​
 E[z 
h,b
​
 ]logp(z 
h,b
​
 ∣θ 
h
​
 )
7️⃣ ✔️ SALIDA — Likelihood formal del problema
🔹 Unidades (Poisson)
y
b
∼
Poisson
(
∑
h
∈
b
λ
h
w
h
,
b
)
y 
b
​
 ∼Poisson( 
h∈b
∑
​
 λ 
h
​
 w 
h,b
​
 )
​
 
con latentes:

z
h
,
b
∼
Poisson
(
λ
h
w
h
,
b
)
z 
h,b
​
 ∼Poisson(λ 
h
​
 w 
h,b
​
 )
🔹 Euros (Gamma)
y
b
∼
Gamma
(
k
∣
H
b
∣
,
∑
h
∈
b
θ
h
w
h
,
b
)
y 
b
​
 ∼Gamma(k∣H 
b
​
 ∣, 
h∈b
∑
​
 θ 
h
​
 w 
h,b
​
 )
​
 
✅ Checkpoint
Antes de pasar al Capítulo 3 — EM paso a paso (E-step y M-step explícitos):

1️⃣ ¿Te convence el Poisson para unidades?
2️⃣ ¿Prefieres que sigamos con Gamma para euros (y dejemos Lognormal como nota)?
3️⃣ ¿Quieres introducir ya weights 
w
h
,
b
w 
h,b
​
  más realistas (visitas, % solape)?

Confírmame y avanzamos.

Tú dijiste:
Cuando has dicho "Si conociéramos 
𝑧
ℎ
,
𝑏
z
h,b
	​

:

Podríamos estimar fácilmente productividad de HCPs" y "Si conociéramos la productividad de HCPs:" -> qué estás entendiendo como productividad?
Data Science Mentor dijo:
Excelente pregunta — y muy importante aclararla ahora, porque “productividad” puede significar cosas muy distintas según el nivel del modelo. Vamos a dejarla formal, precisa y sin ambigüedad.

🔑 Qué significa “productividad” en ESTE curso
Cuando digo productividad del HCP, NO me refiero a:

performance comercial “real”

causal uplift

impacto incremental puro

eficiencia del visitador

👉 Me refiero estrictamente a un parámetro del modelo generativo.

1️⃣ Definición formal (modelo base sin covariables)
🔹 Caso unidades (Poisson)
La productividad del HCP 
h
h es:

λ
h
=
E
[
unidades generadas por 
h
 por unidad de exposici
o
ˊ
n
]
λ 
h
​
 =E[unidades generadas por h por unidad de exposici 
o
ˊ
 n]
​
 
y el modelo dice:

z
h
,
b
∼
Poisson
(
λ
h
 
w
h
,
b
)
z 
h,b
​
 ∼Poisson(λ 
h
​
 w 
h,b
​
 )
Interpretación:

A igualdad de exposición 
w
h
,
b
w 
h,b
​
 

Un HCP con mayor 
λ
h
λ 
h
​
 

“genera” más unidades en promedio

📌 Es una tasa, no un efecto causal.

🔹 Caso euros (Gamma)
Aquí la productividad es:

θ
h
=
E
[
€ generados por 
h
 por unidad de exposici
o
ˊ
n
]
θ 
h
​
 =E[€ generados por h por unidad de exposici 
o
ˊ
 n]
​
 
con:

z
h
,
b
∼
Gamma
(
k
,
θ
h
w
h
,
b
)
z 
h,b
​
 ∼Gamma(k,θ 
h
​
 w 
h,b
​
 )
📌 Es el nivel medio de revenue atribuible al HCP.

2️⃣ “Si conociéramos 
z
h
,
b
z 
h,b
​
 , podríamos estimar productividad”
Ahora sí, con precisión:

🔹 Supón que 
z
h
,
b
z 
h,b
​
  es observado
Entonces para Poisson:

λ
^
h
=
∑
b
z
h
,
b
∑
b
w
h
,
b
λ
^
  
h
​
 = 
∑ 
b
​
 w 
h,b
​
 
∑ 
b
​
 z 
h,b
​
 
​
 
Es el MLE cerrado del Poisson.

👉 No hay EM, no hay dificultad, no hay ambigüedad.

3️⃣ “Si conociéramos la productividad, podríamos repartir ventas”
Supón ahora que conocemos 
λ
h
λ 
h
​
 .

Entonces, para un brick 
b
b:

E
[
z
h
,
b
∣
y
b
]
=
y
b
⋅
λ
h
w
h
,
b
∑
h
′
∈
b
λ
h
′
w
h
′
,
b
E[z 
h,b
​
 ∣y 
b
​
 ]=y 
b
​
 ⋅ 
∑ 
h 
′
 ∈b
​
 λ 
h 
′
 
​
 w 
h 
′
 ,b
​
 
λ 
h
​
 w 
h,b
​
 
​
 
📌 Esta es la regla de atribución del E-step.

Interpretación:

No decimos “el HCP h vendió exactamente X”

Decimos “dado su nivel esperado, le corresponde esta fracción”

4️⃣ Importante: lo que NO es productividad
Muy importante para evitar malinterpretaciones posteriores:

❌ No es:

efecto incremental causal

lift por visita

ROI del visitador

impacto neto frente a control

✔️ Sí es:

un parámetro latente

coherente con los datos agregados

interpretable dentro del modelo

Si mañana cambiamos el modelo (por ejemplo, jerárquico bayesiano), la productividad cambia de significado.

5️⃣ Cuando añadamos covariables (preview)
En el Capítulo 5, redefiniremos:

λ
h
=
exp
⁡
(
X
h
β
)
λ 
h
​
 =exp(X 
h
​
 β)
Aquí la productividad:

ya no es un parámetro libre

es una función de features

permite generalizar a HCPs nuevos

Pero la interpretación base no cambia:

“nivel esperado de generación de ventas por exposición”

✅ Checkpoint conceptual
Dime si esta definición te parece:

✔️ clara

✔️ defendible ante negocio

✔️ compatible con tu intuición

Si estás OK, en el siguiente mensaje arrancamos Capítulo 3 — EM paso a paso (E-step y M-step explícitos), ya con fórmulas cerradas.

Tú dijiste:
no he entendido bien. Qué hace credit attribution y en que se diferencia de em?
Data Science Mentor dijo:
Muy bien que pares aquí: esta confusión es normal incluso en equipos senior, porque credit attribution y EM se usan muchas veces como si fueran lo mismo… y no lo son.
Voy a explicarlo conceptualmente, sin matemáticas innecesarias.

🔍 Credit Attribution vs EM
Qué hace cada uno y en qué se diferencian
1️⃣ ¿Qué es Credit Attribution?
👉 Es un objetivo, no un algoritmo
Credit attribution significa:

Asignar una fracción de un resultado agregado (venta, revenue, conversión) a varios agentes que han participado.

Ejemplos:

Marketing: repartir una conversión entre canales

Tu caso: repartir ventas del brick entre HCPs

Finanzas: repartir P&L entre desks

📌 No dice cómo hacerlo, solo qué quieres obtener.

🔹 Resultado típico
Algo como:

Brick	HCP	Crédito asignado
B1	H1	30%
B1	H2	50%
B1	H3	20%
Eso es credit attribution.

2️⃣ ¿Qué NO es credit attribution?
❌ No es necesariamente estadístico

❌ No implica likelihood

❌ No implica variables latentes

❌ No implica inferencia

Ejemplos de credit attribution no estadístico:

Repartir ventas proporcionalmente al nº de visitas

Repartir ventas a partes iguales

Reglas de negocio (“el más senior se lleva más”)

👉 Todos hacen attribution, ninguno usa EM.

3️⃣ Entonces, ¿qué es EM?
👉 EM es un algoritmo de inferencia estadística
EM responde a:

Dado un modelo probabilístico con variables latentes, ¿cómo estimo sus parámetros?

EM:

Maximiza una likelihood

Asume un modelo generativo

Produce estimaciones consistentes (bajo supuestos)

📌 EM no tiene como objetivo principal repartir créditos,
eso es una consecuencia del E-step.

4️⃣ Relación exacta entre ambos (la clave)
🔑 En tu problema:
Credit attribution =
“¿Cuánto de la venta del brick corresponde a cada HCP?”

EM =
“¿Qué valores de productividad y contribuciones latentes explican mejor los datos agregados?”

🔁 Conexión
En EM:

El E-step calcula:

E
[
z
h
,
b
∣
y
b
]
E[z 
h,b
​
 ∣y 
b
​
 ]
Eso es una attribution probabilística

👉 Pero:

La attribution no es el objetivo

Es un subproducto necesario para aprender el modelo

5️⃣ Diferencia en una tabla clara
Aspecto	Credit Attribution	EM
Qué es	Objetivo	Algoritmo
Define	Qué se reparte	Cómo se infiere
Requiere modelo	No	Sí
Usa likelihood	No	Sí
Produce parámetros	No	Sí
Produce attribution	Sí	Indirectamente
6️⃣ Analogía muy clara (mental model)
🎂 Repartir una tarta
Credit attribution:
“¿Cómo repartimos la tarta entre 5 personas?”

EM:
“Asumimos que cada persona tiene un apetito distinto (latente).
Observamos cuánto se comió el grupo en total.
Inferimos los apetitos y, como consecuencia, cuánto comió cada uno.”

👉 EM explica el reparto, no lo decide arbitrariamente.

7️⃣ Resumen en una frase (para que te quede)
Credit attribution es el qué
EM es el cómo, bajo un modelo estadístico explícito

✅ Checkpoint
Dime si ahora ves clara esta separación:

¿Te queda claro que EM no es un método de attribution, sino un método de inferencia?

¿Ves por qué muchos sistemas de attribution no necesitan EM, pero el tuyo sí?

Si estás OK, en el siguiente paso entramos de lleno en Capítulo 3 — EM paso a paso, donde verás cómo la attribution sale automáticamente del E-step.

Tú dijiste:
es decir, que EM es una de las posibles maneras de CÓMO hacer credit attribution (el QUÉ). Otras maneras son mixture models y bayesian inference. Es así?
Data Science Mentor dijo:
Casi perfecto 👍 — solo hace falta un pequeño ajuste conceptual para que quede exactamente correcto.
Voy a dejarlo cristalino y cerramos esta parte.

✅ La forma correcta de pensarlo
✔️ Lo que sí es correcto
Credit attribution es el QUÉ
→ repartir un resultado agregado entre agentes

Existen muchas maneras de hacer credit attribution

❗ El ajuste importante
Mixture models NO son una alternativa a EM
Bayesian inference NO es una alternativa a EM

👉 Están en niveles distintos del stack conceptual.

🧱 Stack correcto (de arriba a abajo)
1️⃣ QUÉ — Credit attribution
El problema de negocio

Ejemplo:

Repartir ventas del brick entre HCPs

2️⃣ MODELO — Mixture / Latent variable model
Cómo supones que se generan los datos

Ejemplos:

Mixture model

Latent additive model

Hierarchical model

📌 Aquí decides qué es 
z
h
,
b
z 
h,b
​
  y cómo se genera.

3️⃣ CÓMO INFERIR — EM / Bayesian / VI
Cómo estimas los parámetros del modelo

Ejemplos:

EM → Maximum Likelihood con latentes

Bayesian inference → posterior completo

Variational inference → aproximación

📊 Dónde encaja EM exactamente
EM es:

Una forma de inferir parámetros en modelos con variables latentes

No es:

ni el problema

ni el modelo

🔁 Reescribiendo tu frase (100% correcta)
Tu frase:

“EM es una de las posibles maneras de CÓMO hacer credit attribution (el QUÉ). Otras maneras son mixture models y bayesian inference.”

La versión exacta sería:

“Credit attribution es el QUÉ.
Definimos un modelo latente (por ejemplo, un mixture model).
EM es una de las maneras de inferir ese modelo; la inferencia bayesiana es otra.”

🧠 Ejemplo concreto (tu caso)
QUÉ:
Repartir ventas del brick entre HCPs

MODELO:
z
h
,
b
∼
Poisson
(
λ
h
w
h
,
b
)
z 
h,b
​
 ∼Poisson(λ 
h
​
 w 
h,b
​
 )

CÓMO (opción A):
EM → MLE de 
λ
h
λ 
h
​
 

CÓMO (opción B):
Bayes → 
p
(
λ
h
∣
y
)
p(λ 
h
​
 ∣y)

Ambos producen:

una attribution

pero con propiedades distintas

📌 Regla mental útil (para siempre)
Model ≠ Inference ≠ Business objective

Si confundes uno con otro:

los modelos se vuelven “religión”

las discusiones con negocio se rompen

✅ Checkpoint final de claridad
Si esto ya está claro, en el siguiente mensaje entramos sin más interrupciones en:

👉 Capítulo 3 — EM paso a paso
E-step explícito

M-step explícito

Interpretación directa en tu problema HCP–Brick

Confírmame y seguimos.

Tú dijiste:
pasemos a Capítulo 3 — EM paso a paso en este contexto

E-step:

Cálculo de contribución esperada de cada HCP al total del brick

M-step:

Actualización de parámetros de productividad HCP

Interpretación probabilística del “share” de ventas

✔️ Salida: ecuaciones EM totalmente explícitas
Data Science Mentor dijo:
📘 Capítulo 3 — EM paso a paso (HCP–Brick)
Nos centramos en el caso unidades (Poisson) porque ahí EM queda cerrado y muy limpio. Luego te dejo al final el análogo para euros (Gamma).

0️⃣ Recordatorio del modelo (del Capítulo 2)
Para cada brick 
b
b y HCP 
h
∈
H
b
h∈H 
b
​
 :

Latentes (no observados):

z
h
,
b
∼
Poisson
(
λ
h
 
w
h
,
b
)
z 
h,b
​
 ∼Poisson(λ 
h
​
 w 
h,b
​
 )
Observado:

y
b
=
∑
h
∈
H
b
z
h
,
b
y 
b
​
 = 
h∈H 
b
​
 
∑
​
 z 
h,b
​
 
Parámetros:
λ
h
>
0
λ 
h
​
 >0 (productividad/tasa por exposición)

1️⃣ Idea clave: condicionando en el total
Propiedad fundamental:

Si 
z
1
,
…
,
z
K
z 
1
​
 ,…,z 
K
​
  son Poisson independientes con medias 
μ
1
,
…
,
μ
K
μ 
1
​
 ,…,μ 
K
​
 , entonces condicionado en la suma 
y
=
∑
z
k
y=∑z 
k
​
 :

(
z
1
,
…
,
z
K
)
∣
y
∼
Multinomial
(
y
;
  
p
1
,
…
,
p
K
)
(z 
1
​
 ,…,z 
K
​
 )∣y∼Multinomial(y;p 
1
​
 ,…,p 
K
​
 )
donde

p
k
=
μ
k
∑
j
μ
j
p 
k
​
 = 
∑ 
j
​
 μ 
j
​
 
μ 
k
​
 
​
 
En nuestro caso, para un brick 
b
b:

μ
h
,
b
=
λ
h
w
h
,
b
μ 
h,b
​
 =λ 
h
​
 w 
h,b
​
 

y
=
y
b
y=y 
b
​
 

2️⃣ E-step: contribución esperada por HCP dentro del brick
Definimos el “share” esperado (responsabilidad) del HCP 
h
h en el brick 
b
b:

p
h
,
b
(
t
)
=
λ
h
(
t
)
w
h
,
b
∑
h
′
∈
H
b
λ
h
′
(
t
)
w
h
′
,
b
p 
h,b
(t)
​
 = 
∑ 
h 
′
 ∈H 
b
​
 
​
 λ 
h 
′
 
(t)
​
 w 
h 
′
 ,b
​
 
λ 
h
(t)
​
 w 
h,b
​
 
​
 
Entonces:

E
 ⁣
[
z
h
,
b
∣
y
b
,
λ
(
t
)
]
=
y
b
 
p
h
,
b
(
t
)
E[z 
h,b
​
 ∣y 
b
​
 ,λ 
(t)
 ]=y 
b
​
 p 
h,b
(t)
​
 
​
 
y además (útil para el M-step):

E
 ⁣
[
log
⁡
p
(
z
h
,
b
∣
λ
h
)
]
 
se eval
u
ˊ
a usando
 
E
[
z
h
,
b
]
E[logp(z 
h,b
​
 ∣λ 
h
​
 )] se eval 
u
ˊ
 a usando E[z 
h,b
​
 ]
porque en Poisson el log-likelihood depende de 
z
z linealmente salvo el 
log
⁡
(
z
!
)
log(z!) (que no depende de 
λ
h
λ 
h
​
  en el M-step).

🔎 Interpretación inmediata

Dentro de un brick, EM reparte el total 
y
b
y 
b
​
  proporcionalmente a “capacidad” actual:
λ
h
(
t
)
w
h
,
b
λ 
h
(t)
​
 w 
h,b
​
 .

Si 
w
h
,
b
=
1
w 
h,b
​
 =1, es proporcional solo a 
λ
h
(
t
)
λ 
h
(t)
​
 .

3️⃣ M-step: actualizar la productividad de cada HCP
Si los 
z
h
,
b
z 
h,b
​
  fueran observados, el MLE de 
λ
h
λ 
h
​
  sería:

λ
^
h
=
∑
b
z
h
,
b
∑
b
w
h
,
b
λ
^
  
h
​
 = 
∑ 
b
​
 w 
h,b
​
 
∑ 
b
​
 z 
h,b
​
 
​
 
Como no lo son, EM sustituye 
z
h
,
b
z 
h,b
​
  por su esperanza del E-step:

λ
h
(
t
+
1
)
=
∑
b
:
h
∈
H
b
 
E
[
z
h
,
b
∣
y
b
,
λ
(
t
)
]
∑
b
:
h
∈
H
b
w
h
,
b
λ 
h
(t+1)
​
 = 
∑ 
b:h∈H 
b
​
 
​
 w 
h,b
​
 
∑ 
b:h∈H 
b
​
 
​
  E[z 
h,b
​
 ∣y 
b
​
 ,λ 
(t)
 ]
​
 
​
 
Sustituyendo explícitamente:

λ
h
(
t
+
1
)
=
∑
b
:
h
∈
H
b
y
b
⋅
λ
h
(
t
)
w
h
,
b
∑
h
′
∈
H
b
λ
h
′
(
t
)
w
h
′
,
b
∑
b
:
h
∈
H
b
w
h
,
b
λ 
h
(t+1)
​
 = 
∑ 
b:h∈H 
b
​
 
​
 w 
h,b
​
 
∑ 
b:h∈H 
b
​
 
​
 y 
b
​
 ⋅ 
∑ 
h 
′
 ∈H 
b
​
 
​
 λ 
h 
′
 
(t)
​
 w 
h 
′
 ,b
​
 
λ 
h
(t)
​
 w 
h,b
​
 
​
 
​
 
​
 
4️⃣ Interpretación probabilística del “share” de ventas
Hay dos niveles de “share”, y es útil separarlos:

A) Share dentro del brick (local)
p
h
,
b
(
t
)
=
λ
h
(
t
)
w
h
,
b
∑
h
′
∈
b
λ
h
′
(
t
)
w
h
′
,
b
p 
h,b
(t)
​
 = 
∑ 
h 
′
 ∈b
​
 λ 
h 
′
 
(t)
​
 w 
h 
′
 ,b
​
 
λ 
h
(t)
​
 w 
h,b
​
 
​
 
​
 
Esto es literalmente:

la probabilidad de que una unidad del brick 
b
b “venga” del HCP 
h
h,
bajo el modelo actual,

y la esperanza de unidades atribuibles es 
y
b
p
h
,
b
(
t
)
y 
b
​
 p 
h,b
(t)
​
 .

B) Share global del HCP (agregando bricks)
Una vez tienes 
E
[
z
h
,
b
]
E[z 
h,b
​
 ], puedes construir:

Ventas esperadas de 
h
=
∑
b
E
[
z
h
,
b
]
Ventas esperadas de h= 
b
∑
​
 E[z 
h,b
​
 ]
y el share global sobre el total:

Share
h
=
∑
b
E
[
z
h
,
b
]
∑
b
y
b
Share 
h
​
 = 
∑ 
b
​
 y 
b
​
 
∑ 
b
​
 E[z 
h,b
​
 ]
​
 
5️⃣ Resumen del algoritmo EM (Poisson) en 4 líneas
Inicializa 
λ
h
(
0
)
>
0
λ 
h
(0)
​
 >0. Repite hasta convergencia:

E-step:

p
h
,
b
(
t
)
=
λ
h
(
t
)
w
h
,
b
∑
h
′
∈
b
λ
h
′
(
t
)
w
h
′
,
b
;
z
^
h
,
b
(
t
)
=
y
b
 
p
h
,
b
(
t
)
p 
h,b
(t)
​
 = 
∑ 
h 
′
 ∈b
​
 λ 
h 
′
 
(t)
​
 w 
h 
′
 ,b
​
 
λ 
h
(t)
​
 w 
h,b
​
 
​
 ; 
z
^
  
h,b
(t)
​
 =y 
b
​
 p 
h,b
(t)
​
 
M-step:

λ
h
(
t
+
1
)
=
∑
b
z
^
h
,
b
(
t
)
∑
b
w
h
,
b
λ 
h
(t+1)
​
 = 
∑ 
b
​
 w 
h,b
​
 
∑ 
b
​
  
z
^
  
h,b
(t)
​
 
​
 
📌 Esto ya es EM totalmente explícito para tu caso.

6️⃣ Nota rápida: análogo para euros (Gamma)
Si modelas euros con Gamma y eliges una parametrización aditiva (por ejemplo, misma forma 
k
k y media proporcional a 
θ
h
w
h
,
b
θ 
h
​
 w 
h,b
​
 ), aparece un resultado análogo:

El reparto en el E-step suele terminar siendo (bajo esas parametrizaciones) proporcional a la contribución esperada:

E
[
z
h
,
b
∣
y
b
]
≈
y
b
⋅
θ
h
w
h
,
b
∑
h
′
θ
h
′
w
h
′
,
b
E[z 
h,b
​
 ∣y 
b
​
 ]≈y 
b
​
 ⋅ 
∑ 
h 
′
 
​
 θ 
h 
′
 
​
 w 
h 
′
 ,b
​
 
θ 
h
​
 w 
h,b
​
 
​
 
El M-step actualiza 
θ
h
θ 
h
​
  parecido a “ventas esperadas / exposición”.

La diferencia es que, dependiendo de cómo parametrices Gamma (shape/scale vs shape/rate) y si estimas 
k
k, el M-step puede requerir:

o una actualización cerrada,

o un paso numérico (Newton) para 
k
k.

(En el curso, cuando lleguemos a euros, lo dejaremos consistente y operativo.)

✅ Checkpoint
¿Te cuadra esta lectura?

E-step = “reparto probabilístico” por brick según 
λ
h
w
h
,
b
λ 
h
​
 w 
h,b
​
 

M-step = “recalibrar” 
λ
h
λ 
h
​
  como ventas esperadas / exposición

Si todo OK, pasamos al Capítulo 4 y lo hacemos con un ejemplo numérico pequeño a mano (2 bricks, 4 HCPs) para que se vea cómo convergen 
λ
λ y los shares.

Tú dijiste:
adelante Capítulo 4 — Ejemplo numérico pequeño (a mano)

2 bricks, 4 HCPs

Ventas conocidas por brick

Iteraciones EM manuales

Qué aprende el modelo realmente

✔️ Salida: intuición fuerte del algoritmo
Data Science Mentor dijo:
📘 Capítulo 4 — Ejemplo numérico pequeño (a mano)
Vamos a hacerlo mínimo pero completo: 2 bricks, 4 HCPs, ventas agregadas por brick, y veremos 2–3 iteraciones de EM para que la mecánica quede grabada.

Trabajamos con unidades y el modelo Poisson del Capítulo 3, con pesos simples.

1️⃣ Setup del ejemplo
Bricks y ventas observadas
Brick A: 
y
A
=
100
y 
A
​
 =100

Brick B: 
y
B
=
60
y 
B
​
 =60

HCPs y pertenencia (overlap)
En Brick A están: H1, H2, H3

En Brick B están: H2, H3, H4

Exposición (para simplificar)
Tomamos 
w
h
,
b
=
1
w 
h,b
​
 =1 si el HCP pertenece al brick, 0 si no.

2️⃣ Inicialización (iteración 0)
Inicializamos productividades (tasas) arbitrarias, todas positivas:

λ
(
0
)
=
(
λ
1
,
λ
2
,
λ
3
,
λ
4
)
=
(
1.0
,
 
1.0
,
 
1.0
,
 
1.0
)
λ 
(0)
 =(λ 
1
​
 ,λ 
2
​
 ,λ 
3
​
 ,λ 
4
​
 )=(1.0, 1.0, 1.0, 1.0)
3️⃣ Iteración 0 → 1
✅ E-step (reparto dentro de cada brick)
Brick A (H1,H2,H3): suma de tasas = 
1
+
1
+
1
=
3
1+1+1=3

Shares:

p
1
,
A
=
1
/
3
p 
1,A
​
 =1/3

p
2
,
A
=
1
/
3
p 
2,A
​
 =1/3

p
3
,
A
=
1
/
3
p 
3,A
​
 =1/3

Atribuciones esperadas:

z
^
1
,
A
=
100
⋅
1
/
3
=
33.33
z
^
  
1,A
​
 =100⋅1/3=33.33

z
^
2
,
A
=
33.33
z
^
  
2,A
​
 =33.33

z
^
3
,
A
=
33.33
z
^
  
3,A
​
 =33.33

Brick B (H2,H3,H4): suma = 
1
+
1
+
1
=
3
1+1+1=3

Atribuciones esperadas:

z
^
2
,
B
=
60
⋅
1
/
3
=
20
z
^
  
2,B
​
 =60⋅1/3=20

z
^
3
,
B
=
20
z
^
  
3,B
​
 =20

z
^
4
,
B
=
20
z
^
  
4,B
​
 =20

✅ M-step (actualización de 
λ
λ)
Usamos:

λ
h
(
1
)
=
∑
b
z
^
h
,
b
∑
b
w
h
,
b
λ 
h
(1)
​
 = 
∑ 
b
​
 w 
h,b
​
 
∑ 
b
​
  
z
^
  
h,b
​
 
​
 
Exposiciones (número de bricks en los que está cada HCP):

H1: 1 (solo A)

H2: 2 (A y B)

H3: 2 (A y B)

H4: 1 (solo B)

Entonces:

λ
1
(
1
)
=
33.33
/
1
=
33.33
λ 
1
(1)
​
 =33.33/1=33.33

λ
2
(
1
)
=
(
33.33
+
20
)
/
2
=
26.67
λ 
2
(1)
​
 =(33.33+20)/2=26.67

λ
3
(
1
)
=
(
33.33
+
20
)
/
2
=
26.67
λ 
3
(1)
​
 =(33.33+20)/2=26.67

λ
4
(
1
)
=
20
/
1
=
20
λ 
4
(1)
​
 =20/1=20

📌 Ya ves algo: H1 sube mucho porque tiene que explicar parte de un brick grande y no está “penalizado” por aparecer en varios bricks.

4️⃣ Iteración 1 → 2
✅ E-step
Brick A: tasas (H1,H2,H3) = (33.33, 26.67, 26.67), suma = 86.67

Shares:

p
1
,
A
=
33.33
/
86.67
≈
0.3846
p 
1,A
​
 =33.33/86.67≈0.3846

p
2
,
A
=
26.67
/
86.67
≈
0.3077
p 
2,A
​
 =26.67/86.67≈0.3077

p
3
,
A
=
26.67
/
86.67
≈
0.3077
p 
3,A
​
 =26.67/86.67≈0.3077

Atribuciones:

z
^
1
,
A
=
100
⋅
0.3846
=
38.46
z
^
  
1,A
​
 =100⋅0.3846=38.46

z
^
2
,
A
=
30.77
z
^
  
2,A
​
 =30.77

z
^
3
,
A
=
30.77
z
^
  
3,A
​
 =30.77

Brick B: tasas (H2,H3,H4) = (26.67, 26.67, 20), suma = 73.34

Shares:

p
2
,
B
=
26.67
/
73.34
≈
0.3636
p 
2,B
​
 =26.67/73.34≈0.3636

p
3
,
B
≈
0.3636
p 
3,B
​
 ≈0.3636

p
4
,
B
=
20
/
73.34
≈
0.2727
p 
4,B
​
 =20/73.34≈0.2727

Atribuciones:

z
^
2
,
B
=
60
⋅
0.3636
=
21.82
z
^
  
2,B
​
 =60⋅0.3636=21.82

z
^
3
,
B
=
21.82
z
^
  
3,B
​
 =21.82

z
^
4
,
B
=
16.36
z
^
  
4,B
​
 =16.36

✅ M-step
λ
1
(
2
)
=
38.46
/
1
=
38.46
λ 
1
(2)
​
 =38.46/1=38.46

λ
2
(
2
)
=
(
30.77
+
21.82
)
/
2
=
26.30
λ 
2
(2)
​
 =(30.77+21.82)/2=26.30

λ
3
(
2
)
=
(
30.77
+
21.82
)
/
2
=
26.30
λ 
3
(2)
​
 =(30.77+21.82)/2=26.30

λ
4
(
2
)
=
16.36
/
1
=
16.36
λ 
4
(2)
​
 =16.36/1=16.36

Observa:

H1 sigue subiendo (absorbe más del brick A)

H4 baja (ahora comparte con H2/H3 más fuertes)

H2 y H3 se estabilizan

5️⃣ Iteración 2 → 3 (una más para ver estabilidad)
✅ E-step (rápido)
Brick A: (38.46, 26.30, 26.30), suma = 91.06
Shares:

H1: 0.4224 → 
z
^
1
,
A
=
42.24
z
^
  
1,A
​
 =42.24

H2: 0.2888 → 
z
^
2
,
A
=
28.88
z
^
  
2,A
​
 =28.88

H3: 0.2888 → 
z
^
3
,
A
=
28.88
z
^
  
3,A
​
 =28.88

Brick B: (26.30, 26.30, 16.36), suma = 68.96
Shares:

H2: 0.3814 → 
z
^
2
,
B
=
22.88
z
^
  
2,B
​
 =22.88

H3: 0.3814 → 
z
^
3
,
B
=
22.88
z
^
  
3,B
​
 =22.88

H4: 0.2372 → 
z
^
4
,
B
=
14.23
z
^
  
4,B
​
 =14.23

✅ M-step
λ
1
(
3
)
=
42.24
λ 
1
(3)
​
 =42.24

λ
2
(
3
)
=
(
28.88
+
22.88
)
/
2
=
25.88
λ 
2
(3)
​
 =(28.88+22.88)/2=25.88

λ
3
(
3
)
=
(
28.88
+
22.88
)
/
2
=
25.88
λ 
3
(3)
​
 =(28.88+22.88)/2=25.88

λ
4
(
3
)
=
14.23
λ 
4
(3)
​
 =14.23

Ya está casi convergido (cambios pequeños).

6️⃣ ¿Qué aprende EM “realmente” aquí?
✅ 1) Aprende productividades relativas coherentes con todas las ecuaciones de suma
No está “prediciendo” 
y
b
y 
b
​
  (eso ya está dado). Está encontrando 
λ
h
λ 
h
​
  tal que:

Brick A (100) se explique como suma esperada de H1,H2,H3

Brick B (60) se explique como suma esperada de H2,H3,H4

Y que el reparto sea estable y auto-consistente

✅ 2) Los HCPs que aparecen en más bricks quedan “regularizados” por consistencia
H2 y H3 deben cuadrar dos ecuaciones (A y B), por eso se estabilizan.

✅ 3) HCP “exclusivo” de brick grande tiende a llevarse más (si no hay más estructura)
H1 solo está en A, así que el modelo puede subirlo sin que “choque” con otras restricciones.
Esto es una pista de un pitfall real: sin covariables o priors, la identificabilidad puede ser débil.

7️⃣ Lectura de negocio del resultado (share final aproximado)
Dentro de A (cerca de iteración 3):

H1 ≈ 42%

H2 ≈ 29%

H3 ≈ 29%

Dentro de B:

H2 ≈ 38%

H3 ≈ 38%

H4 ≈ 24%

Eso es exactamente la attribution probabilística del E-step en convergencia.

✅ Checkpoint
¿Te ha quedado clara la dinámica?

E-step reparte dentro de cada brick proporcional a 
λ
λ

M-step recalcula 
λ
λ como “ventas esperadas / exposición”

Los HCPs con overlap quedan más “anclados”; los exclusivos pueden absorber más

Si todo OK, pasamos al Capítulo 5 — Incorporando features (GLM: 
λ
h
=
exp
⁡
(
X
h
β
)
λ 
h
​
 =exp(X 
h
​
 β)), que es donde tu caso real cobra potencia.

Tú dijiste:
adelante, Capítulo 5 — Incorporando features de HCP (modelo realista)

Productividad como función de covariables:

𝜆
ℎ
=
exp
⁡
(
𝑋
ℎ
𝛽
)
λ
h
	​

=exp(X
h
	​

β)

EM + GLM (Poisson / Gamma)

Regularización e identificabilidad

Qué pasa cuando un HCP está en muchos bricks

✔️ Salida: modelo listo para datos reales
Data Science Mentor dijo:
📘 Capítulo 5 — Incorporando features de HCP (modelo realista)
Este capítulo es el salto a producción.
Pasamos de “un 
λ
h
λ 
h
​
  libre por HCP” a un modelo paramétrico, generalizable y regularizado.

1️⃣ Por qué necesitamos covariables (motivación)
En el Capítulo 4 vimos un problema clave:

HCPs “exclusivos” de bricks grandes pueden absorber demasiada venta

El modelo es débilmente identificable

No generaliza a HCPs nuevos

👉 Solución: atar la productividad a información observable.

2️⃣ Nueva definición de productividad
Definimos:

λ
h
=
exp
⁡
(
X
h
β
)
λ 
h
​
 =exp(X 
h
​
 β)
​
 
donde:

X
h
∈
R
p
X 
h
​
 ∈R 
p
 : features del HCP
(especialidad, seniority, nº visitas, potencial, etc.)

β
∈
R
p
β∈R 
p
 : coeficientes globales

📌 Interpretación:

Dos HCPs con mismos 
X
X tienen misma productividad esperada

El modelo comparte fuerza estadística

3️⃣ Modelo completo con covariables (Poisson)
🔹 Generativo
z
h
,
b
∼
Poisson
(
exp
⁡
(
X
h
β
)
 
w
h
,
b
)
z 
h,b
​
 ∼Poisson(exp(X 
h
​
 β)w 
h,b
​
 )
y
b
=
∑
h
∈
b
z
h
,
b
y 
b
​
 = 
h∈b
∑
​
 z 
h,b
​
 
4️⃣ EM + GLM: cómo encajan
🔁 E-step (igual que antes)
Con 
λ
h
(
t
)
=
exp
⁡
(
X
h
β
(
t
)
)
λ 
h
(t)
​
 =exp(X 
h
​
 β 
(t)
 ):

E
[
z
h
,
b
∣
y
b
,
β
(
t
)
]
=
y
b
⋅
exp
⁡
(
X
h
β
(
t
)
)
w
h
,
b
∑
h
′
∈
b
exp
⁡
(
X
h
′
β
(
t
)
)
w
h
′
,
b
E[z 
h,b
​
 ∣y 
b
​
 ,β 
(t)
 ]=y 
b
​
 ⋅ 
∑ 
h 
′
 ∈b
​
 exp(X 
h 
′
 
​
 β 
(t)
 )w 
h 
′
 ,b
​
 
exp(X 
h
​
 β 
(t)
 )w 
h,b
​
 
​
 
​
 
📌 Nada cambia conceptualmente.

🔄 M-step (ahora es un GLM)
Definimos los “pseudo-targets”:

y
~
h
=
∑
b
E
[
z
h
,
b
]
y
~
​
  
h
​
 = 
b
∑
​
 E[z 
h,b
​
 ]
y la exposición total:

w
~
h
=
∑
b
w
h
,
b
w
~
  
h
​
 = 
b
∑
​
 w 
h,b
​
 
Entonces el M-step es:

max
⁡
β
∑
h
[
y
~
h
log
⁡
λ
h
−
λ
h
w
~
h
]
con 
λ
h
=
exp
⁡
(
X
h
β
)
β
max
​
  
h
∑
​
 [ 
y
~
​
  
h
​
 logλ 
h
​
 −λ 
h
​
  
w
~
  
h
​
 ]
​
 con λ 
h
​
 =exp(X 
h
​
 β)
👉 Esto es exactamente una Poisson regression con offset:

Response: 
y
~
h
y
~
​
  
h
​
 

Offset: 
log
⁡
(
w
~
h
)
log( 
w
~
  
h
​
 )

📌 Se resuelve con IRLS estándar.

5️⃣ Caso euros (Gamma + covariables)
Análogo:

z
h
,
b
∼
Gamma
(
k
,
θ
h
w
h
,
b
)
con
θ
h
=
exp
⁡
(
X
h
β
)
z 
h,b
​
 ∼Gamma(k,θ 
h
​
 w 
h,b
​
 )conθ 
h
​
 =exp(X 
h
​
 β)
E-step: reparto proporcional a 
θ
h
w
h
,
b
θ 
h
​
 w 
h,b
​
 

M-step:

β
β: GLM Gamma con link log

k
k: fijo o estimado con Newton

📌 Misma lógica, distinta distribución.

6️⃣ Regularización (crítica en la práctica)
Sin regularización:

β
β puede explotar

Especialmente si hay features raras o colineales

🔹 Penalización típica
β
∼
N
(
0
,
σ
2
I
)
β∼N(0,σ 
2
 I)
Equivalente a:

Ridge (L2)

MAP en versión bayesiana

📌 Muy recomendable en producción.

7️⃣ Identificabilidad (qué se arregla y qué no)
✔️ Lo que mejora
HCPs exclusivos ya no “absorben” arbitrariamente

Productividades están ancladas a 
X
h
X 
h
​
 

Generaliza a HCPs nuevos

❌ Lo que sigue siendo cierto
Attribution ≠ causalidad

Si dos HCPs tienen 
X
X casi idéntico y siempre co-ocurren, no se distinguen

8️⃣ ¿Qué pasa cuando un HCP está en muchos bricks?
Esto es bueno, no malo.

Aparece en muchas ecuaciones:

y
b
≈
∑
h
exp
⁡
(
X
h
β
)
w
h
,
b
y 
b
​
 ≈ 
h
∑
​
 exp(X 
h
​
 β)w 
h,b
​
 
El modelo lo usa como ancla

Reduce varianza de 
β
β

📌 En la práctica:

HCPs “centrales” estabilizan el modelo

HCPs raros se benefician del pooling

9️⃣ ✔️ SALIDA — Modelo listo para datos reales
Modelo final (unidades)
z
h
,
b
∼
Poisson
(
exp
⁡
(
X
h
β
)
 
w
h
,
b
)
y
b
=
∑
h
∈
b
z
h
,
b
z 
h,b
​
 
y 
b
​
 
​
  
∼Poisson(exp(X 
h
​
 β)w 
h,b
​
 )
= 
h∈b
∑
​
 z 
h,b
​
 
​
 
​
 
con:

EM para inferencia

GLM en el M-step

Regularización opcional

🔚 Lectura de negocio (muy importante)
“Estamos estimando un modelo probabilístico de generación de ventas,
usando información observable del HCP,
y la attribution es la mejor explicación consistente con ese modelo.”

✅ Checkpoint final del capítulo
¿Te parece este modelo:

suficientemente realista?

defendible ante negocio y tech?

alineado con lo que podrías llevar a producción?

Si confirmas, el siguiente paso natural es:

👉 Capítulo 6 — Generación de datos mock + evaluación
(donde simulamos ground truth y vemos si EM lo recupera).

Tú dijiste:
adelante Capítulo 6 — Mock data generation

Simulación realista:

HCPs con especialidad, visitas, seniority

Bricks con composición heterogénea

Ground truth conocido

Cómo evaluar si EM recupera la verdad

✔️ Salida: dataset sintético reutilizable
Data Science Mentor dijo:
📘 Capítulo 6 — Mock data generation (reutilizable y realista)
La idea es generar un mundo sintético donde conocemos la verdad:

Features por HCP 
X
h
X 
h
​
 

Parámetros “reales” 
β
\*
β 
\*
 

Contribuciones latentes reales 
z
h
,
b
\*
z 
h,b
\*
​
 

Ventas observadas por brick 
y
b
y 
b
​
 

Así luego podemos medir si EM recupera:

β
\*
β 
\*
  (productividad estructural)

z
h
,
b
\*
z 
h,b
\*
​
  (atribución)

y
b
y 
b
​
  (consistencia y calibración)

1️⃣ Diseño de simulación (qué queremos que sea realista)
HCPs
Especialidad (categoría): GP / Cardio / Endo / …

Seniority (numérica o ordinal)

Visitas (conteo; y pueden variar por brick)

Opcional: “potencial” (continua), “segmento” (A/B/C)

Bricks
Composición heterogénea:

bricks “densos” con muchos HCPs

bricks “pequeños” con pocos HCPs

overlaps: un HCP puede estar en varios bricks

Exposición 
w
h
,
b
w 
h,b
​
 :

0 si no pertenece

si pertenece: proporcional a visitas u otro proxy

Verdadera productividad
Unidades (Poisson):

λ
h
\*
=
exp
⁡
(
X
h
β
\*
)
λ 
h
\*
​
 =exp(X 
h
​
 β 
\*
 )
Luego:

z
h
,
b
\*
∼
Poisson
(
λ
h
\*
 
w
h
,
b
)
;
y
b
=
∑
h
z
h
,
b
\*
z 
h,b
\*
​
 ∼Poisson(λ 
h
\*
​
 w 
h,b
​
 );y 
b
​
 = 
h
∑
​
 z 
h,b
\*
​
 
2️⃣ Código Python: generador reutilizable (unidades / Poisson)
Esto te deja un dataset listo para: entrenar EM, comparar contra ground truth, y hacer stress tests.

import numpy as np
import pandas as pd

def simulate_hcp_brick_poisson(
    n_hcps=400,
    n_bricks=80,
    avg_bricks_per_hcp=2.5,
    avg_hcps_per_brick=18,
    seed=7,
):
    rng = np.random.default_rng(seed)

    # ----- (A) HCP features -----
    specialties = np.array(["GP", "CARDIO", "ENDO", "ONCO", "PULMO"])
    spec = rng.choice(specialties, size=n_hcps, p=[0.45, 0.18, 0.15, 0.12, 0.10])

    seniority = rng.integers(0, 21, size=n_hcps)  # years (0..20)
    potential = rng.lognormal(mean=0.0, sigma=0.6, size=n_hcps)  # positive continuous

    # One-hot for specialty
    spec_df = pd.get_dummies(spec, prefix="spec")
    X = np.column_stack([
        np.ones(n_hcps),                         # intercept
        seniority / 10.0,                        # scaled
        np.log1p(potential),                     # log feature
        spec_df.to_numpy(),                      # dummies
    ])
    feature_names = (["intercept", "seniority_x0.1", "log1p_potential"]
                     + list(spec_df.columns))

    p = X.shape[1]

    # ----- (B) True beta* (ground truth) -----
    beta_true = np.zeros(p)
    beta_true[0] = -0.3                    # intercept
    beta_true[1] =  0.20                   # seniority helps
    beta_true[2] =  0.55                   # potential helps

    # Specialty effects (relative to baseline; here baseline is implicitly captured by intercept)
    # Put mild lifts / penalties
    for j, name in enumerate(feature_names):
        if name == "spec_CARDIO":
            beta_true[j] = 0.25
        elif name == "spec_ONCO":
            beta_true[j] = 0.35
        elif name == "spec_PULMO":
            beta_true[j] = 0.10
        elif name == "spec_ENDO":
            beta_true[j] = 0.15
        # GP left at 0 shift (reference-ish), though with full one-hot it's not a strict reference.
    # (With full one-hot + intercept, there is collinearity; in practice you drop one dummy.
    # For simulation it's fine; for fitting, use a reference category or regularize.)

    # True productivity per HCP
    lambda_true = np.exp(X @ beta_true)

    # ----- (C) Brick membership + exposure w_{h,b} -----
    # Goal: heterogeneous bricks + overlaps.
    # We'll assign each HCP to K bricks, K ~ Poisson(avg_bricks_per_hcp) truncated >=1
    K = rng.poisson(lam=avg_bricks_per_hcp, size=n_hcps)
    K = np.clip(K, 1, max(1, n_bricks // 2))

    # Popularity of bricks (some bricks are "bigger")
    brick_pop = rng.lognormal(mean=0.0, sigma=0.7, size=n_bricks)
    brick_pop = brick_pop / brick_pop.sum()

    # Build sparse membership list
    rows = []
    for h in range(n_hcps):
        bricks_h = rng.choice(n_bricks, size=K[h], replace=False, p=brick_pop)
        # visits per (h,b): more variable, depends on seniority & random
        # visits = base + seniority effect + noise, then clipped >=0
        base = rng.poisson(lam=2.5)  # baseline
        for b in bricks_h:
            visits = base + rng.poisson(lam=0.15 * seniority[h] + 1.0)
            # exposure: use visits directly (or normalized variant)
            w_hb = float(visits)
            if w_hb == 0:
                w_hb = 0.5  # keep small exposure if assigned (optional)
            rows.append((h, b, visits, w_hb))

    hb = pd.DataFrame(rows, columns=["hcp_id", "brick_id", "visits", "w"])

    # Make bricks heterogeneous: optionally drop/keep to target avg_hcps_per_brick
    # We'll just report achieved distribution; simulation already creates variation.

    # ----- (D) Generate latent z* and observed y -----
    # z_{h,b} ~ Poisson(lambda_h * w_{h,b})
    mu = lambda_true[hb["hcp_id"].to_numpy()] * hb["w"].to_numpy()
    z_true = rng.poisson(lam=mu)

    hb["z_true"] = z_true

    # Aggregate observed sales by brick
    y_by_brick = hb.groupby("brick_id")["z_true"].sum().rename("y").reset_index()

    # Pack HCP table
    hcp = pd.DataFrame({
        "hcp_id": np.arange(n_hcps),
        "specialty": spec,
        "seniority": seniority,
        "potential": potential,
        "lambda_true": lambda_true,
    })
    for j, nm in enumerate(feature_names):
        hcp[nm] = X[:, j]

    meta = {
        "feature_names": feature_names,
        "beta_true": beta_true,
        "n_hcps": n_hcps,
        "n_bricks": n_bricks,
    }

    return hcp, hb, y_by_brick, meta


# Example usage
hcp_df, hb_df, y_df, meta = simulate_hcp_brick_poisson(seed=42)
print(hcp_df.head())
print(hb_df.head())
print(y_df.head())
print("beta_true:", meta["beta_true"])
Qué te devuelve
hcp_df: tabla HCP con features y lambda_true

hb_df: tabla de relaciones HCP–brick con w, visits, y ground truth z_true

y_df: ventas observadas por brick (lo único que normalmente tendrías)

meta: beta_true y nombres de features

3️⃣ Variantes útiles (para stress testing)
Puedes hacer el mundo más “real” con:

Overdispersion (si Poisson se queda corto):

usar Negative Binomial para 
z
h
,
b
z 
h,b
​
 

Zero inflation:

con probabilidad 
p
p, 
z
h
,
b
=
0
z 
h,b
​
 =0

Brick effects:

añadir un factor por brick 
a
b
a 
b
​
 : 
μ
h
,
b
=
λ
h
w
h
,
b
a
b
μ 
h,b
​
 =λ 
h
​
 w 
h,b
​
 a 
b
​
 

Dependencia en visitas:

que visitas dependan de especialidad o potencial

(Esto lo podemos añadir después si quieres testear robustez.)

4️⃣ ¿Cómo evaluar si EM “recupera la verdad”?
Cuando entrenes EM con solo 
y
b
y 
b
​
 , 
w
h
,
b
w 
h,b
​
  y 
X
h
X 
h
​
 , podrás comparar:

A) Recuperación de parámetros (si usas features)
Error en 
β
β:

RMSE: 
∥
β
^
−
β
\*
∥
∥ 
β
^
​
 −β 
\*
 ∥

o correlación entre 
X
β
^
X 
β
^
​
  y 
X
β
\*
Xβ 
\*
 

Recomendación práctica: comparar la productividad en escala log:

comparar 
η
h
=
X
h
β
η 
h
​
 =X 
h
​
 β (log-rate), suele ser más estable.

B) Recuperación de atribución
Comparas matrices (en formato long) entre:

z
h
,
b
\*
z 
h,b
\*
​
  vs 
z
^
h
,
b
=
E
[
z
h
,
b
∣
y
,
β
^
]
z
^
  
h,b
​
 =E[z 
h,b
​
 ∣y, 
β
^
​
 ]

Métricas típicas:

Correlación por (h,b)

RMSE por (h,b)

Error relativo por brick (aunque por construcción debería sumar bien)

C) Chequeos de calibración (must-have)
Por brick: 
∑
h
z
^
h
,
b
=
y
b
∑ 
h
​
  
z
^
  
h,b
​
 =y 
b
​
  (debe cumplirse numéricamente)

Distribución de residuales (si introduces overdispersion)

D) Métricas de likelihood
Log-likelihood observada:

∑
b
log
⁡
Poisson
(
y
b
∣
∑
h
λ
^
h
w
h
,
b
)
b
∑
​
 logPoisson(y 
b
​
 ∣ 
h
∑
​
  
λ
^
  
h
​
 w 
h,b
​
 )
Monitorizar que EM la no disminuye por iteración (sanity check)

5️⃣ Nota: versión “euros” (Gamma) en mock data
Si quieres simular euros:

genera 
z
h
,
b
z 
h,b
​
  Gamma con media proporcional a 
θ
h
w
h
,
b
θ 
h
​
 w 
h,b
​
 

suma por brick para obtener 
y
b
y 
b
​
 

La evaluación es igual, pero:

compara en escala log o con métricas robustas (outliers pesan más).

✅ Checkpoint
¿Te parece bien que usemos exactamente este generador como base del curso?

Si sí, pasamos al Capítulo 7 — Implementación completa en Python del EM usando estos mock data, incluyendo:

inicialización

E-step vectorizado

M-step como Poisson GLM con offset + regularización

criterios de convergencia

y evaluación contra z_true y beta_true.

Tú dijiste:
explica cada columna de hcp_df
Data Science Mentor dijo:
Perfecto — vamos columna por columna, con significado estadístico y rol en el modelo.
Me centraré en hcp_df, que representa el nivel HCP (unidad individual).

📊 hcp_df — explicación detallada de cada columna
hcp_df contiene una fila por HCP.
Conceptualmente mezcla datos observables + verdad simulada (solo para evaluación).

🆔 Identificación
hcp_id
Identificador único del HCP

Tipo: entero

Uso:

Clave para unir con hb_df

Nunca entra directamente al modelo

🧠 Variables “reales” (observables en la vida real)
Estas son las features que sí existirían en producción.

specialty
Tipo: categórica (GP, CARDIO, ENDO, ONCO, PULMO)

Significado:

Especialidad médica del HCP

Uso:

Se transforma a one-hot (ver columnas spec_*)

Captura diferencias estructurales de productividad

📌 En el modelo:

Diferentes especialidades → diferente productividad esperada

seniority
Tipo: entero (0–20)

Significado:

Años de experiencia del HCP

Uso:

Feature numérica

Se escala (seniority / 10) para estabilidad numérica

📌 Interpretación:

Cada +10 años de seniority multiplica la tasa por exp(β_seniority)

potential
Tipo: continuo positivo (lognormal)

Significado:

Proxy de “potencial comercial” del HCP

Uso:

Se transforma como log1p(potential)

Reduce skew y hace la relación más lineal en log-space

📌 Interpretación:

HCPs con mayor potencial generan más ventas esperadas

🧮 Variables de diseño (matriz 
X
h
X 
h
​
 )
Estas columnas sí entran directamente en:

λ
h
=
exp
⁡
(
X
h
β
)
λ 
h
​
 =exp(X 
h
​
 β)
intercept
Siempre vale 1

Significado:

Nivel base de productividad

Uso:

Captura la tasa media cuando todas las demás features son 0

📌 Sin intercept:

el modelo estaría forzado a pasar por el origen

mala idea en Poisson / Gamma

seniority_x0.1
Definición: seniority / 10

Tipo: continuo

Significado:

Versión escalada de seniority

Uso:

Mejora convergencia del GLM

Hace β más interpretable

📌 Interpretación de β:

+0.2 ⇒ +10 años → ~+22% en tasa (exp(0.2))

log1p_potential
Definición: log(1 + potential)

Tipo: continuo

Significado:

Transformación suave del potencial

Uso:

Evita que outliers dominen el ajuste

📌 Interpretación:

Relación multiplicativa y estable con la productividad

spec_GP, spec_CARDIO, spec_ENDO, spec_ONCO, spec_PULMO
Tipo: binarias (0/1)

Significado:

One-hot encoding de la especialidad

Uso:

Permite efectos específicos por especialidad

⚠️ Nota técnica importante:

Con intercept + todas las dummies hay colinealidad perfecta

En producción harías una de estas:

eliminar una dummy (categoría de referencia)

o usar regularización (ridge)

En la simulación se tolera porque:

queremos control total del ground truth

EM + ridge lo maneja bien

📌 Interpretación:

β positivo ⇒ esa especialidad es más productiva que la media

🔮 Variables de “ground truth” (NO observables en la vida real)
Estas columnas solo existen para evaluación del método.

lambda_true
Tipo: continuo positivo

Definición:

λ
h
\*
=
exp
⁡
(
X
h
β
\*
)
λ 
h
\*
​
 =exp(X 
h
​
 β 
\*
 )
Significado:

Productividad real subyacente del HCP

Uso:

Comparar con 
λ
^
h
λ
^
  
h
​
  estimado por EM

Diagnóstico de sesgo / varianza

📌 Nunca estaría disponible en datos reales.

🧩 Resumen por niveles
🔹 Observables reales
Columna	Uso
hcp_id	Identificación
specialty	Feature categórica
seniority	Feature numérica
potential	Feature numérica
🔹 Diseño del modelo
Columna	Entra en 
X
h
X 
h
​
 ?
intercept	✔️
seniority_x0.1	✔️
log1p_potential	✔️
spec_*	✔️
🔹 Solo para evaluación
Columna	En producción
lambda_true	❌
🧠 Lectura mental correcta
hcp_df define quién es el HCP y qué esperamos de él en promedio.
El EM no aprende ventas por HCP directamente,
aprende cómo esas features explican ventas agregadas por brick.

✅ Checkpoint
¿Quieres que hagamos lo mismo ahora con:

hb_df (HCP–brick, exposiciones y z_true)

o y_df (ventas observadas por brick)

o pasamos ya a Capítulo 7 — Implementación completa del EM en Python?

Tú dijiste:
si, haz lo mismo con las otras
Data Science Mentor dijo:
Perfecto. Vamos igual de sistemático con las otras dos tablas.
Primero hb_df (nivel HCP–Brick), luego y_df (nivel Brick).

📊 hb_df — tabla HCP–Brick (el corazón del problema)
hb_df está en formato long y representa una relación HCP–Brick.
Aquí viven las variables latentes y la exposición.

🆔 Identificación y joins
hcp_id
Identificador del HCP

FK hacia hcp_df.hcp_id

Uso:

unir features 
X
h
X 
h
​
 

agrupar resultados por HCP

brick_id
Identificador del brick

FK hacia y_df.brick_id

Uso:

agrupar ventas observadas

definir los conjuntos 
H
b
H 
b
​
 

📈 Variables de exposición (observables reales)
Estas columnas sí existirían en producción.

visits
Tipo: entero ≥ 0

Significado:

Número de visitas del HCP al brick

Uso:

Proxy de oportunidad / esfuerzo

Puede entrar:

directamente como w_{h,b}

o como feature adicional en 
X
h
X 
h
​
  o a nivel interacción

📌 Intuición:

A más visitas → mayor exposición → más ventas esperadas

w
Tipo: continuo positivo

Significado:

Exposición efectiva del HCP 
h
h en el brick 
b
b

Uso en el modelo:

z
h
,
b
∼
Poisson
(
λ
h
 
w
h
,
b
)
z 
h,b
​
 ∼Poisson(λ 
h
​
 w 
h,b
​
 )
En la simulación:

w ≈ visits

Con un pequeño floor para evitar ceros

📌 En producción:

w puede ser:

visitas

share de territorio

tiempo dedicado

combinación ponderada

👻 Variables latentes (ground truth solo para evaluación)
z_true
Tipo: entero ≥ 0

Significado:

Ventas reales atribuibles al HCP 
h
h en el brick 
b
b

Generación:

z
h
,
b
\*
∼
Poisson
(
λ
h
\*
w
h
,
b
)
z 
h,b
\*
​
 ∼Poisson(λ 
h
\*
​
 w 
h,b
​
 )
📌 En datos reales:

❌ nunca observable

✔️ es lo que EM intenta recuperar en esperanza

🧠 Rol conceptual de hb_df
Esta tabla:

Define quién compite con quién dentro de cada brick

Define las restricciones estructurales:

y
b
=
∑
h
∈
H
b
z
h
,
b
y 
b
​
 = 
h∈H 
b
​
 
∑
​
 z 
h,b
​
 
Es donde vive el E-step

🧩 Resumen hb_df
Columna	Nivel	En producción	Rol
hcp_id	ID	✔️	Join
brick_id	ID	✔️	Join
visits	Observada	✔️	Proxy esfuerzo
w	Observada	✔️	Exposición en el modelo
z_true	Latente	❌	Ground truth
📊 y_df — tabla de ventas por Brick
y_df representa exactamente lo que tienes en la vida real.

🆔 Identificación
brick_id
Identificador único del brick

Uso:

define la unidad de observación

join con hb_df

💰 Variable objetivo observada
y
Tipo: entero ≥ 0

Significado:

Ventas totales del brick

Definición:

y
b
=
∑
h
∈
H
b
z
h
,
b
y 
b
​
 = 
h∈H 
b
​
 
∑
​
 z 
h,b
​
 
📌 Este es el único target real del problema.

🧠 Rol conceptual de y_df
Es la likelihood observada

EM intenta explicar estos 
y
b
y 
b
​
  usando:

estructura de bricks (hb_df)

productividad HCP (hcp_df)

No hay labels por HCP → problema inverso

🧩 Resumen y_df
Columna	En producción	Rol
brick_id	✔️	Identificador
y	✔️	Ventas agregadas
🔗 Cómo encajan las 3 tablas (lectura final)
hcp_df   →  define λ_h = exp(X_h β)
   ↓
hb_df    →  define dónde y cuánto se expone cada HCP (w_{h,b})
   ↓
y_df     →  observa solo la suma por brick
EM hace:

E-step: trabaja en hb_df (estima ẑ)

M-step: trabaja en hcp_df (actualiza β)

Likelihood: vive en y_df

✅ Checkpoint final
Con esto ya tienes:

modelo teórico ✔️

datos mock ✔️

interpretación de cada columna ✔️

Si quieres, el siguiente paso natural es:

👉 Capítulo 7 — Implementación completa del EM en Python,
donde entrenamos el modelo con estos datos y medimos si recupera beta_true y z_true.

Tú dijiste:
Adelante Capítulo 7 — Implementación completa en Python

Código EM desde cero (no sklearn)

Vectorización

Convergencia y criterios de parada

Debugging típico de EM

✔️ Salida: notebook funcional end-to-end
Data Science Mentor dijo:

Pensó durante 23s

Pensó durante 4 segundos

Pensó durante 15s
Aquí tienes el Capítulo 7 con una implementación EM desde cero en Python (sin sklearn), E-step vectorizado, M-step con IRLS (Poisson GLM con offset) + ridge, y un bloque de debugging típico.

Download the notebook

Qué incluye el notebook (end-to-end)
Generación de datos mock (hcp_df, hb_df, y_df) con beta_true, lambda_true, z_true

EM completo:

E-step vectorizado con np.bincount

M-step: Poisson GLM con link log y offset log(w_tilde) implementado con IRLS + ridge

Convergencia: trazado de log-likelihood observada por iteración + criterio de parada por cambio relativo en beta

Evaluación contra ground truth:

correlación y RMSE en η = Xβ (más estable que comparar β directo si hay colinealidad)

correlación y RMSE en z_true vs zhat

check duro: por brick, sum_h zhat_{h,b} == y_b

Puntos clave de implementación (por si quieres leerlo rápido)
E-step vectorizado (la parte crítica)
En cada relación (fila) HCP–brick:

num[r] = lambda_h[h[r]] * w[r]

den[b] = sum_{r: b[r]=b} num[r]

zhat[r] = y[b[r]] * num[r] / den[b[r]]

Esto garantiza automáticamente:

∑
h
∈
b
z
^
h
,
b
=
y
b
h∈b
∑
​
  
z
^
  
h,b
​
 =y 
b
​
 
M-step como GLM con offset
Construyes:

y_tilde[h] = sum_b zhat[h,b]

w_tilde[h] = sum_b w[h,b]

Ajustas:

y
~
h
∼
Poisson
(
exp
⁡
(
X
h
β
+
log
⁡
w
~
h
)
)
y
~
​
  
h
​
 ∼Poisson(exp(X 
h
​
 β+log 
w
~
  
h
​
 ))
con IRLS y ridge.

Debugging típico (lo más útil en producción)
Check #1: max |sum_h zhat - y| por brick debe ser ~1e-9

Check #2: no debe haber bricks con den[b]=0 (normalmente bricks sin HCPs o w=0)

Check #3: si tienes intercept + todas las dummies, usa ridge (el notebook lo hace)

Check #4: si exp(Xβ) explota, sube ridge o estandariza/clipea η

✅ Checkpoint: si lo abres y lo ejecutas, deberías ver:

log-likelihood creciendo y estabilizando

suma por brick consistente

correlaciones razonables z_true vs zhat y η_true vs η_hat

Cuando me digas “OK”, pasamos al Capítulo 8 — Unidades vs Euros (Poisson vs Gamma/Lognormal). 

Tú dijiste:
antes de pasar  al capítulo 8 me gustaría aplicar EM a otro caso de uso: 

- Tenemos un MMM en granularidad tiempo (semanal, diaria) o tiempo (semanal, diaria) x geo
- Por lo tanto, tenemos por medio la evolucion tiempo o tiempo x geo de su contribución
- Queremos repartir las contribuciones a niveles inferiores: por ejemplo campañas o creatividades o los que tú quieras considerar. O sea, queremos hacer Multi Touch Attribution (MTA)
- A resolver: aplicar EM para repartir como hemos dicho las contribuciones de los medios
- Para más adelante: en MTA suelen quererse las atribuciones con granularidades temporales mucho mayores (horarias, por ejemplo). Quedaría ver cómo resolver eso

Necesitas algo más antes de empezar? Podría ser un nuevo capítulo que se proponga como ejercicio a resolver aunque se proporcionesn las soluciones
Data Science Mentor dijo:
No necesito nada más para empezar — tu planteamiento es suficientemente concreto. Sí: lo podemos tratar como un capítulo extra / ejercicio guiado (con solución), porque es el mismo patrón “agregado → desagregado” pero ahora en tiempo (y quizá geo) y con “componentes” tipo campaña/creatividad.

A continuación te propongo el Capítulo 8 (alternativo) como ejercicio resuelto: EM para desagregar contribuciones de MMM a MTA.

Capítulo extra — EM para repartir contribuciones de MMM a campañas/creatividades (MTA)
0) Qué es observado y qué es latente
Observado (sale del MMM)
Tienes para cada periodo (y opcionalmente geo):

t
∈
{
1
,
…
,
T
}
t∈{1,…,T} (semana/día)

g
∈
{
1
,
…
,
G
}
g∈{1,…,G} (geo) opcional

Y del MMM obtienes contribuciones por canal/medio:

C
m
,
t
C 
m,t
​
  o 
C
m
,
t
,
g
C 
m,t,g
​
 : contribución del medio/canal 
m
m en ese corte.

Nota: esto puede ser “incremental contribution” del MMM o “attributed contribution” según el modelo. EM solo lo toma como “total a repartir”.

Objetivo
Repartir esa contribución de cada medio 
m
m hacia unidades inferiores:

campañas 
k
k, creatividades, adsets, publishers… (lo que definas)

Latente
z
m
,
k
,
t
z 
m,k,t
​
  (o 
z
m
,
k
,
t
,
g
z 
m,k,t,g
​
 ): contribución del medio 
m
m en 
t
t asignada a campaña/crea 
k
k

Restricción dura:

∑
k
∈
K
m
z
m
,
k
,
t
=
C
m
,
t
(
o 
∑
k
z
m
,
k
,
t
,
g
=
C
m
,
t
,
g
)
k∈K 
m
​
 
∑
​
 z 
m,k,t
​
 =C 
m,t
​
 (o  
k
∑
​
 z 
m,k,t,g
​
 =C 
m,t,g
​
 )
1) Modelo generativo base (análogamente al HCP–Brick)
La analogía es directa:

HCP–Brick	MMM→MTA
Brick	(medio 
m
m, tiempo 
t
t, geo 
g
g)
HCP	campaña/creatividad 
k
k dentro del medio
ventas 
y
b
y 
b
​
 	contribución 
C
m
,
t
,
g
C 
m,t,g
​
 
exposición 
w
h
,
b
w 
h,b
​
 	señales a nivel campaña: spend, impressions, clicks, etc.
Exposición / evidencia por campaña
Define features o exposición para cada campaña:

w
m
,
k
,
t
,
g
w 
m,k,t,g
​
  = spend (o impresiones) de la campaña 
k
k del medio 
m
m en 
t
,
g
t,g

y opcionalmente features 
X
m
,
k
X 
m,k
​
  (tipo campaña, objetivo, formato…)

Productividad latente por campaña dentro del medio
Caso simple (sin covariables aún):

λ
m
,
k
>
0
λ 
m,k
​
 >0 (tasa/productividad relativa de campaña 
k
k dentro de medio 
m
m)

Modelo Poisson (para “unidades de contribución”):

z
m
,
k
,
t
,
g
∼
Poisson
(
λ
m
,
k
 
w
m
,
k
,
t
,
g
)
z 
m,k,t,g
​
 ∼Poisson(λ 
m,k
​
 w 
m,k,t,g
​
 )
y observamos:

C
m
,
t
,
g
=
∑
k
z
m
,
k
,
t
,
g
C 
m,t,g
​
 = 
k
∑
​
 z 
m,k,t,g
​
 
Si 
C
C es continua (euros), puedes usar Gamma (más abajo).

2) EM explícito en este contexto (solución)
E-step: repartir 
C
m
,
t
,
g
C 
m,t,g
​
  dentro de cada (m,t,g)
Define:

μ
m
,
k
,
t
,
g
(
r
)
=
λ
m
,
k
(
r
)
 
w
m
,
k
,
t
,
g
μ 
m,k,t,g
(r)
​
 =λ 
m,k
(r)
​
 w 
m,k,t,g
​
 
p
m
,
k
,
t
,
g
(
r
)
=
μ
m
,
k
,
t
,
g
(
r
)
∑
k
′
μ
m
,
k
′
,
t
,
g
(
r
)
p 
m,k,t,g
(r)
​
 = 
∑ 
k 
′
 
​
 μ 
m,k 
′
 ,t,g
(r)
​
 
μ 
m,k,t,g
(r)
​
 
​
 
Entonces:

E
[
z
m
,
k
,
t
,
g
∣
C
m
,
t
,
g
,
λ
(
r
)
]
=
C
m
,
t
,
g
 
p
m
,
k
,
t
,
g
(
r
)
E[z 
m,k,t,g
​
 ∣C 
m,t,g
​
 ,λ 
(r)
 ]=C 
m,t,g
​
 p 
m,k,t,g
(r)
​
 
​
 
Interpretación:

dentro de cada medio-tiempo-geo, la campaña se lleva más contribución si tiene:

más exposición 
w
w y/o

más productividad 
λ
λ.

M-step: actualizar 
λ
m
,
k
λ 
m,k
​
 
Acumulas:

z
~
m
,
k
=
∑
t
,
g
E
[
z
m
,
k
,
t
,
g
]
,
w
~
m
,
k
=
∑
t
,
g
w
m
,
k
,
t
,
g
z
~
  
m,k
​
 = 
t,g
∑
​
 E[z 
m,k,t,g
​
 ], 
w
~
  
m,k
​
 = 
t,g
∑
​
 w 
m,k,t,g
​
 
MLE tipo Poisson:

λ
m
,
k
(
r
+
1
)
=
z
~
m
,
k
w
~
m
,
k
λ 
m,k
(r+1)
​
 = 
w
~
  
m,k
​
 
z
~
  
m,k
​
 
​
 
​
 
Eso ya es EM completo (sin covariables).

3) Versión “realista”: covariables + regularización
Como antes:

λ
m
,
k
=
exp
⁡
(
X
m
,
k
β
m
)
λ 
m,k
​
 =exp(X 
m,k
​
 β 
m
​
 )
β
m
β 
m
​
  puede ser por medio, o compartido

M-step se vuelve un Poisson GLM con offset:

response: 
z
~
m
,
k
z
~
  
m,k
​
 

offset: 
log
⁡
w
~
m
,
k
log 
w
~
  
m,k
​
 

regularización ridge/lasso para estabilidad

4) Caso euros (contribuciones continuas)
Si 
C
m
,
t
,
g
C 
m,t,g
​
  es continua (moneda), Gamma suele funcionar bien:

z
m
,
k
,
t
,
g
∼
Gamma
(
k
,
 
θ
m
,
k
w
m
,
k
,
t
,
g
)
z 
m,k,t,g
​
 ∼Gamma(k, θ 
m,k
​
 w 
m,k,t,g
​
 )
con 
θ
m
,
k
=
exp
⁡
(
X
β
)
θ 
m,k
​
 =exp(Xβ)

En muchas parametrizaciones razonables, el reparto del E-step queda (muy similar):

E
[
z
m
,
k
,
t
,
g
∣
C
m
,
t
,
g
]
≈
C
m
,
t
,
g
⋅
θ
m
,
k
w
m
,
k
,
t
,
g
∑
k
′
θ
m
,
k
′
w
m
,
k
′
,
t
,
g
E[z 
m,k,t,g
​
 ∣C 
m,t,g
​
 ]≈C 
m,t,g
​
 ⋅ 
∑ 
k 
′
 
​
 θ 
m,k 
′
 
​
 w 
m,k 
′
 ,t,g
​
 
θ 
m,k
​
 w 
m,k,t,g
​
 
​
 
y el M-step es Gamma-GLM (log link) + regularización.

5) Qué estás aprendiendo realmente (y límites)
Este EM aprende productividad relativa intra-medio de campañas/creas consistente con:

la serie temporal (y geo) de contribución total del MMM

el patrón de exposición de campañas (spend/imp/clicks)

No está recuperando “verdad causal por campaña” si:

el MMM no está bien identificado por canal

hay campañas altamente colineales dentro del medio

falta señal 
w
w (o está muy ruidosa)

Pero como “desagregador coherente” del MMM, funciona muy bien.

6) Lo de “granularidad horaria” en MTA (para más adelante)
Tu comentario es clave: MMM suele estar en semanal/día; MTA a veces se quiere a hora/minuto.

Hay 3 rutas típicas:

Downscaling con modelo de intensidad
Aprendes un “perfil intradía” 
q
(
h
∣
k
,
g
)
q(h∣k,g) con logs de delivery (imp/click/spend horario) y repartes:

z
m
,
k
,
t
,
g
,
h
=
z
m
,
k
,
t
,
g
⋅
q
(
h
∣
k
,
g
)
z 
m,k,t,g,h
​
 =z 
m,k,t,g
​
 ⋅q(h∣k,g)
Esto es determinista o con EM a dos niveles.

Estado-espacio / smoothing temporal
Tratas 
λ
m
,
k
,
t
λ 
m,k,t
​
  como proceso (random walk) y haces inferencia (Kalman/VI).
Útil si quieres que productividades varíen por hora.

Modelo unificado a alta frecuencia
Solo si tienes outcomes y gasto a esa frecuencia (caro y con mucho ruido).

Ejercicio propuesto (con solución)
Ejercicio: Implementa EM para un solo medio 
m
m con:

C
t
C 
t
​
  semanal

campañas 
k
=
1..
K
k=1..K

exposición 
w
k
,
t
w 
k,t
​
  = spend
y estima 
λ
k
λ 
k
​
  + 
z
k
,
t
z 
k,t
​
 .

Solución: las ecuaciones de arriba (E-step/M-step) y luego extender a covariables con GLM.

¿Quieres que lo aterricemos ya en código?
Puedo darte un notebook muy parecido al del HCP–Brick pero con:

input: C_{m,t,g} (del MMM) + w_{m,k,t,g} (spend/imp/click)

output: zhat_{m,k,t,g} y productividades por campaña

Y con dos modos:

“sin covariables” (updates cerrados)

“con covariables” (M-step con IRLS + ridge)

Si lo hacemos, asumiré por defecto:

contribución 
C
C continua pero no negativa

exposición = spend (>=0), con smoothing cuando hay ceros

Dime solo si quieres que empecemos por:

1 medio, sin geo (más simple), o

1 medio, con geo, o

multi-medio (mismo framework, un loop por medio).

Tú dijiste:
de acuerdo. pero como exposición no quiero spend sino impresiones, grps o similares. Como suponemos que vienen de un mmm incremental (causal), debemos reflejar también el uso de transformaciones adstock + saturación. Antes de empezar a generar el notebook:

1) Si el mmm es incremental (causal) el reparto MTA ¿también lo es?
2) Propón como insertar en la solucion el tema de las transformaciones
Data Science Mentor dijo:
Genial: si quieres usar impresiones/GRPs y además respetar adstock + saturación (como en MMM), eso cambia el “qué significa exposición” en el EM, pero el framework encaja muy bien.

Voy por tus 2 preguntas.

1) Si el MMM es incremental (causal), ¿el reparto MTA también lo es?
Depende de qué entiendas por “causal” a nivel campaña, pero la respuesta operativa es:

El total que repartes (por canal/medio y por 
t
t, 
g
g) sí es incremental/causal si tu MMM lo es.

El reparto dentro del canal (campañas/creas) no es automáticamente causal a menos que tengas identificación causal intra-canal.

Por qué
El MMM “incremental” te identifica algo como:

C
m
,
t
,
g
i
n
c
=
f
(
inputs del canal 
m
)
−
f
(
contrafactual sin canal 
m
)
C 
m,t,g
inc
​
 =f(inputs del canal m)−f(contrafactual sin canal m)
Eso es causal a nivel canal (bajo supuestos).

Pero cuando lo repartes entre campañas, normalmente estás usando:

señales de delivery (impresiones/GRPs, targeting, timing)

y un modelo de “propensión” / “intensidad”
para decidir shares.

Eso da una atribución coherente con el incremental del canal, pero no demuestra que “esa campaña” sea incremental vs otra, porque dentro del canal puede haber:

colinealidad fuerte (campañas corren a la vez)

selección/endogeneidad (las campañas se activan cuando se espera demanda)

distinta mezcla de audiencias

Cómo sí hacerlo “más causal” intra-canal
Necesitarías señal de identificación adicional, por ejemplo:

experimentos / geo-lift por campaña

cambios exógenos (holdouts, rotaciones creativas, shocks de supply)

instrumentos o reglas de asignación

o un modelo jerárquico que incorpore “priors causales” basados en pruebas

📌 Conclusión clara:

MTA por EM puede conservar el “incremental total” del MMM, pero el split intra-canal es principalmente model-based attribution, no causal garantizado.

2) Cómo insertar adstock + saturación en la solución EM (con impresiones/GRPs)
La forma limpia es: no usar exposición cruda 
w
w, sino la exposición efectiva tal y como MMM la usa para generar contribución.

En MMM típico
Para una subentidad 
k
k (campaña/crea) del canal 
m
m, tienes una señal “raw”:

x
m
,
k
,
t
,
g
x 
m,k,t,g
​
 : impresiones / GRPs / TRPs (no spend)

MMM aplica transformaciones:

Adstock (carryover):

a
m
,
k
,
t
,
g
=
Adstock
(
x
m
,
k
,
⋅
,
g
;
θ
m
)
a 
m,k,t,g
​
 =Adstock(x 
m,k,⋅,g
​
 ;θ 
m
​
 )
(p. ej. geométrico con decay 
θ
m
θ 
m
​
 , o Weibull)

Saturación (rendimientos decrecientes):

s
m
,
k
,
t
,
g
=
Sat
(
a
m
,
k
,
t
,
g
;
ϕ
m
)
s 
m,k,t,g
​
 =Sat(a 
m,k,t,g
​
 ;ϕ 
m
​
 )
(p. ej. Hill / logistic)

Y la contribución incremental del canal suele ser algo como:

C
m
,
t
,
g
i
n
c
≈
β
m
∑
k
s
m
,
k
,
t
,
g
C 
m,t,g
inc
​
 ≈β 
m
​
  
k
∑
​
 s 
m,k,t,g
​
 
(si el MMM no tiene campañas explícitas, esto es una descomposición plausible)

Cómo meter esto en EM (dos opciones)
✅ Opción A (recomendada): EM reparte usando exposición efectiva MMM-consistente
Define la exposición del EM como:

w
m
,
k
,
t
,
g
:
=
s
m
,
k
,
t
,
g
w 
m,k,t,g
​
 :=s 
m,k,t,g
​
 
(es decir, ya adstockeada y saturada)

Entonces el E-step (shares) queda:

z
^
m
,
k
,
t
,
g
=
C
m
,
t
,
g
i
n
c
⋅
λ
m
,
k
 
s
m
,
k
,
t
,
g
∑
k
′
λ
m
,
k
′
 
s
m
,
k
′
,
t
,
g
z
^
  
m,k,t,g
​
 =C 
m,t,g
inc
​
 ⋅ 
∑ 
k 
′
 
​
 λ 
m,k 
′
 
​
 s 
m,k 
′
 ,t,g
​
 
λ 
m,k
​
 s 
m,k,t,g
​
 
​
 
Ventajas:

Mantienes exactamente la lógica MMM (carryover + diminishing returns)

Evitas atribuir más a campañas solo por impresiones brutas si están saturadas

Muy estable y fácil de explicar

Qué se aprende:

λ
m
,
k
λ 
m,k
​
  = “eficiencia relativa” intra-canal (sobre señal efectiva)

Dónde pones parámetros de adstock/sat:

Los tomas del MMM (fijos) o los fijas por canal.

Opción B: EM también aprende algunos parámetros de transformación
Puedes extender parámetros 
θ
m
,
ϕ
m
θ 
m
​
 ,ϕ 
m
​
  al set de parámetros y alternar:

E-step: imputar 
z
z

M-step: actualizar 
β
β y quizás 
θ
,
ϕ
θ,ϕ

Pero aquí hay un problema práctico:

adstock/saturación + shares suelen estar muy no convexos

identificabilidad débil (especialmente intra-canal)

entrenamiento más frágil (necesitarías constraints/priors fuertes)

📌 Para empezar y para producción, casi siempre:

usar 
θ
m
,
ϕ
m
θ 
m
​
 ,ϕ 
m
​
  del MMM (fijos) y aprender solo el reparto intra-canal.

¿Y si el MMM está a nivel canal y no tienes series por campaña?
Entonces haces “top-down”:

Construyes 
s
m
,
k
,
t
,
g
s 
m,k,t,g
​
  a partir de delivery de campaña (imps/GRPs) usando los mismos 
θ
m
,
ϕ
m
θ 
m
​
 ,ϕ 
m
​
 

Y repartes 
C
m
,
t
,
g
i
n
c
C 
m,t,g
inc
​
  con la fórmula anterior

Esto es exactamente lo que quieres.

Recomendación final antes del notebook (sin pedirte datos extra)
Para el notebook te propongo este diseño:

Inputs mock:

C
t
C 
t
​
  o 
C
t
,
g
C 
t,g
​
 : contrib incremental por canal (observado)

x
k
,
t
,
g
x 
k,t,g
​
 : impresiones/GRPs por campaña (observado)

Transformaciones:

adstock geométrico por canal

saturación Hill por canal

EM:

E-step usando 
w
=
s
(
x
)
w=s(x)

M-step estimando 
λ
k
λ 
k
​
  (cerrado) o 
λ
k
=
exp
⁡
(
X
k
β
)
λ 
k
​
 =exp(X 
k
​
 β) (GLM)

Y añadimos sección “más adelante”:

desagregación a horas via perfil intradía usando delivery horario + conservación de masa

Checkpoint
Si estás OK con esto:

El total es causal (del MMM), el split intra-canal es attribution model-based.

Usamos adstock+saturación para construir 
w
w y EM reparte sobre esa señal efectiva.

Dime y genero el notebook del caso MMM→MTA con mock data (impresiones/GRPs + transforms).

Tú dijiste:
adelante, genera el notebook
Data Science Mentor dijo:
Listo — aquí tienes el notebook del caso MMM incremental → MTA (campañas/creas) usando impresiones/GRPs como exposición y respetando adstock + saturación (Hill) en el reparto con EM.

Download the notebook

Incluye:

mock data con tiempo x geo

transformaciones adstock geométrico + Hill

generación de contribución incremental por medio (como salida del MMM)

EM cerrado (sin covariables) para estimar productividades intra-medio 
λ
m
,
k
λ 
m,k
​
  y atribuciones 
z
^
m
,
k
,
t
,
g
z
^
  
m,k,t,g
​
 

checks: conservación de masa 
∑
k
z
^
=
C
∑ 
k
​
  
z
^
 =C y evaluación vs ground truth

Cuando lo ejecutes, si quieres, lo siguiente es extender el M-step a 
λ
=
exp
⁡
(
X
β
)
λ=exp(Xβ) (regularización, pooling por tipo de campaña/crea), igual que en el HCP–Brick. 

Tú dijiste:
que covariables has usado (me interesan estos ejemplos para tener referencias
Data Science Mentor dijo:
Muy buena pregunta — y además importante para usar esto como referencia reusable 👍
Te explico exactamente qué covariables he usado, dónde, y por qué, y luego te propongo sets de covariables típicos que sí usarías en producción.

Qué covariables he usado en el notebook (y para qué)
1️⃣ Covariables explícitas en el notebook
✅ A nivel campaña (metadata)
En campaign_df he creado metadata categórica, pero NO la he usado aún en el modelo EM (está preparada para el siguiente paso):

campaign_rows.append({
    "medium": m,
    "campaign": f"{m}_C{k+1}",
    "creative_family": rng.choice(["A", "B", "C"]),
    "objective": rng.choice(["Awareness", "Consideration", "Conversion"]),
})
Estas columnas existen como ejemplo de covariables potenciales, pero en este notebook:

❌ no entran en 
λ
m
,
k
λ 
m,k
​
 

✔️ sirven como plantilla conceptual para el siguiente capítulo:

λ
m
,
k
=
exp
⁡
(
X
m
,
k
β
m
)
λ 
m,k
​
 =exp(X 
m,k
​
 β 
m
​
 )
👉 Es decir: las he definido, pero no las he activado todavía.

✅ A nivel tiempo y geo (implícitas, no paramétricas)
Estas no entran como regresores, pero sí afectan al reparto vía la exposición efectiva:

a) Tiempo (t)
Estacionalidad:

time_season = 1.0 + sinusoides(...)
Adstock aplicado a lo largo del tiempo

Saturación dependiente del histórico

📌 El tiempo entra no como feature, sino como estructura dinámica en w_{m,k,t,g}.

b) Geo
geo_effect multiplicativo

Variabilidad de delivery por geo

📌 Geo tampoco entra como covariable paramétrica, pero modula la exposición efectiva.

2️⃣ La “covariable clave” realmente usada: exposición efectiva
Aunque no parezca una covariable tradicional, esto es lo más importante del notebook:

🔑 Exposición usada en EM
w
m
,
k
,
t
,
g
=
s
m
,
k
,
t
,
g
=
Hill
(
Adstock
(
x
m
,
k
,
t
,
g
)
)
w 
m,k,t,g
​
 =s 
m,k,t,g
​
 =Hill(Adstock(x 
m,k,t,g
​
 ))
Donde:

x
x: impresiones / GRPs

Adstock: memoria temporal

Saturación: rendimientos decrecientes

📌 En la práctica:

la mayor parte de la señal explicativa está en esta transformación, no en 
X
β
Xβ.

3️⃣ Qué NO he usado todavía (a propósito)
No he usado aún:

❌ Regresión Poisson / Gamma en el M-step

❌ 
λ
m
,
k
=
exp
⁡
(
X
β
)
λ 
m,k
​
 =exp(Xβ)

❌ Regularización

❌ Pooling entre campañas similares

Esto es deliberado:

primero dejar claro el EM “puro”

luego meter covariables como extensión controlada

Sets de covariables recomendados (para referencia real)
Ahora sí, lo que te interesa como catálogo de ejemplos 👇

A) Covariables típicas a nivel campaña / creatividad
Estas irían en 
X
m
,
k
X 
m,k
​
 :

🔹 Creatividad / formato
tipo de formato (video, display, search text)

duración (6s / 15s / 30s)

tamaño

orientación (vertical/horizontal)

family / concept creativo

🔹 Objetivo
awareness / consideration / conversion

upper vs lower funnel

always-on vs tactical

🔹 Audiencia / targeting
prospecting vs retargeting

broad vs custom

socio-demo bucket

lookalike depth

👉 Uso típico:

lambda_{m,k} = exp(
  β0
+ β1 * is_video
+ β2 * is_conversion
+ β3 * retargeting
+ β4 * creative_family_B
)
B) Covariables de historial / madurez
(no dependientes de t)

antigüedad de la campaña

nº de flights pasados

frecuencia histórica media

% tiempo activa

Sirven para:

regularizar campañas nuevas

evitar que EM sobre-asigne ruido

C) Covariables interacción con exposición
(avanzado, pero muy potente)

Ejemplo:

creatividades saturan antes que otras

distintos decays por formato

Puedes modelar:

λ
m
,
k
=
exp
⁡
(
X
k
β
)
y/o
γ
m
,
k
=
exp
⁡
(
Z
k
δ
)
λ 
m,k
​
 =exp(X 
k
​
 β)y/oγ 
m,k
​
 =exp(Z 
k
​
 δ)
y usar 
γ
γ para modular la saturación (capítulo avanzado).

D) Covariables a nivel medio (shared priors)
Para evitar sobreajuste:

β
m
∼
N
(
β
g
l
o
b
a
l
,
Σ
)
β 
m
​
 ∼N(β 
global
​
 ,Σ)

Esto es:

pooling jerárquico

muy útil cuando hay muchos medios con pocas campañas

Cómo se vería el siguiente paso (conceptual)
En el siguiente notebook, cambiaríamos solo el M-step:

Antes:

λ
m
,
k
=
∑
t
,
g
z
^
m
,
k
,
t
,
g
∑
t
,
g
w
m
,
k
,
t
,
g
λ 
m,k
​
 = 
∑ 
t,g
​
 w 
m,k,t,g
​
 
∑ 
t,g
​
  
z
^
  
m,k,t,g
​
 
​
 
Después:

λ
m
,
k
=
exp
⁡
(
X
m
,
k
β
m
)
λ 
m,k
​
 =exp(X 
m,k
​
 β 
m
​
 )
y el M-step sería:

Poisson o Gamma GLM

response: 
z
~
m
,
k
z
~
  
m,k
​
 

offset: 
log
⁡
w
~
m
,
k
log 
w
~
  
m,k
​
 

ridge / lasso

Resumen corto (para llevarte)
✔️ Usado realmente:

exposición efectiva = adstock + saturación

tiempo y geo entran estructuralmente

✔️ Definido pero no usado aún:

creative_family, objective (ejemplos de 
X
X)

❌ Aún no:

GLM / regularización / pooling

Si quieres, el próximo capítulo puede ser exactamente:

“Capítulo siguiente — EM + covariables en MMM→MTA (GLM + regularización)”

y ahí usamos esas covariables concretas como referencia industrial.

Tú dijiste:
Antes de continuar, que sw a disposicion publica permite hacer todo esto? Que recomiendas?
Data Science Mentor dijo:
Muy buena pregunta, porque aquí hay mucho marketing y poca claridad en el ecosistema. Te doy una respuesta honesta y accionable, separando qué existe, qué sirve realmente para lo que tú quieres, y qué recomiendo según madurez.

Software público para MMM → MTA con adstock + saturación + EM
TL;DR (ejecutivo)
No existe un software open-source que haga todo lo que hemos modelado (MMM incremental + EM intra-canal con adstock/saturación).

Lo que sí existe:

herramientas muy buenas de MMM

herramientas de MTA heurístico o probabilístico

El puente MMM → MTA vía EM es hoy custom / research-grade.

Mi recomendación: stack híbrido (MMM OSS + capa EM propia).

Ahora vamos con detalle.

1️⃣ Software de MMM (adstock + saturación, incremental)
Estos sí están bien resueltos en open source.

🔹 Meta — Robyn
GitHub: facebookexperimental/Robyn

Lenguaje: R

Qué hace muy bien:

Adstock (geométrico, Weibull)

Saturación (Hill)

MMM incremental con regularización

Decomposition por canal y por tiempo

Qué no hace:

No baja a campañas/creas

No hace MTA intra-canal

📌 Estado: estándar de facto open-source para MMM.

🔹 Google — LightweightMMM
Lenguaje: Python (JAX)

Muy bueno para:

MMM bayesiano

Incertidumbre

Limitaciones:

Menos flexible en descomposición avanzada

No MTA

📌 Bueno si tu equipo es Python-heavy y Bayesian-friendly.

🔹 Uber — Orbit
Time-series causal / structural

No es MMM puro, pero:

útil para incrementalidad y counterfactuals

No resuelve MTA

2️⃣ Software de MTA (pero no MMM-consistente)
Aquí hay mucha confusión.

🔹 Plataformas MTA clásicas (rule-based / probabilísticas)
Ejemplos:

Adobe Attribution IQ

Google Attribution (deprecated / absorbed)

AppsFlyer / Adjust (mobile)

Problemas para tu caso:

❌ No usan MMM incremental

❌ No respetan adstock/saturación

❌ Operan a nivel touchpoint, no a nivel contribución causal

📌 No compatibles con tu planteamiento.

3️⃣ ¿Existe software open-source que haga EM para attribution?
🔹 Spotify — Luigi attribution models
Algunos repos internos/papers con EM y Poisson

No producto mantenido

No MMM-aware

🔹 Paquetes genéricos
pomegranate (Python): EM para mixtures

hmmlearn: HMM

pyro, numpyro: inferencia probabilística

👉 Ninguno viene con:

adstock

saturación

conservación de masa sobre contribuciones MMM

4️⃣ Entonces… ¿qué hacen las empresas “serias”?
🧱 Stack realista (industry best practice)
Capa 1 — MMM (off-the-shelf)
Robyn o LightweightMMM

Output:

C
m
,
t
,
g
i
n
c
C 
m,t,g
inc
​
 

parámetros adstock/sat por canal

Capa 2 — EM intra-canal (custom)
Exactamente lo que hemos construido:

EM Poisson/Gamma

exposición = Hill(Adstock(imps))

reparto top-down

Capa 3 — Downscaling temporal (opcional)
perfiles horarios

conservation of mass

📌 Esto no está empaquetado en ningún OSS hoy.

5️⃣ Recomendación clara (según objetivo)
🔹 Si quieres algo que funcione mañana
MMM: Robyn

MTA: heurístico simple (share de imps adstockeadas)

❌ Pierdes rigor probabilístico

🔹 Si quieres rigor + control (tu caso)
👉 Build propio:

MMM: Robyn / LightweightMMM

MTA: EM como el notebook que ya tienes

Regularización + covariables

Esto es exactamente lo que hacen:

big tech

marketplaces

empresas con equipos de econometría/causal inference

🔹 Si quieres Bayesian end-to-end
MMM bayesiano

Attribution bayesiana jerárquica

Tools: numpyro / pyro

⚠️ Mucho más caro computacionalmente y difícil de explicar a negocio.

6️⃣ Por qué no hay “producto” que haga esto
Honestamente:

cada empresa tiene:

distinta definición de incremental

distinto MMM

distinta granularidad

distintas restricciones legales (privacy)

la atribución intra-canal no es identificable sin supuestos

vendors evitan exponer supuestos “opinables”

👉 Resultado: custom pipelines.

7️⃣ Mi recomendación concreta para ti
Dado tu nivel (senior) y lo que ya has hecho:

Usa Robyn para MMM + mantén una capa EM propia como librería interna.

Ventajas:

transparencia

control metodológico

extensible a nuevos casos (HCPs, MTA, geo, retail…)

Si quieres, el siguiente paso puede ser:

convertir el notebook EM en una mini-lib Python

o diseñar la API conceptual (inputs/outputs) para integrarlo con Robyn

Dime cómo quieres seguir:

Arquitectura end-to-end MMM → MTA

EM + covariables (GLM) en el notebook

Versión bayesiana conceptual

Checklist de riesgos / governance para producción

Tú dijiste:
EM intra-canal (custom): no hay un sklearn o similar para esto?
Data Science Mentor dijo:
No en el sentido “lo enchufas y ya”, como sklearn.GaussianMixture.

Por qué no existe un sklearn para tu EM intra-canal
Tu problema tiene dos cosas muy específicas que sklearn no cubre:

Restricción de conservación de masa por grupo

∑
k
z
m
,
k
,
t
,
g
=
C
m
,
t
,
g
k
∑
​
 z 
m,k,t,g
​
 =C 
m,t,g
​
 
Esto no es el setup típico de supervised learning ni de clustering estándar.

E-step “custom” con responsabilidades condicionadas al total agregado (el “brick” aquí es 
(
m
,
t
,
g
)
(m,t,g)).
Es más cercano a “data augmentation / latent allocation with constraints” que a un estimator estándar.

sklearn está pensado para:

estimadores genéricos (regresión, clasificación)

mixtures clásicos (GaussianMixture) donde observas puntos individuales 
x
i
x 
i
​
 , no totales agregados con suma fija.

Qué puedes reutilizar “estilo sklearn” (sin reinventar todo)
✅ 1) Usar statsmodels para el M-step (GLM)
Si haces la versión:

λ
m
,
k
=
exp
⁡
(
X
m
,
k
β
m
)
λ 
m,k
​
 =exp(X 
m,k
​
 β 
m
​
 )
entonces el M-step es un Poisson/Gamma GLM con offset, y ahí sí puedes usar:

statsmodels.api.GLM(..., family=Poisson())

statsmodels.api.GLM(..., family=Gamma(link=log))

Eso te evita implementar IRLS a mano y te da:

SEs, diagnósticos, etc.

El E-step seguirá siendo tuyo (pero es 20 líneas vectorizadas).

✅ 2) Optimización genérica para M-step
Si no quieres statsmodels:

scipy.optimize.minimize con penalización ridge/lasso

y mantienes E-step vectorizado

✅ 3) Probabilistic programming (si quieres Bayes)
PyMC, Pyro, NumPyro
pero aquí no es “EM”: es inference (NUTS/VI). Potente, más coste/complexidad.

Librerías EM existentes (pero no encajan del todo)
sklearn.mixture.GaussianMixture: EM, pero para Gaussian mixtures sobre datos individuales (no sumas agregadas).

pomegranate: mixtures/HMM con EM, pero no trae tu restricción 
∑
z
=
C
∑z=C.

hmmlearn: HMM EM, irrelevante salvo que modeles temporalidad latente.

Puedes inspirarte en su estructura (fit/predict_proba), pero no te resuelven el core.

Recomendación práctica (lo que suele funcionar en equipos DS)
Construir un estimator “sklearn-like” pequeñito:

fit(C_df, x_df, campaign_features_df)

predict_allocation() → devuelve 
z
^
m
,
k
,
t
,
g
z
^
  
m,k,t,g
​
 

get_params() → devuelve 
λ
^
λ
^
  o 
β
^
β
^
​
 

Internamente:

E-step: numpy vectorizado

M-step: statsmodels.GLM o IRLS propio + ridge

Esto te da:

reproducibilidad

tests (mass conservation, monotonicity, stability)

integración fácil con tu pipeline MMM

Si quieres, el siguiente paso lo puedo hacer directamente: convertir el notebook MMM→MTA en una clase tipo sklearn (MMM2MTAEM) con fit/transform, soportando:

exposición efectiva = adstock+saturación

modo “closed form” (sin covariables)

modo “GLM” (con covariables + regularización)

Tú dijiste:
Creo que no entiendo bien el concepto $\omega_{bh}$, exposición al brick ({0,1}) o peso en el brick ([0,1])
Data Science Mentor dijo:
Muy buena pregunta — y es clave para entender todo el modelo.
La confusión es totalmente normal porque 
ω
b
,
h
ω 
b,h
​
  (o 
w
h
,
b
w 
h,b
​
 ) no es una sola cosa, sino un concepto que puede instanciarse de varias formas coherentes.

Voy paso a paso y al final te dejo una regla mental para no perderte.

Qué es realmente 
ω
b
,
h
ω 
b,h
​
 
En todos los ejemplos (HCP–Brick, MMM→MTA),

ω
b
,
h
(o 
w
h
,
b
)
ω 
b,h
​
 (o w 
h,b
​
 )
significa:

la intensidad de exposición / elegibilidad / oportunidad
que tiene la unidad 
h
h para generar contribución dentro del agregado 
b
b

No es “probabilidad”, no es “share” por sí sola, y no tiene por qué sumar 1.

Las tres interpretaciones válidas de 
ω
b
,
h
ω 
b,h
​
 
1️⃣ Exposición binaria: 
{
0
,
1
}
{0,1} (la más simple)
Definición
ω
b
,
h
=
{
1
si 
h
 pertenece al brick 
b
0
si no
ω 
b,h
​
 ={ 
1
0
​
  
si h pertenece al brick b
si no
​
 
Ejemplo
HCP–Brick:

el HCP trabaja en ese brick → 1

no trabaja → 0

Qué implica el modelo
z
h
,
b
∼
Poisson
(
λ
h
)
z 
h,b
​
 ∼Poisson(λ 
h
​
 )
📌 Aquí toda la diferenciación viene de 
λ
h
λ 
h
​
 .

Cuándo usarlo
Ejemplo didáctico

No tienes info adicional

Quieres entender EM “en limpio”

⚠️ Limitación: poco realista.

2️⃣ Exposición como intensidad 
[
0
,
+
∞
)
[0,+∞) (la más habitual)
Definición
ω
b
,
h
=
cantidad de oportunidad
ω 
b,h
​
 =cantidad de oportunidad
Ejemplos:

nº de visitas del HCP al brick

nº de médicos en ese brick

impresiones / GRPs de una campaña en (t,geo)

spend (aunque tú ya has dicho que no quieres usarlo)

Modelo
z
h
,
b
∼
Poisson
(
λ
h
⋅
ω
b
,
h
)
z 
h,b
​
 ∼Poisson(λ 
h
​
 ⋅ω 
b,h
​
 )
📌 Interpretación:

a igual productividad 
λ
h
λ 
h
​
 , más exposición → más contribución esperada

Importante
ω
ω no tiene por qué estar normalizada

no tiene por qué sumar 1 por brick

puede ser grande (1000 imps) o pequeña (0.2 GRPs)

3️⃣ Peso normalizado 
[
0
,
1
]
[0,1] (caso especial, NO obligatorio)
A veces se define:

ω
~
b
,
h
=
ω
b
,
h
∑
h
′
ω
b
,
h
′
ω
~
  
b,h
​
 = 
∑ 
h 
′
 
​
 ω 
b,h 
′
 
​
 
ω 
b,h
​
 
​
 
Esto no cambia el E-step, porque en el E-step siempre aparece el cociente:

λ
h
ω
b
,
h
∑
h
′
λ
h
′
ω
b
,
h
′
∑ 
h 
′
 
​
 λ 
h 
′
 
​
 ω 
b,h 
′
 
​
 
λ 
h
​
 ω 
b,h
​
 
​
 
Si multiplicas todos los 
ω
ω por una constante, se cancela.

Entonces:
Normalizar o no normalizar es irrelevante para el reparto

Sí afecta a la escala de 
λ
h
λ 
h
​
  (pero no a los shares)

📌 Por eso verás implementaciones con 
[
0
,
1
]
[0,1] y otras con valores brutos.

Entonces… ¿qué es 
ω
b
,
h
ω 
b,h
​
  en tu cabeza?
La forma correcta de pensarlo es:

ω
b
,
h
ω 
b,h
​
  = “cuánto puede contribuir 
h
h al brick 
b
b, antes de saber si es bueno o malo”

Luego:

λ
h
λ 
h
​
  = qué tan bueno es 
h
h

ω
b
,
h
ω 
b,h
​
  = cuánta oportunidad tiene

Y EM combina ambos.

Por qué NO es una probabilidad
Errores comunes:

❌ “
ω
ω es el share dentro del brick”
→ No. El share sale del E-step, no es input.

❌ “
ω
ω debe sumar 1”
→ No. Solo importa relativamente dentro del brick.

❌ “
ω
ω es causal”
→ No. Es una señal de exposición, no de efecto.

Ejemplos concretos en tus dos casos
HCP–Brick
Interpretación	
ω
b
,
h
ω 
b,h
​
 
mínima	1 si está, 0 si no
realista	nº visitas
mejor	visitas × tiempo × potencial
MMM → MTA
Señal	
ω
m
,
k
,
t
,
g
ω 
m,k,t,g
​
 
cruda	impresiones / GRPs
mejor	adstock(imps)
MMM-consistente	Hill(adstock(imps))
📌 En este último:

ω
ω ya incorpora carryover y saturación.

Regla mental (la más importante)
Si quitas 
λ
h
λ 
h
​
 , 
ω
b
,
h
ω 
b,h
​
  debe seguir teniendo sentido como “oportunidad de generar contribución”

Si cumple eso, es una buena 
ω
ω.

Cierre
Tu duda es exactamente la correcta, porque:

muchos papers y códigos mezclan estos conceptos sin decirlo

y parece que 
ω
ω “tiene que ser” una cosa concreta

No:
👉 
ω
ω es una elección de modelado, y lo importante es que sea:

no negativa

interpretable

coherente con el proceso real

Si quieres, en el siguiente mensaje podemos:

dibujar el paralelismo exacto HCP–Brick ↔ MMM–MTA con una tabla formal

o ver qué pasa si eliges una 
ω
ω “mala” (ejemplos de fallo del EM)

Tú dijiste:
Si, dibuja el paralelismo exacto HCP–Brick ↔ MMM–MTA con una tabla formal
Data Science Mentor dijo:
Perfecto. Vamos a hacerlo formal, exacto y simétrico, para que puedas usarlo como referencia mental y técnica en cualquier documento o discusión.

Paralelismo exacto: HCP–Brick ↔ MMM–MTA
Piensa que es el mismo modelo con nombres distintos.
La siguiente tabla es isomórfica: cada fila es exactamente el mismo objeto estadístico.

🧩 Tabla formal de equivalencia
Concepto estadístico	HCP–Brick	MMM → MTA
Unidad agregada (observada)	Brick 
b
b	(Medio 
m
m, tiempo 
t
t, geo 
g
g)
Unidad individual (latente)	HCP 
h
h	Campaña / Creatividad 
k
k
Observación agregada	Ventas del brick 
y
b
y 
b
​
 	Contribución incremental 
C
m
,
t
,
g
C 
m,t,g
​
 
Variable latente	
z
h
,
b
z 
h,b
​
 : ventas de 
h
h en 
b
b	
z
m
,
k
,
t
,
g
z 
m,k,t,g
​
 : contribución de 
k
k
Restricción dura	
∑
h
z
h
,
b
=
y
b
∑ 
h
​
 z 
h,b
​
 =y 
b
​
 	
∑
k
z
m
,
k
,
t
,
g
=
C
m
,
t
,
g
∑ 
k
​
 z 
m,k,t,g
​
 =C 
m,t,g
​
 
Productividad	
λ
h
λ 
h
​
 	
λ
m
,
k
λ 
m,k
​
 
Exposición	
ω
b
,
h
ω 
b,h
​
 	
ω
m
,
k
,
t
,
g
ω 
m,k,t,g
​
 
Exposición cruda	pertenencia / visitas	impresiones / GRPs
Exposición efectiva	visitas ponderadas	Hill(Adstock(imps))
Modelo latente	
z
∼
Poisson
(
λ
ω
)
z∼Poisson(λω)	
z
∼
Poisson/Gamma
(
λ
ω
)
z∼Poisson/Gamma(λω)
E-step	reparto dentro del brick	reparto dentro de (m,t,g)
M-step (simple)	
λ
h
=
∑
b
z
^
∑
b
ω
λ 
h
​
 = 
∑ 
b
​
 ω
∑ 
b
​
  
z
^
 
​
 	
λ
m
,
k
=
∑
t
,
g
z
^
∑
t
,
g
ω
λ 
m,k
​
 = 
∑ 
t,g
​
 ω
∑ 
t,g
​
  
z
^
 
​
 
M-step (con features)	
λ
h
=
exp
⁡
(
X
h
β
)
λ 
h
​
 =exp(X 
h
​
 β)	
λ
m
,
k
=
exp
⁡
(
X
m
,
k
β
m
)
λ 
m,k
​
 =exp(X 
m,k
​
 β 
m
​
 )
Interpretación del output	atribución por HCP	atribución por campaña/crea
Naturaleza causal	❌ (atribución)	❌ intra-canal (total sí)
🔁 Misma ecuación central (cambiando nombres)
HCP–Brick
z
^
h
,
b
=
y
b
⋅
λ
h
 
ω
b
,
h
∑
h
′
λ
h
′
 
ω
b
,
h
′
z
^
  
h,b
​
 =y 
b
​
 ⋅ 
∑ 
h 
′
 
​
 λ 
h 
′
 
​
 ω 
b,h 
′
 
​
 
λ 
h
​
 ω 
b,h
​
 
​
 
MMM–MTA
z
^
m
,
k
,
t
,
g
=
C
m
,
t
,
g
⋅
λ
m
,
k
 
ω
m
,
k
,
t
,
g
∑
k
′
λ
m
,
k
′
 
ω
m
,
k
′
,
t
,
g
z
^
  
m,k,t,g
​
 =C 
m,t,g
​
 ⋅ 
∑ 
k 
′
 
​
 λ 
m,k 
′
 
​
 ω 
m,k 
′
 ,t,g
​
 
λ 
m,k
​
 ω 
m,k,t,g
​
 
​
 
👉 Es la misma ecuación.

🎯 Interpretación semántica (muy importante)
Símbolo	Significado universal
z
z	“Quién explica cuánto del total”
y
y / 
C
C	Total observado que debe explicarse
λ
λ	Eficiencia / productividad relativa
ω
ω	Oportunidad / intensidad de exposición
E-step	reparto consistente
M-step	aprendizaje de productividades
🧠 Qué cambia realmente entre los casos
En HCP–Brick
ω
b
,
h
ω 
b,h
​
  suele ser simple

0/1

visitas

el problema es espacial

En MMM–MTA
ω
m
,
k
,
t
,
g
ω 
m,k,t,g
​
  es modelada

adstock

saturación

el problema es temporal + causal top-down

Pero matemáticamente:

son el mismo problema de inferencia con variables latentes y suma fija.

⚠️ Errores comunes que esta tabla evita
❌ “En MMM–MTA es otro modelo”
→ No: es el mismo EM con otra semántica.

❌ “
ω
ω debe sumar 1”
→ No en ninguno de los dos.

❌ “Si MMM es causal, MTA también”
→ El total sí; el reparto no necesariamente.

🧭 Regla de oro final
Si sabes explicar HCP–Brick, sabes explicar MMM–MTA.
Solo cambia qué significa 
ω
ω y qué significa el total observado.

Si quieres, el siguiente paso natural sería:

misma tabla pero para “con covariables”

o ejemplos de malas elecciones de 
ω
ω y cómo rompen el modelo

o cómo explicar esta tabla a negocio en 3 slides

Tú mandas.

Tú dijiste:
Vamos al siguiente capítulo:

Capítulo 8 — Unidades vs Euros

Diferencias conceptuales:

Poisson vs Gamma / Lognormal

Impacto en:

Interpretación

Estabilidad

Sesgo por outliers

Cuándo conviene cada uno

✔️ Salida: guía práctica de model choice

(toca este ahora, verdad?)
Data Science Mentor dijo:
Sí — toca exactamente ahora 👍
Este capítulo es el que evita muchos errores de modelado en producción. Vamos a hacerlo práctico, no académico.

📘 Capítulo 8 — Unidades vs Euros
Poisson vs Gamma / Lognormal

Pregunta central:
¿Qué distribución uso para repartir contribuciones cuando el total observado son unidades vs euros?

1️⃣ Diferencia conceptual clave (la más importante)
🟦 Unidades
Ejemplos:

nº de prescripciones

nº de ventas

nº de conversiones

nº de tickets

👉 Son:

discretas

no negativas

con varianza ≈ media (o mayor)

📌 Modelo natural: Poisson (o NegBin)

🟧 Euros
Ejemplos:

revenue

margin

GMV

contribución monetaria del MMM

👉 Son:

continuas

positivas

heavy-tailed

con outliers estructurales

📌 Modelo natural: Gamma o Lognormal

2️⃣ Qué cambia realmente entre Poisson y Gamma
Aspecto	Poisson (unidades)	Gamma / Lognormal (euros)
Tipo de variable	Discreta	Continua
Soporte	{0,1,2,…}	(0, +∞)
Varianza	≈ media	>> media
Outliers	Poco frecuentes	Comunes
Interpretación	Conteos	Valor monetario
Robustez	Alta	Media / baja
Estabilidad EM	Muy alta	Más delicada
Sensible a escalado	No	Sí
3️⃣ Impacto directo en el EM
🔹 E-step (reparto)
Importante:
👉 El E-step es casi idéntico en los tres casos.

En la práctica:

z
^
h
,
b
=
y
b
⋅
λ
h
ω
b
,
h
∑
h
′
λ
h
′
ω
b
,
h
′
z
^
  
h,b
​
 =y 
b
​
 ⋅ 
∑ 
h 
′
 
​
 λ 
h 
′
 
​
 ω 
b,h 
′
 
​
 
λ 
h
​
 ω 
b,h
​
 
​
 
Poisson → exacto

Gamma → exacto si shape común

Lognormal → aproximado (pero funciona)

📌 El reparto (shares) cambia poco entre modelos.

🔹 M-step (aprendizaje de 
λ
λ)
Aquí sí hay diferencias fuertes.

4️⃣ Poisson (unidades): el caso “feliz”
Modelo
z
h
,
b
∼
Poisson
(
λ
h
ω
b
,
h
)
z 
h,b
​
 ∼Poisson(λ 
h
​
 ω 
b,h
​
 )
M-step cerrado (sin covariables)
λ
h
=
∑
b
z
^
h
,
b
∑
b
ω
b
,
h
λ 
h
​
 = 
∑ 
b
​
 ω 
b,h
​
 
∑ 
b
​
  
z
^
  
h,b
​
 
​
 
​
 
Ventajas
ultra-estable

convexidad

convergencia rápida

fácil de explicar

Riesgos
si hay overdispersion fuerte → subestima varianza

📌 Default recomendado siempre que puedas.

5️⃣ Gamma (euros): el caso realista
Modelo
z
h
,
b
∼
Gamma
(
k
,
 
θ
h
ω
b
,
h
)
z 
h,b
​
 ∼Gamma(k, θ 
h
​
 ω 
b,h
​
 )
(media = 
k
θ
h
ω
kθ 
h
​
 ω)

M-step
θ
h
θ 
h
​
 : GLM Gamma (log link)

k
k: fijo o estimado global

Ventajas
respeta continuidad

maneja colas largas

interpretable en media

Riesgos
sensible a outliers extremos

EM más lento

puede volverse inestable sin regularización

📌 Requiere:

winsorización o trimming

regularización

buen escalado de 
ω
ω

6️⃣ Lognormal (euros): el caso peligroso
Modelo
log
⁡
z
h
,
b
∼
N
(
μ
h
+
log
⁡
ω
b
,
h
,
 
σ
2
)
logz 
h,b
​
 ∼N(μ 
h
​
 +logω 
b,h
​
 , σ 
2
 )
Ventajas
modela muy bien heavy tails

muy común en revenue real

Problemas serios en EM
el reparto depende de 
exp
⁡
(
μ
)
exp(μ)

un outlier puede:

dominar el M-step

“secuestrar” 
λ
λ

no hay M-step cerrado

📌 Solo recomendable si:

haces inferencia bayesiana

o usas strong priors + VI

7️⃣ Sesgo por outliers (ejemplo mental)
Supón:

100 bricks normales

1 brick con revenue 100× mayor

Poisson
ese brick pesa 100×

pero no rompe el modelo

Gamma
ese brick domina el likelihood

λ
λ se ajusta para “explicarlo”

Lognormal
el log ayuda, pero:

el EM puede volverse errático

👉 Esto no es un bug, es matemática.

8️⃣ Cuándo conviene cada uno (guía práctica)
✅ Usa Poisson si:
trabajas con unidades

puedes redefinir euros como:

nº de transacciones × ticket medio

quieres estabilidad y explicabilidad

Recomendación fuerte:
incluso para revenue, intenta modelar unidades primero.

✅ Usa Gamma si:
el negocio exige euros

los outliers están controlados

tienes buena señal en 
ω
ω

aplicas regularización

⚠️ Usa Lognormal solo si:
tienes colas extremas reales

estás cómodo con Bayesian inference

aceptas más complejidad

9️⃣ Regla de oro (muy importante)
El EM reparte masa.
Cuanto más “pesada” sea la cola del total observado,
más cuidado necesitas en el M-step.

10️⃣ Recomendación final (industrial)
En la práctica, equipos maduros hacen:

Modelar unidades con Poisson EM

Convertir a euros post hoc:

z
^
h
,
b
€
=
z
^
h
,
b
u
n
i
t
s
×
ticket medio
z
^
  
h,b
€
​
 = 
z
^
  
h,b
units
​
 ×ticket medio
Usar Gamma solo si el paso 2 no es aceptable

✔️ Salida — Guía de model choice
Caso	Recomendación
Unidades	Poisson (default)
Euros “limpios”	Gamma
Euros con colas extremas	Lognormal (con cautela)
Dudas	Poisson + conversión
Producción crítica	Poisson + regularización
Checkpoint
¿Te encaja esta guía con lo que has visto en datos reales?

El siguiente capítulo natural sería:

Capítulo 9 — Regularización, pooling y priors (cómo evitar que EM se rompa)
o, si prefieres,

Capítulo 9 — Cómo explicar todo esto a negocio sin ecuaciones

Tú dijiste:
adelante Capítulo 9 — Pitfalls reales y extensiones

Identifiability

Overfitting silencioso

Cold start HCPs

EM vs Bayesian Hierarchical Models

Cuándo pasar a variational inference

✔️ Salida: criterio de senior data scientist
Data Science Mentor dijo:
Perfecto. Este es el capítulo que diferencia a alguien que “sabe EM” de alguien que lo puede poner en producción. Voy a ser deliberadamente pragmático y un poco duro: esto es criterio de senior.

📕 Capítulo 9 — Pitfalls reales y extensiones
Criterio de Senior Data Scientist

1️⃣ Identifiability: el problema que nunca desaparece
❓ Qué significa aquí
Un modelo es identificable si los datos contienen suficiente información para distinguir los parámetros.

En EM intra-canal / HCP–Brick:

y
b
=
∑
h
z
h
,
b
,
z
h
,
b
∼
f
(
λ
h
ω
b
,
h
)
y 
b
​
 = 
h
∑
​
 z 
h,b
​
 ,z 
h,b
​
 ∼f(λ 
h
​
 ω 
b,h
​
 )
👉 No todo 
λ
λ es identificable.

🚨 Casos típicos de no-identificabilidad
a) Colinealidad perfecta en 
ω
ω
Ejemplo:

dos campañas siempre activas juntas

mismo perfil temporal y geo

mismas impresiones adstockeadas

Entonces:

λ
1
ω
1
+
λ
2
ω
2
λ 
1
​
 ω 
1
​
 +λ 
2
​
 ω 
2
​
 
no se puede separar.

📌 EM “elige” arbitrariamente.

b) Escala no identificable
Si multiplicas:

λ
h
←
c
λ
h
λ 
h
​
 ←cλ 
h
​
 

ω
b
,
h
←
ω
b
,
h
/
c
ω 
b,h
​
 ←ω 
b,h
​
 /c

👉 El likelihood no cambia.

📌 Solución:

fijar escala de 
ω
ω

normalizar 
λ
λ (media = 1)

usar offsets explícitos

🧠 Criterio senior
Si dos entidades no se diferencian en 
ω
ω a lo largo del dataset, no esperes que EM las diferencie.

2️⃣ Overfitting silencioso (el más peligroso)
Qué lo hace “silencioso”
El likelihood sube

Las métricas internas mejoran

El output parece “razonable”

Pero:

el modelo está explicando ruido

los 
λ
λ son inestables entre runs

Síntomas típicos
λ
λ con varianza enorme

rankings que cambian por seed

campañas nuevas “ganan” sin evidencia

extrema sensibilidad a un brick

Antídotos prácticos
✅ Regularización (no opcional)
ridge / lasso

o priors normales

✅ Pooling jerárquico
λ
h
∼
LogNormal
(
μ
group
,
σ
)
λ 
h
​
 ∼LogNormal(μ 
group
​
 ,σ)
✅ Tests de estabilidad
re-fit con bootstrap temporal

compara rankings

📌 Si no haces esto, EM miente educadamente.

3️⃣ Cold start (HCPs / campañas nuevas)
El problema
Un HCP o campaña con:

poca 
ω
ω

pocos bricks

datos recientes

👉 EM tiende a:

asignarles extremos

o colapsarlos a cero

Soluciones ordenadas por madurez
🟢 Nivel 1 — Heurística
floor en 
ω
ω

shrinkage manual

🟡 Nivel 2 — Covariables
λ
h
=
exp
⁡
(
X
h
β
)
λ 
h
​
 =exp(X 
h
​
 β)
Comparte señal entre entidades similares.

🔵 Nivel 3 — Jerárquico
β
h
∼
N
(
β
group
,
Σ
)
β 
h
​
 ∼N(β 
group
​
 ,Σ)
Regla senior
Si tienes cold start, EM sin pooling es mala idea.

4️⃣ EM vs Bayesian Hierarchical Models (BHM)
Qué hace EM realmente
estima puntos (
λ
^
λ
^
 )

asume máxima verosimilitud

no propaga incertidumbre

Qué hace un BHM
estima distribuciones

hace shrinkage automático

maneja mejor colas y escasez

Comparación honesta
Aspecto	EM	Bayesian Jerárquico
Complejidad	Baja	Alta
Escalabilidad	Muy alta	Media
Interpretabilidad	Alta	Media
Incertidumbre	❌	✅
Cold start	❌	✅
Priors	Implícitos	Explícitos
Debug	Fácil	Difícil
Criterio senior
EM es un excelente baseline productivo.
BHM es para cuando ya sabes exactamente por qué EM falla.

5️⃣ Cuándo pasar a Variational Inference (VI)
Señales claras de que EM ya no basta
🚩 1) Mucha jerarquía
campañas dentro de medios

creatividades dentro de campañas

geos dentro de países

EM se vuelve un Frankenstein.

🚩 2) Incertidumbre importa
decisiones de inversión

intervalos de confianza

risk management

🚩 3) Datos escasos + colas pesadas
revenue extremo

pocos puntos por entidad

Qué te da VI
posteriors aproximados

shrinkage natural

control fino de regularización

Coste
diseño de modelo

tuning

tiempo de cómputo

dificultad de explicación

📌 No es un upgrade trivial, es un cambio de paradigma.

6️⃣ Anti-patterns (cosas que NO hacer)
❌ “EM converge, luego está bien”
❌ “Más features = mejor”
❌ “Si sube el likelihood, es correcto”
❌ “Usar Lognormal porque es revenue”
❌ “Cold start sin pooling”

7️⃣ Checklist de senior antes de producción
Antes de poner EM en prod, pregúntate:

 ¿
ω
ω distingue realmente a las entidades?

 ¿He fijado la escala?

 ¿Hay regularización explícita?

 ¿He probado estabilidad temporal?

 ¿Tengo estrategia para cold start?

 ¿Sé explicar por qué no es causal?

Si fallas 2 o más → no está listo.

8️⃣ Conclusión (criterio real)
EM es un bisturí, no un martillo.
En manos expertas: preciso, rápido, explicable.
En manos inexpertas: elegante y peligrosamente convincente.

✔️ Salida — Criterio de Senior Data Scientist
Usa EM cuando:

el problema es “repartir un total”

tienes buena señal en 
ω
ω

necesitas algo estable y explicable

Pásate a jerárquico / VI cuando:

hay mucha escasez

necesitas incertidumbre

el negocio lo exige

Si quieres, el siguiente (y último) capítulo podría ser:

Capítulo 10 — Cómo explicar EM + MMM + MTA a negocio en 3 slides,
o

Capítulo 10 — Diseño de una librería interna EM para attribution (API + tests)

Tú dijiste:
Me parecwe bien Capítulo 10 — Cómo explicar EM + MMM + MTA a negocio en 3 slides,
Data Science Mentor dijo:
Perfecto. Te lo doy exactamente como lo usaría un senior delante de comité, en 3 slides, con mensajes claros, sin ecuaciones, y con frases defendibles si te preguntan.

🧩 Capítulo 10 — Cómo explicar EM + MMM + MTA a negocio en 3 slides
Objetivo:
Que entiendan qué hacemos, por qué es coherente, y qué NO promete.

🟦 Slide 1 — El problema real (y por qué una sola técnica no basta)
Título
De incrementalidad (MMM) a granularidad (MTA)

Mensaje clave (en lenguaje negocio)
El MMM nos dice cuánto aporta cada canal de forma incremental

Pero el negocio necesita saber qué campañas y creatividades dentro del canal funcionan mejor

No queremos perder el rigor causal del MMM al bajar el nivel de detalle

Visual mental (descríbelo, no lo dibujes)
MMM (canal)
   ↓  total incremental
MTA (campañas / creatividades)
Frase clave (para decir en voz alta)
“El MMM nos da la verdad a nivel canal; el MTA nos da el detalle operativo.
El reto es conectar ambos sin inventarnos ventas.”

🟦 Slide 2 — La solución: reparto coherente y controlado
Título
Repartimos el total incremental de forma consistente

Mensaje clave
Tomamos la contribución incremental del MMM como total fijo

La repartimos entre campañas según:

Exposición real (impresiones / GRPs)

Efectos de memoria y saturación (igual que el MMM)

Eficiencia relativa aprendida de los datos

Qué hace el algoritmo (sin matemáticas)
Cada periodo y región:

el total no cambia

solo cambia cómo se reparte

Las campañas con:

más exposición efectiva

y mejor eficiencia histórica
reciben mayor parte del total

Frase clave
“No creamos ventas nuevas ni quitamos ventas al canal:
solo repartimos lo que ya sabemos que es incremental.”

🟦 Slide 3 — Qué sí es, qué no es (y por qué confiar en ello)
Título
Qué garantiza el método (y qué no promete)

✔️ Lo que SÍ garantiza
El total por canal cuadra exactamente con el MMM

El reparto:

respeta timing, geo y saturación

es estable y reproducible

Es transparente y auditable

⚠️ Lo que NO promete
No prueba causalidad entre campañas dentro del canal

No sustituye experimentos

No es “verdad absoluta”, es la mejor explicación consistente con los datos

Frase final (muy importante)
“Es la forma más rigurosa de bajar de MMM a MTA sin romper la incrementalidad.”

🎯 Cierre para preguntas difíciles (chuleta)
Si te preguntan…

❓ “¿Esto es causal?”
👉

“El total sí, viene del MMM.
El reparto es un modelo explicativo basado en exposición y comportamiento histórico.”

❓ “¿Por qué no usar solo MTA?”
👉

“Porque el MTA solo no distingue correlación de incrementalidad.
Aquí mantenemos ambas cosas separadas.”

❓ “¿Podemos usarlo para optimizar?”
👉

“Sí, como señal comparativa y de priorización,
no como sustituto de experimentos.”

🧠 Regla de oro para negocio (una frase)
MMM decide cuánto invertir por canal.
EM–MTA ayuda a decidir cómo ejecutar dentro del canal.

✔️ Resultado final del curso
Con esto ya tienes:

marco teórico sólido

implementación realista

criterio senior

y un storytelling claro para negocio

Si quieres, el siguiente paso opcional sería:

convertir estas 3 slides en un deck listo para comité

o preparar Q&A defensivo para finance / marketing / legal

Tú dirás.

Tú dijiste:
prepara Q&A defensivo para analytics / finance / marketing / legal
Data Science Mentor dijo:
Perfecto. Te dejo un Q&A defensivo, estructurado por stakeholder, con respuestas cortas, consistentes y defendibles.
Esto está pensado para reuniones duras, no para docencia.

🛡️ Q&A defensivo — EM + MMM + MTA
🧠 ANALYTICS / DATA SCIENCE
❓ “¿Por qué EM y no un modelo bayesiano jerárquico?”
Respuesta corta

EM es más simple, más rápido y suficiente para el nivel de granularidad y estabilidad que necesitamos ahora.

Respuesta técnica

EM maximiza verosimilitud bajo restricciones de masa fija.
El jerárquico lo consideramos cuando necesitamos intervalos de incertidumbre o pooling fuerte por escasez. Hoy no es el cuello de botella.

❓ “¿Cómo sabemos que el modelo es identificable?”
Respuesta

No siempre lo es, y somos explícitos al respecto.
Por eso usamos regularización, normalización de escala y pruebas de estabilidad temporal.

❓ “¿El EM converge al óptimo global?”
Respuesta

No necesariamente, pero el problema es cuasi-convexo con estas restricciones.
Usamos inicializaciones estables y monitorizamos convergencia y sensibilidad.

❓ “¿Qué pasa si dos campañas son idénticas?”
Respuesta

El modelo no puede diferenciarlas, y no lo intenta.
En ese caso el reparto es simétrico o se apoya en priors/covariables.

💰 FINANCE / CONTROLLING
❓ “¿Esto crea o destruye ventas?”
Respuesta clara

No.
El total por canal, periodo y región cuadra exactamente con el MMM.

📌 Frase clave:

“Es una redistribución contable del incremental, no una reestimación.”

❓ “¿Podemos reconciliar esto con P&L?”
Respuesta

Sí.
Las contribuciones agregadas por canal coinciden con las cifras aprobadas del MMM.
El nivel campaña es un desglose interno para optimización.

❓ “¿Qué pasa con outliers de revenue?”
Respuesta

Los controlamos explícitamente:

model choice (Poisson vs Gamma)

winsorización

regularización

No dejamos que un punto extremo domine el modelo.

❓ “¿Esto es suficientemente estable para forecast?”
Respuesta

Para forecast estratégico: usamos MMM.
Para ejecución táctica: el EM es estable a corto plazo, pero no se usa como predictor standalone.

📣 MARKETING / MEDIA
❓ “¿Esto me dice qué campaña funciona mejor?”
Respuesta honesta

Te dice qué campañas explican mejor el incremental del canal, dadas sus impresiones y timing.

📌 Aclara:

No es una prueba causal entre campañas, es una señal comparativa.

❓ “¿Por qué no usar solo MTA clásico?”
Respuesta

Porque el MTA clásico no distingue correlación de incrementalidad.
Aquí partimos de incremental validado y luego bajamos el nivel.

❓ “¿Por qué una campaña con más impresiones no se lleva todo?”
Respuesta

Porque:

hay saturación

hay memoria (adstock)

hay diferencias de eficiencia histórica

Más impresiones no implica más impacto incremental.

❓ “¿Podemos optimizar creatividades con esto?”
Respuesta

Sí, como ranking y priorización, no como verdad absoluta.
Idealmente se combina con tests creativos.

⚖️ LEGAL / COMPLIANCE / PRIVACY
❓ “¿Usa datos personales?”
Respuesta clara

No.
Trabajamos con datos agregados (impresiones, GRPs, contribuciones), sin identificadores individuales.

❓ “¿Es un modelo determinista o automatizado de decisión?”
Respuesta

Es un modelo analítico de apoyo a decisiones humanas.
No ejecuta acciones automáticas ni discrimina individuos.

❓ “¿Cumple con explicabilidad?”
Respuesta

Sí.
El reparto se basa en reglas claras: exposición, memoria, saturación y eficiencia aprendida.

No usamos cajas negras opacas.

❓ “¿Podría inducir sesgos?”
Respuesta

El modelo refleja patrones históricos del delivery.
Por eso se usa como herramienta de análisis, no como único criterio de decisión.

🧾 PREGUNTAS TRANSVERSALES (las más difíciles)
❓ “¿Qué pasa si el MMM está mal?”
Respuesta

El reparto hereda la calidad del MMM.
Por eso el MMM es el componente crítico y está validado por separado.

❓ “¿Cómo sabemos que esto funciona?”
Respuesta

Validamos:

coherencia contable

estabilidad temporal

consistencia con tests conocidos

plausibilidad de negocio

No hay una única métrica mágica.

❓ “¿Podemos auditarlo?”
Respuesta

Sí.
Es un modelo reproducible, versionado y con reglas explícitas.
Cada decisión puede rastrearse.

🧠 Frase de cierre universal (úsala tal cual)
“El MMM decide cuánto invertir por canal.
Este modelo nos ayuda a ejecutar mejor dentro del canal,
sin romper la incrementalidad ni inventar ventas.”

Si quieres, el siguiente paso puede ser:

convertir este Q&A en one-pager para comité

o preparar respuestas técnicas extendidas solo para analytics

o simular una reunión hostil (role-play) y ensayar respuestas 😄

Tú dijiste:
Quiero saber también el planteamiento del enfoque bayesiano jerarquico. La idea es inferir el modelo generativo de las variables latentes mediante inferencia bayesiana en vez de usar MLE, no? O es otra? O hay más cosas? Como se organizarian los datos, como se formularia el modelo, como tratamos las variables latentes, que salidas habría,
Data Science Mentor dijo:
Excelente pregunta. Y muy bien formulada: ya estás en el nivel correcto para pasar de “usar EM” a diseñar modelos.

Voy a responder de forma estructurada y honesta, porque aquí hay varios malentendidos comunes.

Enfoque Bayesiano Jerárquico (BHM) para HCP–Brick / MMM–MTA
Respuesta corta (para alinear conceptos)
👉 Sí, la idea central es:

inferir el modelo generativo completo de las variables latentes mediante inferencia bayesiana, en lugar de estimar puntos vía MLE (EM).

👉 Pero no es solo eso.
El enfoque bayesiano no es EM con priors, sino que:

cambia qué se estima

cambia qué significa el resultado

cambia cómo se controla el overfitting

cambia qué preguntas puedes responder

Vamos por partes.

1️⃣ EM vs Bayesiano: qué cambia realmente
EM (lo que ya conoces)
Asume un modelo generativo

Trata 
z
z como latente

Optimiza:

θ
^
=
arg
⁡
max
⁡
θ
p
(
y
∣
θ
)
θ
^
 =arg 
θ
max
​
 p(y∣θ)
Resultado:

estimaciones puntuales (
λ
^
λ
^
 , 
β
^
β
^
​
 )

asignación esperada 
E
[
z
∣
y
,
θ
^
]
E[z∣y, 
θ
^
 ]

👉 No hay incertidumbre explícita.

Bayesiano jerárquico
Define el mismo modelo generativo, pero:

Trata todo como variable aleatoria:

productividades

coeficientes

(a veces) los propios 
z
z

Infiere:

p
(
θ
,
z
∣
y
)
p(θ,z∣y)
👉 Resultado:

distribuciones posteriores, no puntos

shrinkage automático

intervalos creíbles

decisiones basadas en riesgo

2️⃣ El modelo generativo (forma general)
Voy a escribirlo en forma canónica, válida tanto para HCP–Brick como MMM–MTA.

Observado
Agregado:

y
b
o
C
m
,
t
,
g
y 
b
​
 oC 
m,t,g
​
 
Latente
Contribuciones individuales:

z
i
,
b
≥
0
,
∑
i
z
i
,
b
=
y
b
z 
i,b
​
 ≥0, 
i
∑
​
 z 
i,b
​
 =y 
b
​
 
Nivel 1 — Likelihood (idéntico conceptualmente a EM)
Ejemplo Poisson (unidades):

z
i
,
b
∼
Poisson
(
λ
i
ω
b
,
i
)
z 
i,b
​
 ∼Poisson(λ 
i
​
 ω 
b,i
​
 )
o Gamma (euros):

z
i
,
b
∼
Gamma
(
k
,
 
θ
i
ω
b
,
i
)
z 
i,b
​
 ∼Gamma(k, θ 
i
​
 ω 
b,i
​
 )
Y:

y
b
=
∑
i
z
i
,
b
y 
b
​
 = 
i
∑
​
 z 
i,b
​
 
📌 Hasta aquí no hay diferencia conceptual con EM.

3️⃣ Dónde entra lo Bayesiano (la diferencia clave)
Nivel 2 — Productividades jerárquicas
En lugar de:

λ
i
=
exp
⁡
(
X
i
β
)
λ 
i
​
 =exp(X 
i
​
 β)
defines:

β
∼
N
(
0
,
σ
β
2
)
λ
i
∼
LogNormal
(
X
i
β
,
 
σ
λ
2
)
β
λ 
i
​
 
​
  
∼N(0,σ 
β
2
​
 )
∼LogNormal(X 
i
​
 β, σ 
λ
2
​
 )
​
 
o, por grupos:

λ
i
,
g
∼
LogNormal
(
μ
g
,
 
σ
g
)
λ 
i,g
​
 ∼LogNormal(μ 
g
​
 , σ 
g
​
 )
👉 Esto introduce:

pooling

regularización automática

control del cold start

Nivel 3 — Hyperpriors
μ
g
∼
N
(
0
,
1
)
σ
g
∼
HalfNormal
(
0.5
)
μ 
g
​
 ∼N(0,1)σ 
g
​
 ∼HalfNormal(0.5)
📌 Esto evita que el modelo “explote”.

4️⃣ ¿Qué pasa con las variables latentes 
z
z?
Aquí hay dos estrategias.

🔵 Opción A — Integrar 
z
z (más común)
No muestreas 
z
z explícitamente.

Usas la propiedad:

suma de Poisson → Poisson

suma de Gamma → Gamma

Ejemplo:

y
b
∼
Poisson
(
∑
i
λ
i
ω
b
,
i
)
y 
b
​
 ∼Poisson( 
i
∑
​
 λ 
i
​
 ω 
b,i
​
 )
📌 Ventajas:

menos variables

mejor escalabilidad

inferencia más estable

📌 Desventaja:

z
z se recupera a posteriori como expectativa

🔵 Opción B — Muestrear 
z
z explícitamente (más literal)
Defines:

(
z
1
,
b
,
…
,
z
K
,
b
)
∼
Multinomial
(
y
b
,
 
p
i
,
b
)
(z 
1,b
​
 ,…,z 
K,b
​
 )∼Multinomial(y 
b
​
 , p 
i,b
​
 )
con:

p
i
,
b
∝
λ
i
ω
b
,
i
p 
i,b
​
 ∝λ 
i
​
 ω 
b,i
​
 
📌 Ventajas:

muy interpretativo

asignaciones explícitas

📌 Desventajas:

muchísimas variables latentes

escalabilidad pobre

👉 En producción, se usa casi siempre la opción A.

5️⃣ Organización de los datos (muy importante)
Formato long (igual que EM)
b (brick / m,t,g)	i (hcp / campaign)	ω	X_i	y_b
Pero en Bayes:

no necesitas duplicar y_b

puedes agrupar por b y usar sumas

6️⃣ Inferencia: cómo se estima
Aquí está el gran cambio respecto a EM.

Opciones reales
🟢 MCMC (NUTS)
PyMC / Stan

Muy preciso

Muy lento

Difícil de escalar

👉 Usado en:

research

validación

small datasets

🟡 Variational Inference (VI)
PyMC VI

NumPyro SVI

Pyro SVI

Aproxima la posterior

Mucho más rápido

Algo menos preciso

👉 Es el estándar industrial para estos modelos.

7️⃣ Qué salidas tienes (mucho más ricas que EM)
En EM
λ
^
i
λ
^
  
i
​
 

z
^
i
,
b
z
^
  
i,b
​
 

En Bayesiano
Posterior de 
λ
i
λ 
i
​
 

media

intervalos creíbles

Posterior predictivo de 
z
i
,
b
z 
i,b
​
 

Incertidumbre por:

campaña

periodo

grupo

Probabilidad de que:

campaña A > campaña B

uplift > 0

📌 Esto es oro para decisiones.

8️⃣ Entonces… ¿cuándo merece la pena el enfoque bayesiano?
✅ Merece la pena si:
hay mucho cold start

necesitas intervalos de confianza

tienes jerarquías profundas

el coste de una mala decisión es alto

❌ No merece la pena si:
necesitas escalar rápido

solo quieres rankings

el negocio no entiende incertidumbre

el MMM ya es el cuello de botella

9️⃣ Regla mental final (muy importante)
EM estima “el mejor reparto”.
Bayesiano estima “qué repartos son plausibles y con qué incertidumbre”.

No es solo cambiar MLE por Bayes:
👉 es cambiar la pregunta que haces al modelo.

10️⃣ Cómo suele usarse en la práctica (honesto)
En empresas maduras:

EM para:

baseline

escalabilidad

explicabilidad

Bayesiano para:

cold start

validation

decisiones de alto riesgo

EM + shrinkage inspirado en Bayes (híbrido)

Si quieres, el siguiente paso puede ser:

escribir el modelo completo en PyMC / NumPyro (pseudo-código)

comparar EM vs VI en el mismo dataset

o diseñar un roadmap de madurez analítica (EM → Bayes)

Dime cómo seguimos.

Tú dijiste:
Pon ejemplos de gomo sserian los "grupios"
Data Science Mentor dijo:
Perfecto — aquí voy a ser muy concreto y operativo.
Cuando hablamos de “grupos” en un modelo bayesiano jerárquico, nos referimos a estructuras donde varias entidades comparten información parcial (partial pooling).

Voy a darte ejemplos reales, organizados por caso de uso, y para cada uno te digo:

qué es el grupo

por qué tiene sentido

cómo entra en el modelo

Qué es un “grupo” (definición clara)
En un BHM, un grupo es un conjunto de entidades para las cuales creemos que:

sus productividades no son iguales, pero tampoco completamente independientes

Matemáticamente:

λ
i
∼
LogNormal
(
μ
grupo
(
i
)
,
 
σ
grupo
(
i
)
)
λ 
i
​
 ∼LogNormal(μ 
grupo(i)
​
 , σ 
grupo(i)
​
 )
1️⃣ Grupos en HCP–Brick
🔹 Ejemplo 1 — Especialidad médica
Grupo: especialidad del HCP

GP

Cardio

Endo

Onco

Por qué tiene sentido
Médicos de la misma especialidad:

tienen patrones de prescripción similares

responden de forma parecida a visitas

Un GP nuevo se parece más a otros GPs que a un Onco

Modelo
λ
h
∼
LogNormal
(
μ
spec
h
,
σ
spec
)
μ
spec
∼
N
(
μ
0
,
σ
0
)
λ 
h
​
 
μ 
spec
​
 
​
  
∼LogNormal(μ 
spec 
h
​
 
​
 ,σ 
spec
​
 )
∼N(μ 
0
​
 ,σ 
0
​
 )
​
 
👉 Cold start resuelto automáticamente

🔹 Ejemplo 2 — Seniority buckets
Grupo: seniority

0–2 años

3–7 años

8+ años

Uso típico
Médicos jóvenes tienen menos impacto

Seniors más estables

🔹 Ejemplo 3 — Región
Grupo: región geográfica

Norte / Centro / Sur

Urbano / Rural

📌 Muy útil cuando:

el mercado no es homogéneo

hay diferencias estructurales

2️⃣ Grupos en MMM → MTA (campañas / creatividades)
Aquí es donde más se usan.

🔹 Ejemplo 4 — Tipo de campaña (el más común)
Grupo: objective

Awareness

Consideration

Conversion

Por qué
Campañas de awareness:

saturan antes

menor eficiencia directa

Conversion:

menos volumen

más impacto por impresión

Modelo
λ
m
,
k
∼
LogNormal
(
μ
objective
k
,
σ
objective
)
λ 
m,k
​
 ∼LogNormal(μ 
objective 
k
​
 
​
 ,σ 
objective
​
 )
🔹 Ejemplo 5 — Formato creativo
Grupo:

Video

Display

Search text

Rich media

📌 Muy útil cuando:

tienes muchas creatividades con poca historia

necesitas estabilizar rankings

🔹 Ejemplo 6 — Creative family / concepto
Grupo:

Concept A

Concept B

Concept C

Uso real
tests creativos

aprendizaje transferido entre variantes

🔹 Ejemplo 7 — Plataforma / publisher
Grupo:

Meta

Google

TikTok

Programmatic

Aunque el MMM sea por canal, intra-canal puedes tener:

distintas dinámicas

distinta saturación efectiva

3️⃣ Grupos jerárquicos anidados (nivel senior)
Aquí es donde el enfoque bayesiano brilla.

🔹 Ejemplo 8 — Jerarquía completa en MTA
Canal
 └── Plataforma
      └── Formato
           └── Campaña
                └── Creatividad
Modelo conceptual:

λ
crea
∼
LogNormal
(
μ
campa
n
˜
a
,
σ
crea
)
λ 
crea
​
 ∼LogNormal(μ 
campa 
n
˜
 a
​
 ,σ 
crea
​
 )
y así sucesivamente hacia arriba.

📌 EM no puede manejar esto limpiamente.
📌 Bayesiano sí.

4️⃣ Grupos “blandos” (no obvios, pero muy potentes)
🔹 Ejemplo 9 — Cohortes temporales
Grupo:

campañas lanzadas el mismo mes

HCPs onboarded el mismo trimestre

👉 Captura:

efectos de madurez

cambios estructurales del mercado

🔹 Ejemplo 10 — Clusters aprendidos
Grupo:

clusters no supervisados (k-means, embeddings)

Ejemplo:

agrupar creatividades por similitud visual

agrupar HCPs por comportamiento histórico

📌 Muy potente, pero cuidado con interpretabilidad.

5️⃣ Qué NO es un buen grupo (anti-ejemplos)
❌ ID individual (no agrupa nada)
❌ Grupos con 1 elemento
❌ Grupos altamente colineales entre sí
❌ Grupos “porque sí” sin hipótesis de similitud

6️⃣ Cómo decidir si algo merece ser grupo (regla senior)
Antes de crear un grupo, pregúntate:

¿Creemos a priori que estas entidades se parecen?

¿Hay escasez de datos a nivel individual?

¿Mejoraría el cold start?

¿Acepta el negocio esta segmentación?

Si respondes sí a 2 o más → buen candidato.

7️⃣ Resumen visual (mental)
Caso	Grupo típico	Beneficio
HCP–Brick	Especialidad	Cold start
HCP–Brick	Región	Estabilidad
MMM–MTA	Objective	Comparabilidad
MMM–MTA	Formato	Pooling
MMM–MTA	Creative family	Transfer learning
Ambos	Cohorte temporal	Robustez
Cierre (muy importante)
Los grupos no son un detalle técnico.
Son donde introduces conocimiento del negocio en el modelo.

Si quieres, el siguiente paso puede ser:

escribir un modelo bayesiano completo con 2–3 niveles de grupos

comparar qué grupos valen la pena vs cuáles no

o ver cómo traducir un EM actual a una versión jerárquica mínima

Tú decides cómo seguimos.

Tú dijiste:
si la jerarquia va desde canal a creatividad, estariamos atribuyendo directamente a cada creatividad, verdad?
Data Science Mentor dijo:
Sí — exactamente, pero con un matiz muy importante que conviene dejar cristalino.

Voy a explicarlo en 3 capas:

qué significa “atribuir a creatividad” en un modelo jerárquico

cómo se hace técnicamente

qué no significa (para evitar malentendidos de negocio)

1️⃣ ¿Estamos atribuyendo directamente a cada creatividad?
Respuesta corta
👉 Sí: el modelo puede producir

z
^
creatividad
,
 
t
,
g
z
^
  
creatividad,t,g
​
 
es decir, atribución directa por creatividad.

Pero:

esa atribución está regularizada y condicionada por toda la jerarquía
(canal → plataforma → formato → campaña → creatividad).

2️⃣ Qué significa esto en términos de modelo
Supongamos la jerarquía:

Canal (m)
 └── Plataforma (p)
      └── Formato (f)
           └── Campaña (k)
                └── Creatividad (c)
Productividad a nivel creatividad
Definimos:

λ
c
∼
LogNormal
(
μ
k
,
σ
c
)
λ 
c
​
 ∼LogNormal(μ 
k
​
 ,σ 
c
​
 )
y recursivamente:

μ
k
∼
LogNormal
(
μ
f
,
σ
k
)
μ 
k
​
 ∼LogNormal(μ 
f
​
 ,σ 
k
​
 )
μ
f
∼
LogNormal
(
μ
p
,
σ
f
)
μ 
f
​
 ∼LogNormal(μ 
p
​
 ,σ 
f
​
 )
μ
p
∼
LogNormal
(
μ
m
,
σ
p
)
μ 
p
​
 ∼LogNormal(μ 
m
​
 ,σ 
p
​
 )
👉 Cada creatividad tiene su propio 
λ
c
λ 
c
​
 
pero:

si tiene pocos datos → se “pega” a su campaña

si tiene muchos datos → se separa

Eso es partial pooling.

3️⃣ Cómo se calcula la atribución final
En el E-step (o posterior predictivo bayesiano), para cada unidad agregada 
(
m
,
t
,
g
)
(m,t,g):

z
^
c
,
t
,
g
=
C
m
,
t
,
g
⋅
λ
c
 
ω
c
,
t
,
g
∑
c
′
∈
m
λ
c
′
 
ω
c
′
,
t
,
g
z
^
  
c,t,g
​
 =C 
m,t,g
​
 ⋅ 
∑ 
c 
′
 ∈m
​
 λ 
c 
′
 
​
 ω 
c 
′
 ,t,g
​
 
λ 
c
​
 ω 
c,t,g
​
 
​
 
👉 Sí, la unidad final de atribución es la creatividad.

Pero la estimación de 
λ
c
λ 
c
​
 :

no es independiente

hereda información de toda la jerarquía

4️⃣ Qué NO significa (esto es crucial)
❌ No significa:
que cada creatividad tenga identificación causal propia

que puedas comparar creatividades de canales distintos “en bruto”

que una creatividad nueva tenga un 
λ
λ libre

✔️ Sí significa:
ranking estable de creatividades dentro de su contexto

control del ruido extremo

cold start gestionado

5️⃣ Comparación con enfoques no jerárquicos
Enfoque	¿Atribuye a creatividad?	Estabilidad	Cold start
Heurístico (share imps)	✔️	Baja	❌
EM plano	✔️	Media	❌
Bayes jerárquico	✔️	Alta	✔️
📌 La diferencia no es si atribuyes, sino cómo de confiable es esa atribución.

6️⃣ Cómo explicarlo a negocio (frase clave)
“Sí, atribuimos a creatividad,
pero la creatividad no compite sola:
compite dentro de su campaña y formato,
y el modelo lo tiene en cuenta.”

7️⃣ Regla senior para decidir el nivel final de atribución
Atribuye al nivel más bajo
para el que tengas señal suficiente
o pooling jerárquico adecuado.

Si no:

baja el nivel (campaña)

o refuerza la jerarquía

8️⃣ Conclusión clara
✔️ Sí, un modelo jerárquico canal → creatividad atribuye directamente a creatividad

✔️ Lo hace de forma:

regularizada

estable

consistente con MMM

⚠️ No convierte esa atribución en causal

Si quieres, el siguiente paso natural es:

dibujar un diagrama completo del modelo generativo jerárquico

o escribir pseudo-código PyMC / NumPyro del modelo canal→creatividad

o discutir cuándo NO conviene bajar hasta creatividad

Dime cómo seguimos.

Tú dijiste:
cual es el nombre tecnico de $\omega_{bh}$?
Data Science Mentor dijo:
Muy buena pregunta — y muy pertinente, porque ponerle nombre técnico correcto a 
ω
b
,
h
ω 
b,h
​
  evita muchísimos malentendidos.

La respuesta corta es: no tiene un único nombre universal, pero sí tiene nombres técnicos aceptados según la tradición estadística en la que te sitúes.

Voy de más formal a más aplicado, y te digo cuál usar en cada contexto.

Respuesta corta (para uso práctico)
En tu contexto (EM, Poisson/Gamma, HCP–Brick, MMM–MTA), el nombre técnico más correcto y defendible es:

Exposure (o Exposure term)

Y, más precisamente:

Known exposure / offset / intensity modifier

1️⃣ En estadística clásica (Poisson / GLM)
Nombre técnico
🔹 Exposure
Modelo típico:

z
∼
Poisson
(
λ
⋅
ω
)
z∼Poisson(λ⋅ω)
Aquí:

λ
λ = rate (tasa)

ω
ω = exposure (tiempo, área, población, impresiones, etc.)

Ejemplos canónicos:

accidentes por km → km = exposure

llamadas por hora → horas = exposure

ventas por visitas → visitas = exposure

📌 Este es el paralelismo exacto con tu modelo.

En forma log-lineal
log
⁡
E
[
z
]
=
log
⁡
ω
+
log
⁡
λ
logE[z]=logω+logλ
Aquí 
log
⁡
ω
logω se llama:

Offset

📌 En GLM:

ω
ω = exposure

log
⁡
ω
logω = offset

2️⃣ En modelos de conteo jerárquicos / epidemiología
Nombres usados
Exposure

Risk set size

At-risk population

Opportunity

Ejemplo:

nº de infecciones ~ población expuesta

nº de eventos ~ personas “en riesgo”

📌 En HCP–Brick:

HCP “en riesgo” de generar ventas en ese brick.

3️⃣ En mixture models / EM allocation
Aquí el término cambia ligeramente de sabor.

Nombres comunes
Mixing weight (known)

Eligibility

Allocation weight

Structural weight

Pero ojo:

mixing weight suele reservarse para parámetros que suman 1

en tu caso NO suma 1

📌 Por eso no es el mejor nombre técnico, aunque algunos papers lo usen.

4️⃣ En econometría / marketing analytics (MMM / MTA)
Aquí el naming es más “business-oriented”.

Términos usados en la práctica
Effective exposure

Effective media pressure

Adstocked exposure

Saturated exposure

Delivered opportunity

Ejemplo típico:

ω
m
,
k
,
t
,
g
=
Hill
(
Adstock
(
Impressions
)
)
ω 
m,k,t,g
​
 =Hill(Adstock(Impressions))
📌 Aquí “effective exposure” es el término más limpio.

5️⃣ En causal inference (con cuidado)
A veces verás:

Dose

Treatment intensity

⚠️ No recomendado en tu caso, porque:

induce lectura causal fuerte

tu 
ω
ω no es exógena necesariamente

6️⃣ Qué NO es (y cómo NO llamarlo)
❌ Probability
❌ Share
❌ Mixing proportion (sin aclarar)
❌ Weight (sin contexto)

Estos nombres inducen errores conceptuales.

7️⃣ Recomendación concreta según audiencia
Para documentos técnicos
Exposure term 
ω
b
,
h
ω 
b,h
​
 

o

Known exposure (offset in the log-link)

Para negocio
Exposición efectiva
“cuánta oportunidad tiene X de generar impacto”

Para código
exposure
# o
w
# o
effective_exposure
8️⃣ Frase formal que puedes usar sin riesgo
“
ω
b
,
h
ω 
b,h
​
  es el término de exposición conocido que escala la intensidad del proceso generativo; en un GLM con link log entra como offset.”

Esa frase es 100% correcta en estadística.

9️⃣ Resumen final (para fijarlo)
Contexto	Nombre técnico
Poisson / GLM	Exposure
Log-link	Offset
MMM / MTA	Effective exposure
EM allocation	Known exposure term
Si quieres, el siguiente paso puede ser:

ver cómo cambia el modelo si 
ω
ω se trata como latente

o ver papers de referencia donde aparece exactamente este término

o ayudarte a redactar la sección metodológica con el naming correcto

Tú decides.

Tú dijiste:
Tenemos que preparar un documento en inglés dirigido a CMOs y Data Science Head.

He pensado que los primeros apartados sean:

<START>
# What is Multitouch Attribution (MTA)?

# MTA and Marketing Mix Models (MMM)

# Measurment (MMM + MTA) and causalty: (quasi)experiments
<END>

posteriormente hablaremos de:

<START>
# MTA as a credit allocation problem

## Expectation Maximization (EM) algorithm

## Potential pitfalls of EM for MTA

## Modeling alternatives: Bayesian Inference and Variational Inference (VI)

## FAQ

# MTA as a sequence mining problem: using transformers and graphs
<END>

para lo que usaremos el contenido de este curso.

¿Qué te parece? ¿Cómo plantearias el documento? Cuando acordemos el planteamietno te pediré que lo escribas completo
Data Science Mentor dijo:
Me parece muy buena la estructura y, sobre todo, muy acertado el orden.
Lo que propones está alineado con cómo CMOs y Heads of Data Science entienden el problema cuando está bien explicado.

Dicho eso, te propongo refinar el planteamiento para que:

el CMO no se pierda ni se sienta “modelado”

el Head of DS vea rigor, trade-offs y control

ambos entiendan por qué MTA no es una cosa única

el documento tenga autoridad metodológica, no “opinión”

Voy por partes.

1️⃣ Evaluación general de tu planteamiento
Lo que está muy bien
✔️ Empiezas por qué es MTA, no por algoritmos
✔️ Anclas MTA en MMM e incrementalidad (crítico)
✔️ Separas:

qué es MTA

cómo se implementa (credit allocation)

qué NO cubre (sequences / transformers)
✔️ EM aparece como una solución, no como “la solución”

Esto ya te pone por encima del 90% de documentos que circulan.

2️⃣ El ajuste clave: framing por “problemas”, no por técnicas
Mi recomendación principal:

El documento debe estar estructurado por “problemas de medición”,
y dentro de cada uno presentar familias de soluciones.

Eso hace que:

el CMO siga la historia

el DS lead vea criterio

no parezca que “vendemos EM”

3️⃣ Propuesta de estructura refinada (acordable)
Te propongo esta estructura muy cercana a la tuya, pero con algunos ajustes de framing y títulos.

PART I — Setting the ground truth
1. What is Multitouch Attribution (MTA)?
Objetivo
Alinear definiciones y expectativas.

Mensajes clave

Qué problema intenta resolver MTA

Qué decisiones pretende informar

Qué NO es MTA (no causal per se)

2. MTA and Marketing Mix Models (MMM)
Objetivo
Dejar claro que MTA sin MMM es incompleto.

Mensajes clave

MMM responde al “how much”

MTA responde al “where inside the channel”

Por qué mezclar ambos es inevitable en entornos modernos

3. Measurement (MMM + MTA) and causality: (quasi-)experiments
Objetivo
Blindar el documento ante críticas de causalidad.

Mensajes clave

Qué partes son causales

Qué partes son model-based

Dónde entran los experimentos

Qué se puede y no se puede afirmar

📌 Este bloque da credibilidad institucional.

PART II — MTA as a credit allocation problem
Aquí entramos en el “core” del curso que hemos hecho.

4. MTA as a credit allocation problem
Objetivo
Reformular MTA de forma matemática pero comprensible.

Mensajes clave

Observamos totales agregados

Queremos repartir crédito

El problema es estructural, no tecnológico

Aquí introduces:

analogía HCP–Brick

analogía MMM→MTA

5. Expectation–Maximization (EM) for MTA
Objetivo
Presentar EM como una solución natural y controlada.

Mensajes clave

Qué asume EM

Qué garantiza

Por qué es atractivo en producción

Cómo preserva incrementalidad del MMM

Sin fórmulas duras, pero con claridad conceptual.

6. Potential pitfalls of EM for MTA
Objetivo
Demostrar seniority y evitar overselling.

Mensajes clave

Identifiability

Overfitting silencioso

Cold start

Sensibilidad a exposición y outliers

📌 Esta sección es clave para el Head of DS.

7. Modeling alternatives: Bayesian Inference and Variational Inference (VI)
Objetivo
Mostrar que EM no es dogma.

Mensajes clave

Qué añade el enfoque bayesiano

Cuándo merece la pena

Costes reales (complejidad, compute, explicabilidad)

Aquí usas directamente lo que ya discutimos:

jerarquías

pooling

incertidumbre

8. FAQ
Objetivo
Cerrar frentes políticos y operativos.

Audiencias:

CMO

Finance

Analytics

Legal

👉 Aquí puedes reutilizar casi tal cual el Q&A defensivo.

PART III — Beyond credit allocation
9. MTA as a sequence mining problem: transformers and graphs
Objetivo
Poner límites claros y mostrar visión de futuro.

Mensajes clave

Qué problema distinto resuelven estos enfoques

Cuándo aplican (user-level, paths)

Por qué no sustituyen MMM+MTA

Riesgos de interpretabilidad y causalidad

📌 Muy importante:

no vender esto como “the next step”, sino como otro eje.

4️⃣ Qué añadiría (muy poco) para hacerlo excelente
🔹 Un Executive Summary (1 página)
Al principio, con:

5 bullets

1 diagrama mental

1 frase fuerte tipo:

“MTA is not a single model, but a family of solutions to different measurement problems.”

🔹 Un “Decision map”
Cerca del final:

Need	Recommended approach
Channel budgeting	MMM
Intra-channel optimization	EM-based MTA
Cold start & uncertainty	Bayesian MTA
User journey analysis	Sequence models
Esto encanta a CMOs.

5️⃣ Veredicto final
Tu planteamiento es muy sólido.
Mi recomendación es:

Mantener exactamente tus bloques

Ajustar títulos para:

enfatizar problem → solution

no sonar “tool-centric”

Separar claramente:

measurement

causality

optimization

Si estás de acuerdo con esta estructura:
👉 en el siguiente mensaje puedo escribir el documento completo en inglés, con:

tono C-level + DS-level

sin ecuaciones

con frases defendibles

listo para circular internamente o externamente

Dime:

¿Audiencia principal: más CMO o más DS Head?

¿Longitud objetivo? (10–15 páginas / whitepaper / blog long-form)

Tú dijiste:
Me parece genial! Algunas precisiones:

- La parte III  no la trataremos ahora
- FAQ: reutiliza las secciones "Cierre para preguntas difíciles (chuleta)" y "Q&A defensivo — EM + MMM + MTA"

El documento debe valer solo para CMO, solo para DS Head y para los dos juntos
Longitud: si, como 10-15 páginas, más bien whitepaper. Lo usaremos después para generar presentación con slides y blog post.
Data Science Mentor dijo:
Perfecto — con esas precisiones ya estamos 100% alineados.
Lo que propones da para un whitepaper sólido (10–15 páginas) que:

un CMO puede leer sin perderse

un Head of Data Science respeta metodológicamente

ambos pueden usar como referencia común

se puede reutilizar casi sin fricción para:

slides ejecutivas

blog posts

FAQs internas

A continuación te propongo el planteamiento definitivo del documento, ya cerrado para escritura, y luego te explico por qué funciona para ambas audiencias.

Propuesta final de estructura del whitepaper
Executive Summary (1 página)
Objetivo

Alinear expectativas

Explicar qué problema resolvemos y qué no

Dar una “north star” clara

Contenido

Qué es MTA (y qué no)

Por qué MMM + MTA deben convivir

Qué aporta el enfoque EM

Qué decisiones habilita

Qué límites tiene

Esta sección debe poder leerse sola por un CMO.

PART I — Measurement foundations
1. What is Multitouch Attribution (MTA)?
Objetivo

Definición clara, no técnica

Desmitificar MTA

Claves

MTA como problema de atribución, no de predicción

Touchpoints, exposure y credit

Por qué “last-click” es insuficiente

Nivel

80% negocio

20% analítico ligero

2. MTA and Marketing Mix Models (MMM)
Objetivo

Posicionar MTA dentro del ecosistema de medición

Evitar el error “MTA vs MMM”

Claves

Qué responde MMM

Qué responde MTA

Por qué MTA sin MMM pierde incrementalidad

Enfoque top-down vs bottom-up

📌 Aquí se gana la confianza del CMO y del DS Head.

3. Measurement (MMM + MTA) and causality: (quasi-)experiments
Objetivo

Blindar el documento frente a críticas de causalidad

Claves

Qué parte es causal (MMM, experimentos)

Qué parte es model-based (MTA)

Rol de los experimentos:

validación

calibración

aprendizaje

📌 Esta sección es clave para credibilidad institucional.

PART II — MTA as a credit allocation problem
4. MTA as a credit allocation problem
Objetivo

Reformular MTA de forma rigurosa pero comprensible

Claves

Observamos resultados agregados

Queremos repartir crédito a niveles más bajos

Analogía intuitiva:

HCP–Brick

MMM → campañas / creatividades

📌 Aquí introduces el marco conceptual único del documento.

5. Expectation–Maximization (EM) for MTA
Objetivo

Presentar EM como una solución natural y controlada

Claves

Por qué EM encaja con el problema

Qué asume

Qué garantiza:

conservación de masa

coherencia con MMM

estabilidad

Muy importante

Nada de ecuaciones duras

Mucha intuición

Frases defendibles

6. Potential pitfalls of EM for MTA
Objetivo

Mostrar madurez y evitar overselling

Claves

Identifiability

Overfitting silencioso

Cold start

Sensibilidad a exposición y outliers

📌 Esta sección es donde el Head of DS dice:

“OK, aquí hay criterio”.

7. Modeling alternatives: Bayesian Inference and Variational Inference (VI)
Objetivo

Posicionar EM dentro de un continuo metodológico

Claves

Qué añade Bayes:

pooling

incertidumbre

robustez

Costes reales:

complejidad

compute

explicabilidad

Cuándo tiene sentido dar el salto

📌 Muy importante: no vender Bayes como “mejor”, sino como “distinto”.

PART III — FAQ and defensive Q&A
8. FAQ
👉 Aquí reutilizamos explícitamente:

“Cierre para preguntas difíciles (chuleta)”

“Q&A defensivo — EM + MMM + MTA”

Organizado por audiencia:

Analytics / DS

Finance

Marketing

Legal / Compliance

📌 Esta sección convierte el documento en:

material de comité

referencia interna

escudo político

Qué NO entra (por ahora)
❌ Parte III original (transformers, graphs, sequence mining)

❌ User-level path modeling

❌ Deep learning details

👉 Perfectamente coherente con un whitepaper de measurement, no de adtech hype.

Por qué este documento sirve a ambas audiencias
Para el CMO
Empieza por decisiones, no por modelos

Refuerza incrementalidad

Marca límites claros

Evita promesas irreales

Para el Head of Data Science
Marco formal consistente

Trade-offs explícitos

Alternativas bien posicionadas

Lenguaje metodológico correcto

Para ambos
Vocabulario compartido

Expectativas alineadas

Base común para discusión estratégica

Próximo paso (si estás de acuerdo)
Si confirmas este planteamiento, en el siguiente mensaje puedo:

👉 Escribir el documento completo en inglés, con:

tono whitepaper (neutral, riguroso, claro)

10–15 páginas equivalentes

secciones bien balanceadas

texto reutilizable para:

slides

blog posts

FAQs internas

Antes de escribir, solo una última confirmación rápida (sí/no basta):

¿Usamos un tono neutral/academic-industry (tipo Google / Meta whitepaper)?

¿Lo escribimos como vendor-agnostic (sin mencionar tools concretas)?

Cuando me digas, empiezo a escribir.

Tú dijiste:
si y si. Escribe el documento
Data Science Mentor dijo:
Perfecto. A continuación tienes el whitepaper completo, escrito en inglés, con tono neutral industry / academic, vendor-agnostic, pensado explícitamente para CMOs y Heads of Data Science a la vez.
El texto está estructurado para poder reutilizarse casi directamente en slides y blog posts.

Multitouch Attribution in Modern Marketing Measurement
Bridging Marketing Mix Models, Incrementality, and Intra-Channel Optimization
Executive Summary
Multitouch Attribution (MTA) aims to explain how marketing impact should be distributed across touchpoints, campaigns, or creatives. However, when used in isolation, MTA often conflates correlation with causation and can lead to misleading conclusions.

Marketing Mix Models (MMM), on the other hand, provide robust, incremental and causal estimates at an aggregated channel level, but lack the granularity required for day-to-day execution.

This whitepaper presents a unified measurement framework in which:

MMM establishes incremental impact at the channel level

MTA distributes that incremental impact within channels

Expectation–Maximization (EM) is introduced as a principled and scalable method for credit allocation

Bayesian hierarchical models are positioned as a complementary extension when uncertainty, cold start, or deep hierarchies matter

The goal is not to promote a single model, but to provide a decision-oriented measurement framework that is rigorous, transparent, and operationally useful.

PART I — Measurement Foundations
1. What Is Multitouch Attribution (MTA)?
Multitouch Attribution is a family of methods that aim to distribute marketing credit across multiple touchpoints involved in a customer journey.

In practical terms, MTA tries to answer questions such as:

Which campaigns or creatives contributed most to outcomes?

How should performance be compared within a channel?

Where should execution be optimized?

What MTA Is
A credit allocation problem

A tool for intra-channel optimization

A way to bring structure to complex delivery data

What MTA Is Not
A causal model by default

A replacement for MMM

A guarantee of incremental impact at granular levels

A key limitation of traditional MTA approaches is that they often operate on user-level paths without a reliable counterfactual. As a result, they are highly sensitive to selection bias and timing effects.

2. MTA and Marketing Mix Models (MMM)
MMM and MTA address different but complementary questions.

Question	MMM	MTA
How much impact does marketing have?	✔️	❌
Which channels drive incremental results?	✔️	❌
Which campaigns or creatives perform better within a channel?	❌	✔️
Suitable for budget allocation	✔️	❌
Suitable for execution optimization	❌	✔️
Why MTA Without MMM Is Incomplete
MTA models typically allocate credit based on observed exposure patterns. Without an incremental baseline, they cannot distinguish:

correlation vs causation

demand capture vs demand creation

Why MMM Without MTA Is Insufficient
MMM produces reliable channel-level insights, but:

execution teams need guidance below the channel level

creative, campaign, and targeting decisions remain under-informed

Conclusion:
MMM and MTA should not compete. They should be connected.

3. Measurement, Causality, and (Quasi-)Experiments
Marketing measurement combines different levels of causal confidence.

Causality in MMM
MMM estimates incremental impact via counterfactual modeling

When well specified, MMM provides causal estimates at an aggregated level

Causality in MTA
MTA is typically model-based, not causal

It explains how observed outcomes can be allocated, not what would have happened otherwise

Role of Experiments
Experiments remain the gold standard for causality:

Geo-experiments

Holdouts

Creative tests

In practice:

MMM provides global causal grounding

MTA provides granular structure

Experiments validate and calibrate both

PART II — MTA as a Credit Allocation Problem
4. MTA as a Credit Allocation Problem
At its core, MTA can be reframed as a credit allocation problem under constraints.

We observe:

aggregated outcomes (e.g., conversions, revenue, incremental contribution)

detailed exposure data (campaigns, creatives, impressions, timing)

We want to infer:

how much each granular entity contributed to the observed total

This structure appears in many domains:

sales attribution across territories

healthcare outcomes across providers

marketing contribution across campaigns

The defining constraint is:

The allocated contributions must sum exactly to the observed total.

This reframing allows us to use well-understood statistical tools rather than ad-hoc heuristics.

5. Expectation–Maximization (EM) for MTA
Why EM Fits the Problem
The Expectation–Maximization algorithm is designed for models with:

latent variables

observed aggregates

structured constraints

In MTA:

latent variables represent campaign-level contributions

observed data are aggregated outcomes

constraints enforce conservation of total impact

What EM Guarantees
Mass conservation: allocated credit always matches MMM totals

Stability: small data changes lead to smooth updates

Scalability: works with large datasets

Transparency: assumptions are explicit and auditable

Interpretation
EM does not “create” performance.
It distributes known incremental impact using exposure patterns and learned efficiencies.

This makes EM particularly suitable as the bridge between MMM and execution-level optimization.

6. Potential Pitfalls of EM for MTA
EM is powerful, but not foolproof.

Identifiability
If two campaigns have identical exposure patterns, the model cannot distinguish them. EM will distribute credit arbitrarily unless additional structure is introduced.

Silent Overfitting
Likelihood can increase even when the model is fitting noise. Without regularization and stability checks, results may appear plausible but be unreliable.

Cold Start
New campaigns or creatives with limited history may receive unstable estimates unless pooling or priors are used.

Sensitivity to Exposure Design
Poorly defined exposure signals (e.g., raw impressions without saturation or carryover) can distort attribution.

Key takeaway:
EM requires careful modeling choices, not blind application.

7. Modeling Alternatives: Bayesian Inference and Variational Inference
Bayesian hierarchical models extend EM by introducing uncertainty and structured pooling.

What Bayesian Models Add
Partial pooling across campaigns, creatives, or groups

Natural handling of cold start

Posterior distributions instead of point estimates

Explicit uncertainty quantification

Trade-offs
Aspect	EM	Bayesian (VI)
Scalability	High	Medium
Complexity	Low	High
Interpretability	High	Medium
Uncertainty	❌	✔️
Cold start	Limited	Strong
Practical Positioning
EM is often the right production baseline

Bayesian approaches are valuable when:

uncertainty matters for decisions

data are sparse

hierarchies are deep

PART III — FAQ and Defensive Q&A
8. FAQ and Defensive Q&A
This section consolidates common questions from Analytics, Finance, Marketing, and Legal stakeholders.

Does this model create or destroy revenue?
No. All allocations strictly preserve MMM totals.

Is this causal?
The total impact is causal (from MMM). The allocation within channels is model-based.

Can this be audited?
Yes. The methodology is transparent, reproducible, and version-controlled.

Why not use user-level MTA only?
Because user-level attribution alone cannot reliably identify incrementality.

Can this guide optimization?
Yes—as a prioritization signal, not as a substitute for experimentation.

Final Takeaway
MMM determines how much marketing works.
MTA determines how to execute better within that reality.

A robust measurement strategy recognizes that:

no single model answers all questions

causality and granularity must be handled separately

rigor and usability must coexist

This framework provides a principled way to connect strategy, analytics, and execution—without over-promising or oversimplifying.

End of document

Cuando quieras, a partir de este texto puedo:

generar la presentación ejecutiva (10–12 slides)

extraer 2–3 blog posts (CMO-focused vs DS-focused)

o preparar una versión con diagramas y esquemas visuales



Ningún archivo seleccionadoNingún archivo seleccionado
Una nueva versión de GPT está disponible. Continúa chateando para usar la versión antigua o empieza un nuevo chat para acceder a la versión más reciente.
