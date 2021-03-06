from util import iohandler

# --- solution ---


def init(input_file):
    report = list()
    for e in input_file:
        report.append(int(e.strip()))
    return report


def find_entry_pair(report_list):
    for entry in report_list:
        diff = 2020 - entry
        if diff in report_list:
            return entry * diff


# --- solution ---

# unittests calls global script parts, so we need to avoid reruning the evaluation
# by telling it to only run this, if running the srcipt directly
if __name__ == '__main__':
    input_list = init(iohandler.begin(__file__))
    iohandler.end(str(find_entry_pair(input_list)))
