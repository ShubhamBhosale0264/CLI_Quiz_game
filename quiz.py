import pyttsx3
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)
questions = [
    "What is the highest score in ODI cricket?",
    "Which team won the WTC first edition?",
    "What is the highest score for India in T Twenty cricket?",
    "What is the national currency of the United States of America (USA)?",
    "What language did Guido van Rossum design in 1991?",
    "Where is the Garampani Sanctuary located?",
    "Which was the first fully supported 64-bit operating system?",
    "On which day is Red Crescent Day celebrated?",
    "What time corresponds to 23:23 hours?",
    "What are gravity chambers used to remove?",
    "Which is the largest planet in our solar system?",
    "How many continents are there in the world?",
    "How many years are there in one millennium?",
    "In which year was hockey introduced in the Asian Games?",
    "With which game is the Durand Cup associated?",
    "On which day is International Literacy Day observed?"
]
options = [
    ["209", "264", "109", "123"],
    ["AUS", "Eng", "New Zealand", "AUS"],
    ["117", "109", "126", "108"],
    ["Dollar", "Euro", "Peso", "Yen"],
    ["Java", "Python", "Javascript", "JS"],
    ["Assam", "Diphu", "Kohima", "Gangtok"],
    ["Linux", "Windows 7", "Mac", "Windows XP"],
    ["May 8", "June 9", "May 16", "April 7"],
    ["11.11 PM", "7:23 PM", "11:23 PM", "9.11 PM"],
    ["SO", "Sus. matter", "NO", "CO"],
    ["Earth", "Jupiter", "Uranus", "Mars"],
    ["7", "8", "5", "6"],
    ["100 years", "1000 years", "50 years", "500 years"],
    ["1958-Tokyo", "1962-Jakarta", "1966-BK", "1970-BK"],
    ["Football", "Cricket", "Hockey", "Volleyball"],
    ["Sep 8", "Nov 28", "May 8", "Sep 22"]
]
correct_answers = [
    "264",
    "New Zealand",
    "126",
    "Dollar",
    "Python",
    "Assam",
    "Linux",
    "May 8",
    "7:23 PM",
    "Sus. matter",
    "Jupiter",
    "7",
    "1000 years",
    "1958-Tokyo",
    "Football",
    "Sep 8"
]
import pyttsx3


def play_game():
    score = 0
    current_question = 0
    chances = 3

    while current_question < len(questions) and chances > 0:
        engine.say(questions[current_question])
        print(questions[current_question])
        engine.runAndWait()

        for option in options[current_question]:
            print(option)

        user_answer = input("Enter your answer: ")

        if user_answer == correct_answers[current_question]:
            print("Correct Answer!")
            score += 1000
            chances = 3
        else:
            chances -= 1
            if chances > 0:
                print("Incorrect Answer. You have", chances, "chances left.")
                print("The correct answer is:", correct_answers[current_question])
            else:
                print("Out of chances. Game over!")
                break

        current_question += 1

    # Display the final score
    print("Your final score is:", score)

# Start the game
play_game()

