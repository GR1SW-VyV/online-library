from django.db.models.signals import post_migrate
from django.dispatch import receiver
from social.models import User
from social.models import Collection
from social.models import Document
from faker import Faker


@receiver(post_migrate)
def create_test_users(sender, **kwargs):
    if User.objects.count() == 0:
        fake = Faker()
        User.objects.create_reader_user(
            username="test",
            password="test",
            first_name="Test",
            last_name="User",
            email="test@localhost"
        )
        for _ in range(10):
            User.objects.create_reader_user(
                username=fake.user_name(),
                password=fake.password(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email()
            )

            User.objects.create_professor_user(
                username=fake.user_name(),
                password=fake.password(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                email=fake.email()
            )

            Collection.objects.create(
                name=fake.sentence(nb_words=2),
            )

        User.objects.get(username="test").follow(User.objects.get(id=2))
        User.objects.get(username="test").follow(User.objects.get(id=3))
        User.objects.get(username="test").follow(User.objects.get(id=4))
        User.objects.get(username="test").follow(User.objects.get(id=9))
        User.objects.get(username="test").follow(Collection.objects.get(id=2))
        User.objects.get(username="test").follow(Collection.objects.get(id=3))
        User.objects.get(id=3).follow(User.objects.get(id=2))
        User.objects.get(id=4).follow(User.objects.get(id=2))
        User.objects.get(id=5).follow(User.objects.get(id=2))
        User.objects.get(id=6).follow(User.objects.get(id=2))
        User.objects.get(id=7).follow(User.objects.get(id=2))
        User.objects.get(id=8).follow(User.objects.get(id=2))
        User.objects.get(id=2).do_activity()
        User.objects.get(id=2).do_activity()
        User.objects.get(id=3).do_activity()
        User.objects.get(id=3).do_activity()
        User.objects.get(id=2).do_activity()
        User.objects.get(id=4).do_activity()
        Collection.objects.get(id=3).add_document(Document.objects.create(title=fake.sentence(nb_words=2)))
        Collection.objects.get(id=3).add_document(Document.objects.create(title=fake.sentence(nb_words=2)))
        Collection.objects.get(id=3).add_document(Document.objects.create(title=fake.sentence(nb_words=2)))
        Collection.objects.get(id=2).add_document(Document.objects.create(title=fake.sentence(nb_words=2)))