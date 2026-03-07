import math

def calculate_specific_cards_prob(total_cards: int, cards_in_hand: int, total_decks: int, required_counts: dict) -> float:
    """
    Calculate the probability of drawing an exact set of specific cards in a hand,
    accounting for multiple copies of the same card across decks.
    """
    if sum(required_counts.values()) > cards_in_hand:
        return 0.0

    unique_targets = list(required_counts.keys())
    
    def count_ways(index, current_drawn):
        if index == len(unique_targets):
            remaining_to_draw = cards_in_hand - current_drawn
            remaining_in_deck = total_cards - len(unique_targets) * total_decks
            
            if remaining_to_draw < 0 or remaining_to_draw > remaining_in_deck:
                return 0
            return math.comb(remaining_in_deck, remaining_to_draw)
            
        target = unique_targets[index]
        req_count = required_counts[target]
        ways = 0
        
        for i in range(req_count, total_decks + 1):
            if current_drawn + i <= cards_in_hand:
                ways += math.comb(total_decks, i) * count_ways(index + 1, current_drawn + i)
        return ways

    valid_hands = count_ways(0, 0)
    total_hands = math.comb(total_cards, cards_in_hand)
    
    return valid_hands / total_hands

def get_int_input(prompt: str, default: int) -> int:
    """Helper to get integer input with a default fallback."""
    try:
        user_input = input(f"{prompt} (default [{default}]): ").strip()
        if not user_input:
            return default
        return int(user_input)
    except ValueError:
        print(f"Invalid input, using default: {default}")
        return default

def main():
    print("--- Tractor (Sheng ji) Probability Calculator ---")
    
    total_decks = get_int_input("Number of decks", 2)
    players = get_int_input("Number of players", 4)

    bottom_cards = (total_decks * 54) % players or players
    print(f"bottom_cards: {bottom_cards:,}")

    _ = input("Choose a suit (e.g., Spades): ")
    ranks_input = input("Enter ranks separated by commas or spaces (e.g., 10, 10, 9, 9): ")
    ranks = [r.strip() for r in ranks_input.replace(',', ' ').split() if r.strip()]
    
    required_counts = {}
    for r in ranks:
        required_counts[r] = required_counts.get(r, 0) + 1

    cards_per_deck = 54 # 52 standard cards + 2 jokers
    total_cards = total_decks * cards_per_deck
    
    # Calculate cards in hand based on remaining cards
    cards_remaining = total_cards - bottom_cards
    cards_in_hand = cards_remaining // players

    prob = calculate_specific_cards_prob(total_cards, cards_in_hand, total_decks, required_counts)
    
    print("\n" + "-" * 45)
    print(f"Total cards: {total_cards}")
    print(f"Cards in hand per player: {cards_in_hand}")
    print(f"Specific ranks required: {required_counts}")
    print("-" * 45)
    print(f"Probability: {prob:.6f}")
    if prob > 0:
        print(f"Percentage:  {prob * 100:.4f}%")
        print(f"Odds:        1 in {int(1/prob):,}")
    else:
        print("Percentage:  0.0000%")
        print("Odds:        N/A (Impossible)")

if __name__ == "__main__":
    main()
