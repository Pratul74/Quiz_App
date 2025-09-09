class Question:
    def __init__(self, text, option, answer):
        self.text=text #Main Question to ask the Player
        self.option=option
        self.answer=answer

    def is_correct(self,answer):
        return answer==self.answer


class Player:
    def __init__(self, username, age):
        self.username=username
        self.age=age
        self.score=0

class Quiz:
    def __init__(self, player):
        self.questions=[]
        self.player=player
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
            self.player.score+=1
            print("Yes, You got the right answer")
            return True
        else:
            print("OOh, You answer is wrong")
            return False
        
    def __str__(self):
        return f"This Quiz has {len(self.questions)} no. of questions."
    



