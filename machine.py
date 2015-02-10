class CoinDispenser:
    coins = [25,10,5,1]
    def make_change(self,amount):
        result = [0,0,0,0]
        i=0
        while i<4:
            result[i] = (int)(amount / self.coins[i])
            amount = amount % self.coins[i]
            i=i+1
        return result
