import django
import datetime
import os
import json

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "django_homework.settings")
django.setup()


from articles.models import Article


def main():
    data_dir = "data"
    for file in os.listdir(data_dir):
        file_name = data_dir + '/' + file
        article_json = json.load(open(file_name, encoding='utf-8'))
        title = article_json['title']
        source = article_json['source']
        time = str_to_datetime(article_json['time'])
        content = article_json['content']
        Article.objects.create(title=title, source=source, time=time, content=content)
        print("Successfully import", Article.objects.last(), " !")


def str_to_datetime(time):
    fs = "%Y-%m-%d %H:%M:%S"
    return datetime.datetime.strptime(time, fs)


if __name__ == "__main__":
    main()
