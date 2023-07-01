from app.crud.base import CRUDBase
from app.models.advert import Advert


class CRUDAdvert(CRUDBase):
    pass


advert_crud = CRUDAdvert(Advert)
