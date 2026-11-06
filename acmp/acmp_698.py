RANKS = "6789TJQKA"


def can_beat(card, target, trump):
    r1, s1 = card[0], card[1]
    r2, s2 = target[0], target[1]

    if s1 == s2 and RANKS.index(r1) > RANKS.index(r2):
        return True

    if s1 == trump and s2 != trump:
        return True

    return False


N, M, trump = input().split()
N = int(N)
M = int(M)

hand = input().split()
attack = input().split()

is_complete_attack = False
while True:
    if len(attack) == 0:
        is_complete_attack = True
        break

    current_beat_index = -1

    for i in range(len(hand)):
        if can_beat(hand[i], attack[0], trump) == True:
            current_beat_index = i
            break

    if current_beat_index != -1:
        attack.pop(0)
        hand.pop(current_beat_index)
    else:
        is_complete_attack = False
        break

if is_complete_attack == True:
    print("YES")
else:
    print("NO")
