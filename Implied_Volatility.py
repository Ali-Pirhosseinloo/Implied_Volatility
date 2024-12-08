from Option import Option as op

class Implied_Volatility:
    def __init__(self, S, K, r, T, market_price):
        self.S = S
        self.K = K
        self.r = r
        self.T = T
        self.market_price = market_price

    def Call_IV(self, tol=1e-5, max_iterations=200):
        v = 0.2  # initial guess
        for i in range(max_iterations):
            model = op(self.S, self.K, self.r, v, self.T)
            model_price = model.BSM_Call_Price() 
            price_diff = self.market_price - model_price
            if abs(price_diff) < tol:
                return v
            derivative = max(model.Call_Vega(),1.1)  # make sure the derivative is not too small
            v += price_diff / derivative  # Newton-Raphson step
            if v < 0: # if v becomes negative, set it to a small positive value
                v = 0.0001
        return float(v)  # return the last computed v if convergence not reached
    
    def Put_IV(self, tol=1e-5, max_iterations=200):
        v = 0.2  # initial guess
        for i in range(max_iterations):
            model = op(self.S, self.K, self.r, v, self.T)
            model_price = model.BSM_Put_Price()
            price_diff = self.market_price - model_price
            if abs(price_diff) < tol:
                return v
            derivative = max(model.Put_Vega(),1.1)  # make sure the derivative is not too small
            v += price_diff / derivative  # Newton-Raphson step
            if v < 0: # if v becomes negative, set it to a small positive value
                v = 0.0001
        return float(v)  # return the last computed v if convergence not reached