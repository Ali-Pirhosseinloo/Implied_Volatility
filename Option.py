import numpy as np
from scipy.stats import norm

class Option:
    def __init__(self, S, K, r, v, T):
        self.S = S
        self.K = K
        self.r = r
        self.v = v
        self.T = T

    def d_plus(self):
        return np.float32(np.log(self.S / self.K) + (self.r + 0.5 * self.v ** 2) * self.T) / (np.sqrt((self.v ** 2) * self.T))

    def d_minus(self):
        return np.float32(np.log(self.S / self.K) + (self.r - 0.5 * self.v ** 2) * self.T) / (np.sqrt((self.v ** 2) *self.T))

    def BSM_Call_Price(self):
        return np.float32(self.S * norm.cdf(self.d_plus()) - self.K * np.exp(-self.r * self.T) * norm.cdf(self.d_minus()))

    def BSM_Put_Price(self):
        return np.float32(-self.S * norm.cdf(-self.d_plus()) + self.K * np.exp(-self.r * self.T) * norm.cdf(-self.d_minus()))

    def Call_Delta(self):
        return np.float32(norm.cdf(self.d_plus()))

    def Call_Gamma(self):
        return np.float32(norm.pdf(self.d_plus()) / (self.S * self.v * np.sqrt(self.T)))

    def Call_Vega(self):
        return np.float32(self.S * norm.pdf(self.d_plus()) * np.sqrt(self.T))

    def Call_Theta(self):
        return -(self.S * norm.pdf(self.d_plus()) * self.v) / (2 * np.sqrt(self.T)) - self.r * self.K * np.exp(-self.r * self.T) * norm.cdf(self.d_minus())

    def Call_Rho(self):
        return self.K * self.T * np.exp(-self.r * self.T) * norm.cdf(self.d_minus())

    def Put_Delta(self):
        return norm.cdf(self.d_plus()) - 1

    def Put_Gamma(self):
        return self.Call_Gamma()

    def Put_Vega(self):
        return self.Call_Vega()

    def Put_Theta(self):
        return -(self.S * norm.pdf(self.d_plus()) * self.v) / (2 * np.sqrt(self.T)) + self.r * self.K * np.exp(-self.r * self.T) * norm.cdf(-self.d_minus())

    def Put_Rho(self):
        return -self.T * self.K * np.exp(-self.r * self.T) * norm.cdf(-self.d_minus())

    def MC_Call_Price(self, num_simulations=100000):
        sum_payoffs = 0.0
        for _ in range(num_simulations):
            simulated_price = self.S * np.exp(self.T * (self.r - 0.5 * self.v ** 2) + self.v * np.sqrt(self.T) * np.random.normal())
            sum_payoffs += self.Call_PayOff(simulated_price)
        return (np.exp(-self.r * self.T) * sum_payoffs) / num_simulations

    def MC_Put_Price(self, num_simulations=100000):
        sum_payoffs = 0.0
        for _ in range(num_simulations):
            simulated_price = self.S * np.exp(self.T * (self.r - 0.5 * self.v ** 2) + self.v * np.sqrt(self.T) * np.random.normal())
            sum_payoffs += self.Put_PayOff(simulated_price)
        return (np.exp(-self.r * self.T) * sum_payoffs) / num_simulations

    def Call_PayOff(self, X):
        raise NotImplementedError("Subclass must implement abstract method")

    def Put_PayOff(self, X):
        raise NotImplementedError("Subclass must implement abstract method")