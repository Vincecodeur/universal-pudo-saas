from universal_pudo_saas.shared.entities import BaseEntity


def test_base_entity_is_abstract() -> None:
    assert BaseEntity.__abstract__ is True