prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "AMZN": 190,
    "MSFT": 420,
    "META": 510,
    "NFLX": 630
}

portfolio = {}

print("=== Stock Portfolio Tracker ===")
print("Available stocks:", list(prices.keys()))
print("Type 'done' when finished.\n")

while True:
    stock = input("Enter stock name: ").upper()
    if stock == "DONE":
        break
    if stock not in prices:
        print("Stock not found. Try again.\n")
        continue
    qty = int(input(f"Enter quantity for {stock}: "))
    portfolio[stock] = portfolio.get(stock, 0) + qty
    print(f"Added {qty} shares of {stock} at ${prices[stock]} each.\n")

print("\n=== Portfolio Summary ===")
total = 0
with open("portfolio.txt", "w") as f:
    f.write("Stock Portfolio Summary\n")
    f.write("=" * 30 + "\n")
    for stock, qty in portfolio.items():
        value = prices[stock] * qty
        total += value
        line = f"{stock}: {qty} shares x ${prices[stock]} = ${value}"
        print(line)
        f.write(line + "\n")
    print(f"\nTotal Investment: ${total}")
    f.write(f"\nTotal Investment: ${total}\n")

print("\nPortfolio saved to portfolio.txt")