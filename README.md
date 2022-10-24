# lectura_pdfs_sunat
Script de Python que lee las facturas PDF de SUNAT cargadas en una carpeta específica de OneDrive, extrae la información necesaria para el área de finanzas y construye una tabla con dicha información

## Requerimientos generales
1. Crear una aplicación dentro de Microsfot Azure con la cuenta de correo de 99minutos para poder acceder a las funciones del API de OneDrive
2. Setear el script utilizando la configuración de la aplicación en Azure

## 1) Aplicación en Azure para poder acceder al API de Microsoft 365 - OneDrive
Para poder acceder a los archivos donde se vayan a guardar los PDF que se van leer guardados en una carpeta de OneDrive, es necesario realiza la conexión con el API de Microsfot 365. Para esto, se requeriere de utilizar una aplicación registrada en Azure.

### Crear y configurar una aplicación en Azure
#### - Entrar con la cuenta de Outlook a la aplicación de Azure e ir a App Registrations (o buscarlo en la barra de búsqueda)
![image](https://user-images.githubusercontent.com/103086601/197580663-b872e405-1a63-4f0d-8418-ebd13ed13809.png)

#### - Click en "New Registration", determinar un nombre para el app, colocar la segunda opcion de "Supporter account types" ("Multitenant") y colocar "http://localhost:8000/callback" en "Redirect URI" con "Select a plataform" puesto en "Web". Puesto todo eso, dar click en "Register"

![image](https://user-images.githubusercontent.com/103086601/197595558-61e90d5c-8ea4-4a4f-9595-3245ff91ed27.png)

#### - Tomar copia del App Id. Luego ir a "Certification & secrets", dar click en "New client secret", colocar un nombre al secret, determinar la fecha de expiración, dar click en "Add" y tomar copia de la columna value (que es el "client secret" de la aplicación")

![image](https://user-images.githubusercontent.com/103086601/197590058-a8b519c4-1bbf-4d01-95d9-237b0dad34d7.png)
![image](https://user-images.githubusercontent.com/103086601/197590407-d5193fac-3c06-40ce-9fc4-afa0eaff2cbf.png)

#### - Por último, dar click en la opción "Authentication" y colocar la opción de "Allow public client flows" en "Yes". Para guardar la configuración, dar click en "Save"

![image](https://user-images.githubusercontent.com/103086601/197592053-51facb82-f927-4f12-acef-d478fbc693cf.png)

## 2) Configuración y run del script

Las siguientes lineas son las que tienen que ser configuradas para poder correr el script

![image](https://user-images.githubusercontent.com/103086601/197592779-3515440b-6d62-4e40-9d7c-18876812b11d.png)
![image](https://user-images.githubusercontent.com/103086601/197598466-f607dc32-8ba8-417e-8a2a-f0ac0dda9092.png)

El primero es determinar donde se va a colocar el output de la tabla final con la información de las boletas. El segundo es el APP_ID de la aplicación creada anteriormente. Las dos siguientes hacen referencia a la carpeta en OneDrive donde se encuentran los PDFs que se van a leer, el cual tiene que se configurado en la variable "ruta"

Una vez puesto todo, al hacer run al script, se va a acceder a la solicitud de permisos de Microsoft Online para poder acceder a la utilización del API. Lo que se tiene que hacer es lo siguiente.

#### 1) Aparecerá la web de solicitud de permisos pidiendo un código. Dicho código aparece en los resultados del mismo script. Copiar y pegar el código y continuar con la identificación.

![image](https://user-images.githubusercontent.com/103086601/197596339-1a86d91b-7155-48ed-8893-a4fb8ec93d68.png)
![image](https://user-images.githubusercontent.com/103086601/197596398-978fc2d4-4098-471c-b083-809fe2d3435d.png)

#### 2) Seleccionar la cuenta de Outlook de 99 con al que se registro la aplicación en Azure. Dar en "Aceptar" y saldrá el mensaje de confirmación. Luego, cerrar la página. El script continuará con la parte de lectura de PDFS.








