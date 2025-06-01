class Handler():
    
    def __init__(self) -> None:
        
        self.__prev_output = "0"

    def get_prev_output(self) -> str:
        return self.__prev_output
    
    def set_prev_output(self, output: str) -> None:
        self.__prev_output = output

    def solve(self, user_input: str) -> str:

        user_input = user_input.replace(" ", "")

        # TODO: For any instances of "--", replace with "+" to account for a negative subtracting a negative.
        user_input = list(user_input)
        for i in range(len(user_input)-2, -1, -1):
            if user_input[i] == "-" and user_input[i+1] == "-":
                user_input[i] = "+"
                del user_input[i+1]
        user_input = "".join(user_input)

        if user_input[0] in ["+", "-"]:
            user_input = self.get_prev_output() + user_input

        # Parenthesis

        # Exponent

        # Multiplication & Division

        # Addition & Subtraction
        output = self.add_sub(user_input)

        self.set_prev_output(output) 
        return output

    def add_sub(self, user_input: str):

        equation = list(user_input)

        for i in range(len(equation)-1, 0, -1):
            if equation[i] == "-" and equation[i-1] != "+":
                equation.insert(i, "+")

        equation = "".join(equation)
        nums = [num.split(".") for num in equation.split("+")]
        
        for num in nums:
            # Add zeros to any empty string parent integer or negative sign parent integer
            if num[0] == "-" or num[0] == "":
                num[0] += "0"

            # Apply negative values to decimals who's parent integers are negative
            if len(num) > 1 and num[0][0] == "-":
                num[1] = str(int(num[1]) * -1)

        # Find the longest decimal
        dec_len = 0
        for num in nums:
            if len(num) > 1:
                if int(num[1]) < 0:
                    if len(str(int(num[1])*-1)) > dec_len:
                        dec_len = len(num[1]) - 1
                elif len(num[1]) > dec_len:
                    dec_len = len(num[1])
        
        # Add zeros to the decimals who aren't as long
        for num in nums:
            if len(num) > 1:
                num[1] = num[1] + ("0" * (dec_len - len(num[1])))

        # Get the totals of decimals and integer values
        int_total = 0
        dec_total = 0
        for num in nums:
            int_total += int(num[0])
            if len(num) > 1:
                dec_total += int(num[1])
        
        total = str(dec_total*float("." + ("0" * (dec_len-1)) + "1") + int_total)
        if total.split(".")[1] == "0":
            return total.split(".")[0]
        
        return total