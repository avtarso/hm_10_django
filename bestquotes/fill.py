import os
import django
from datetime import datetime

# Установка Django окружения
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'bestquotes.settings')
django.setup()

from quotes.models import Author, Tag, Quote
from django.contrib.auth.models import User

authors = [
    {
        "fullname": "Albert Einstein",
        "born_date": "March 14, 1879",
        "born_location": "in Ulm, Germany",
        "description": "description"
    },
    {
        "fullname": "J.K. Rowling",
        "born_date": "July 31, 1965",
        "born_location": "description"
    }
]

quotes = [
    {
        "tags": [
            "change",
            "deep-thoughts",
            "thinking",
            "world"
        ],
        "author": "Albert Einstein",
        "quote": "“The world as we have created it is a process of our thinking. It cannot be changed without changing our thinking.”"
    },
    {
        "tags": [
            "abilities",
            "choices"
        ],
        "author": "J.K. Rowling",
        "quote": "“It is our choices, Harry, that show what we truly are, far more than our abilities.”"
    }
]

def parse_date(date_str):
    try:
        return datetime.strptime(date_str, "%B %d, %Y").date()
    except ValueError:
        return None

def import_data():
    for author_data in authors:
        author, created = Author.objects.get_or_create(
            fullname=author_data['fullname'],
            born_date=parse_date(author_data['born_date']),
            born_location=author_data['born_location'],
            description=author_data.get('description', ''),
            added_by=None
        )

    for quote_data in quotes:
        author = Author.objects.get(fullname=quote_data['author'])
        quote = Quote.objects.create(
            text=quote_data['quote'],
            author=author,
            added_by=None
        )

        for tag_name in quote_data['tags']:
            tag, created = Tag.objects.get_or_create(name=tag_name, defaults={'added_by': None})
            quote.tags.add(tag)

    print("Data imported successfully!")


def create_user():
    username = "user"
    password = "user"

    if not User.objects.filter(username=username).exists():
        User.objects.create_user(username=username, password=password)
        print(f"User '{username}' created successfully!")
    else:
        print(f"User '{username}' already exists.")


if __name__ == "__main__":
    import_data()
    create_user()
