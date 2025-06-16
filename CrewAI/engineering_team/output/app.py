import gradio as gr
from accounts import Account, InsufficientFundsError, InsufficientSharesError, get_share_price

# Initialize the account
account = Account(account_id="user123", initial_balance=0.0)

def deposit(amount):
    try:
        amount = float(amount)
        account.deposit(amount)
        return f"Deposit successful. New balance: {account.balance}"
    except ValueError:
        return "Invalid deposit amount."

def withdraw(amount):
    try:
        amount = float(amount)
        account.withdraw(amount)
        return f"Withdrawal successful. New balance: {account.balance}"
    except ValueError:
        return "Invalid withdrawal amount."
    except InsufficientFundsError:
        return "Insufficient funds."

def buy_shares(symbol, quantity):
    try:
        quantity = int(quantity)
        account.buy_shares(symbol, quantity, get_share_price)
        return f"Buy successful. New balance: {account.balance}, Holdings: {account.holdings}"
    except ValueError:
        return "Invalid quantity."
    except InsufficientFundsError:
        return "Insufficient funds."

def sell_shares(symbol, quantity):
    try:
        quantity = int(quantity)
        account.sell_shares(symbol, quantity, get_share_price)
        return f"Sell successful. New balance: {account.balance}, Holdings: {account.holdings}"
    except ValueError:
        return "Invalid quantity."
    except InsufficientSharesError:
        return "Insufficient shares."

def get_account_info():
    portfolio_value = account.get_portfolio_value(get_share_price)
    profit_loss = account.get_profit_loss(get_share_price)
    transactions = "\n".join([str(t) for t in account.get_transactions()])
    holdings = str(account.get_holdings())
    return f"Balance: {account.balance}\nHoldings: {holdings}\nPortfolio Value: {portfolio_value}\nProfit/Loss: {profit_loss}\n\nTransactions:\n{transactions}"

with gr.Blocks() as demo:
    gr.Markdown("# Simple Trading Account")

    with gr.Column():
        deposit_amount = gr.Number(label="Deposit Amount")
        deposit_button = gr.Button("Deposit")

        withdraw_amount = gr.Number(label="Withdraw Amount")
        withdraw_button = gr.Button("Withdraw")

        symbol = gr.Textbox(label="Symbol")
        buy_quantity = gr.Number(label="Buy Quantity")
        buy_button = gr.Button("Buy Shares")

        sell_quantity = gr.Number(label="Sell Quantity")
        sell_button = gr.Button("Sell Shares")

        account_info = gr.Textbox(label="Account Information", interactive=False)
        update_button = gr.Button("Update Account Info")

        deposit_button.click(deposit, inputs=deposit_amount, outputs=account_info)
        withdraw_button.click(withdraw, inputs=withdraw_amount, outputs=account_info)
        buy_button.click(buy_shares, inputs=[symbol, buy_quantity], outputs=account_info)
        sell_button.click(sell_shares, inputs=[symbol, sell_quantity], outputs=account_info)
        update_button.click(get_account_info, outputs=account_info)

demo.launch()
