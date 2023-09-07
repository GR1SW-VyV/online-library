from bookcollections.models import Collection, CollectionDAO, MockArticle

collection = CollectionDAO.create(
    name="Math Books", description="Math books", is_public=True, category="Math", user_id=1
)

print(collection)
