class ShoppingCart:
    
    def __init__(self, discount=None):
        self._total=0
        self._items=[]
        self._employee_discount=discount
        
    def get_total(self):
        return self._total
    
    def set_total(self, total):
        self._total=total
        
    def del_total(self):
        del self._total
        
    total=property(get_total, set_total, del_total)

    def get_items(self):
        return self._items
    
    def set_items(self, items):
        self._items=items
        
    def del_items(self):
        del self._items
        
    items=property(get_items, set_items, del_items)
    
    def get_employee_discount(self):
        return self._employee_discount
    
    def set_employee_discount(self, employee_discount):
        self._employee_discount=employee_discount
        
    def del_employee_discount(self):
        del self._employee_discount
        
    employee_discount=property(get_employee_discount, set_employee_discount, del_employee_discount)
    
    
    def add_item(self, item, price, quantity=1):
        for i in range(0,quantity):
            self._items.append({item:price})
        self._total += price*quantity
        return self._total
        
    def mean_item_price(self):
        prices=[]
        for item in self._items:
            a=list(item.values())
            prices.append(a[0])
        return sum(prices)/len(prices)
    
    def median_item_price(self):
        prices=[]
        for item in self._items:
            a=list(item.values())
            prices.append(a[0])
        prices.sort()
        if len(prices) % 2 != 0:
            middle= int((len(prices)+1)/2)
            return prices[middle]
        else:
            mid1= int((len(prices))/2)
            mid2= int((len(prices)/2)-1)
            return (prices[mid1]+prices[mid2])/2
        
    def apply_discount(self):
        if self._employee_discount==None:
            return 'no discount for you! come back 1 year'
        else:
            disc_total = self._total*((100-self._employee_discount)/100)
            return disc_total
        
    def item_names(self):
        names=[]
        for item in self._items:
            a=list(item.keys())
            names.append(a[0])
        return names