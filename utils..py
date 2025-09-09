class Question:
    def __init__(self, text, option, answer):
        self.text=text #Main Question to ask the Player
        self.option=option
        self.answer=answer

    def is_correct(self,answer):
        return answer==self.answer


class Player:
    def __init__(self, name, age):
        self.name=name
        self.age=age

class Quiz:
    def __init__(self, player):
        self.questions=[]
        self.player=player
        self.score=0
        self.question_index=0

    def add_questions(self, question):
        if question not in self.questions:
            self.questions.append(question)
            return True
        return False
    
    def has_more_question(self):
        return self.question_index<len(self.questions)
    

    def get_next_question(self):
        if self.has_more_question():
            question=self.questions[self.question_index]
            self.question_index+=1
            return question
        
    def check_answer(self,answer):
        if self.questions[self.question_index].is_correct(answer):
            self.score+=1
            print("Yes, You got the right answer")
            return True
        else:
            print("OOh, You answer is wrong")
            return False
        
    def __str__(self):
        return f"This Quiz has {len(self.questions)} no. of questions."
    
question=Question("What is the full form of CPU?",["A.Central Processing unit","B.Central Power Unit","C.Central Machine Unit"],"A")
question1=Question("2+229=?",["A.231","B.340","C.431"],"A")
player=Player("Pratul Kumar",22)
quiz=Quiz(player)
print(quiz)
quiz.add_questions(question)
quiz.add_questions(question1)
print(quiz.check_answer("A"))
quiz.get_next_question()
print(quiz.check_answer("C"))



