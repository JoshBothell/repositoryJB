import data
correct = False
guess_num = 0
def main():
    score = 0
    print(data.main_menu)
    input("...")
    score = score + q1()
    score = score + p1()
    score = score + q2()

def q1():
    correct = False
    guess_num = 0
    while correct == False and guess_num < 10:
        guess_num += 1
        guess = input(data.trivia_1)
        if guess == data.answer_1:
            print(data.correct)
            correct = True
            return guess_num
        else:
            print(data.incorrect)
    print(data.fail)
    return guess_num
def p1():
    guess = input(data.enter_pos, data.answer_1)
    i = 0
    foundword = ""
    while i < data.length_1
def q2():
    correct = False
    guess_num = 0
    while correct == False and guess_num < 10:
        guess_num += 1
        guess = input(data.trivia_2)
        if guess == data.answer_2:
            print(data.correct)
            correct = True
            return guess_num
        else:
            print(data.incorrect)
    print(data.fail)
    return guess_num
##def q3():
##def q4():
##def q5():
##def q6():
##def q7():
##def q8():
##def q9():
##def q10():


main()
