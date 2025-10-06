

from app.features.admin.country.domain.country_entity import CountryEntity
from app.features.admin.country.infrastructure.model.country_model import CountryModel


def country_e_to_m(country_entity: CountryEntity) -> CountryModel:
    return CountryEntity(
        id=country_entity.id,
        name=country_entity.name,
        country_code=country_entity.country_code,
        currency_code=country_entity.currency_code,
        created_at=country_entity.created_at,
        updated_at=country_entity.updated_at,
    )