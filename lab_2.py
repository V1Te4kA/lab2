import csv
import sys

def writeToFile(animes):
    with open(sys.argv[2], 'w', encoding = 'utf-8') as f:
        if (len(animes) > 0):
            for anime in animes:
                f.write(anime['Name'] + '\n' + anime['Url'] + '\n' + '\n')


def findAnimeByName(text, animes):
    print('Вас интересует какое-то конкретное аниме? (Если да, введите его название; иначе нажмите ENTER): ', end = '')
    name = input(str())
    if (name != ''):
        for anime in text:
            if (anime['Name'].lower() == name.lower() or anime['Alternative Name'].lower() == name.lower()):
                animes.append(anime)
                writeToFile(animes)
                print('Нужное аниме выведено в файл')
                quit()
        print('Такого аниме не найдено')
        quit()


def findAnimeByTag(text, animes):
    print('Какой жанр Вас интересует? (Введите через запятую, если это не очень важно нажмите ENTER): ', end = '')
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


def findAnimeByEpisodes(text, animes):
    print('Вас интересует короткометражное или полнометражное аниме? (ENTER, если не важно): ', end = '')
    episodes = str(input())
    if (episodes.lower() != 'полнометражное' or episodes.lower() != 'короткометражное'):
        print('Введённые данные некорректны')
        quit()
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
    

def findAnimeByDuration(text, animes):
    print('Какая продолжительность Вас интересует (Кол-во часов)? (ENTER, если не важно): ', end = '')
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


def main():
    if (len(sys.argv) < 3):
        print('Не указаны нужные файлы: файл с перечнем аниме и файл вывода данных')
        return
    animes = list()
    with open(sys.argv[1], encoding = 'utf-8') as file:
        text = csv.DictReader(file, delimiter = ',')
        findAnimeByName(text, animes)
        findAnimeByTag(text, animes)
        findAnimeByEpisodes(text, animes)
        findAnimeByDuration(text, animes)
        if (len(animes) > 0):
            writeToFile(animes)
            print('Список подходящих вам аниме записан в файл')
            return
        print('Вам подходят все аниме')


if (__name__ == '__main__'):
    main()
