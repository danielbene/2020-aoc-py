from util import iohandler

inputFile = iohandler.begin(__file__)

# --- solution ---

report = list()
e1, e2, e3 = 0, 0, 0

for entry in inputFile:
    report.append(int(entry.strip()))

for entry in report:
    diff = 2020 - entry
    for iEntry in report:
        iDiff = diff - iEntry
        if iDiff in report:
            e1 = entry
            e2 = iEntry
            e3 = iDiff

# --- solution ---

iohandler.end(str(e1*e2*e3))
