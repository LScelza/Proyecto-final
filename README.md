# Proyecto de Análisis de Transporte y Calidad del Aire en NYC

## Contexto

En la ciudad de Nueva York, los servicios de taxis y de viajes compartidos en vehículos como Uber han transformado la forma en que las personas se desplazan. Estos servicios ofrecen una alternativa conveniente y relativamente accesible al transporte público y al alquiler de automóviles. Además, generan una gran cantidad de datos que pueden ser procesados y analizados por consultoras, empresas, organismos públicos y estudiantes de Ciencias de Datos.

Los datos generados por estos servicios incluyen información sobre la ubicación del vehículo, la duración del viaje, la tarifa cobrada y la calificación del conductor. Estos datos pueden ser utilizados para identificar patrones de viaje y demanda, así como para mejorar la eficiencia y la calidad del servicio.

El cambio climático se ha acelerado a niveles sin precedentes debido a las actividades humanas, principalmente la necesidad de energía obtenida a partir de combustibles fósiles. El impacto del desarrollo energético en el ambiente y los consumos generados llevan a las compañías a tomar acción para intervenir y mejorar la generación y consumo de energía.

## Nombre de la Empresa

**Lumen**

## Nuestro Rol

Lumen es una empresa de servicios de transporte de pasajeros, actualmente operando en el sector de micros de media y larga distancia. Estamos interesados en invertir en el sector de transporte de pasajeros con automóviles. Con una visión de un futuro menos contaminado y adaptándonos a las tendencias del mercado, queremos corroborar la relación entre estos medios de transporte particulares y la calidad del aire, así como la contaminación sonora, para estudiar la posibilidad de implementar vehículos eléctricos en nuestra flota.

Debido a que sería una unidad de negocio nueva, se pretende hacer un análisis preliminar del movimiento de los taxis en la ciudad de Nueva York, para obtener un marco de referencia y poder tomar decisiones bien fundamentadas.

## ¿Qué Hicimos?

### 1. Análisis Preliminar de la Situación Actual

Para tener un panorama claro de la situación actual, realizamos un análisis exhaustivo de los siguientes datos:

