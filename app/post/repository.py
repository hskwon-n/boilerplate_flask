from app.database import db
from app.models.post_model import PostModel


class PostRepository:
    def increase_count(self):
        post_model = db.session.query(PostModel).filter_by(id=1).with_for_update().one()

        count = post_model.views

        increased_count = count + 1

        post_model.views = increased_count

        db.session.commit()

    def get_count(self):
        post_model = db.session.query(PostModel).filter_by(id=1).one()

        count = post_model.views

        return count
