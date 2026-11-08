import math

movies = [
    {
        "title": "The Dune Chronicles", "year": 2021, "genres": {"sci-fi", "drama"},
        "rating": 8.6, "duration_min": 155,
        "actors": ["T. Chalamet", "R. Ferguson", "O. Isaac"],
    },
    {
        "title": "Kitchen Stories", "year": 2019, "genres": {"comedy", "drama"},
        "rating": 7.1, "duration_min": 98, "actors": ["A. Novak", "M. Ferguson"],
    },
    {
        "title": "silent hours", "year": 2016, "genres": {"thriller", "drama"},
        "rating": 6.4, "duration_min": 112, "actors": ["J. Bloom", "K. Lee"],
    },
    {
        "title": "Comet Racers", "year": 2023, "genres": {"sci-fi", "action"},
        "rating": 5.9, "duration_min": 101, "actors": ["O. Isaac", "P. Diaz"],
    },
    {
        "title": "The Last Bakery", "year": 2014, "genres": {"comedy"},
        "rating": 7.8, "duration_min": 89, "actors": ["A. Novak", "T. Chalamet"],
    },
    {
        "title": "midnight in oslo", "year": 2020, "genres": {"thriller", "mystery"},
        "rating": 8.9, "duration_min": 124, "actors": ["K. Lee", "R. Ferguson"],
    },
    {
        "title": "Garden of Static", "year": 2022, "genres": {"drama"},
        "rating": 4.8, "duration_min": 137, "actors": ["P. Diaz", "J. Bloom"],
    },
    {
        "title": "The Quiet Algorithm", "year": 2024, "genres": {"sci-fi", "drama"},
        "rating": 9.2, "duration_min": 118, "actors": ["M. Ferguson", "O. Isaac"],
    },
    {
        "title": "Two Left Shoes", "year": 2011, "genres": {"comedy"},
        "rating": 6.0, "duration_min": 95, "actors": ["A. Novak", "K. Lee"],
    },
    {
        "title": "Red Harbor", "year": 2018, "genres": {"action", "thriller"},
        "rating": 7.3, "duration_min": 129, "actors": ["P. Diaz", "T. Chalamet"],
    },
]


# Этап 1. Переменные, числа, math


def average_rating(movies):
    """Средняя оценка по каталогу, округленная до одного знака."""
    total = 0.0
    for movie in movies:
        total += movie["rating"]
    return round(total / len(movies), 1)


def catalog_age_stats(movies, current_year=2026):
    """Возраст фильмов в годах: (самый старый, самый новый, среднее вверх)."""
    ages = [current_year - movie["year"] for movie in movies]
    oldest = max(ages)
    newest = min(ages)
    average = math.ceil(sum(ages) / len(ages))
    return (oldest, newest, average)


def duration_in_hours(minutes):
    """Переводит минуты в строку вида "2ч 35м"."""
    hours = minutes // 60
    rest = minutes % 60
    return f"{hours}ч {rest}м"


# Этап 2. Условия и match


def rating_tier(rating):
    """Категория фильма по оценке."""
    if rating >= 9:
        return "шедевр"
    elif rating >= 7:
        return "хорошо"
    else:
        return "средне" if rating >= 5 else "слабо"


def decade_label(year):
    """Метка свежести фильма по году выпуска."""
    match year:
        case _ if year > 2020:
            return "новые"
        case _ if year >= 2015:
            return "недавние"
        case _:
            return "старые"


# Этап 3. Циклы


def print_non_comedy(movies):
    """Печатает названия всех фильмов, не относящихся к комедиям."""
    for movie in movies:
        if "comedy" in movie["genres"]:
            continue
        print(f"  {movie['title']}")


def find_first_masterpiece(movies, threshold=9.0):
    """Ищет первый фильм с рейтингом выше threshold и печатает результат."""
    found = None
    index = 0
    while index < len(movies):
        movie = movies[index]
        if movie["rating"] > threshold:
            found = movie
            print(f"  Первый шедевр: {movie['title']} ({movie['rating']})")
            break
        index += 1
    else:
        print("  Шедевров не найдено")
    return found


def count_long_movies(movies, threshold=120):
    """Считает фильмы длиннее threshold минут."""
    count = 0
    for movie in movies:
        if movie["duration_min"] > threshold:
            count += 1
    return count


# Демонстрация работы функций по этапам


def demo(movies):
    """Печатает результаты функций каждого этапа."""
    print("Этап 1. Базовая статистика")
    print(f"  average_rating: {average_rating(movies)}")
    print(f"  catalog_age_stats: {catalog_age_stats(movies)}")
    print(f"  duration_in_hours(155): {duration_in_hours(155)}")

    print()
    print("Этап 2. Категории")
    for movie in movies:
        tier = rating_tier(movie["rating"])
        label = decade_label(movie["year"])
        print(f"  {movie['title']}: {movie['rating']} — {tier}, {label}")

    print()
    print("Этап 3. Циклы")
    print(" Фильмы не из жанра comedy:")
    print_non_comedy(movies)
    print(" Поиск шедевра в полном каталоге:")
    find_first_masterpiece(movies)
    print(" Поиск шедевра в каталоге без The Quiet Algorithm:")
    find_first_masterpiece(movies[:7])
    print(f"  count_long_movies: {count_long_movies(movies)}")


if __name__ == "__main__":
    demo(movies)