- **Recorridos de taxis verdes y amarillos en NYC y ciudades cercanas**:
  - **Objetivo**: Comprender los patrones de movilidad y demanda.
  - **Metodología**: Recopilamos datos históricos de los recorridos de taxis, incluyendo tiempos de viaje, puntos de inicio y fin, tarifas y frecuencias de viaje. Estos datos se obtuvieron del portal oficial de la ciudad de Nueva York. 
  - [Datos de Recorridos de Taxis](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
  - **Resultados esperados**: Identificación de zonas de alta demanda, patrones de movilidad y tiempos pico de uso de taxis.

- **Distribución de estaciones de carga para vehículos eléctricos y con combustibles alternativos**:
  - **Objetivo**: Evaluar la infraestructura actual para vehículos eléctricos.
  - **Metodología**: Mapeamos las estaciones de carga disponibles en NYC, analizando su distribución geográfica y capacidad. También consideramos la disponibilidad de estaciones para combustibles alternativos.
  - **Resultados esperados**: Identificación de áreas bien servidas y zonas que requieren mayor infraestructura de carga.

- **Características de distintos vehículos**:
  - **Objetivo**: Comparar diferentes tipos de vehículos en términos de costos y beneficios.
  - **Metodología**: Analizamos especificaciones técnicas, costos de adquisición, mantenimiento y operación de varios modelos de vehículos eléctricos e híbridos.
  - **Resultados esperados**: Una lista comparativa que detalle las ventajas y desventajas de cada tipo de vehículo.

- **Rendimiento de vehículos híbridos enchufables**:
  - **Objetivo**: Evaluar la eficiencia y costos operativos de vehículos híbridos enchufables.
  - **Metodología**: Estudiamos datos sobre eficiencia energética, costos operativos, emisiones y autonomía de varios modelos de vehículos híbridos enchufables.
  - **Resultados esperados**: Determinación de la viabilidad y costos-beneficios de utilizar vehículos híbridos enchufables en la flota.

### 2. Clasificación de Datasets Relevantes y Definición de Objetivos

Para estructurar nuestro análisis y asegurar que estamos trabajando con los datos más relevantes, llevamos a cabo los siguientes pasos:

- **Identificación de datasets relevantes**:
  - **Objetivo**: Seleccionar conjuntos de datos que proporcionen información crucial para nuestro análisis.
  - **Metodología**: Revisamos diversas fuentes de datos y seleccionamos aquellos que son más pertinentes para nuestro estudio, asegurándonos de que sean completos y precisos.

- **Definición de objetivos**:
  - **Objetivo**: Establecer metas claras y alcanzables para el proyecto.
  - **Metodología**: Trabajamos en colaboración con los interesados para definir objetivos específicos como la evaluación de la viabilidad económica y ambiental de diferentes tipos de vehículos, y la identificación de zonas con mayor necesidad de infraestructura.

- **Alcances del proyecto**:
  - **Objetivo**: Delimitar el alcance del proyecto para enfocarnos en los aspectos más críticos.
  - **Metodología**: Definimos los límites del análisis, como las áreas geográficas a cubrir y los tipos de vehículos a considerar, para asegurar que nuestros esfuerzos se centren en los elementos más importantes.

### 3. Proceso de Transformación (ETL)

Realizamos un proceso ETL (Extracción, Transformación y Carga) sobre los siguientes datos para prepararlos para el análisis:

- **ETL sobre recorridos de taxis**:
  - **Objetivo**: Preparar datos de recorridos para un análisis detallado.
  - **Metodología**: Extraímos datos de recorridos de taxis, los transformamos para limpiar y estructurar la información, y los cargamos en nuestra base de datos para su análisis posterior.
  - **Detalles**: La extracción se hizo desde la fuente original, transformando los datos para incluir solo las columnas necesarias y normalizar la información. 
  - [Enlace a ETL sobre Recorridos](#)

- **ETL sobre el rendimiento de vehículos híbridos enchufables**:
  - **Objetivo**: Procesar datos sobre eficiencia energética y costos operativos.
  - **Metodología**: Extraímos datos sobre el rendimiento de vehículos híbridos enchufables, los transformamos para estandarizar las métricas y los cargamos en la base de datos.
  - **Detalles**: Se incluyó la conversión de unidades de medida y la agregación de datos relevantes como costos de operación y mantenimiento. 
  - [Enlace a ETL sobre Rendimiento de Vehículos Híbridos Enchufables](#)

- **ETL sobre distribución y disponibilidad de estaciones de carga**:
  - **Objetivo**: Preparar datos sobre la infraestructura de carga para el análisis.
  - **Metodología**: Extraímos datos sobre estaciones de carga, los transformamos para mapear su distribución y capacidad, y los cargamos en nuestra base de datos.
  - **Detalles**: Incluimos la geolocalización de estaciones y la capacidad de carga disponible en cada una.
  - [Enlace a ETL sobre Distribución y Disponibilidad de Estaciones de Carga](#)

### 4. Análisis Exploratorio de Datos (EDA)

Para entender mejor los conjuntos de datos y extraer información relevante, realizamos un Análisis Exploratorio de Datos (EDA) sobre los siguientes archivos:

- **EDA sobre recorridos de taxis**:
  - **Objetivo**: Identificar patrones de viaje y zonas de alta demanda.
  - **Metodología**: Utilizamos técnicas de visualización de datos y estadísticas descriptivas para analizar los datos de recorridos de taxis. Esto incluyó gráficos de dispersión, histogramas y mapas de calor para visualizar las rutas y zonas más frecuentes.
  - **Resultados**: Identificamos patrones de uso durante diferentes horas del día, días de la semana y estaciones del año. También mapeamos las zonas de alta demanda y los tiempos de espera promedio.
  - [Enlace a EDA sobre Recorridos](#)

- **EDA sobre el rendimiento de vehículos híbridos enchufables**:
  - **Objetivo**: Evaluar la eficiencia y costos operativos.
  - **Metodología**: Analizamos los datos de rendimiento utilizando gráficos de línea, box plots y análisis de correlación para entender cómo varían los costos y la eficiencia bajo diferentes condiciones de uso.
  - **Resultados**: Determinamos que los vehículos híbridos enchufables tienen una alta eficiencia en entornos urbanos con baja velocidad y frecuentes paradas.
  - [Enlace a EDA sobre Rendimiento de Vehículos Híbridos Enchufables](#)

- **EDA sobre distribución y disponibilidad de estaciones de carga**:
  - **Objetivo**: Evaluar la cobertura y accesibilidad de las estaciones de carga.
  - **Metodología**: Utilizamos mapas de geolocalización y análisis de densidad para evaluar la distribución de las estaciones de carga en NYC.
  - **Resultados**: Identificamos áreas con buena cobertura y zonas que requieren una mayor infraestructura de carga.
  - [Enlace a EDA sobre Distribución y Disponibilidad de Estaciones de Carga](#)

### 5. Análisis Profundo y Conclusiones Preliminares

En esta etapa, llevamos a cabo un estudio profundo sobre la viabilidad de implementar una flota de vehículos eléctricos:

- **Estudio económico**:
  - **Objetivo**: Evaluar los costos y beneficios económicos.
  - **Metodología**: Realizamos un análisis de costos que incluyó la inversión inicial, costos de mantenimiento y operativos, y el análisis del retorno de inversión (ROI).
  - **Resultados**: Concluimos que los autos híbridos enchufables, especialmente el Toyota Prius Prime, ofrecen una mejor relación costo-beneficio debido a su menor costo inicial y eficiente rendimiento.
  - **Detalles**: El análisis mostró que, aunque los vehículos eléctricos puros tienen menores costos operativos, su alto costo inicial los hace menos atractivos desde una perspectiva económica a corto plazo.

- **Estudio ambiental**:
  - **Objetivo**: Evaluar el impacto ambiental.
  - **Metodología**: Analizamos las emisiones de CO2 y otros contaminantes comparando vehículos eléctricos, híbridos y de combustión interna.
  - **Resultados**: Aunque los vehículos eléctricos puros tienen cero emisiones locales, las diferencias no eran significativas cuando se consideraron las emisiones totales del ciclo de vida. Por lo tanto, decidimos centrarnos en el análisis económico.
  - **Detalles**: Incluimos un análisis del ciclo de vida completo, desde la producción hasta el reciclaje de los vehículos, para obtener una visión más completa de su impacto ambiental.

- **Inversiones en infraestructura**:
  - **Objetivo**: Determinar las inversiones necesarias para infraestructura de carga.
  - **Metodología**: Realizamos un análisis de costos para la instalación de estaciones de carga propias y evaluamos la viabilidad de asociaciones con proveedores de infraestructura de carga existentes.
  - **Resultados**: Determinamos que la inversión en infraestructura de carga es viable si se implementa de manera gradual, comenzando en zonas de alta demanda y expandiéndose según la adopción de vehículos eléctricos.
  - **Detalles**: Incluimos un plan de fases para la implementación de estaciones de carga, comenzando con ubicaciones estratégicas que maximicen el uso inicial.

### 6. Diseño de Base de Datos

Para manejar eficientemente los datos analizados, diseñamos y estructuramos una base de datos:

- **Modelo Entidad-Relación (E/R)**:
  - **Objetivo**: Organizar los datos de manera estructurada y eficiente.
  - **Metodología**: Creamos un modelo E/R que define las entidades principales y las relaciones entre ellas, asegurando la integridad y consistencia de los datos.
  - **Detalles**: Las entidades incluyeron tablas para recorridos de taxis, rendimiento de vehículos, estaciones de carga, entre otras. 

- **Asignación de claves primarias (PK) y claves foráneas (FK)**:
  - **Objetivo**: Definir relaciones y asegurar la integridad referencial.
  - **Metodología**: Asignamos claves primarias a cada tabla y definimos claves foráneas para establecer las relaciones entre tablas.
  - **Detalles**: Nos aseguramos de que cada tabla tuviera identificadores únicos y que las relaciones entre tablas fueran correctamente definidas para evitar inconsistencias.

- **Carga de tablas**:
  - **Objetivo**: Poner en funcionamiento la base de datos con los datos transformados.
  - **Metodología**: Implementamos las tablas en la base de datos y cargamos los datos transformados, verificando la integridad y calidad de los datos cargados.
  - **Detalles**: Utilizamos procedimientos almacenados para automatizar la carga de datos y realizar validaciones para asegurar que los datos cumplieran con los estándares de calidad.

### 7. Pipeline y ETL Automatizado

Para automatizar y mejorar la eficiencia del proceso ETL, utilizamos las siguientes herramientas en la plataforma GCP:

- **Cloud Functions para ETL Automatizado**:
  - **Objetivo**: Automatizar la extracción, transformación y carga de datos.
  - **Metodología**: Desarrollamos funciones en Google Cloud Functions que se activan en base a eventos para extraer datos de diversas fuentes, transformarlos según nuestras necesidades y cargarlos en BigQuery.
  - **Detalles**: Las Cloud Functions fueron programadas para manejar grandes volúmenes de datos de manera eficiente, asegurando que los procesos se ejecuten de manera escalable y sin interrupciones.
  - [Enlace a Cloud Functions](#)

- **BigQuery para Carga de Datos Transformados**:
  - **Objetivo**: Almacenar y analizar grandes volúmenes de datos transformados.
  - **Metodología**: Utilizamos BigQuery para almacenar los datos transformados, aprovechando su capacidad de manejar grandes volúmenes de datos y realizar consultas rápidas.
  - **Detalles**: Configuramos particiones y clustering en las tablas de BigQuery para optimizar las consultas y reducir costos.
  - [Enlace a BigQuery](#)

- **Conexión con PowerBI para Visualización**:
  - **Objetivo**: Crear visualizaciones interactivas y dashboards.
  - **Metodología**: Conectamos BigQuery con PowerBI para crear dashboards interactivos que permiten visualizar los datos de manera dinámica y facilitar la toma de decisiones.
  - **Detalles**: Diseñamos varias visualizaciones clave, incluyendo mapas de calor de demanda de taxis, gráficos de tendencias de uso y comparaciones de costos operativos entre diferentes tipos de vehículos.
  - [Enlace a PowerBI](#)

## Enlaces Importantes

- [Datos de Recorridos de Taxis](https://www.nyc.gov/site/tlc/about/tlc-trip-record-data.page)
- [ETL sobre Recorridos](#)
- [ETL sobre Rendimiento de Vehículos Híbridos Enchufables](#)
- [ETL sobre Distribución y Disponibilidad de Estaciones de Carga](#)
- [EDA sobre Recorridos](#)
- [EDA sobre Rendimiento de Vehículos Híbridos Enchufables](#)
- [EDA sobre Distribución y Disponibilidad de Estaciones de Carga](#)
- [Cloud Functions para ETL Automatizado](#)
- [BigQuery para Carga de Datos Transformados](#)
- [Conexión con PowerBI](#)

## Contacto

Para más información sobre el proyecto o para cualquier consulta, por favor contacta a:

- **Nombre**: [Tu Nombre]
- **Correo Electrónico**: [tu.correo@ejemplo.com]
- **Teléfono**: [+123 456 7890]
- **LinkedIn**: [Enlace a LinkedIn](#)

---

¡Gracias por tu interés en nuestro proyecto! Esperamos que este README proporcione una visión clara y detallada de nuestro trabajo y objetivos.
