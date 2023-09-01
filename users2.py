from fastapi import FastAPI

from pydantic import BaseModel

app= FastAPI()

class User(BaseModel):
    id: int
    nombre: str
    autor: str
    idioma: str
    anio: str
    editorial: str

users_list= [User(id=1, nombre = 'Las mil y una noches',autor = 'Cervantes',idioma = 'Ruso',anio = '1850',editorial = 'Akal' ), 
             User(id=2, nombre = 'Las mil y una noches',autor = 'Cervantes',idioma = 'Inglés',anio = '2003',editorial = 'Akal' ), 
             User(id=3, nombre = 'Las mil y una noches',autor = 'Cervantes',idioma = 'Francés',anio = '2003',editorial = 'Akal' ), 
             User(id=4, nombre = 'Las mil y una noches',autor = 'Cervantes',idioma = 'Inglés',anio = '1850',editorial = 'HERDER' ), 
             User(id=5, nombre = 'Libro de job',autor = 'Celine',idioma = 'Inglés',anio = '1930',editorial = 'Akal' ), 
             User(id=6, nombre = 'Las mil y una noches',autor = 'Kafka',idioma = 'Ruso',anio = '1850',editorial = 'Austral' ), 
             User(id=7, nombre = 'Las mil y una noches',autor = 'Kafka',idioma = 'Francés',anio = '1850',editorial = 'Austral' ), 
             User(id=8, nombre = 'Libro de job',autor = 'Cervantes',idioma = 'Ruso',anio = '2003',editorial = 'HERDER' ), 
             User(id=9, nombre = 'Divina comedia',autor = 'Kafka',idioma = 'Francés',anio = '2003',editorial = 'HERDER' ), 
             User(id=10, nombre = 'Las mil y una noches',autor = 'Celine',idioma = 'Francés',anio = '1850',editorial = 'HERDER' ), 
             User(id=11, nombre = 'Libro de job',autor = 'Cervantes',idioma = 'Inglés',anio = '1850',editorial = 'Austral' ), 
             User(id=12, nombre = 'Las mil y una noches',autor = 'Kafka',idioma = 'Inglés',anio = '1930',editorial = 'HERDER' ), 
             User(id=13, nombre = 'Las mil y una noches',autor = 'Kafka',idioma = 'Inglés',anio = '1930',editorial = 'Akal' ), 
             User(id=14, nombre = 'Las mil y una noches',autor = 'Cervantes',idioma = 'Francés',anio = '2003',editorial = 'Akal' ), 
             User(id=15, nombre = 'Libro de job',autor = 'Cervantes',idioma = 'Ruso',anio = '1850',editorial = 'Akal' ), 
             User(id=16, nombre = 'Divina comedia',autor = 'Cervantes',idioma = 'Inglés',anio = '2003',editorial = 'Austral' ), 
             User(id=17, nombre = 'Libro de job',autor = 'Cervantes',idioma = 'Ruso',anio = '2003',editorial = 'Austral' ), 
             User(id=18, nombre = 'Libro de job',autor = 'Kafka',idioma = 'Inglés',anio = '1850',editorial = 'Akal' ), 
             User(id=19, nombre = 'Libro de job',autor = 'Kafka',idioma = 'Francés',anio = '1930',editorial = 'HERDER' ), 
             User(id=20, nombre = 'Las mil y una noches',autor = 'Cervantes',idioma = 'Francés',anio = '1850',editorial = 'Akal' ), 
             User(id=21, nombre = 'Libro de job',autor = 'Celine',idioma = 'Francés',anio = '1930',editorial = 'Austral' ), 
             User(id=22, nombre = 'Divina comedia',autor = 'Cervantes',idioma = 'Ruso',anio = '1930',editorial = 'Akal' ), 
             User(id=23, nombre = 'Las mil y una noches',autor = 'Cervantes',idioma = 'Inglés',anio = '1930',editorial = 'Austral' ), 
             User(id=24, nombre = 'Divina comedia',autor = 'Cervantes',idioma = 'Inglés',anio = '2003',editorial = 'Akal' ), 
             User(id=25, nombre = 'Las mil y una noches',autor = 'Cervantes',idioma = 'Ruso',anio = '1850',editorial = 'Akal' ), 
             User(id=26, nombre = 'Divina comedia',autor = 'Kafka',idioma = 'Francés',anio = '1850',editorial = 'Austral' ), 
             User(id=27, nombre = 'Divina comedia',autor = 'Kafka',idioma = 'Francés',anio = '2003',editorial = 'Austral' ), 
             User(id=28, nombre = 'Divina comedia',autor = 'Cervantes',idioma = 'Ruso',anio = '2003',editorial = 'Akal' ), 
             User(id=29, nombre = 'Libro de job',autor = 'Cervantes',idioma = 'Francés',anio = '1930',editorial = 'Austral' ), 
             User(id=30, nombre = 'Libro de job',autor = 'Celine',idioma = 'Francés',anio = '1930',editorial = 'HERDER' ), 
             User(id=31, nombre = 'Libro de job',autor = 'Celine',idioma = 'Francés',anio = '1930',editorial = 'Akal' ), 
             User(id=32, nombre = 'Libro de job',autor = 'Celine',idioma = 'Inglés',anio = '1930',editorial = 'HERDER' ), 
             User(id=33, nombre = 'Las mil y una noches',autor = 'Cervantes',idioma = 'Ruso',anio = '1930',editorial = 'HERDER' ), 
             User(id=34, nombre = 'Las mil y una noches',autor = 'Kafka',idioma = 'Inglés',anio = '1850',editorial = 'HERDER' ), 
             User(id=35, nombre = 'Divina comedia',autor = 'Cervantes',idioma = 'Inglés',anio = '1850',editorial = 'Austral' ), 
             User(id=36, nombre = 'Divina comedia',autor = 'Cervantes',idioma = 'Francés',anio = '1850',editorial = 'Akal' ), 
             User(id=37, nombre = 'Las mil y una noches',autor = 'Celine',idioma = 'Francés',anio = '1930',editorial = 'Austral' ), 
             User(id=38, nombre = 'Las mil y una noches',autor = 'Kafka',idioma = 'Inglés',anio = '1930',editorial = 'Akal' ), 
             User(id=39, nombre = 'Divina comedia',autor = 'Cervantes',idioma = 'Ruso',anio = '1930',editorial = 'HERDER' ), 
             User(id=40, nombre = 'Libro de job',autor = 'Celine',idioma = 'Ruso',anio = '2003',editorial = 'HERDER' ), 
             User(id=41, nombre = 'Libro de job',autor = 'Kafka',idioma = 'Francés',anio = '2003',editorial = 'Akal' ), 
             User(id=42, nombre = 'Las mil y una noches',autor = 'Cervantes',idioma = 'Ruso',anio = '1850',editorial = 'Austral' ), 
             User(id=43, nombre = 'Divina comedia',autor = 'Kafka',idioma = 'Francés',anio = '1930',editorial = 'HERDER' ), 
             User(id=44, nombre = 'Divina comedia',autor = 'Cervantes',idioma = 'Ruso',anio = '1850',editorial = 'Akal' ), 
             User(id=45, nombre = 'Libro de job',autor = 'Kafka',idioma = 'Francés',anio = '2003',editorial = 'HERDER' ), 
             User(id=46, nombre = 'Divina comedia',autor = 'Celine',idioma = 'Ruso',anio = '1850',editorial = 'HERDER' ), 
             User(id=47, nombre = 'Divina comedia',autor = 'Cervantes',idioma = 'Inglés',anio = '1930',editorial = 'Austral' ), 
             User(id=48, nombre = 'Libro de job',autor = 'Celine',idioma = 'Ruso',anio = '1930',editorial = 'Austral' ), 
             User(id=49, nombre = 'Las mil y una noches',autor = 'Cervantes',idioma = 'Ruso',anio = '1930',editorial = 'Austral' ), 
             User(id=50, nombre = 'Las mil y una noches',autor = 'Kafka',idioma = 'Inglés',anio = '2003',editorial = 'Akal' ), 
             User(id=51, nombre = 'Las mil y una noches',autor = 'Kafka',idioma = 'Francés',anio = '2003',editorial = 'Austral' ), 
             User(id=52, nombre = 'Las mil y una noches',autor = 'Cervantes',idioma = 'Francés',anio = '2003',editorial = 'Akal' ), 
             User(id=53, nombre = 'Las mil y una noches',autor = 'Celine',idioma = 'Ruso',anio = '2003',editorial = 'HERDER' ), 
             User(id=54, nombre = 'Divina comedia',autor = 'Celine',idioma = 'Ruso',anio = '2003',editorial = 'Akal' ), 
             User(id=55, nombre = 'Las mil y una noches',autor = 'Cervantes',idioma = 'Inglés',anio = '1930',editorial = 'HERDER' ), 
             User(id=56, nombre = 'Libro de job',autor = 'Kafka',idioma = 'Inglés',anio = '2003',editorial = 'Austral' ), 
             User(id=57, nombre = 'Divina comedia',autor = 'Celine',idioma = 'Francés',anio = '1850',editorial = 'Austral' ), 
             User(id=58, nombre = 'Las mil y una noches',autor = 'Celine',idioma = 'Ruso',anio = '1850',editorial = 'Akal' ), 
             User(id=59, nombre = 'Libro de job',autor = 'Cervantes',idioma = 'Ruso',anio = '1930',editorial = 'Akal' ), 
             User(id=60, nombre = 'Libro de job',autor = 'Celine',idioma = 'Francés',anio = '1850',editorial = 'Akal' ), 
             User(id=61, nombre = 'Divina comedia',autor = 'Celine',idioma = 'Francés',anio = '2003',editorial = 'Akal' ), 
             User(id=62, nombre = 'Divina comedia',autor = 'Celine',idioma = 'Francés',anio = '2003',editorial = 'Austral' ), 
             User(id=63, nombre = 'Libro de job',autor = 'Cervantes',idioma = 'Ruso',anio = '2003',editorial = 'Austral' ), 
             User(id=64, nombre = 'Divina comedia',autor = 'Celine',idioma = 'Inglés',anio = '2003',editorial = 'Akal' ), 
             User(id=65, nombre = 'Divina comedia',autor = 'Cervantes',idioma = 'Ruso',anio = '2003',editorial = 'Akal' ), 
             User(id=66, nombre = 'Libro de job',autor = 'Kafka',idioma = 'Inglés',anio = '2003',editorial = 'Austral' ), 
             User(id=67, nombre = 'Divina comedia',autor = 'Cervantes',idioma = 'Francés',anio = '1850',editorial = 'Akal' ), 
             User(id=68, nombre = 'Las mil y una noches',autor = 'Kafka',idioma = 'Inglés',anio = '2003',editorial = 'Austral' ), 
             User(id=69, nombre = 'Las mil y una noches',autor = 'Kafka',idioma = 'Ruso',anio = '1850',editorial = 'Austral' ), 
             User(id=70, nombre = 'Divina comedia',autor = 'Celine',idioma = 'Ruso',anio = '2003',editorial = 'Akal' ), 
             User(id=71, nombre = 'Divina comedia',autor = 'Kafka',idioma = 'Inglés',anio = '1850',editorial = 'Akal' ), 
             User(id=72, nombre = 'Divina comedia',autor = 'Celine',idioma = 'Ruso',anio = '1930',editorial = 'Austral' ), 
             User(id=73, nombre = 'Libro de job',autor = 'Cervantes',idioma = 'Ruso',anio = '1850',editorial = 'HERDER' ), 
             User(id=74, nombre = 'Libro de job',autor = 'Kafka',idioma = 'Ruso',anio = '1930',editorial = 'Austral' ), 
             User(id=75, nombre = 'Las mil y una noches',autor = 'Cervantes',idioma = 'Ruso',anio = '2003',editorial = 'Austral' ), 
             User(id=76, nombre = 'Las mil y una noches',autor = 'Kafka',idioma = 'Francés',anio = '1930',editorial = 'Austral' ), 
             User(id=77, nombre = 'Las mil y una noches',autor = 'Kafka',idioma = 'Ruso',anio = '1850',editorial = 'Akal' ), 
             User(id=78, nombre = 'Las mil y una noches',autor = 'Celine',idioma = 'Ruso',anio = '1850',editorial = 'HERDER' ), 
             User(id=79, nombre = 'Divina comedia',autor = 'Celine',idioma = 'Ruso',anio = '2003',editorial = 'Austral' ), 
             User(id=80, nombre = 'Libro de job',autor = 'Kafka',idioma = 'Inglés',anio = '2003',editorial = 'HERDER' ), 
             User(id=81, nombre = 'Libro de job',autor = 'Cervantes',idioma = 'Inglés',anio = '2003',editorial = 'Akal' ), 
             User(id=82, nombre = 'Las mil y una noches',autor = 'Cervantes',idioma = 'Ruso',anio = '2003',editorial = 'Akal' ), 
             User(id=83, nombre = 'Libro de job',autor = 'Cervantes',idioma = 'Inglés',anio = '1930',editorial = 'Austral' ), 
             User(id=84, nombre = 'Divina comedia',autor = 'Cervantes',idioma = 'Inglés',anio = '1850',editorial = 'HERDER' ), 
             User(id=85, nombre = 'Libro de job',autor = 'Celine',idioma = 'Ruso',anio = '1850',editorial = 'HERDER' ), 
             User(id=86, nombre = 'Libro de job',autor = 'Celine',idioma = 'Inglés',anio = '1930',editorial = 'Akal' ), 
             User(id=87, nombre = 'Libro de job',autor = 'Kafka',idioma = 'Ruso',anio = '1850',editorial = 'HERDER' ), 
             User(id=88, nombre = 'Las mil y una noches',autor = 'Kafka',idioma = 'Inglés',anio = '2003',editorial = 'Akal' ), 
             User(id=89, nombre = 'Las mil y una noches',autor = 'Kafka',idioma = 'Inglés',anio = '1850',editorial = 'Akal' ), 
             User(id=90, nombre = 'Divina comedia',autor = 'Celine',idioma = 'Francés',anio = '1930',editorial = 'Austral' ), 
             User(id=91, nombre = 'Divina comedia',autor = 'Celine',idioma = 'Inglés',anio = '2003',editorial = 'Austral' ), 
             User(id=92, nombre = 'Libro de job',autor = 'Kafka',idioma = 'Ruso',anio = '1930',editorial = 'HERDER' ), 
             User(id=93, nombre = 'Divina comedia',autor = 'Celine',idioma = 'Francés',anio = '2003',editorial = 'Austral' ), 
             User(id=94, nombre = 'Libro de job',autor = 'Cervantes',idioma = 'Ruso',anio = '1930',editorial = 'Austral' ), 
             User(id=95, nombre = 'Divina comedia',autor = 'Celine',idioma = 'Francés',anio = '1850',editorial = 'HERDER' ), 
             User(id=96, nombre = 'Las mil y una noches',autor = 'Celine',idioma = 'Francés',anio = '1930',editorial = 'Akal' ), 
             User(id=97, nombre = 'Libro de job',autor = 'Cervantes',idioma = 'Ruso',anio = '1930',editorial = 'Austral' ), 
             User(id=98, nombre = 'Las mil y una noches',autor = 'Cervantes',idioma = 'Inglés',anio = '1930',editorial = 'HERDER' ), 
             User(id=99, nombre = 'Divina comedia',autor = 'Celine',idioma = 'Inglés',anio = '2003',editorial = 'HERDER' ), 
             User(id=100, nombre = 'Libro de job',autor = 'Celine',idioma = 'Inglés',anio = '1930',editorial = 'Austral' ), 
             User(id=101, nombre = 'Las mil y una noches',autor = 'Cervantes',idioma = 'Ruso',anio = '1930',editorial = 'Akal' ), 
             User(id=102, nombre = 'Libro de job',autor = 'Celine',idioma = 'Francés',anio = '1850',editorial = 'HERDER' ), 
             User(id=103, nombre = 'Las mil y una noches',autor = 'Cervantes',idioma = 'Inglés',anio = '1930',editorial = 'Austral' ), 
             User(id=104, nombre = 'Las mil y una noches',autor = 'Celine',idioma = 'Ruso',anio = '1850',editorial = 'Akal' ), 
             User(id=105, nombre = 'Las mil y una noches',autor = 'Celine',idioma = 'Francés',anio = '1850',editorial = 'Austral' ), 
             User(id=106, nombre = 'Las mil y una noches',autor = 'Cervantes',idioma = 'Inglés',anio = '1930',editorial = 'Austral' ), 
             User(id=107, nombre = 'Divina comedia',autor = 'Kafka',idioma = 'Ruso',anio = '2003',editorial = 'Austral' ), 
             User(id=108, nombre = 'Libro de job',autor = 'Cervantes',idioma = 'Ruso',anio = '2003',editorial = 'Akal' ), 
             User(id=109, nombre = 'Las mil y una noches',autor = 'Celine',idioma = 'Inglés',anio = '1930',editorial = 'Austral' ), 
             User(id=110, nombre = 'Divina comedia',autor = 'Cervantes',idioma = 'Ruso',anio = '2003',editorial = 'HERDER' ), 
             User(id=111, nombre = 'Las mil y una noches',autor = 'Kafka',idioma = 'Ruso',anio = '2003',editorial = 'HERDER' ), 
             User(id=112, nombre = 'Libro de job',autor = 'Cervantes',idioma = 'Francés',anio = '1850',editorial = 'Austral' ), 
             User(id=113, nombre = 'Las mil y una noches',autor = 'Cervantes',idioma = 'Ruso',anio = '1930',editorial = 'Austral' ), 
             User(id=114, nombre = 'Divina comedia',autor = 'Kafka',idioma = 'Inglés',anio = '2003',editorial = 'Austral' ), 
             User(id=115, nombre = 'Las mil y una noches',autor = 'Cervantes',idioma = 'Francés',anio = '1930',editorial = 'HERDER' ), 
             User(id=116, nombre = 'Libro de job',autor = 'Cervantes',idioma = 'Francés',anio = '2003',editorial = 'HERDER' ), 
             User(id=117, nombre = 'Libro de job',autor = 'Celine',idioma = 'Francés',anio = '1930',editorial = 'Austral' ), 
             User(id=118, nombre = 'Libro de job',autor = 'Kafka',idioma = 'Ruso',anio = '2003',editorial = 'Austral' ), 
             User(id=119, nombre = 'Libro de job',autor = 'Celine',idioma = 'Ruso',anio = '1850',editorial = 'Austral' ), 
             User(id=120, nombre = 'Divina comedia',autor = 'Cervantes',idioma = 'Ruso',anio = '2003',editorial = 'Akal' ), 
             User(id=121, nombre = 'Las mil y una noches',autor = 'Celine',idioma = 'Francés',anio = '2003',editorial = 'HERDER' ), 
             User(id=122, nombre = 'Libro de job',autor = 'Kafka',idioma = 'Francés',anio = '1930',editorial = 'HERDER' ), 
             User(id=123, nombre = 'Las mil y una noches',autor = 'Cervantes',idioma = 'Francés',anio = '2003',editorial = 'HERDER' ), 
             User(id=124, nombre = 'Las mil y una noches',autor = 'Cervantes',idioma = 'Francés',anio = '2003',editorial = 'HERDER' ), 
             User(id=125, nombre = 'Divina comedia',autor = 'Kafka',idioma = 'Francés',anio = '2003',editorial = 'Akal' ), 
             User(id=126, nombre = 'Libro de job',autor = 'Cervantes',idioma = 'Francés',anio = '1930',editorial = 'Austral' ), 
             User(id=127, nombre = 'Divina comedia',autor = 'Celine',idioma = 'Inglés',anio = '1930',editorial = 'Akal' ), 
             User(id=128, nombre = 'Divina comedia',autor = 'Celine',idioma = 'Ruso',anio = '1850',editorial = 'Akal' ), 
             User(id=129, nombre = 'Libro de job',autor = 'Celine',idioma = 'Francés',anio = '1930',editorial = 'Austral' ), 
             User(id=130, nombre = 'Libro de job',autor = 'Kafka',idioma = 'Inglés',anio = '1850',editorial = 'HERDER' ), 
             User(id=131, nombre = 'Divina comedia',autor = 'Kafka',idioma = 'Ruso',anio = '1850',editorial = 'Austral' ), 
             User(id=132, nombre = 'Divina comedia',autor = 'Cervantes',idioma = 'Inglés',anio = '1930',editorial = 'Austral' ), 
             User(id=133, nombre = 'Libro de job',autor = 'Kafka',idioma = 'Francés',anio = '1930',editorial = 'Austral' ), 
             User(id=134, nombre = 'Libro de job',autor = 'Celine',idioma = 'Ruso',anio = '1850',editorial = 'Austral' ), 
             User(id=135, nombre = 'Las mil y una noches',autor = 'Celine',idioma = 'Ruso',anio = '2003',editorial = 'Akal' ), 
             User(id=136, nombre = 'Divina comedia',autor = 'Kafka',idioma = 'Ruso',anio = '2003',editorial = 'HERDER' ), 
             User(id=137, nombre = 'Libro de job',autor = 'Celine',idioma = 'Ruso',anio = '1850',editorial = 'HERDER' ), 
             User(id=138, nombre = 'Libro de job',autor = 'Celine',idioma = 'Francés',anio = '1850',editorial = 'HERDER' ),
             User(id=139, nombre = 'Las mil y una noches',autor = 'Celine',idioma = 'Ruso',anio = '1930',editorial = 'HERDER' ), 
             User(id=140, nombre = 'Las mil y una noches',autor = 'Cervantes',idioma = 'Francés',anio = '1930',editorial = 'Akal' ), 
             User(id=141, nombre = 'Libro de job',autor = 'Cervantes',idioma = 'Ruso',anio = '1930',editorial = 'HERDER' ), 
             User(id=142, nombre = 'Divina comedia',autor = 'Kafka',idioma = 'Ruso',anio = '1850',editorial = 'Austral' ), 
             User(id=143, nombre = 'Libro de job',autor = 'Celine',idioma = 'Francés',anio = '1850',editorial = 'HERDER' ), 
             User(id=144, nombre = 'Divina comedia',autor = 'Celine',idioma = 'Inglés',anio = '1850',editorial = 'Akal' ), 
             User(id=145, nombre = 'Divina comedia',autor = 'Cervantes',idioma = 'Francés',anio = '2003',editorial = 'HERDER' ), 
             User(id=146, nombre = 'Divina comedia',autor = 'Cervantes',idioma = 'Inglés',anio = '1850',editorial = 'Austral' ), 
             User(id=147, nombre = 'Divina comedia',autor = 'Kafka',idioma = 'Ruso',anio = '1850',editorial = 'Austral' ), 
             User(id=148, nombre = 'Libro de job',autor = 'Kafka',idioma = 'Ruso',anio = '1850',editorial = 'Austral' ), 
             User(id=149, nombre = 'Divina comedia',autor = 'Kafka',idioma = 'Inglés',anio = '1850',editorial = 'HERDER' ), 
             User(id=150, nombre = 'Las mil y una noches',autor = 'Cervantes',idioma = 'Ruso',anio = '1850',editorial = 'Austral' ), 
             User(id=151, nombre = 'Divina comedia',autor = 'Celine',idioma = 'Francés',anio = '1930',editorial = 'Austral' ), 
             User(id=152, nombre = 'Libro de job',autor = 'Cervantes',idioma = 'Inglés',anio = '1850',editorial = 'HERDER' ), 
             User(id=153, nombre = 'Libro de job',autor = 'Celine',idioma = 'Francés',anio = '2003',editorial = 'Austral' ), 
             User(id=154, nombre = 'Las mil y una noches',autor = 'Celine',idioma = 'Ruso',anio = '1930',editorial = 'Akal' ), 
             User(id=155, nombre = 'Libro de job',autor = 'Kafka',idioma = 'Ruso',anio = '2003',editorial = 'Austral' ), 
             User(id=156, nombre = 'Libro de job',autor = 'Celine',idioma = 'Inglés',anio = '1930',editorial = 'Austral' ), 
             User(id=157, nombre = 'Libro de job',autor = 'Kafka',idioma = 'Inglés',anio = '2003',editorial = 'Austral' ), 
             User(id=158, nombre = 'Divina comedia',autor = 'Kafka',idioma = 'Inglés',anio = '2003',editorial = 'Akal' ), 
             User(id=159, nombre = 'Las mil y una noches',autor = 'Cervantes',idioma = 'Francés',anio = '2003',editorial = 'Akal' ), 
             User(id=160, nombre = 'Libro de job',autor = 'Kafka',idioma = 'Ruso',anio = '1850',editorial = 'Austral' ), 
             User(id=161, nombre = 'Libro de job',autor = 'Cervantes',idioma = 'Francés',anio = '2003',editorial = 'Austral' ), 
             User(id=162, nombre = 'Libro de job',autor = 'Cervantes',idioma = 'Ruso',anio = '2003',editorial = 'Akal' ), 
             User(id=163, nombre = 'Libro de job',autor = 'Cervantes',idioma = 'Ruso',anio = '1930',editorial = 'Akal' ), 
             User(id=164, nombre = 'Divina comedia',autor = 'Celine',idioma = 'Ruso',anio = '1850',editorial = 'Akal' ), User(id=165, nombre = 'Libro de job',autor = 'Kafka',idioma = 'Francés',anio = '2003',editorial = 'Akal' ), User(id=166, nombre = 'Las mil y una noches',autor = 'Celine',idioma = 'Francés',anio = '2003',editorial = 'HERDER' ), User(id=167, nombre = 'Libro de job',autor = 'Celine',idioma = 'Ruso',anio = '1930',editorial = 'HERDER' ), User(id=168, nombre = 'Libro de job',autor = 'Celine',idioma = 'Ruso',anio = '1930',editorial = 'Austral' ), User(id=169, nombre = 'Las mil y una noches',autor = 'Cervantes',idioma = 'Inglés',anio = '1850',editorial = 'Austral' ), User(id=170, nombre = 'Las mil y una noches',autor = 'Celine',idioma = 'Francés',anio = '2003',editorial = 'Austral' ), User(id=171, nombre = 'Divina comedia',autor = 'Kafka',idioma = 'Inglés',anio = '2003',editorial = 'Akal' ), User(id=172, nombre = 'Las mil y una noches',autor = 'Cervantes',idioma = 'Ruso',anio = '1930',editorial = 'HERDER' ), User(id=173, nombre = 'Divina comedia',autor = 'Kafka',idioma = 'Inglés',anio = '1850',editorial = 'Austral' ), User(id=174, nombre = 'Libro de job',autor = 'Kafka',idioma = 'Inglés',anio = '2003',editorial = 'HERDER' ), User(id=175, nombre = 'Divina comedia',autor = 'Celine',idioma = 'Inglés',anio = '2003',editorial = 'HERDER' ), User(id=176, nombre = 'Divina comedia',autor = 'Kafka',idioma = 'Inglés',anio = '2003',editorial = 'Akal' ), User(id=177, nombre = 'Libro de job',autor = 'Kafka',idioma = 'Ruso',anio = '1930',editorial = 'Akal' ), User(id=178, nombre = 'Libro de job',autor = 'Cervantes',idioma = 'Ruso',anio = '2003',editorial = 'HERDER' ), User(id=179, nombre = 'Libro de job',autor = 'Kafka',idioma = 'Inglés',anio = '1850',editorial = 'Austral' ), User(id=180, nombre = 'Libro de job',autor = 'Cervantes',idioma = 'Francés',anio = '1930',editorial = 'HERDER' ), User(id=181, nombre = 'Las mil y una noches',autor = 'Kafka',idioma = 'Ruso',anio = '1930',editorial = 'Akal' ), User(id=182, nombre = 'Divina comedia',autor = 'Kafka',idioma = 'Inglés',anio = '1930',editorial = 'HERDER' ), User(id=183, nombre = 'Libro de job',autor = 'Kafka',idioma = 'Francés',anio = '1930',editorial = 'Austral' ), User(id=184, nombre = 'Libro de job',autor = 'Kafka',idioma = 'Ruso',anio = '2003',editorial = 'Austral' ), User(id=185, nombre = 'Las mil y una noches',autor = 'Celine',idioma = 'Francés',anio = '1850',editorial = 'HERDER' ), User(id=186, nombre = 'Las mil y una noches',autor = 'Kafka',idioma = 'Inglés',anio = '1850',editorial = 'Akal' ), User(id=187, nombre = 'Libro de job',autor = 'Cervantes',idioma = 'Ruso',anio = '2003',editorial = 'Austral' ), User(id=188, nombre = 'Las mil y una noches',autor = 'Celine',idioma = 'Inglés',anio = '2003',editorial = 'Austral' ), User(id=189, nombre = 'Las mil y una noches',autor = 'Celine',idioma = 'Ruso',anio = '2003',editorial = 'HERDER' ), User(id=190, nombre = 'Libro de job',autor = 'Kafka',idioma = 'Ruso',anio = '2003',editorial = 'Akal' ), User(id=191, nombre = 'Las mil y una noches',autor = 'Cervantes',idioma = 'Francés',anio = '1930',editorial = 'HERDER' ), User(id=192, nombre = 'Divina comedia',autor = 'Cervantes',idioma = 'Ruso',anio = '1930',editorial = 'HERDER' ), User(id=193, nombre = 'Las mil y una noches',autor = 'Cervantes',idioma = 'Ruso',anio = '1850',editorial = 'HERDER' ), User(id=194, nombre = 'Libro de job',autor = 'Celine',idioma = 'Francés',anio = '1930',editorial = 'Akal' ), User(id=195, nombre = 'Divina comedia',autor = 'Celine',idioma = 'Francés',anio = '1850',editorial = 'Akal' ), User(id=196, nombre = 'Divina comedia',autor = 'Kafka',idioma = 'Francés',anio = '1850',editorial = 'HERDER' ), User(id=197, nombre = 'Las mil y una noches',autor = 'Celine',idioma = 'Ruso',anio = '1850',editorial = 'HERDER' ), User(id=198, nombre = 'Divina comedia',autor = 'Kafka',idioma = 'Ruso',anio = '1930',editorial = 'Austral' ), User(id=199, nombre = 'Las mil y una noches',autor = 'Celine',idioma = 'Inglés',anio = '1930',editorial = 'Austral' ), User(id=200, nombre = 'Divina comedia',autor = 'Cervantes',idioma = 'Francés',anio = '1850',editorial = 'Akal' )]

