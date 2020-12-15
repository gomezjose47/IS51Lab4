

"""
This program allows a user three tries to try to guess the correct answer to the question
"what is the capital of california" The answer is "sacramento"

We first set max_tries to 3 then we create a loop to iterate three times. for each iteration
we ask the user for the answer (user input). Then based on the answer the user gives, we check to see 
if the user input matches the answer. If so, print "correct" then terminate the loop with a break statement.

if the user could not guess the answer within the Max_tries, then print "you have 
used up your allotment of guesses." then print "the correct answer is "sacramento"

"""

"""

main 
  question = "what is the capital of california"
  answer = "Sacramento"
  ask (question, answer)

Ask
  tries = 0 
  loop three times 
    increment tries by 1 
    ask user input()
    check to see if user input is equal to answer
      if so print "Correct" the exit loop
  if not correct
    print "You have used up your allotment of guesses."
    print the correct answer "the correct answer is Sacramento"

Main
"""

def main():
  question = "What is the capital of California"
  answer = "california"
  ask (question, answer)

def ask(question, answer, max_tries):
    tries = 0 
    Ans = ""
    while tries < max_tries:
      tries = tries + 1
      ans = input(question)
      if ans == answer:
          print ("Correct")
          break
   if ans != answer:
        print ("you have used up your allotment of guesses.")

main()