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

#### - Click en "New Registration", determinar un nombre para el app, dejar la opción por defecto de "Supporter account types" y colocar "http://localhost:8000/callback" en "Redirect URI" con "Select a plataform" puesto en "Web". Puesto todo eso, dar click en "Register"

![image](https://user-images.githubusercontent.com/103086601/197584688-c03f024c-433c-4ecd-8d85-6126f44cd166.png)

#### - Tomar copia del App Id. Luego ir a "Certification & secrets", dar click en "New client secret", colocar un nombre al secret, determinar la fecha de expiración, dar click en "Add" y tomar copia de la columna value (que es el "client secret" de la aplicación")

![image](https://user-images.githubusercontent.com/103086601/197590058-a8b519c4-1bbf-4d01-95d9-237b0dad34d7.png)
![image](https://user-images.githubusercontent.com/103086601/197590407-d5193fac-3c06-40ce-9fc4-afa0eaff2cbf.png)

#### - Por último, dar click en la opción "Authentication" y colocar la opción de "Allow public client flows" en "Yes". Para guardar la configuración, dar click en "Save"

![image](https://user-images.githubusercontent.com/103086601/197592053-51facb82-f927-4f12-acef-d478fbc693cf.png)

## 2) Configuración del script