@app. get("/usersclass/")
async def usersclass():
    return (users_list)

@app.get("/usersclass/{id}")
async def usersclass(id:int):
    users=filter (lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return{"error":"No se ha encontrado el usuario"}
    
 #***Get con Filtro Query
@app.get("/usersclass2/")
async def usersclass(autor:str, idioma:str):
    users=list(filter (lambda user: user.autor == autor, users_list))#Función de orden superior
    users1=list(filter (lambda user: user.idioma == idioma, users))#Función de orden superior
    try:
        return list(users1)
    except:
        return{"error":"No se ha encontrado el  usuario"}

@app.get("/usersclass3/")
async def usersclass(nombre:str, autor:str, idioma:str):
    usersMU=list(filter (lambda user: user.nombre == nombre, users_list))
    users=list(filter (lambda user: user.autor == autor, usersMU))#Función de orden superior
    users1=list(filter (lambda user: user.idioma == idioma, users))#Función de orden superior
    try:
        return list(users1)
    except:
        return{"error":"No se ha encontrado el  usuario"}

@app.get("/usersclass4/")
async def usersclass(nombre:str, autor:str, idioma:str, anio:str):
    usersMU=list(filter (lambda user: user.nombre == nombre, users_list))
    users=list(filter (lambda user: user.autor == autor, usersMU))#Función de orden superior
    users1=list(filter (lambda user: user.idioma == idioma, users))#Función de orden superior
    users2=list(filter (lambda user: user.anio == anio, users1))
    try:
        return list(users2)
    except:
        return{"error":"No se ha encontrado el  usuario"}

@app.get("/usersclass5/")
async def usersclass(nombre:str, autor:str, idioma:str, anio:str, editorial:str):
    usersMU=list(filter (lambda user: user.nombre == nombre, users_list))
    users=list(filter (lambda user: user.autor == autor, usersMU))#Función de orden superior
    users1=list(filter (lambda user: user.idioma == idioma, users))#Función de orden superior
    users2=list(filter (lambda user: user.anio == anio, users1))
    users3=list(filter (lambda user: user.editorial == editorial, users2))
    try:
        return list(users3)
    except:
        return{"error":"No se ha encontrado el  usuario"}
 # En el explorador colocamos la raiz de la ip: http://127.0.0.1:8000/usersclass5/?nombre=Divina%20comedia&autor=Celine&idioma=Ruso&anio=2003&editorial=Akal