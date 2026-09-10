class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        # All 13 Roman values in descending order
        value_map = [
            (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
            (100, "C"),  (90, "XC"),  (50, "L"),  (40, "XL"),
            (10, "X"),   (9, "IX"),   (5, "V"),   (4, "IV"),
            (1, "I")
        ]
        
        output = []
        
        for value, symbol in value_map:
            # While the remaining number can fit this value, append symbol and subtract
            while num >= value:
                output.append(symbol)
                num -= value
                
        return "".join(output)