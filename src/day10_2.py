from util import iohandler

# --- solution ---


def get_adapter_arrangement_count(input_file):
    adapter_list = [int(row.strip()) for row in input_file]
    adapter_list.append(0)
    adapter_list.append(max(adapter_list) + 3)
    adapter_list.sort()

    size = len(adapter_list)

    # i gave up, this (really clever) solution is not mine
    # basically it continuously adding up the possible paths for each of the input positions in an array
    # i learned more about graphs, and tried two nice (but practically not working) ideas, so i dont feel bad
    # src: https://tinyurl.com/y63o6ub8
    counter = [1] * size
    for i in range(1, size):
        counter[i] = counter[i - 1]
        if i > 1 and adapter_list[i] - adapter_list[i - 2] <= 3:
            counter[i] += counter[i - 2]
        if i > 2 and adapter_list[i] - adapter_list[i - 3] <= 3:
            counter[i] += counter[i - 3]

        # print(counter)

    # theoretically there will be no duplicated paths when iterating the builded graph
    """combinations_graph = dict((adapter, []) for adapter in adapter_list)  # {child, [parents]}

    for adapter in adapter_list:
        for i in range(1, 4):
            if combinations_graph.get(adapter - i) is not None:
                combinations_graph.get(adapter).append(adapter - i)"""

    return counter[-1]


# this is stupid, don't do this
# in this case, there is more than a trillion paths, so it requires a minimum of 180 hours of runtime
# (based on the average counts per hour on my VM):_)
"""def find_all_paths(graph, start, end, counter):
    global print_time
    if time.time() > print_time + 60:
        print(time.strftime('%X') + " - Processed paths count: " + str(counter))
        print_time = time.time()

    if start == end:
        return counter + 1

    for node in graph[start]:
        counter = find_all_paths(graph, node, end, counter)

    return counter"""


# on the real input it's running out of ram
# keeping it for future reference
"""def find_all_paths(graph, start, end, path=[]):
    path = path + [start]
    if start == end:
        return [path]

    if start not in graph:
        return []

    paths = []

    for node in graph[start]:
        if node not in path:
            newpaths = find_all_paths(graph, node, end, path)
            for newpath in newpaths:
                paths.append(newpath)

    return paths"""


# --- solution ---

if __name__ == '__main__':
    iohandler.end(str(get_adapter_arrangement_count(iohandler.begin(__file__))))
