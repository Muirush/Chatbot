import nltk 
from nltk.chat.util import Chat, reflections
#setting replies where the bot compares what a user enters and replies with the matching one

print("\n\n Hello my namie is CU_Nav Chuka University Students developed me to guide people in this site")
print('What is your name? how can i help you?')
pairs = [
   
    [
        r"my name is (.*)",
        ["Hello @ %1, How are you doing?",]
         #,"Hello @ %2, How are you doing?
    ],
    [
        r"hi|hello|hey there",
        ["Hi too","Hello there",]
    ],
    [
        r"iam doing good|fine|iam fine|cool|iam cool|good",
        ["Good to hear, how can i help you?",]
    ],
    [
        r"what do you do?",
        ["I guide people through Chuka University",]
    ],
    [
        r"chuka|chuka university|university",
        ["Chuka University is located 186Km North of Nairobi along Meru-Nairobi highway",]
    ],
    [
        r"who created you?",
        ["Group 3 members did",]
    ],
    [
     #|what courses do you offer|courses|course
        r"offer|what courses do you offer|courses|course",
        ["Courses are offered in different fuculties as indicated below \n 1. FSET \n 2.FERED \n 3. FHSS \n4. FAES \n 5. FBUST \n 6. NURSING\n  7. LAW",]
    ],
    [
        r"1",
        ["FSET-Faculty of Science Engineering and Technology offers the following courses: \n a. Computer Science \n b. Applied Computer Science \n c. Electrical and Electronic Engeneering",]
    ],
    
    [
        r"fee|fee structure|fee for a semister",
        ["Fees are normally indicated in call letter but you can check from the cyber cafes around the University",]
    ],
    [
        r"bye",
        ["Thank you you for contacting CU_Nav, Bye, Stay safe",]
    ],
]

def chatbot():
    chatbot()
    
chat = Chat(pairs, reflections)
chat.converse()