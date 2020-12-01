from util import iohandler

# --- solution ---


def init(input_file):
    report = list()
    for e in input_file:
        report.append(int(e.strip()))
    return report


def find_entry_triplet(report_list):
    for entry in report_list:
        diff = 2020 - entry
        for i_entry in report_list:
            i_diff = diff - i_entry
            if i_diff in report_list:
                return entry * i_entry * i_diff


# --- solution ---

if __name__ == '__main__':
    input_list = init(iohandler.begin(__file__))
    iohandler.end(str(find_entry_triplet(input_list)))
