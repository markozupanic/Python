#5. Za uneseni string zagrada, prevjeri dali je svaka otvorena zagrada pravilno zatvorena.
#   Primjer: "((()))" -> True | "((()()))" -> True | "(()))" -> False | "(()()" -> False

unos=input("Unesi zagrade: ")

pronadi_otvorenu=unos.count("(")
pronadi_zatvorenu=unos.count(")")

if(pronadi_otvorenu==pronadi_zatvorenu):
    print("True")
else:
    print("False") 













