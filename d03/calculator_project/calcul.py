#!/usr/bin/env python3
from tkinter import *
import my_arithmetic
import re
import math

window = Tk()
calc_input = ""
in_memory = ""

def input_key(value):
    global calc_input
    calc_input += value
    calc_input_text.set(calc_input)

def clear():
    global calc_input
    calc_input = ""
    calc_input_text.set(calc_input)

def error_check(formated):
    if "-" in formated:
        formated = check_for_neg_nbr(formated)
    if len(formated)%2 == 0 and "√" not in formated and "sin" not in formated and "cos" not in formated and "tan" not in formated and "exp" not in formated and "factorial" not in formated:
        result = "ERROR"
    elif "(" in formated and ")" not in formated:
        result = "ERROR"
    elif ")" in formated and "(" not in formated:
        result = "ERROR"
    else:
        result = formated
    return result

def merger(to_merge, formated, pos):
    formated.pop(pos+1)
    formated.pop(pos)
    formated[pos-1] = to_merge
    return formated

def paranthese_merger(para_result, formated, start, end):
    while end > start:
        formated.pop(end)
        end-=1
    formated[start] = para_result[0]
    return formated

def get_multiply(formated, pos):
    nbrs = [formated[pos-1], formated[pos+1]]
    
    op = my_arithmetic.multiply(nbrs)
    to_merge = str(op)
    
    merged = merger(to_merge, formated, pos)
    
    return merged

def get_division(formated, pos):
    nbrs = [formated[pos-1], formated[pos+1]]
    
    op = my_arithmetic.division(nbrs)
    to_merge = str(op)
    
    merged = merger(to_merge, formated, pos)
    
    return merged

def get_addition(formated, pos):
    nbrs = [formated[pos-1], formated[pos+1]]
    
    op = my_arithmetic.add(nbrs)
    to_merge = str(op)
    
    merged = merger(to_merge, formated, pos)
    
    return merged

def get_substraction(formated, pos):
    nbrs = [formated[pos-1], formated[pos+1]]
    
    op = my_arithmetic.subtract(nbrs)
    to_merge = str(op)
    
    merged = merger(to_merge, formated, pos)
    
    return merged

def get_paranthese_end(formated, pos):
    paranthese = 1
    i = 1
    
    while paranthese != 0:
        
        if formated[pos+i] == "(":
            
            paranthese += 1
        if formated[pos+i] == ")":
            
            paranthese -= 1
        i +=1
        
    pos_of_close = (pos+i)-1
    return pos_of_close

def get_squareroot(formated):
    pos = formated.index("√")
    i = 2
    end = get_paranthese_end(formated, pos+1)
    in_squareroot = formated[pos+2:end]
    
    squareroot_result = priority(in_squareroot)
    squareroot_result = [str(math.sqrt(int(squareroot_result[0])))]
    
    formated = paranthese_merger(squareroot_result, formated, pos, end)
    
    formated = priority(formated)
    formated = error_check(formated)
    if formated == "ERROR":
        return "ERROR"
    else:
        result = priority(formated)
    return result

def get_sin(formated):
    pos = formated.index("sin")
    i = 2
    end = get_paranthese_end(formated, pos+1)
    in_sin = formated[pos+2:end]
    
    sin_result = priority(in_sin)
    sin_result = [str(math.sin(int(sin_result[0])))]
    
    formated = paranthese_merger(sin_result, formated, pos, end)
    
    formated = priority(formated)
    formated = error_check(formated)
    if formated == "ERROR":
        return "ERROR"
    else:
        result = priority(formated)
    return result

def get_cos(formated):
    pos = formated.index("cos")
    i = 2
    end = get_paranthese_end(formated, pos+1)
    in_cos = formated[pos+2:end]
    
    cos_result = priority(in_cos)
    cos_result = [str(math.cos(int(cos_result[0])))]
    
    formated = paranthese_merger(cos_result, formated, pos, end)
    
    formated = priority(formated)
    formated = error_check(formated)
    if formated == "ERROR":
        return "ERROR"
    else:
        result = priority(formated)
    return result

def get_tan(formated):
    pos = formated.index("tan")
    i = 2
    end = get_paranthese_end(formated, pos+1)
    in_tan = formated[pos+2:end]
    
    tan_result = priority(in_tan)
    tan_result = [str(math.tan(int(tan_result[0])))]
    
    formated = paranthese_merger(tan_result, formated, pos, end)
    
    formated = priority(formated)
    formated = error_check(formated)
    if formated == "ERROR":
        return "ERROR"
    else:
        result = priority(formated)
    return result

def get_exp(formated):
    pos = formated.index("exp")
    i = 2
    end = get_paranthese_end(formated, pos+1)
    in_exp = formated[pos+2:end]
    
    exp_result = priority(in_exp)
    exp_result = [str(math.exp(int(exp_result[0])))]
    
    formated = paranthese_merger(exp_result, formated, pos, end)
    
    formated = priority(formated)
    formated = error_check(formated)
    if formated == "ERROR":
        return "ERROR"
    else:
        result = priority(formated)
    return result

