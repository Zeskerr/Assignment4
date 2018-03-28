import tkinter as tk
from tkinter import ttk
from tkinter import *

class App(tk.Frame):

    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master.title("Assignment 4")
        self.master.minsize(width=1200, height=600)
        self.master.maxsize(width=1200, height=600)

        self.master.rowconfigure(0, pad=1)
        self.master.rowconfigure(1, pad=1)
        self.master.rowconfigure(2, pad=1)
        self.master.rowconfigure(3, pad=1)
        self.master.rowconfigure(4, pad=1)
        self.master.rowconfigure(5, pad=1)
        self.master.rowconfigure(6, pad=1)
        self.master.rowconfigure(7, pad=1)
        self.master.rowconfigure(8, pad=1)
        self.master.rowconfigure(9, pad=1)

        self.master.columnconfigure(0, pad=3)
        self.master.columnconfigure(1, pad=3)
        self.master.columnconfigure(2, pad=3)
        self.master.columnconfigure(3, pad=3)
        self.master.columnconfigure(4, pad=3)

        expression_variables = []
        expression = []
        logical_operator = []

        def disable_buttons():
            for buttons in prepositions:
                buttons.config(state="disabled")

        def reset():
            for buttons in prepositions:
                buttons.config(state="enable")
            p.config(state="enable")
            q.config(state="enable")
            expression_variables.clear()
            expression.clear()
            logical_operator.clear()
            clear_textBox()

        def add_variable(variable):
            expression_variables.append(variable)
            expression.append(variable)
            if(len(expression_variables) == 2):
                p.config(state="disable")
                q.config(state="disable")

        def add_operator(operator):
            expression.append(operator)
            if(operator != "¬"):
                logical_operator.append(operator)

        def draw_truth_table(p, q, preposition):
            for i in range(len(expression_variables)):
                third_textbox.insert(END, "%s        |  " % expression_variables[i])
            for i in range(len(expression)):
                third_textbox.insert(END, "%s  " % expression[i])
            third_textbox.insert(END, "  |" + "\n")
            for i in range(len(p)):
                third_textbox.insert(END, "%s     " % p[i])
                third_textbox.insert(END, "|  ")
                third_textbox.insert(END, "%s     " % q[i])
                third_textbox.insert(END, "|  %s  \n" % preposition[i])

        def clear_textBox():
            third_textbox.delete("1.0", END)

        def calculate():
            print(expression)
            if(expression_variables[0] == expression_variables[1]):
                firstVar = [True, False]
                secondVar = [False, True]
            else:
                firstVar = [True, True, False, False]
                secondVar = [True, False, True, False]
            if((expression[0] == "¬") and ((expression[1] == "P" or expression[1] == "Q"))):
                print("Entered if")
                for i in range(len(firstVar)):
                    firstVar[i] = not(firstVar[i])
            if((expression[2] == "¬") and ((expression[3] == "P" or expression[3] == "Q"))):
                print("Entered if 2")
                for i in range(len(secondVar)):
                    secondVar[i] = not(secondVar[i])

            print(firstVar)
            print(secondVar)
            truth_values = []
            if(logical_operator[0] == "V"):
                for i in range(len(firstVar)):
                    truth_value = firstVar[i] or secondVar[i]
                    truth_values.append(truth_value)
            if(logical_operator[0] == "→"):
                for i in range(len(firstVar)):
                    truth_value = not(firstVar[i]) or secondVar[i]
                    truth_values.append(truth_value)
            if(logical_operator[0] == "∧"):
                for i in range(len(firstVar)):
                    truth_value = (firstVar[i] and secondVar[i])
                    truth_values.append(truth_value)
            if(logical_operator[0] == "↔"):
                for i in range(len(firstVar)):
                    truth_value = ((firstVar[i] and secondVar[i]) or ((not(firstVar[i])) and (not(secondVar[i]))))
                    truth_values.append(truth_value)
            if(logical_operator[0] == "⊕"):
                for i in range(len(firstVar)):
                    truth_value = firstVar[i] != secondVar[i]
                    truth_values.append(truth_value)

            draw_truth_table(firstVar, secondVar, truth_values)
            truth_values.clear()
            firstVar.clear()
            secondVar.clear()
            expression.clear()
            expression_variables.clear()
            logical_operator.clear()

        p = ttk.Button(text="P", command=lambda: add_variable("P"))
        q = ttk.Button(text="Q",command=lambda: add_variable("Q"))
        negation = ttk.Button(text="¬", command=lambda: add_operator("¬"))
        disjunction = ttk.Button(text="V", command=lambda:[disable_buttons(), add_operator("V")])
        implication = ttk.Button(text="→", command=lambda:[disable_buttons(), add_operator("→")])
        conjunction = ttk.Button(text="∧", command=lambda:[disable_buttons(), add_operator("∧")])
        xclusiveOr = ttk.Button(text="⊕", command=lambda:[disable_buttons(), add_operator("⊕")])
        biconditional = ttk.Button(text="↔", command=lambda:[disable_buttons(), add_operator("↔")])
        reset = ttk.Button(text="Reset", command=reset)
        calculate = ttk.Button(text="Calculate", command=calculate)
        third_textbox = Text(width=125, height=35, bg='#f5f5dc')

        prepositions = [disjunction, implication, conjunction, xclusiveOr, biconditional]

        p.grid(padx=5, row=2, column=1)
        q.grid(row=2, column=2)
        negation.grid(row=3, column=1)
        disjunction.grid(row=3, column=2)
        implication.grid(row=4, column=1)
        conjunction.grid(row=4, column=2)
        xclusiveOr.grid(row=5, column=1)
        biconditional.grid(row=5,column=2)
        reset.grid(row=6, column=1)
        calculate.grid(row=6, column=2)
        third_textbox.grid(row=1, column=4, rowspan=50, columnspan=50, pady=5, padx=10)

assigment = App()
assigment.mainloop()
