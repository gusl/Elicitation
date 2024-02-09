def main():
    probabilities = []
    
    while True:
        user_input = input("Enter a probability (0 to 1 or 0% to 100%), or 'quit' to exit: ").strip().lower()
        
        if user_input == 'quit':
            print("Exiting...")
            break
        
        try:
            # Handle percentage inputs
            if user_input.endswith('%'):
                probability = float(user_input[:-1]) / 100
            else:
                probability = float(user_input)
            
            if 0 <= probability <= 1:
                probabilities.append(probability)
                aggregate = sum(probabilities) / len(probabilities)
                print(f"Aggregate probability: {aggregate:.4f} (or {aggregate*100:.2f}%)")
            else:
                print("Error: Probability must be between 0 and 1, or 0% to 100%.")
        except ValueError:
            print("Error: Invalid input. Please enter a valid number.")
        
if __name__ == "__main__":
    main()
    
