### AUTORES
    Eduard Forés
    Denys Sydorenko

### PASOS A SEGUIR PARA EL FUNCIONAMIENTO DEL PROGRAMA 

    - paso 1: Creamos un BUCKET en nuestro servidor de AWS (Amazon Web Service), al cual subimos los 
    archivos a los cuales vamos a aplicar el algoritmo MapReducer.
    - paso 2: Configuramos las funciones lambda. En nuestro caso tenemos 2 lambda, una de ellas es el 
    Mapper que se encarga de hacer el HashMap del fichero y la segunda lambda es el Reducer, que se encarga 
    de hacer un HashMap concatenando los HashMap de los diferentes Mappers.
    - paso 3: Debemos sustituir las Claves en nuestros ficheros para que la comunicación sea segura.
    - paso 4: Nos colocamos en el directorio de la práctica y ejecutamos nuestro fichero Python con el 
    número de Mappers que queremos y el nombre del fichero del cual se va a hacer el HashMap. 
    (Comanda: python SD_Practica2.py 5 big.txt)
    - paso 5: Observamos los resultados obtenidos en el BUCKET de nuestro servidor AWS, ya que generamos 
    un fichero de salida en el cual se guarda el HashMap total y el número total de palabras (save_final.txt).
    
### DESCRIPCIÓN DE LA SOLUCIÓN

- Para que la práctica funcione, hemos tenido que aprender como funciona AWS y aprender a crear un BUCKET con el módulo S3 de AWS.
- Hemos tenido que configurar nuestro BUCKET con las 2 funciones lambda que hemos creado (mapper y reducer).
- Hemos tenido en cuenta la seguridad de la solución ya que hemos configurado la comunicación con la Claves de Acceso a nuestro BUCKET.
- Hemos creado un archivo upload_download.py desde el cual podemos cargar y descargar archivos a nuestro BUCKET. (Comanda: upload_download.py big.txt 1 en caso de SUBIR el archivo o upload_download.py big.txt 2 en caso de DESCARGAR el archivo)
- Desde el fichero SD_Practica2.py invocamos a los diferentes Mappers y al Reducer.
- Una vez hemos invocado a las 2 funciones, podemos observar lo que se devuelve en el fichero "save_final.txt" que se encontrará en nuestro BUCKET.
- Podemos observar también los resultados por pantalla.

### OBSERVACIONES DEL SPEED-UP

    Respecto a nuestra práctica 1 (www.github.com/denyssydorenko/SD_Practica1), podemos observar 
    que los resultados de los Speed-up son muy parecidos y bastante óptimos.

### OBERVACIONES DEL DISEÑO

    Debido a la complicación del particionamiento de ficheros, esta solución esta basada en que cada 
    Mapper va a leer un fichero entero. Es decir, en la práctica 1 
    (www.github.com/denyssydorenko/SD_Practica1) cada mapper leía un trozo del fichero 
    (fichero/núm. mappers), en la práctica 2 cada Mapper lee 1 fichero entero.
    Por lo tanto, las pruebas se han realizado con X Mappers entre los cuales han hecho el HashMap y 
    han devuelto el número total de palabras de los X ficheros.
    Por si no ha quedado del todo claro, el programa guarda en el fichero save_final.txt un HashMap final 
    que es la concatenación de los diferentes HashMap que devuelven los Mappers y el número total de 
    palabras que hay en este HashMap final.
