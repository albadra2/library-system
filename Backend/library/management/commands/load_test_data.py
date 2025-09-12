import random
from datetime import timedelta, date
from faker import Faker

from django.core.management.base import BaseCommand
from django.db import connection

from library.models import Author, Genre, Book, Customer, Inventory, Borrowing

class Command(BaseCommand):
    help = 'Load test data into the library app'

    def reset_sequences(self):
        with connection.cursor() as cursor:
            tables = ['myapp_author', 'myapp_genre', 'myapp_book', 'myapp_customer', 'myapp_inventory', 'myapp_borrowing']
            for table in tables:
                if connection.vendor == 'postgresql':
                    cursor.execute(f"ALTER SEQUENCE {table}_id_seq RESTART WITH 1;")
                elif connection.vendor == 'sqlite':
                    cursor.execute(f"DELETE FROM sqlite_sequence WHERE name='{table}';")
                elif connection.vendor == 'mysql':
                    cursor.execute(f"ALTER TABLE {table} AUTO_INCREMENT = 1;")

    def handle(self, *args, **kwargs):
        fake = Faker()

        # Clear previous data (optional)
        Author.objects.all().delete()
        Genre.objects.all().delete()
        Book.objects.all().delete()
        Customer.objects.all().delete()
        Inventory.objects.all().delete()
        Borrowing.objects.all().delete()

        # Reset sequences
        self.reset_sequences()

        # Create Genres
        genres = ['Science Fiction', 'Fantasy', 'Mystery', 'Romance', 'Horror']
        genre_objs = [Genre.objects.create(name=g) for g in genres]

        # Create Authors with biographies and birth dates
        authors_info = {
            'Isaac Asimov': {
                'bio': 'Isaac Asimov was a prolific Russian-born American science fiction writer and professor of biochemistry.',
                'birth_date': '1920-01-02',
                'books': ['Foundation', 'I, Robot']
            },
            'J.K. Rowling': {
                'bio': 'J.K. Rowling is a British author, best known for writing the Harry Potter fantasy series.',
                'birth_date': '1965-07-31',
                'books': ["Harry Potter and the Sorcerer's Stone", "Harry Potter and the Chamber of Secrets", "Harry Potter and the Prisoner of Azkaban"]
            },
            'Agatha Christie': {
                'bio': 'Agatha Christie was an English writer known for her sixty-six detective novels and fourteen short story collections.',
                'birth_date': '1890-09-15',
                'books': ['Murder on the Orient Express', 'And Then There Were None']
            },
            'Jane Austen': {
                'bio': 'Jane Austen was an English novelist known primarily for her six major novels.',
                'birth_date': '1775-12-16',
                'books': ['Pride and Prejudice', 'Emma']
            },
            'Stephen King': {
                'bio': 'Stephen King is an American author of horror, supernatural fiction, suspense, and fantasy novels.',
                'birth_date': '1947-09-21',
                'books': ['The Shining', 'It', 'Carrie']
            },
            'Dan Abnett': {
                'bio': 'Dan Abnett is a British comic book writer and novelist.',
                'birth_date': '1965-10-12',
                'books': ['Horus Rising']
            },
            'George Orwell': {
                'bio': 'George Orwell was an English novelist, essayist, journalist and critic.',
                'birth_date': '1903-06-25',
                'books': ['1984']
            },
            'Frank Herbert': {
                'bio': 'Frank Herbert was an American science-fiction author best known for the novel Dune.',
                'birth_date': '1920-10-08',
                'books': ['Dune']
            }
        }

        author_objs = {}
        books = []

        for author_name, info in authors_info.items():
            author = Author.objects.create(
                name=author_name,
                biography=info['bio'],
                birth_date=info['birth_date']
            )
            author_objs[author_name] = author

            for title in info['books']:
                book = Book.objects.create(
                    title=title,
                    author=author,
                    genre=random.choice(genre_objs),
                    published_date=fake.date_between(start_date='-50y', end_date='today'),
                    isbn=fake.isbn13()
                )
                books.append(book)

        # Create Inventory
        for book in books:
            Inventory.objects.create(
                book=book,
                quantity=random.randint(1, 10)
            )

        # Create Customers
        customers = []
        for _ in range(10):
            customer = Customer.objects.create(
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.unique.email(),
                phone_number=fake.phone_number(),
                address=fake.address()
            )
            customers.append(customer)

        # Create Borrowings
        total_borrowings = 15

        for i in range(total_borrowings):
            customer = random.choice(customers)
            book = random.choice(books)

            checkout_date = fake.date_between(start_date='-1y', end_date='-1d')
            borrow_duration = random.randint(7, 30)  # Borrow duration between 7 and 30 days
            due_date = checkout_date + timedelta(days=borrow_duration)

            # Randomly decide if overdue (30% chance)
            overdue = fake.boolean(chance_of_getting_true=30)

            if overdue:
                due_date = fake.date_between(start_date='-90d', end_date='-1d')
                checkout_date = due_date - timedelta(days=random.randint(7, 30))

            Borrowing.objects.create(
                customer=customer,
                book=book,
                checkout_date=checkout_date,
                due_date=due_date,
                overdue=overdue
            )

        self.stdout.write(self.style.SUCCESS('Test data loaded: Books matched to correct authors with biographies and birth dates, 10 customers, 15 borrowings with randomized dates (some overdue)'))