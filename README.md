***Este es el primer proyecto individual del bootcamp de data science de SoyHenry desarrollado por mi.***

Consiste en la realización de un modelo de machine learning basado en las bases de datos de películas y series de algunas plataformas de streaming junto con las calificaciones de los usuarios de dichas plataformas.

*El rol a desarrollar es el de **Data Scientist**.*

En la primera etapa de este proyecto se realizarán los protocolos de *extracción, tratamiento y carga de datos **(ETL)***. En esta se analizarán todos los datasets para identificar qué valores son innecesarios para la finalidad del proyecto, así mismo, se limpiarán los datasets, eliminando o modificando los datos que no serán utilizados en las siguientes dos etapas del proyecto. Finalmente se exportarán los datasets como archivos CSV limpios para tener un mejor manejo de la información requerida.
Se hará el planteamiento de una API que responda a ciertas consultas necesarias para el usuario. 
Se definirán 4 consultas para el desarrollo de la API que son:
**1-** Película con mayor duración con filtros opcionales de AÑO, PLATAFORMA Y TIPO DE DURACIÓN. (la función debe llamarse *get_max_duration(year, platform, duration_type)*)
**2-** Cantidad de películas por plataforma con un puntaje mayor a XX en determinado año (la función debe llamarse *get_score_count(platform, scored, year)*)
**3-** Cantidad de películas por plataforma con filtro de PLATAFORMA. (La función debe llamarse *get_count_platform(platform)*)
**4-** Actor que más se repite según plataforma y año. (La función debe llamarse *get_actor(platform, year)*)
Esto con la finalidad de disponibilizar los datos de la empresa. Se hace uso del framework *FastAPI* para ejecutar esta parte de esta etapa.
Con la información obtenida y se definirá una visualización de *fastAPI* que se ejecutará en un localhost.

En la segunda etapa se llevará a cabo el proceso del *analisis exploratorio de datos **EDA***. En esta etapa se realizará un análisis de relación entre las diferentes columnas de los datasets obtenidos en el **ETL** con la finalidad de saber cuáles de las columnas que resultaron relevantes en la primera etapa serán útiles para la etapa final.
Del mismo modo que en la primera etapa se obtendrán datasets como archivos CSV limpios para manejarlo de mejor manera en la etapa siguiente.

En la etapa final se planteará un modelo de recomendación para los usuarios de algunas plataformas de streaming.
Utilizando los datos obtenidos en las dos etapas anteriores se dividirán los datos de las calificaciónes de los usuarios en una parte de entrenamiento y otra de evaluación. 
Se utilizará un modelo de SVD para hacer todo el trabajo de *machine learning **ML***.
Se harán algunas pruebas al azar para verificar si el modelo de recomendación funciona cómo es deseado.
Se optimizarán los hiperparámetros para el buen funcionamiento del modelo.
Finalmente se creará una interfaz que permita que el usuario haga uso del modelo de machine learning en su máquina o en línea inclusive.


En este proyecto se exploraron muchas herramientas muy interesantes, como lo son *Pandas, FastAPI, uvicorn, glob, matplotlib.pyplot, seaborn, scikit-surprise, numpy,* entre otras. Fue un proyecto bastante desafiante, pero a su vez bastante motivante y satisfactorio. 