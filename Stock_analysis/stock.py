import pandas as pd
import yfinance as yf
import matplotlib as plt

def  fetch_data(tickers, start, end):
    data = yf.download(tickers, start=start, end=end)['Close']
    return data

def calculate_daily_returns(data):
    daily_returns =data.pct_chande()
    return daily_returns

def calculate_cumulativereturns(daily_returns):
    cumulative_returns = (1 + daily_returns).cumprod()
    return cumulative_returns

def plot_data(data, title):
    data.plot(figsize=(10,6))
    plt.title(title)
    plt.xlabel('Fecha')
    plt.ylabel('Precio')
    plt.legend(data.columns)
    plt.show()

def main():
    tickers = input("Ingresar stock tickers ( separados por comas): ").split(',')
    start_date = input("Ingresar fecha (AAAA-MM-DD): ")
    end_date = input("Ingresar fecha fin (AAAA-MM-DD): " )
    
    #fetch data
    data = fetch_data(tickers, start_date, end_date)
    
    #calculo returns
    daily_returns = calculate_daily_returns(data)
    cumulative_returns =calculate_cumulativereturns(daily_returns)
    
    #dibuja datos
    plot_data(data, "Precio acciones")
    plot_data(daily_returns, "Retornos diarios")
    plot_data(cumulative_returns, "Retornos acumulados")

if __name__ == "__main__":
    main()