def get_factorial(formated):
    pos = formated.index("factorial")
    i = 2
    end = get_paranthese_end(formated, pos+1)
    in_factorial = formated[pos+2:end]
    
    factorial_result = priority(in_factorial)
    factorial_result = [str(math.factorial(int(factorial_result[0])))]
    
    formated = paranthese_merger(factorial_result, formated, pos, end)
    
    formated = priority(formated)
    formated = error_check(formated)
    if formated == "ERROR":
        return "ERROR"
    else:
        result = priority(formated)
    return result

def priority(formated):
    
    if "factorial" in formated:
        formated = get_factorial(formated)
    if "√" in formated:
        formated = get_squareroot(formated)
    if "sin" in formated:
        formated = get_sin(formated)
    if "cos" in formated:
        formated = get_cos(formated)
    if "tan" in formated:
        formated = get_tan(formated)
    if "exp" in formated:
        formated = get_exp(formated)
    if "(" in formated and ")" in formated:
        start = formated.index("(")
        
        end = get_paranthese_end(formated, start)
        
        in_para = formated[start+1:end]
        para_result = priority(in_para)
        formated = paranthese_merger(para_result, formated, start, end)
        
        formated = priority(formated)
    if "*" in formated and "/" in formated:
        pos_multi = formated.index("*")
        pos_div = formated.index("/")
        if pos_div > pos_multi: 
            
            merged = get_multiply(formated, pos_multi)
            
            formated = priority(merged)    
        else: 
            
            merged = get_division(formated, pos_div)
            
            formated = priority(merged)
    if "*" in formated:
        pos_multi = formated.index("*")
        
        merged = get_multiply(formated, pos_multi)
        
        formated = priority(merged)
    if "/" in formated:
        pos_div = formated.index("/")
        
        merged = get_division(formated, pos_div)
        
        formated = priority(merged)
    if "+" in formated and "-" in formated:
        pos_add = formated.index("+")
        pos_sub = formated.index("-")
        if pos_sub > pos_add: 
            
            merged = get_addition(formated, pos_add)
            
            formated = priority(merged)    
        else: 
            
            merged = get_substraction(formated, pos_sub)
            
            formated = priority(merged)
    if "+" in formated:
        pos_add = formated.index("+")
        
        merged = get_addition(formated, pos_add)
        
        formated = priority(merged) 
    if "-" in formated:
        pos_sub = formated.index("-")
        
        merged = get_substraction(formated, pos_sub)
        
        formated = priority(merged)
    result = formated   
    return result

def check_for_neg_nbr(formated):
    
    if "-" not in formated:
        return formated
    if formated[0] == "-":
        formated.pop(0)
        formated[0]= "-"+formated[0]
    pos = formated.index("-")
    if formated[pos+1] == "-":
        formated[pos+1] = formated[pos+1]+formated[pos+2]
        formated.pop(pos+2)
        formated = check_for_neg_nbr(formated)
    check_against = ["(","+", "*", "/"]
    if formated[pos-1] in check_against:
        formated.pop(pos)
        formated[pos] ="-"+formated[pos]
        formated = check_for_neg_nbr(formated)
    return formated

def formater(to_format):
    formated = re.split('(\W)', to_format)
    
    formated[:] = [x for x in formated if x != ""]
    
    formated = error_check(formated)
    if formated == "ERROR":
        return "ERROR"
    else:
        result = priority(formated)
    return result

def equal():
    global calc_input
    result = 0

    result = formater(calc_input)
    if isinstance(result, list):
        result[:] = [x for x in result if x != "(" and x != ")"]  
    calc_input = ""
    calc_input_text.set(calc_input)
    result_text.set(result)
    global in_memory 
    in_memory = result
    
def convert_binary():
    global in_memory 
    to_convert = int(in_memory[0])
    converted = bin(to_convert)
    
    result_text.set(converted)

def convert_octal():
    global in_memory 
    to_convert = int(in_memory[0])
    converted = oct(to_convert)
    
    result_text.set(converted)

def convert_decimal():
    global in_memory 
    to_convert = int(in_memory[0])
    converted = int(to_convert)
    
    result_text.set(converted)

def convert_hexadecimal():
    global in_memory 
    to_convert = int(in_memory[0])
    converted = hex(to_convert)
    
    result_text.set(converted)

