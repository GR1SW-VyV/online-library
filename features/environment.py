import os

from faker import Faker
from faker.providers import address, BaseProvider
from articles.choices.category import Category
from articles.models import Document


class CategoryProvider: pass


class DocumentTypeProvider: pass


def before_tag(context, tag):
    if 'fake_data' == tag:
        fake = Faker()
        fake.add_provider(address)
        fake.add_provider(CategoryProvider)
        fake.add_provider(DocumentTypeProvider)
        context.fake = fake


def before_scenario(context, scenario):
    if 'documents_setup' in scenario.feature.tags:
        context.document = dict()


def after_scenario(context, scenario):
    if 'documents_purge' in scenario.feature.tags:
        document_dict: dict[str, Document] = context.document
        for doc in document_dict.values():
            os.remove(doc.local_path())
            doc.delete()

        try:
            os.remove(context.pdf_path)
        except AttributeError:
            ...


class CategoryProvider(BaseProvider):
    CATEGORY: list[Category] = [
        Category.UNKNOWN,
        Category.MATH,
        Category.PHYSICS,
        Category.CALCULUS,
        Category.PROGRAMMING,
        Category.LITERATURE,
        Category.ECONOMY,
        Category.GEOMETRY,
        Category.CHEMISTRY,
    ]

    def category(self) -> str:
        return self.random_element(self.CATEGORY)


class DocumentTypeProvider(BaseProvider):
    TYPE: list[Document.Type] = [
        Document.Type.BOOK,
        Document.Type.ARTICLE,
    ]

    def document_type(self) -> str:
        return self.random_element(self.TYPE)


class CategoryProvider(BaseProvider):
    CATEGORY: list[Category] = [
        Category.UNKNOWN,
        Category.MATH,
        Category.PHYSICS,
        Category.CALCULUS,
        Category.PROGRAMMING,
        Category.LITERATURE,
        Category.ECONOMY,
        Category.GEOMETRY,
        Category.CHEMISTRY,
    ]

    def category(self) -> str:
        return self.random_element(self.CATEGORY)
