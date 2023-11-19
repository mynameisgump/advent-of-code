from dataclasses import dataclass
import re


@dataclass
class BingoCard:
    board_num: int
    rows: list

    def check_bingo(self, numbers_drawn):
        cases = self.rows+self.get_columns()
        cases = [[num for num in case if num in numbers_drawn] for case in cases]
        
        for case in cases:
            if len(case) == 5:
                return True
        return False
        
    def check_score(self, numbers_drawn):
        marked = [[num for num in row if num in numbers_drawn] for row in self.rows]
        unmarked = [[int(num) for num in row if num not in numbers_drawn] for row in self.rows]
        unmarked_score = sum([sum(row) for row in unmarked])
        return unmarked_score*int(numbers_drawn[-1:][0])

    def get_columns(self):
        columns = []
        for i in range(len(self.rows)):
            columns.append([row[i] for row in self.rows])
        return columns


    

if __name__ == "__main__":
    filename="input.txt"
    with open(filename) as f:
        lines = [line.rstrip() for line in f]
        #print(lines)
        counter = 0
        numbers_drawn = ""
        cards = []
        board_count = 0
        for line in lines:
            
            if counter == 0:
                numbers_drawn = line.split(",")

            elif line == "":
                rows = [lines[counter+1].split(" "),
                        lines[counter+2].split(" "),
                        lines[counter+3].split(" "),
                        lines[counter+4].split(" "),
                        lines[counter+5].split(" ")]
                rows = [[x for x in row if x] for row in rows]
                card = BingoCard(board_count,rows)
                cards.append(card)
                board_count += 1
            counter += 1

        current_numbers = []
        bingo = False
        winners = []
        #print(len(cards))
        #print(numbers_drawn)
        number_appends = 0
        for number in numbers_drawn:
            current_numbers.append(number)

            for card in cards:
                card_bingo = card.check_bingo(current_numbers)

                if card_bingo == True:
                    #print("Bingo")
                    winner_names = [pair[0].board_num for pair in winners]
                    if card.board_num not in winner_names:
                        winners.append([card,card.check_score(current_numbers)])

        # Guessed 31010
        for winner in winners:
            print(winner)
            
        last_winner = winners[-1:]
        print()
        print(last_winner)
        
            #if len(winners) > 0:
            #    scores = 0
            #    for winner in winners:
            #        winner.check_score(current_numbers) 
            #    break

            #print(current_numbers)
        #print("Post Search")
            