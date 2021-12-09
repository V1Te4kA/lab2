import csv
import requests

def write_to_file(animes):
    with open('D:/anime.txt', 'w', encoding = 'utf-8') as f:
        if (len(animes) > 0):
            for anime in animes:
                f.write(anime['Name'] + '\n' + anime['Url'] + '\n'+ '\n')


def find_anime_by_name(text, animes):
    print('Вас интересует какое-то конкретное аниме?\
    (Если да, введите его название; иначе нажмите ENTER): ', end = '')
    name = input(str())
    if (name != ''):
        for anime in text:
            if (anime['Name'].lower() == name.lower() or\
                anime['Alternative Name'].lower() == name.lower()):
                print(anime['Name'] + '\n' + anime['Url'])
                quit()
        print('Такого аниме не найдено')
        quit()


def find_anime_by_tag(text, animes):
    print('Какой жанр Вас интересует?\ 
    (Введите через запятую, если это не очень важно нажмите ENTER): ', end = '')
    tags = str(input())
    tags_array = list()
    if (tags != ''):
        tags_array = tags.split(',')
        for tag in tags_array:
            for dict in text:
                if (tag.lower() in dict['Tags'].lower()):
                    animes.append(dict)
        if (len(animes) == 0):
            print('Таких жанров не найдено')
            quit()


def find_anime_by_episodes(text, animes):
    print('Вас интересует короткометражное или полнометражное аниме?\ 
    (ENTER, если не важно): ', end = '')
    episodes = str(input())
    if (episodes != ''):
        if (len(animes)) > 0:
            temp_animes = animes
            animes = list()
            if (episodes.lower() == 'короткометражное'):
                for anime in temp_animes:
                    if (anime['Episodes'] == 'Unknown'):
                        continue
                    if (int(anime['Episodes']) > 1):
                        animes.append(anime)
            elif (episodes.lower() == 'полнометражное'):
                for anime in temp_animes:
                    if (anime['Episodes'] == '1'):
                        animes.append(anime)
        else:
            for anime in text:
                if (episodes.lower() == 'короткометражное'):
                    if (anime['Episodes'] == 'Unknown'):
                        continue
                    if (int(anime['Episodes']) > 1):
                        animes.append(anime)
                elif (episodes.lower() == 'полнометражное'):
                    if (anime['Episodes'] == '1'):
                        animes.append(anime)
        if (len(animes) < 1):
            print('Таких аниме не найдено')
            quit()
    

def find_anime_by_duration(text, animes):
    print('Какая продолжительность Вас интересует (Кол-во часов)?\ 
    (ENTER, если не важно): ', end = '')
    duration = str(input())
    if (duration != ''):
        if (len(animes)) > 0:
            temp_animes = animes
            animes = list()
            for anime in temp_animes:
                if (anime['Duration'] == 'Unknown'):
                    continue
                if (anime['Duration'] == duration):
                    animes.append(anime)
        else:
            for anime in text:
                if (anime['Duration'] == 'Unknown'):
                    continue
                if (anime['Duration'] == duration):
                    animes.append(anime)
        if (len(animes) < 1):
            print('Таких аниме не найдено')
            quit()


def rating_sort(animes):
    ratingsort = list()
    for anime in animes:
        if (anime['Rating Score'] == 'Unknown'):
            continue
        else:
            ratingsort.append(float(anime['Rating Score']))
    ratingsort = list(set(ratingsort))
    ratingsort.sort()
    ratingsort.reverse()
    temp_animes = animes
    animes = list()
    for score in ratingsort:
        for anime in temp_animes:
            if (anime['Rating Score'] == 'Unknown'):
                continue
            if (score == float(anime['Rating Score'])):
                animes.append(anime)
        for anime in temp_animes:
            if (anime['Rating Score'] == 'Unknown'):
                animes.append(anime)
    return animes


def main():
    animes = list()
    with open('D:/anime.csv', encoding = 'utf-8') as file:
        text = csv.DictReader(file, delimiter = ',')
        find_anime_by_name(text, animes)
        find_anime_by_tag(text, animes)
        find_anime_by_episodes(text, animes)
        find_anime_by_duration(text, animes)
        if (len(animes) > 0):
            rating_sort(animes)
            write_to_file(animes)
            print('Список подходящих вам аниме записан в файл')
           
            for anime in animes[:5]:
                url = str('https://www.anime-planet.com/images/anime/covers/'\
                          + str(anime['Anime-PlanetID']) + '.jpg?t=1523213250')
                name = anime['Anime-PlanetID']
                img = requests.get(url)
                img_opt = open(name + '.jpg', 'wb')
                img_opt.write(img.content)
                img_opt.close()
            return
        print('Вам подходят все аниме')

if (__name__ == '__main__'):
    main()
