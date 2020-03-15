from collections import deque
def search(lines, searchword, history):
    previous_lines = deque(maxlen = history)
    for line in lines:
        if searchword in line:
            yield line, previous_lines
        previous_lines.append(line)

if __name__ == '__main__':
    with open('cricket.txt') as f:
        for line, prevlines in search(f, 'b Plunkett', 5):
            for pline in prevlines:
                print(pline, end = '')
            print(line, end = '')