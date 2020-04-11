#!/usr/bin/env python3
from tkinter import *
import my_arithmetic
import re

window = Tk()
calc_input = ""

def input_key(value):
    global calc_input
    calc_input += value
    calc_input_text.set(calc_input)
    print(calc_input)


def merger(to_merge, formated, pos):
    print("merging", formated, "with", to_merge,"on position", pos-1)
    formated.pop(pos+1)
    formated.pop(pos)
    formated[pos-1] = to_merge
    return formated


def get_multiply(formated, pos_multi):
    nbrs = [formated[pos_multi-1], formated[pos_multi+1]]
    print("numbers to multiply :",nbrs)
    op = my_arithmetic.multiply(nbrs)
    to_merge = str(op)
    print("result added to a list to be concatenated to trimmed original list :", to_merge)
    merged = merger(to_merge, formated, pos_multi)
    print("concatenated the two list, here it is before sending it back to priority", merged)
    return merged


def get_division(formated, pos_div):
    nbrs = [formated[pos_div-1], formated[pos_div+1]]
    print("numbers to divide :",nbrs)
    op = my_arithmetic.division(nbrs)
    to_merge = str(op)
    print("result added to a list to be concatenated to trimmed original list :", to_merge)
    merged = merger(to_merge, formated, pos_div)
    print("concatenated the two list, here it is before sending it back to priority", merged)
    return merged

def get_addition(formated, pos_add):
    nbrs = [formated[pos_add-1], formated[pos_add+1]]
    print("numbers to add :",nbrs)
    op = my_arithmetic.add(nbrs)
    to_merge = str(op)
    print("result added to a list to be concatenated to trimmed original list :", to_merge)
    merged = merger(to_merge, formated, pos_add)
    print("concatenated the two list, here it is before sending it back to priority", merged)
    return merged

def get_substraction(formated, pos_sub):
    nbrs = [formated[pos_sub-1], formated[pos_sub+1]]
    print("numbers to substract :",nbrs)
    op = my_arithmetic.substract(nbrs)
    to_merge = str(op)
    print("result added to a list to be concatenated to trimmed original list :", to_merge)
    merged = merger(to_merge, formated, pos_sub)
    print("concatenated the two list, here it is before sending it back to priority", merged)
    return merged

def priority(formated):
    #------checks if there is a multiplication and division and then checks which one to do first
    print("priority received this list :", formated)
    if "*" in formated and "/" in formated:
        pos_multi = formated.index("*")
        pos_div = formated.index("/")
        if pos_div > pos_multi: # multiplication is first
            print("going to multiply this", formated,"with the element on position", pos_multi)
            merged = get_multiply(formated, pos_multi)
            print("in second if of priority, did a multi, result is :",merged)
            formated = priority(merged)    
        else: #division is first
            print("going to divide this", formated,"with the element on position", pos_div)
            merged = get_division(formated, pos_div)
            print("in first else of priority, did a division, result is :",merged)
            formated = priority(merged)
    if "*" in formated:
        pos_multi = formated.index("*")
        print("going to multiply this", formated,"with the element on position", pos_multi)
        merged = get_multiply(formated, pos_multi)
        print("in third if of priority, did a multi, result is :",merged)
        formated = priority(merged)
    if "/" in formated:
        pos_div = formated.index("/")
        print("going to divide this", formated,"with the element on position", pos_div)
        merged = get_division(formated, pos_div)
        print("in fourth if of priority, did a division, result is :",merged)
        formated = priority(merged)
    if "*" in formated and "/" in formated:
        pos_add = formated.index("+")
        pos_sub = formated.index("-")
        if pos_sub > pos_add: # addition is first
            print("going to add this", formated,"with the element on position", pos_add)
            merged = get_addition(formated, pos_add)
            print("in second if of priority, did a addition, result is :",merged)
            formated = priority(merged)    
        else: #substraction is first
            print("going to substract this", formated,"with the element on position", pos_sub)
            merged = get_substraction(formated, pos_sub)
            print("in first else of priority, did a substraction, result is :",merged)
            formated = priority(merged)
    if "+" in formated:
        pos_add = formated.index("+")
        print("going to add this", formated,"with the element on position", pos_add)
        merged = get_addition(formated, pos_add)
        print("in second if of priority, did a addition, result is :",merged)
        formated = priority(merged) 
    if "-" in formated:
        pos_sub = formated.index("-")
        print("going to substract this", formated,"with the element on position", pos_sub)
        merged = get_substraction(formated, pos_sub)
        print("in first else of priority, did a substraction, result is :",merged)
        formated = priority(merged)
    result = formated   
    return result

def formater(to_format):
    formated = re.split('(\W)', to_format)
    print("input formated ->",formated)
    result = priority(formated)
    return result


        

def equal(*input):
    global calc_input
    result = 0

    result = formater(calc_input)    
    calc_input = ""
    calc_input_text.set(calc_input)
    result_text.set(result)
    print(result)




Button(window, text=" 0 ", command=lambda: input_key("0")).grid(row=6, column=0)
Button(window, text=" 1 ", command=lambda: input_key("1")).grid(row=5, column=0)
Button(window, text=" 2 ", command=lambda: input_key("2")).grid(row=5, column=1)
Button(window, text=" 3 ", command=lambda: input_key("3")).grid(row=5, column=2)
Button(window, text=" 4 ", command=lambda: input_key("4")).grid(row=4, column=0)
Button(window, text=" 5 ", command=lambda: input_key("5")).grid(row=4, column=1)
Button(window, text=" 6 ", command=lambda: input_key("6")).grid(row=4, column=2)
Button(window, text=" 7 ", command=lambda: input_key("7")).grid(row=3, column=0)
Button(window, text=" 8 ", command=lambda: input_key("8")).grid(row=3, column=1)
Button(window, text=" 9 ", command=lambda: input_key("9")).grid(row=3, column=2)
Button(window, text=" + ", command=lambda: input_key("+")).grid(row=5, column=3)
Button(window, text=" - ", command=lambda: input_key("-")).grid(row=6, column=3)
Button(window, text=" * ", command=lambda: input_key("*")).grid(row=4, column=3)
Button(window, text=" / ", command=lambda: input_key("/")).grid(row=3, column=3)
Button(window, text=" . ", command=lambda: input_key(".")).grid(row=6, column=1)
Button(window, text=" = ", command=lambda: equal()).grid(row=6, column=2)

calc_input_text = StringVar()
Label(window, textvariable=calc_input_text).grid(row=1, column=0)
result_text = StringVar()
Label(window, textvariable=result_text).grid(row=2, column=0)
window.mainloop()