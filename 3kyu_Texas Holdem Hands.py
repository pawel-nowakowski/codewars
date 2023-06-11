from typing import List


def hand(hole_cards: List, community_cards: List) -> tuple:
    """
    3 kyu texas holden hands https://www.codewars.com/kata/524c74f855025e2495000262
    :param hole_cards: cards in your hand
    :param community_cards: cards on the table
    :return: list what type of hand has won and list of 5 cards
    """
    all_cards = hole_cards + community_cards
    all_cards_to_num, cards_to_ret, counted_cards, pair_check = [], [], [], []
    spades, clubs, hearts, diamonds = 0, 0, 0, 0
    flush = False
    pair_counter, straight_counter, straight_flush_counter = 0, 0, 0
    hand_type = "nothing"
    for card in all_cards:
        if card[0] == "A":
            rank = 14
        elif card[0] == "K":
            rank = 13
        elif card[0] == "Q":
            rank = 12
        elif card[0] == "J":
            rank = 11
        elif card[0] == "1":
            rank = 10
        else:
            rank = int(card[0])
        all_cards_to_num.append([rank, card[-1]])
        counted_cards.append(rank)
    all_cards_to_num.sort(reverse=True)
    for card_and_color in all_cards_to_num:
        color = card_and_color[-1]
        if color == "♠":  # spades
            spades += 1
        elif color == "♣":  # clubs
            clubs += 1
        elif color == "♥":  # heart
            hearts += 1
        elif color == "♦":  # diamond
            diamonds += 1
    if spades >= 5 or clubs >= 5 or hearts >= 5 or diamonds >= 5:
        new_list = all_cards_to_num
        new_list.sort(key=lambda x: x[1])
        for count, card_and_color in enumerate(new_list):
            try:
                if all_cards_to_num[count][1] == all_cards_to_num[count + 1][1]:
                    if all_cards_to_num[count][0] == all_cards_to_num[count + 1][0] + 1:
                        straight_flush_counter += 1
                        if straight_flush_counter == 4:
                            break
                    else:
                        straight_flush_counter = 0
                else:
                    straight_flush_counter = 0
            except:
                break
    for count, card_and_color in enumerate(all_cards_to_num):
        try:
            if all_cards_to_num[count][0] == all_cards_to_num[count + 1][0]:
                continue
            elif all_cards_to_num[count][0] == all_cards_to_num[count + 1][0] + 1:
                straight_counter += 1
                if straight_counter == 4:
                    break
            else:
                straight_counter = 0
        except:
            break
    counted_cards = {i: counted_cards.count(i) for i in counted_cards}
    sorted(counted_cards, key=counted_cards.get, reverse=True)
    # straight flush
    if straight_flush_counter >= 4:
        hand_type = "straight-flush"
        for count, card_and_color in enumerate(all_cards_to_num):
            try:
                if (
                    all_cards_to_num[count][0] == all_cards_to_num[count + 1][0] + 1
                    and all_cards_to_num[count][1] == all_cards_to_num[count + 1][1]
                ):
                    cards_to_ret.append(all_cards_to_num[count][0])
                    if len(cards_to_ret) == 4:
                        cards_to_ret.append(all_cards_to_num[count + 1][0])
                        break
                else:
                    cards_to_ret = []
            except:
                break
    # flush
    elif spades >= 5:
        flush = True
        for card in all_cards_to_num:
            if card[-1] == "♠":
                cards_to_ret.append(card[0])
            if len(cards_to_ret) == 5:
                break
    elif clubs >= 5:
        flush = True
        for card in all_cards_to_num:
            if card[-1] == "♣":
                cards_to_ret.append(card[0])
            if len(cards_to_ret) == 5:
                break
    elif hearts >= 5:
        flush = True
        for card in all_cards_to_num:
            if card[-1] == "♥":
                cards_to_ret.append(card[0])
            if len(cards_to_ret) == 5:
                break
    elif diamonds >= 5:
        flush = True
        for card in all_cards_to_num:
            if card[-1] == "♦":
                cards_to_ret.append(card[0])
            if len(cards_to_ret) == 5:
                break
    # straight
    elif straight_counter >= 4 and flush is False:
        hand_type = "straight"
        for count, card_and_color in enumerate(all_cards_to_num):
            try:
                if all_cards_to_num[count][0] == all_cards_to_num[count + 1][0]:
                    continue
                elif all_cards_to_num[count][0] == all_cards_to_num[count + 1][0] + 1:
                    cards_to_ret.append(all_cards_to_num[count][0])
                    if len(cards_to_ret) == 4:
                        cards_to_ret.append(all_cards_to_num[count + 1][0])
                        break
                else:
                    cards_to_ret = []
            except:
                break

    if flush is True:
        hand_type = "flush"

    if hand_type != "straight-flush":
        for v, k in counted_cards.items():
            pair_check.append(k)
            if k == 4:
                cards_to_ret.append(v)
                hand_type = "four-of-a-kind"
                for i in range(len(all_cards_to_num) - 1):
                    if all_cards_to_num[i][0] not in cards_to_ret:
                        cards_to_ret.append(all_cards_to_num[i][0])
                        break
                break
            elif k == 3:
                if len(cards_to_ret) >= 2:
                    pass
                elif len(cards_to_ret) == 1:
                    new_value = cards_to_ret[0]
                    cards_to_ret = []
                    cards_to_ret.append(v)
                    cards_to_ret.append(new_value)
                else:
                    cards_to_ret.append(v)
            elif k == 2:
                cards_to_ret.append(v)
        if hand_type == "four-of-a-kind":
            pass
        elif 3 in pair_check and 2 in pair_check:
            hand_type = "full house"
        elif hand_type == "flush":
            cards_to_ret = cards_to_ret[:5]
        elif hand_type == "straight":
            cards_to_ret = cards_to_ret[:5]
        elif 3 in pair_check:
            hand_type = "three-of-a-kind"
            for i in range(len(all_cards_to_num) - 1):
                if all_cards_to_num[i][0] not in cards_to_ret:
                    cards_to_ret.append(all_cards_to_num[i][0])
                    if len(cards_to_ret) == 3:
                        break
        elif pair_check.count(2) == 2:
            hand_type = "two pair"
            cards_to_ret.sort(reverse=True)
            for i in range(len(all_cards_to_num) - 1):
                if all_cards_to_num[i][0] not in cards_to_ret:
                    cards_to_ret.append(all_cards_to_num[i][0])
                    if len(cards_to_ret) == 3:
                        break
        elif 2 in pair_check:
            hand_type = "pair"
            for i in range(len(all_cards_to_num) - 1):
                if all_cards_to_num[i][0] not in cards_to_ret:
                    cards_to_ret.append(all_cards_to_num[i][0])
                    if len(cards_to_ret) == 4:
                        break
        else:
            hand_type = "nothing"
            for i in range(len(all_cards_to_num) - 1):
                cards_to_ret.append(all_cards_to_num[i][0])
                if len(cards_to_ret) == 5:
                    break

    cards_to_ret = num_to_card(cards_to_ret)
    return hand_type, cards_to_ret


