# Question
# Codeforces 381A - Sereja and Dima


# Solution
def card_game(card):

    left = 0
    right = len(card)-1
    s = 0
    d = 0

    is_player_1_turn = True
    
    while left <= right:
        r = max(card[left],card[right])
        
        if r == card[left]:
            left += 1
        else:
            right -= 1
            
        if is_player_1_turn:
            s += r
        else:
            d += r
            
        is_player_1_turn = not is_player_1_turn
        
    return s,d

n = int(input())
card = list(map(int,input().split()))
print(*card_game(card))
