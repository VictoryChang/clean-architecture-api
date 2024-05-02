from typing import List

from models.product import Product


def product_list_use_case(repo, params: dict) -> List[Product]:
	return repo.list()