def num_to_card(list_of_numbers: List) -> List:
    """
    convert number back to card figure
    :param list_of_numbers: list of cards as numbers
    :return: list of cards as figures
    """
    for n, number in enumerate(list_of_numbers):
        if number == 14:
            list_of_numbers[n] = "A"
        elif number == 13:
            list_of_numbers[n] = "K"
        elif number == 12:
            list_of_numbers[n] = "Q"
        elif number == 11:
            list_of_numbers[n] = "J"
        else:
            list_of_numbers[n] = str(number)
    return list_of_numbers


print(hand(["Q♦", "4♦"], ["10♦", "5♦", "9♦", "4♥", "J♦"]))
print(hand(["7♣", "6♠"], ["4♦", "5♥", "4♠", "3♥", "3♦"]))
# print(hand(['7♦', '9♦'], ['8♣', '5♦', '8♦', '6♦', '2♠']))
# print(hand(['2♦', '10♦'], ['9♦', '9♠', '4♦', '6♥', '7♦']))
# print(hand(['5♠', '5♦'], ['J♥', 'A♥', '10♦', '10♥', '10♠']))
print(hand(["2♠", "3♦"], ["2♣", "2♥", "3♠", "3♥", "2♦"]))
# ('four-of-a-kind', ['2', '3'])
print(
    hand(["K♠", "J♦"], ["J♣", "K♥", "9♥", "2♥", "3♦"]),
)
# ("two pair", ["K", "J", "9"]),

print(hand(["K♠", "A♦"], ["J♣", "Q♥", "9♥", "2♥", "3♦"]))
# ("nothing", ["A", "K", "Q", "J", "9"])

print(hand(["K♠", "Q♦"], ["J♣", "Q♥", "9♥", "2♥", "3♦"]))
# ("pair", ["Q", "K", "J", "9"])

print(hand(["4♠", "9♦"], ["J♣", "Q♥", "Q♠", "2♥", "Q♦"]))
# ("three-of-a-kind", ["Q", "J", "9"])

print(hand(["8♠", "6♠"], ["7♠", "5♠", "9♠", "J♠", "10♠"]))
# ("straight-flush", ["J", "10", "9", "8", "7"])

print(hand(["A♠", "K♦"], ["J♥", "5♥", "10♥", "Q♥", "3♥"]))
