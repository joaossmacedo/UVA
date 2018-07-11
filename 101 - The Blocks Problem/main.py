class Board:
    def __init__(self, n: int):
        self.board = []
        for i in range(n):
            self.board.append([i])

    # prints a stack
    def print(self, pos):
        stack = self.board[pos]

        print(str(pos) + ':', end = '')

        for i in range(len(stack)):
            print(' ' + str(stack[i]), end = '')

        print()

    # return the position of the stack the block is in
    def find(self, value: int) -> int:
        r = 0
        for i in range(len(self.board)):
            if value in self.board[i]:
                r = i
                break
        return r

    # moves block a to the stack in the position b
    def move_to(self, a: int, position_b: int):
        position_a = self.find(a)
        index_a = self.board[position_a].index(a)
        self.board[position_b].append(a)
        self.board[position_a] = self.board[position_a][:index_a]

    def move_onto(self, a: int, b: int):
        position_a = self.find(a)
        position_b = self.find(b)

        if position_b == position_a:
            return

        # finds the position inside the stack
        index_a = self.board[position_a].index(a)
        index_b = self.board[position_b].index(b)

        # move the blocks on top of a to their initial positions
        length_a = len(self.board[position_a])
        for i in range(length_a - index_a - 1):
            pos = self.board[position_a][length_a - i - 1]
            self.move_to(pos, pos)

        # move the blocks on top of b to their initial positions
        length_b = len(self.board[position_b])
        for i in range(length_b - index_b - 1):
            pos = self.board[position_b][length_b - i - 1]
            self.move_to(pos, pos)

        self.board[position_b] += self.board[position_a][index_a:]
        self.board[position_a] = self.board[position_a][:index_a]

    def move_over(self, a: int, b: int):
        position_a = self.find(a)
        position_b = self.find(b)

        if position_b == position_a:
            return

        index_a = self.board[position_a].index(a)

        # move the blocks on top of a to their initial positions
        length = len(self.board[position_a])
        for i in range(length - index_a - 1):
            pos = self.board[position_a][length - i - 1]
            self.move_to(pos, pos)

        self.board[position_b] += self.board[position_a][index_a:]
        self.board[position_a] = self.board[position_a][:index_a]

    def pile_onto(self, a: int, b: int):
        position_a = self.find(a)
        position_b = self.find(b)

        if position_b == position_a:
            return

        index_a = self.board[position_a].index(a)
        index_b = self.board[position_b].index(b)

        # move the blocks on top of b to their initial positions
        length = len(self.board[position_b])
        for i in range(length - index_b - 1):
            pos = self.board[position_b][length - i - 1]
            self.move_to(pos, pos)

        self.board[position_b] += self.board[position_a][index_a:]
        self.board[position_a] = self.board[position_a][:index_a]

    def pile_over(self, a: int, b: int):
        position_a = self.find(a)
        position_b = self.find(b)

        if position_b == position_a:
            return

        index_a = self.board[position_a].index(a)
        self.board[position_b] += self.board[position_a][index_a:]
        self.board[position_a] = self.board[position_a][:index_a]


n = int(input())

new_board = Board(n)


while True:
    expression = input().replace('\n', '')

    if expression == "quit":
        break

    expression = expression.split(' ')

    command = expression[0] + ' ' + expression[2]

    a = int(expression[1])
    b = int(expression[3])

    if command == 'move over':
        new_board.move_over(a, b)
    elif command == 'move onto':
        new_board.move_onto(a, b)
    elif command == 'pile over':
        new_board.pile_over(a, b)
    elif command == 'pile onto':
        new_board.pile_onto(a, b)


for i in range(n):
    new_board.print(i)
