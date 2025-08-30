from uuid import UUID

import pytest

from src.schemas.products import ProductIn

from pydantic import ValidationError


def test_schemas_validated():
    product = ProductIn(name='Cadeira', quantity=3, price=4.500, status=True)

    assert product.name == 'Cadeira'
    assert isinstance(product.id, UUID)


def test_schemas_raise():
    date = {'name': 'Cadeira', 'quantity': 3, 'price': 4.500}

    with pytest.raises(ValidationError) as err:
        ProductIn.model_validate(date)

    # breakpoint()

    assert err.value.errors()[0] == {
        'type': 'missing',
        'loc': ('status',),
        'msg': 'Field required',
        'input': {'name': 'Cadeira', 'quantity': 3, 'price': 4.5},
        'url': 'https://errors.pydantic.dev/2.11/v/missing',
    }
