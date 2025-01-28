def analyze_prices(prices):
    prices = prices.split()
    prices = list(map(int, prices))
    v_min = min(prices)
    v_max = max(prices)
    v_sum = sum(prices)
    return f"Min = {v_min}, max = {v_max}, sum = {v_sum}"
