import os
import csv
from datetime import datetime

# ANSI Color Codes
GREEN = "\033[92m"
BLUE = "\033[94m"
CYAN = "\033[96m"
YELLOW = "\033[93m"
RED = "\033[91m"
BOLD = "\033[1m"
RESET = "\033[0m"

# Hardcoded dictionary
STOCK_PRICES = {
    "AAPL": 182.50,
    "TSLA": 251.75,
    "GOOGL": 152.20,
    "AMZN": 178.10,
    "MSFT": 425.30,
    "NVDA": 895.15,
    "NFLX": 612.45,
    "META": 485.30,
    "BTC": 65430.00
}

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def display_header():
    print(f"{BLUE}{BOLD}{'='*60}")
    print(f"        📈 PREMIUM STOCK PORTFOLIO TRACKER        ")
    print(f"{'='*60}{RESET}")
    print(f"\n{CYAN}{BOLD}[ Market Dashboard - Latest Prices ]{RESET}")
    for i, (stock, price) in enumerate(STOCK_PRICES.items()):
        end_char = "\n" if (i + 1) % 3 == 0 else "  "
        print(f" {YELLOW}• {stock:6}: {GREEN}${price:,.2f}{RESET}", end=end_char)
    print(f"\n{BLUE}{'-' * 60}{RESET}")

def export_portfolio(portfolio, total_value, file_type="txt"):
    date_str = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    
    if file_type == "csv":
        filename = f"portfolio_export_{date_str}.csv"
        try:
            with open(filename, "w", newline="", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerow(["Stock", "Quantity", "Purchase Price", "Total Value"])
                for item in portfolio:
                    writer.writerow([item['name'], item['quantity'], item['price'], item['value']])
                writer.writerow([])
                writer.writerow(["TOTAL INVESTMENT", "", "", total_value])
            print(f"\n{GREEN}✅ Portfolio exported to '{filename}'!{RESET}")
        except Exception as e:
            print(f"\n{RED}❌ CSV Export Error: {e}{RESET}")
    else:
        filename = "portfolio_summary.txt"
        try:
            with open(filename, "w", encoding="utf-8") as f:
                f.write("="*60 + "\n")
                f.write("          STOCK PORTFOLIO INVESTMENT SUMMARY          \n")
                f.write("="*60 + "\n\n")
                f.write(f"{'Stock':<15} {'Quantity':<15} {'Price':<15} {'Value':<15}\n")
                f.write("-" * 60 + "\n")
                for item in portfolio:
                    f.write(f"{item['name']:<15} {item['quantity']:<15} ${item['price']:<14,.2f} ${item['value']:<15,.2f}\n")
                f.write("-" * 60 + "\n")
                f.write(f"{'TOTAL INVESTMENT VALUE:':<46} ${total_value:,.2f}\n")
                f.write(f"\nGenerated on: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n")
            print(f"\n{GREEN}✅ Portfolio saved to '{filename}'!{RESET}")
        except Exception as e:
            print(f"\n{RED}❌ File Error: {e}{RESET}")

def main():
    portfolio = []
    total_investment = 0.0

    while True:
        clear_screen()
        display_header()
        
        print(f"\n{BOLD}Menu Options:{RESET}")
        print(f"{CYAN}1.{RESET} Add Stock to Portfolio")
        print(f"{CYAN}2.{RESET} View Detailed Portfolio")
        print(f"{CYAN}3.{RESET} Save as TXT Summary")
        print(f"{CYAN}4.{RESET} Export to CSV Spreadsheet")
        print(f"{CYAN}5.{RESET} Exit")
        
        choice = input(f"\n{BOLD}Select an option (1-5): {RESET}").strip()

        if choice == '1':
            ticker = input(f"{YELLOW}Enter Stock Ticker (e.g. AAPL): {RESET}").upper().strip()
            if ticker in STOCK_PRICES:
                try:
                    qty = int(input(f"{YELLOW}Enter quantity of {ticker}: {RESET}"))
                    if qty <= 0:
                        print(f"{RED}⚠️ Quantity must be positive.{RESET}")
                    else:
                        price = STOCK_PRICES[ticker]
                        value = price * qty
                        portfolio.append({
                            "name": ticker,
                            "quantity": qty,
                            "price": price,
                            "value": value
                        })
                        total_investment += value
                        print(f"\n{GREEN}✨ Successfully added {qty} shares of {ticker}.{RESET}")
                except ValueError:
                    print(f"{RED}⚠️ Invalid number entered.{RESET}")
            else:
                print(f"{RED}❌ '{ticker}' not found in market data.{RESET}")
            input(f"\n{BLUE}Press Enter to return to menu...{RESET}")

        elif choice == '2':
            if not portfolio:
                print(f"\n{YELLOW}📂 Your portfolio is currently empty.{RESET}")
            else:
                print(f"\n{BOLD}{'Stock':<15} {'Quantity':<15} {'Price':<15} {'Value':<15}{RESET}")
                print(f"{BLUE}{'-' * 60}{RESET}")
                for item in portfolio:
                    print(f"{item['name']:<15} {item['quantity']:<15} ${item['price']:<14,.2f} {GREEN}${item['value']:<15,.2f}{RESET}")
                print(f"{BLUE}{'-' * 60}{RESET}")
                print(f"{BOLD}✨ TOTAL INVESTMENT: {GREEN}${total_investment:,.2f}{RESET}")
            input(f"\n{BLUE}Press Enter to return to menu...{RESET}")

        elif choice in ['3', '4']:
            if not portfolio:
                print(f"{RED}⚠️ Nothing to save. Add stocks first.{RESET}")
            else:
                ext = "csv" if choice == '4' else "txt"
                export_portfolio(portfolio, total_investment, ext)
            input(f"\n{BLUE}Press Enter to return...{RESET}")

        elif choice == '5':
            print(f"\n{CYAN}👋 Goodbye! Happy trading.{RESET}")
            break
        
        else:
            print(f"{RED}⚠️ Invalid selection.{RESET}")
            input(f"\n{BLUE}Press Enter to continue...{RESET}")

if __name__ == "__main__":
    main()


if __name__ == "__main__":
    main()
