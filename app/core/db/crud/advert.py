from app.core.db.crud.base import CRUDBase
from app.core.db.models import Advert


class CRUDAdvert(CRUDBase):
    pass


advert_crud = CRUDAdvert(Advert)
