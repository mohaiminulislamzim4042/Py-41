#1=>
# tk=int(input("Koto tk khoroch hoilo: "))

# if tk>500:
#     print("Boroloks")
# elif 200<=tk<=500:
#     print("Mitobayee")
# elif tk<200:
#     print("Kipta")
#------------------------------------------------------------------------------------------------------------------
#2=>
# tk=int(input("Koto tk khoroch hoilo: "))

# if tk>500:
#      print("Lok ti Boroloks")
# elif 200<=tk<=500:
#      print("Lok ti Mitobayee")
# elif tk<200:
#      print("Lok ti Kipta")
# if tk%2:
#      print("Lok ti bijor beabohar koreche")
# else:
#      print("Lok ti jor beabohar koreche")
#------------------------------------------------------------------------------------------------------------------
#3=>
# main_balance=20000
# withraw=int(input("Enter amount: "))

# if withraw > main_balance:
#     print("Not have sufuciant balance")

# elif withraw>10000:
#         print("Todays total limit 10000")
# elif withraw % 500 == 0:
#         print("Balance trunsfer succsessful")
# else:
#         print("Enter amount what is devided by 500")
#------------------------------------------------------------------------------------------------------------------
#4=>
main_balance = 20000
print(f"Presant balance: {main_balance} TK")

action = input("Want to Add (add) Or withraw (out)? ")
tk = int(input("Enter amount: "))

if action == "add":
    main_balance = main_balance + tk # টাকা যোগ করা
    print(f"Successfully added {tk} TK to account । New balance: {main_balance}")

elif action == "out":
    if tk > main_balance:
        print("You have not sufficiant balance!")
    elif tk % 500 != 0:
        print("Enter amount what is devided by 500")
    else:
        main_balance = main_balance - tk # টাকা বিয়োগ করা
        print(f" Withraw {tk} Successfully। : Remaining balance {main_balance}")
else:
    print("Choise correct option (add/out)")
