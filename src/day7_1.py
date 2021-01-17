from util import iohandler

# --- solution ---

bag_dict = dict()  # parent, child -> spec_bag, bags that spec_bag is inside
holders = set()


def containing_bag_num(input_file):
    rules = [row.strip() for row in input_file]
    for rule in rules:
        splitted = rule.split(' ')
        parents = list()
        child = splitted[0] + " " + splitted[1]

        if len(splitted) > 7:
            for index in list(range(len(splitted)))[4::4]:
                parents.append(splitted[index + 1] + " " + splitted[index + 2])

        for parent in parents:
            if bag_dict.get(parent) is None:
                bag_dict.update({parent: []})

            bag_dict.get(parent).append(child)

    walker(bag_dict.get('shiny gold'))
    return len(holders)


def walker(container_list):
    for container in container_list:
        children = bag_dict.get(container)
        holders.add(container)

        if children is not None:
            walker(children)


# --- solution ---

if __name__ == '__main__':
    iohandler.end(str(containing_bag_num(iohandler.begin(__file__))))
