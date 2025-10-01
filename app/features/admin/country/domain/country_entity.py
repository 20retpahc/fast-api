from dataclasses import dataclass
from datetime import datetime


@dataclass
class CountryEntity:
    id: int
    name: str
    code: str
    country_code: str
    created_at: datetime
    updated_at: datetime
