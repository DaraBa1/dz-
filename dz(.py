questions = [
    "Як вас звати?",
    "Скільки вам років?",
    "Як у вас справи?",
    "Яка ваша улюблена пора року?",
    "Який улюблений колр?",
    "Яка ваша улюблена страва?",
    "Кіт чи собака?",
    "Який у вас улюблений фільм?",
    "Яке місце хочете відвідати?",
    "Любите дощ?"
]
answers = []
print("=== ОПИТУВАННЯ КОРИСТУВАЧА ===")
for q in questions:
    ans = input(q + " ")
    answers.append(ans)
print("\n" + "="*40 + "\n")
print("--- ВАРІАНТ 1 (Конкатенація) ---")
print("Питання 1: " + questions[0] + " | Відповідь: " + answers[0])
print("Питання 2: " + questions[1] + " | Відповідь: " + answers[1])
print("Питання 3: " + questions[2] + " | Відповідь: " + answers[2])
print("Питання 4: " + questions[3] + " | Відповідь: " + answers[3])
print("Питання 5: " + questions[4] + " | Відповідь: " + answers[4])
print("Питання 6: " + questions[5] + " | Відповідь: " + answers[5])
print("Питання 7: " + questions[6] + " | Відповідь: " + answers[6])
print("Питання 8: " + questions[7] + " | Відповідь: " + answers[7])
print("Питання 9: " + questions[8] + " | Відповідь: " + answers[8])
print("Питання 10: " + questions[9] + " | Відповідь: " + answers[9])
print("\n" + "="*40 + "\n")
print("--- ВАРІАНТ 2 (f-форматування) ---")
for i in range(10):
    print(f"Питання {i+1}: {questions[i]} | Відповідь: {answers[i]}")