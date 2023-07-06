from app.crud.base import CRUDBase
from app.models.all_models import Advert


class CRUDAdvert(CRUDBase):
    pass


advert_crud = CRUDAdvert(Advert)
