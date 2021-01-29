import random
from gen.house.type_data import (
    tavern, review
)

DATA_MODULE = {
    'Barkeep': tavern
}

def get_house_type_data(seed, house):
    random.seed(str(seed))
    try:
        module = DATA_MODULE[house.occupation]
    except KeyError:
        r = review.get_review(house)
        if r is not None:
            return {'review': r}
        return {}
    else:
        return module.get_data(house)