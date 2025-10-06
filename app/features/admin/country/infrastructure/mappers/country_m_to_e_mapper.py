

from app.features.admin.country.domain.country_entity import CountryEntity
from app.features.admin.country.infrastructure.model.country_model import CountryModel


def country_m_to_e(country_model: CountryModel) -> CountryEntity:
    return CountryEntity(
        id=country_model.id,
        name=country_model.name,
        country_code=country_model.country_code,
        currency_code=country_model.currency_code,
        created_at=country_model.created_at,
        updated_at=country_model.updated_at,
    )