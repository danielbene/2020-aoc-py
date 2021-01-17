from util import iohandler

# --- solution ---

bag_dict = dict()  # parent, child -> spec_bag, bags that spec_bag is inside
holders = set()


def contained_bag_num(input_file):
    bag_dict.clear()
    rules = [row.strip() for row in input_file]
    for rule in rules:
        splitted = rule.split(' ')
        container = splitted[0] + " " + splitted[1]

        if bag_dict.get(container) is None:
            bag_dict.update({container: []})

        if len(splitted) > 7:
            for index in list(range(len(splitted)))[4::4]:
                child = splitted[index + 1] + " " + splitted[index + 2]
                bag_dict.get(container).append([child, splitted[index]])

    return walker(bag_dict.get('shiny gold'))


def walker(container_list):
    child_values = 0
    for container in container_list:
        children = bag_dict.get(container[0])
        counter = int(container[1])
        if len(children) > 0:
            child_values += walker(children) * counter + counter
        else:
            child_values += counter

    return child_values


# --- solution ---

if __name__ == '__main__':
    iohandler.end(str(contained_bag_num(iohandler.begin(__file__))))
