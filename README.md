# Star Classifier

## Проектът представлява приложение за класифициране на звездни обекти на база на астрономически характеристики. Ползва се Random Forest Classifier модел.

Звездите биват разделени на следните групи:

- Brown Dwarf
- Red Dwarf
- White Dwarf
- Main Sequence
- Supergiant
- Hypergiant

По параметри:

- Temperature (Температура на звездата (Kелвин))
- Luminosity (Спрямо Слънцето)
- Radius (Спрямо Слънцето)
- Absolute Magnitude (Абсолютна звездна величина)
- Spectral Class (Категория: O, B, A, F, G, K, M)

## Ползвани са следните технологии:

- FastAPI (уеб сървър)
- Scikit-learn (обучен модел
- Pydantic (валидиране на входни данни)
- Docker (контейнеризация)
- Pytest (тестове)

## Стартиране на проекта:

1. Локално

- Създава и се активира виртуална среда:

<code>python3 -m venv venv</code>

<code>source venv/bin/activate</code>

- Инсталиране на зависимостите

<code>pip install -r requirements.txt</code>

 - Стартиране на приложението:

<code>uvicorn main:app --reload</code>

2. Docker container

В root директорията, където е Dockerfile  се стартира

<code> docker build -t star-api .  </code>  създава image, ползвайки Dockerfile от текущата директория

<code>docker run -d --name star-api-container -p 8000:8000 star-api</code> създава и стартира контейнер в detached режим

FastApi поддържа Swagger UI, приложението може да бъде достъпено на адрес: http://127.0.0.1:8000/docs#

<code>docker exec -it star-api-container /bin/bash</code> достъп до контейнера с шел

<code>pytest</code> - стартиране на юнит тестове



