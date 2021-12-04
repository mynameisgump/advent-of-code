from dataclasses import dataclass
import re


@dataclass
class BingoCard:
    rows: list

    def check_bingo(self, numbers_drawn):
        cases = self.rows+self.get_columns()
        cases = [[num for num in case if num in numbers_drawn] for case in cases]
        for case in cases:
            if len(case) == 5:
                #print("BINGO")
                #print(case)
                return True
        return False
        
    def check_score(self, numbers_drawn):
        marked = [[num for num in row if num in numbers_drawn] for row in self.rows]
        unmarked = [[int(num) for num in row if num not in numbers_drawn] for row in self.rows]
        unmarked_score = sum([sum(row) for row in unmarked])
        print(unmarked_score)
        print(int(numbers_drawn[-1:][0]))
        print("Final Score: ")
        print(unmarked_score*int(numbers_drawn[-1:][0]))

    def get_columns(self):
        columns = []
        for i in range(len(rows)):
            columns.append([row[i] for row in rows])
        return columns


    

if __name__ == "__main__":
    filename="input.txt"
    with open(filename) as f:
        lines = [line.rstrip() for line in f]
        #print(lines)
        counter = 0
        numbers_drawn = ""
        cards = []
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
                card = BingoCard(rows)
                cards.append(card)
            counter += 1

        current_numbers = []
        bingo = False
        winners = []
        print(len(cards))
        for number in numbers_drawn:
            current_numbers.append(number)


            card_count = 0
            for card in cards:
                card_bingo = card.check_bingo(current_numbers)

                if card_bingo == True:
                    print("Bingo")
                    winners.append(card)
                    #print(len(winners))
                card_count += 1
            
            if len(winners) > 0:
                scores = 0
                for winner in winners:
                    winner.check_score(current_numbers) 
                break

            #print(current_numbers)
        #print("Post Search")
            