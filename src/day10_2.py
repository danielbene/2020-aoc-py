from util import iohandler
import time

# --- solution ---

print_time = time.time()


def get_adapter_arrangement_count(input_file):
    adapter_list = [int(row.strip()) for row in input_file]
    adapter_list.append(0)
    adapter_list.append(max(adapter_list) + 3)
    adapter_list.sort()

    # theoretically there will be no duplicate paths when iterating the builded graph
    combinations_graph = dict((adapter, []) for adapter in adapter_list)  # {child, [parents]}

    for adapter in adapter_list:
        for i in range(1, 4):
            if combinations_graph.get(adapter - i) is not None:
                combinations_graph.get(adapter).append(adapter - i)

    print(combinations_graph)
    print(find_all_paths(combinations_graph, max(adapter_list), 0, 0))
    return ''


# this is stupid, don't do this
def find_all_paths(graph, start, end, counter):
    global print_time
    if time.time() > print_time + 60:
        print(time.strftime('%X') + " - Processed paths count: " + str(counter))
        print_time = time.time()

    if start == end:
        return counter + 1

    for node in graph[start]:
        counter = find_all_paths(graph, node, end, counter)

    return counter


# on the real input it's eating all the ram
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
