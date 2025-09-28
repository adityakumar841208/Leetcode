class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:

        if numerator == 0:
            return "0"

        res = []

        # Handle sign
        if (numerator < 0) ^ (denominator < 0):
            res.append("-")

        numerator, denominator = abs(numerator), abs(denominator)

        # Integer part
        div = numerator // denominator
        res.append(str(div))
        mod = numerator % denominator

        if mod == 0:
            return "".join(res)

        res.append(".")

        # Fractional part
        mod_map = {}
        while mod != 0:
            if mod in mod_map:
                idx = mod_map[mod]
                res.insert(idx, "(")
                res.append(")")
                break

            mod_map[mod] = len(res)
            mod *= 10
            res.append(str(mod // denominator))
            mod %= denominator

        return "".join(res)