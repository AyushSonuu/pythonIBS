from minesweeper import MineSweeper
from level import Level


class Play:
    def __init__(self):
        self.sc = input
        self.game()

    def game(self):
        print("----------ENTER YOUR SWEET NAME----------")
        name = input()
        m1 = MineSweeper(Level.EASY, name)
        
        while True:
            print(m1.print_board())
            print("Enter your choice:\n"
                  + "1. Click on a position\n"
                  + "2. Mark as flagged\n"
                  + "3. Mark as unflagged\n"
                  + "4. Reveal the Bombs\n"
                  + "5. Restart the game\n"
                  + "6. Exit")

            choice = int(input())

            if m1.win():
                print("CONGRATULATIONS! YOU WON THE MATCH")
                
            if choice == 6:
                break
            elif choice == 1:
                print("Enter the position to click (e.g., 4,4 as 44)")
                position = input()
                row = int(position[0])
                col = int(position[1])
                print(m1.make_click(row, col))
                
                if m1.get_boardd().get_board()[row][col].is_mine():
                    break

            elif choice in [2, 3]:
                flag_text = "flagged" if choice == 2 else "unflagged"
                print(f"Enter position to make it as {flag_text}")
                position = input()
                row = int(position[0])
                col = int(position[1])
                m1.makeFlagged(row, col, choice == 2)

            elif choice == 4:
                print(m1.revealMine())

            elif choice == 5:
                self.game()

            else:
                print("Enter a valid choice")

        

