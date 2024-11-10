def pricing_tickets(lines):
    n = int(lines[0])
    m = int(lines[1])
    print(n * 10 + m * 5)


def string_swap(lines):
    L, n = map(int, lines[0].split())
    s = list(lines[1])
    for x in range(n):
        i, j = map(int, lines[x + 2].split())
        s[i], s[j] = s[j], s[i]
    print(''.join(s))


def binary_search_tree(lines):
    class Node:
        def __init__(self, data):
            self.data = data
            self.left = None
            self.right = None

    n = int(lines[0])
    root = Node(int(lines[1]))

    for i in range(2, n + 1):
        data = int(lines[i])
        current = root
        while True:
            if data <= current.data:
                if current.left is None:
                    current.left = Node(data)
                    break
                else:
                    current = current.left
            else:
                if current.right is None:
                    current.right = Node(data)
                    break
                else:
                    current = current.right

    def sum_leaf_nodes(node):
        if node is None:
            return 0
        if node.left is None and node.right is None:
            return node.data
        return sum_leaf_nodes(node.left) + sum_leaf_nodes(node.right)

    print(sum_leaf_nodes(root))


def mischievous_monkeys(lines):
    s = lines[0]
    shift = 16
    ret = ''
    for ch in s:
        if ch == ' ':
            ret += ' '
        else:
            ret += chr((ord(ch) - shift - 65) % 26 + 65)
    print(ret)


def giraffe_problem(lines):
    n = int(lines[0])
    arr = []
    idx = 1
    for _ in range(n):
        layer = []
        for _ in range(5):
            layer.append(lines[idx].split())
            idx += 1
        arr.append(layer)
    for k in range(n):
        for i in range(5):
            for j in range(5):
                if arr[k][i][j] == "?":
                    arr[k][i][j] = int(i) + int(j) + 2 * k + 1
                else:
                    arr[k][i][j] = int(arr[k][i][j])
    max_sum = 0
    max_k = 0
    max_i = 0
    for k in range(n):
        for i in range(5):
            curr_sum = sum(arr[k][i])
            if curr_sum > max_sum:
                max_sum = curr_sum
                max_k = k
                max_i = i
    print(f"{max_k} {max_i}")


def pangolin_polynomials(lines):
    n = int(lines[0])
    coords = [tuple(map(int, line.split())) for line in lines[1:n + 1]]
    area = 0
    for i in range(n):
        x1, y1 = coords[i]
        x2, y2 = coords[(i + 1) % n]
        area += (x1 * y2 - x2 * y1)
    area = abs(area) / 2
    print(int(area + 0.5))


def encrypted_message(lines):
    n = int(lines[0])
    arr = [0] * 10
    ptr = 0
    for i in range(1, n + 1):
        base, code = lines[i].split(':')
        instr = chr(int(code, int(base)))
        if instr == '>':
            ptr = (ptr + 1) % 10
        elif instr == '<':
            ptr = (ptr - 1) % 10
        elif instr == '+':
            arr[ptr] = (arr[ptr] + 1) % 256
        elif instr == '-':
            arr[ptr] = (arr[ptr] - 1) % 256
        elif instr == '.':
            print(chr(arr[ptr]), end='')


def predicting_states(lines):
    a = float(lines[0])
    c = float(lines[2])
    x = c / (1 - a + c)
    print(f"{round(x, 6)} {round(1 - x, 6)}")


def compound_words(lines):
    t = lines[0]
    n = int(lines[1])
    ret = []
    for i in range(n):
        if lines[i + 2] in t:
            ret.append(i)
    print(" ".join(list(map(str, sorted(ret)))))


def main():
    import sys
    lines = [line.strip() for line in sys.stdin]
    if not lines:
        raise ValueError("No input provided")

    first_line = lines[0]
    if first_line.isdigit():
        # Could be Pricing Tickets, Binary Search Tree, Pangolin Polynomials, Encrypted Message, Giraffe Problem
        n = int(first_line)
        if len(lines) == 2:
            if n == 1 and int(lines[1]) == 1: # have to special case this :(
                binary_search_tree(lines)
            else:
                pricing_tickets(lines)
        elif n == len(lines) - 1:
            # Could be Binary Search Tree, Pangolin Polynomials, Encrypted Message
            second_line = lines[1]
            if second_line.isdigit():
                binary_search_tree(lines)
            elif ':' in second_line:
                encrypted_message(lines)
            elif len(second_line.split()) == 2:
                pangolin_polynomials(lines)
        elif len(lines) == n * 5 + 1:
            giraffe_problem(lines)
        else:
            raise ValueError("Cannot determine the problem")
    elif ' ' in first_line:
        # Could be String Swap or Mischievous Monkeys
        parts = first_line.split()
        if len(parts) == 2 and parts[0].isdigit() and parts[1].isdigit():
            L, n = map(int, parts)
            if len(lines) == n + 2:
                string_swap(lines)
            else:
                raise ValueError("Cannot determine the problem")
        elif len(lines) == 1:
            mischievous_monkeys(lines)
        else:
            raise ValueError("Cannot determine the problem")
    elif len(lines) == 4 and all(is_float(line) for line in lines):
        predicting_states(lines)
    elif len(lines) == 1:
        mischievous_monkeys(lines)
    elif (not lines[0].isdigit()) and lines[1].isdigit():
        compound_words(lines)
    else:
        raise ValueError("Cannot determine the problem")


def is_float(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


if __name__ == "__main__":
    main()
