# Q8. Create a class Player  with: 
# • a class variable player_count 
# • instance variables name and level 
# Track how many players were created. 

class Player:
    player_count = 0
    def __init__(self, name, level):
        self.name = name
        self.level = level
        Player.player_count += 1
# Example usage
player1 = Player("Alice", 5)
player2 = Player("Bob", 10)
print(f"Player 1: Name: {player1.name}, Level: {player1.level}")
print(f"Player 2: Name: {player2.name}, Level: {player2.level}")
print(f"Total Players Created: {Player.player_count}")

