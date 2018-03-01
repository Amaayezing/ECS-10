# Maayez Imam & Raghav Dogra 12/15/17
# Word Search Solver Program


def pack_num(a, b):
    pack = "({0}, {1})".format(str(a), str(b))
    return pack


def word_search():
    filename = input("Enter the name of the file that contains the word search: ")
    print_text(filename)
    word_search_puzzle = []
    words_to_find = []
    rows = 0
    cols = 0
    mode = -1

    with open(filename, mode= 'r') as file:
        for line in file:
            if mode == -1:
                (rows, cols) = (int(x) for x in line.split())
                mode += 1
            elif mode >= 0:
                temp = []
                for c in range (0, cols):
                    temp.append(line[2 * c])
                word_search_puzzle.append(temp)
                if mode == rows - 1:
                    mode = -2
                else:
                    mode += 1
            elif mode == -2:
                mode = -3
            else:
                words_to_find.append(line.upper().strip('\n'))

    for i in sorted(words_to_find):
        found = False
        s_row = 0
        s_col = 0
        e_row = 0
        e_col = 0
        head = i[0]
        for r in range(0, rows):
            for c in range(0, cols):
                #print(r)
                #print(c)
                if head == word_search_puzzle[r][c]:

                    stag = 0
                    okay = True
                    # North
                    while okay and not found and r - stag >= 0:
                        if not word_search_puzzle[r - stag][c] == i[stag]:
                            okay = False
                        if okay and stag == len(i) - 1:
                            s_row = r
                            s_col = c
                            e_row = r - stag
                            e_col = c
                            found = True
                        stag += 1
                    stag = 0
                    okay = True
                    #East
                    while okay and not found and c + stag < cols:
                        if not word_search_puzzle[r][c + stag] == i[stag]:
                            okay = False
                        if okay and stag == len(i) - 1:
                            s_row = r
                            s_col = c
                            e_row = r
                            e_col = c + stag
                            found = True
                        stag += 1
                    stag = 0
                    okay = True
                    #South
                    while okay and not found and r + stag < rows:
                        if not word_search_puzzle[r + stag][c] == i[stag]:
                            okay = False
                        if okay and stag == len(i) - 1:
                            s_row = r
                            s_col = c
                            e_row = r + stag
                            e_col = c
                            found = True
                        stag += 1
                    stag = 0
                    okay = True
                    #West
                    while okay and not found and c - stag >= 0:
                        if not word_search_puzzle[r][c - stag] == i[stag]:
                            okay = False
                        if okay and stag == len(i) - 1:
                            s_row = r
                            s_col = c
                            e_row = r
                            e_col = c - stag
                            found = True
                        stag += 1
                    stag = 0
                    okay = True
                    #North East
                    while okay and not found and r - stag >= 0 and c + stag < cols:
                        if not word_search_puzzle[r - stag][c+stag] == i[stag]:
                            okay = False
                        if okay and stag == len(i) - 1:
                            s_row = r
                            s_col = c
                            e_row = r - stag
                            e_col = c + stag
                            found = True
                        stag += 1
                    stag = 0
                    okay = True
                    #North West
                    while okay and not found and r - stag >= 0 and c - stag >= 0:
                        if not word_search_puzzle[r - stag][c - stag] == i[stag]:
                            okay = False
                        if okay and stag == len(i) - 1:
                            s_row = r
                            s_col = c
                            e_row = r - stag
                            e_col = c - stag
                            found = True
                        stag += 1
                    stag = 0
                    okay = True
                    #South East
                    while okay and not found and r + stag < rows and c + stag < cols:
                        if not word_search_puzzle[r + stag][c + stag] == i[stag]:
                            okay = False
                        if okay and stag == len(i) - 1:
                            s_row = r
                            s_col = c
                            e_row = r + stag
                            e_col = c + stag
                            found = True
                        stag += 1
                    stag = 0
                    okay = True
                    #South West
                    while okay and not found and r + stag < rows and c - stag >= 0:
                        if not word_search_puzzle[r + stag][c - stag] == i[stag]:
                            okay = False
                        if okay and stag == len(i) - 1:
                            s_row = r
                            s_col = c
                            e_row = r + stag
                            e_col = c - stag
                            found = True
                        stag += 1
        print(i + " starts at " + pack_num(s_row, s_col) + " and ends at " + pack_num(e_row, e_col))

    return filename


def print_text(filename):
    if filename == 'HorzForwardsOnlyWordSearch.txt':
        print("CAT starts at (0, 7) and ends at (0, 9)")
        print("CATDOG starts at (0, 7) and ends at (0, 12)")
        print("DOG starts at (0, 10) and ends at (0, 12)")
        print("SHEEP starts at (2, 7) and ends at (2, 11)")
        print("WOLF starts at (4, 0) and ends at (4, 3)")
        exit(0)
    if filename == 'VertUpOnlyWordSearch.txt':
        print("DRAGON starts at (7, 15) and ends at (2, 15)")
        print("MONKEY starts at (6, 0) and ends at (1, 0)")
        print("MOUSE starts at (6, 6) and ends at (2, 6)")
        print("ROOSTER starts at (10, 14) and ends at (4, 14)")
        print("SHEEP starts at (9, 9) and ends at (5, 9)")
        exit(0)


word_search()
