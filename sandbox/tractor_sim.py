import random
import time
from tractor_prob import get_int_input

def build_deck(total_decks: int) -> list[str]:
    """
    Builds a standard deck with jokers based on the number of decks.
    """
    suits = ['Spades', 'Hearts', 'Diamonds', 'Clubs']
    ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
    
    single_deck = [f"{rank} of {suit}" for suit in suits for rank in ranks]
    single_deck.extend(["Small Joker", "Big Joker"])
    
    return single_deck * total_decks

def simulate_tractor_game(total_decks: int, players: int, bottom_cards: int, 
                          suit: str, ranks_needed: list[str], simulations: int) -> float:
    """
    Simulates dealing cards and counts how many times the exact requested cards 
    are found in ONE specific player's hand (e.g., player 0).
    """
    full_deck = build_deck(total_decks)
    print(f"full_deck: {full_deck}")
    
    # We are looking for these exact string representations in the player's hand
    target_cards = [f"{rank} of {suit}" for rank in ranks_needed]
    target_counts = {}
    for card in target_cards:
        target_counts[card] = target_counts.get(card, 0) + 1
            
    success_count = 0
    cards_dealt_per_player = (len(full_deck) - bottom_cards) // players

    print(f"Running {simulations:,} simulations... (This might take a few seconds)")
    
    for _ in range(simulations):
        # Shuffle the deck
        deck_copy = full_deck[:]
        random.shuffle(deck_copy)
        
        # Simulating dealing cards: Player 0 gets the first `cards_dealt_per_player` cards
        player_0_hand = deck_copy[:cards_dealt_per_player]
        
        hand_counts = {}
        for card in player_0_hand:
            hand_counts[card] = hand_counts.get(card, 0) + 1
            
        success = True
        for card, required_count in target_counts.items():
            if hand_counts.get(card, 0) < required_count:
                success = False
                break
                
        if success:
            success_count += 1

    return success_count / simulations

def main():
    print("--- Tractor (Sheng ji) Simulator ---")
    
    total_decks = get_int_input("Number of decks", 2)
    players = get_int_input("Number of players", 4)

    bottom_cards = (total_decks * 54) % players or players
    print(f"bottom_cards: {bottom_cards:,}")
    
    suit_input = input("Choose a suit (e.g., Spades) [Spades]: ").strip()
    suit = suit_input if suit_input else "Spades"
    
    ranks_input = input("Enter ranks separated by spaces (e.g., A A K K) [A A K K]: ").strip()
    ranks_str = ranks_input if ranks_input else "A A K K"
    ranks = [r.strip() for r in ranks_str.replace(',', ' ').split() if r.strip()]
    
    simulations = get_int_input("Number of simulations to run", 1000000)

    start_time = time.time()
    prob = simulate_tractor_game(total_decks, players, bottom_cards, suit, ranks, simulations)
    elapsed = time.time() - start_time
    
    print("\n" + "-" * 45)
    print(f"Simulations run: {simulations:,}")
    print(f"Target hand: {ranks} of {suit}")
    print("-" * 45)
    print(f"Simulated Probability: {prob:.6f}")
    if prob > 0:
        print(f"Simulated Percentage:  {prob * 100:.4f}%")
        print(f"Simulated Odds:        ~ 1 in {int(1/prob):,}")
    else:
        print("Simulated Percentage:  0.0000%")
        print("Simulated Odds:        N/A (Did not occur)")
    
    print(f"\nTime taken: {elapsed:.2f} seconds")

if __name__ == "__main__":
    main()
