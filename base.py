from utils import Question, Player, Quiz

def run_quiz():
    q1=Question("What is the Capital of France?",["A.London","B.Paris","C.Berlin","D.Rome"],"B")
    q2=Question("2 + 2 = ?",["A.4","B.3","C.5","D.10"],"A")
    q3=Question("What RAM Stands for?",["A.Random Access Memory","B.Random Alpha Memory","C.Reckless Access Memory","D.Random Automatic Memory"],"A")

    #Creating a Player object
    player=Player("Pratul74",22)

    #Creating a Quiz Object
    quiz=Quiz(player)

    #Adding Questions
    quiz.add_questions([q1,q2,q3])

    while quiz.has_more_question():
        q=quiz.get_next_question()
        print(q.text)
        for option in q.option:
            print(option)
        ans=input("Your Answer: ").upper()
        if quiz.check_answer(ans):
            print("Correct Answer!")
        else:
            print("\nWrong Answer")
        print(f"Final Score: {quiz.player.score}/{len(quiz.questions)}")
