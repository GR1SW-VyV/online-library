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
    CATEGORY: list[Document.Type] = [
        Document.Type.BOOK,
        Document.Type.ARTICLE,
    ]

    def document_type(self) -> str:
        return self.random_element(self.CATEGORY)


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
