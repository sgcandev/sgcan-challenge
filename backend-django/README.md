# Django API

## Requerimientos del sistema

* Versión de Python 3.10 o superior
* Git

## Instalación

``` bash
$ git clone https://github.com/sgcandev/sgcan-challenge

$ cd backend-django 

# Crear entorno virtual (opcional)
$ python -m venv venv
$ source ./venv/bin/activate

# Instalar dependencias
$ pip install -r requirements.txt

# Ejecutar servidor Django
$ python manage.py runserver

Watching for file changes with StatReloader
Performing system checks...

Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

```

## Endpoints

NOTA: Los endpoints son dinamicos, se esta utilizando la libreria [Django Dynamic Rest](https://github.com/AltSchool/dynamic-rest). Aquí solo dejamos algunos ejemplos.

### /api/transcripts

GET [/api/transcripts](http://127.0.0.1:8000/api/transcripts/)


```json
// Retorna el listado de todas las transcripciones
{
    "transcripts": [
        {
            "id": 47,
            "title": "How Far is Too Far_ _ The Age of A.I.",
            "date": "2024-05-17T18:10:00Z",
            "duration": 34,
            "summary": {
            },
            "video_url": "",
            "links": {
                "sentences": "sentences/"
            }
        },
        {
            "id": 48,
            "title": "¿Para qué usa ChatGPT Sam Altman en su día a día",
            "date": "2024-05-17T20:20:00Z",
            "duration": 2,
            "summary": {
               
            },
            "video_url": "",
            "links": {
                "sentences": "sentences/"
            }
        },
    ]
}

```

GET [/api/transcripts/47/?include[]=sentences](http://127.0.0.1:8000/api/transcripts/47/?include[]=sentences.*)

```json
// Retorna el listado de la transcripcion con ID=47 incluyendo sus sentencias
{
    "sentences": [
        {
            "id": 1117,
            "index": 0,
            "text": "Welcome to YouTube original stages.",
            "start_time": "7.36",
            "end_time": "9.634",
            "speaker_id": "0",
            "speaker_name": null,
            "transcript": 47
        },
        {
            "id": 1118,
            "index": 1,
            "text": "Once home to Howard Hughes's spruce Goose assembly hangar, and home to much of the first Iron man, filmed twelve years ago.",
            "start_time": "9.974",
            "end_time": "16.594",
            "speaker_id": "0",
            "speaker_name": null,
            "transcript": 47
        },
        ...
        ...
    ],
    "transcript": {
        "id": 47,
        "title": "How Far is Too Far_ _ The Age of A.I.",
        "date": "2024-05-17T18:10:00Z",
        "duration": 34,
        ...
    },
}
```

GET [/api/transcripts/47/sentences](http://127.0.0.1:8000/api/transcripts/47/sentences)

```json
// Retorna las sentencias de la transcripcion con ID=47
{
    "sentences": [
        {
            "id": 1117,
            "index": 0,
            "text": "Welcome to YouTube original stages.",
            "start_time": "7.36",
            "end_time": "9.634",
            "speaker_id": "0",
            "speaker_name": null,
            "transcript": 47
        },
        {
            "id": 1118,
            "index": 1,
            "text": "Once home to Howard Hughes's spruce Goose assembly hangar, and home to much of the first Iron man, filmed twelve years ago.",
            "start_time": "9.974",
            "end_time": "16.594",
            "speaker_id": "0",
            "speaker_name": null,
            "transcript": 47
        },
        ...
        ...
}
```

### /api/sentences

GET [GET /api/sentences](http://127.0.0.1:8000/api/sentences/)

```json
// Retorna el listado de todas las sentencias
{
    "sentences": [
         {
            "id": 1117,
            "index": 0,
            "text": "Welcome to YouTube original stages.",
            "start_time": "7.36",
            "end_time": "9.634",
            "speaker_id": "0",
            "speaker_name": null,
            "transcript": 47
        },
        ...
        ...
    ]
}
```

GET [GET /api/sentences/?filter{transcript}=47&sort[]=index](http://127.0.0.1:8000/api/sentences/?filter{transcript}=47&sort[]=index)

```json
// Retorna el listado de todas las sentencias de la transcripcion con ID=47
{
    "sentences": [
        {
            "id": 1117,
            "index": 0,
            "text": "Welcome to YouTube original stages.",
            "start_time": "7.36",
            "end_time": "9.634",
            "speaker_id": "0",
            "speaker_name": null,
            "transcript": 47
        },
        {
            "id": 1118,
            "index": 1,
            "text": "Once home to Howard Hughes's spruce Goose assembly hangar, and home to much of the first Iron man, filmed twelve years ago.",
            "start_time": "9.974",
            "end_time": "16.594",
            "speaker_id": "0",
            "speaker_name": null,
            "transcript": 47
        },
        ...
        ...
}
```
