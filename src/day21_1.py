from util import iohandler
from itertools import groupby

# --- solution ---

# Each allergen is found in exactly one ingredient
# Each ingredient contains zero or one allergen
# However, even if an allergen isn't listed, the ingredient that contains that allergen could still be present


def non_allergen_ingredient_count(input_file):
    data_list = [str(row.strip()) for row in input_file]
    allergens = dict()
    ingredients = set()

    for row in data_list:
        parts = row.split('(contains ')
        allergs = parts[1].replace(')', '')
        ingreds = parts[0].strip().split(' ')

        for allergen in allergs.split(', '):
            if allergens.get(allergen) is None:
                allergens.update({allergen: list()})

            allergens.get(allergen).extend(ingreds)
            ingredients.update(ingreds)

    print(len(ingredients))

    for key in allergens:
        allergens.get(key).sort()
        print(key + str(allergens.get(key)))
        grouped = [str(len(list(group))) + ' - ' + str(key) for key, group in groupby(allergens.get(key))]
        grouped.sort()
        print(grouped)

    return ''


# --- solution ---

if __name__ == '__main__':
    iohandler.end(str(non_allergen_ingredient_count(iohandler.begin(__file__))))