btn_params = {
    'padx': 16,
    'pady': 1,
    'bd': 4,
    'fg': 'white',
    'bg': '#4d4d4d',
    'font': ('arial', 18),
    'width': 2,
    'height': 2,
    'relief': 'flat',
    'activebackground': "#666666"
}
spc_params = {
    'padx': 16,
    'pady': 1,
    'bd': 4,
    'fg': 'white',
    'bg': '#666666',
    'font': ('arial', 18),
    'width': 2,
    'height': 2,
    'relief': 'flat',
    'activebackground': "#4d4d4d"
}
clear_params = {
    'padx': 16,
    'pady': 1,
    'bd': 4,
    'fg': 'red',
    'bg': '#666666',
    'font': ('arial', 18),
    'width': 2,
    'height': 2,
    'relief': 'flat',
    'activebackground': "#4d4d4d"
}
display_params = {
    'font' : ('arial', 20),
    'relief' :'flat',
    'bg' : '#666666', 
    'fg' : 'white', 
    'width' : 20, 
    'bd' : 21, 
    'justify' : 'right',
    'wraplength' : 350  
}
equal_params = {
    'padx': 16,
    'pady': 1,
    'bd': 4,
    'fg': 'white',
    'bg': '#9e5644',
    'font': ('arial', 18),
    'width': 2,
    'height': 2,
    'relief': 'flat',
    'activebackground': "#ff9980"
}

class Calculator:
    def __init__(self, master):
        Button(window, **spc_params, text=" Bi", command=lambda: convert_binary()).grid(row=3, column=0)
        Button(window, **spc_params, text=" Oct ", command=lambda: convert_octal()).grid(row=3, column=1)
        Button(window, **spc_params, text=" Dec ", command=lambda: convert_decimal()).grid(row=3, column=2)
        Button(window, **spc_params, text=" Hex ", command=lambda: convert_hexadecimal()).grid(row=3, column=3)
        Button(window, **clear_params, text=" AC ", command=lambda: clear()).grid(row=3, column=4)
        Button(window, **spc_params, text=" n! ", command=lambda: input_key("factorial(")).grid(row=4, column=0)
        Button(window, **spc_params, text=u"x\u00B3", command=lambda: input_key("*3")).grid(row=4, column=1)
        Button(window, **spc_params, text=" √ ", command=lambda: input_key("√(")).grid(row=4, column=2)
        Button(window, **spc_params, text=" ( ", command=lambda: input_key("(")).grid(row=4, column=3)
        Button(window, **spc_params, text=" ) ", command=lambda: input_key(")")).grid(row=4, column=4)
        Button(window, **spc_params, text=" exp ", command=lambda: input_key("exp(")).grid(row=5, column=0)
        Button(window, **btn_params, text=" 7 ", command=lambda: input_key("7")).grid(row=5, column=1)
        Button(window, **btn_params, text=" 8 ", command=lambda: input_key("8")).grid(row=5, column=2)
        Button(window, **btn_params, text=" 9 ", command=lambda: input_key("9")).grid(row=5, column=3)
        Button(window, **spc_params, text=" / ", command=lambda: input_key("/")).grid(row=5, column=4)
        Button(window, **spc_params, text=" sin ", command=lambda: input_key("sin(")).grid(row=6, column=0)
        Button(window, **btn_params, text=" 4 ", command=lambda: input_key("4")).grid(row=6, column=1)
        Button(window, **btn_params, text=" 5 ", command=lambda: input_key("5")).grid(row=6, column=2)
        Button(window, **btn_params, text=" 6 ", command=lambda: input_key("6")).grid(row=6, column=3)
        Button(window, **spc_params, text=" * ", command=lambda: input_key("*")).grid(row=6, column=4)
        Button(window, **spc_params, text=" cos ", command=lambda: input_key("cos(")).grid(row=7, column=0)
        Button(window, **btn_params, text=" 1 ", command=lambda: input_key("1")).grid(row=7, column=1)
        Button(window, **btn_params, text=" 2 ", command=lambda: input_key("2")).grid(row=7, column=2)
        Button(window, **btn_params, text=" 3 ", command=lambda: input_key("3")).grid(row=7, column=3)
        Button(window, **spc_params, text=" + ", command=lambda: input_key("+")).grid(row=7, column=4)
        Button(window, **spc_params, text=" tan ", command=lambda: input_key("tan(")).grid(row=8, column=0)
        Button(window, **btn_params, text=" 0 ", command=lambda: input_key("0")).grid(row=8, column=1)
        Button(window, **btn_params, text=" . ", command=lambda: input_key(".")).grid(row=8, column=2)
        Button(window, **equal_params, text=" = ", command=lambda: equal()).grid(row=8, column=3)
        Button(window, **spc_params, text=" - ", command=lambda: input_key("-")).grid(row=8, column=4)

calcul = Calculator(window)
window.title("Simple Scientific Calculator")
calc_input_text = StringVar()
Label(window, **display_params, textvariable=calc_input_text).grid(row=1, columnspan=6)
result_text = StringVar()
Label(window, **display_params, textvariable=result_text).grid(row=2, columnspan=6)
window.resizable(False, False)
window.mainloop()