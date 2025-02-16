import sqlite3

def create_database():
    connection = sqlite3.connect('clues.db')
    cursor = connection.cursor()

    
    cursor.execute(''' 
        CREATE TABLE clues (
            id INTEGER PRIMARY KEY,
            Python TEXT NOT NULL,
            JavaScript TEXT NOT NULL,
            Docker TEXT NOT NULL,
            AI TEXT NOT NULL,
            HTTPS TEXT NOT NULL,
            Binary TEXT NOT NULL,
            Bash TEXT NOT NULL,
            Hashmap TEXT NOT NULL
        )
    ''')


    cursor.executemany(''' 
        INSERT INTO clues (id, Python, JavaScript, Docker, AI, HTTPS, Binary, Bash, Hashmap) 
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    ''', [
        (1, 'Try, try again!', 'Almost there, keep pushing!', 'No luck yet, try again!', 2, 'Not this time, keep trying!', '1011', 'Almost there, stay focused!', 'Stay persistent, it’s coming!'), # b
        (2, 'Oops, not quite right!', 'Keep the faith, you’re getting closer!', 'Not the answer, but nice try!', 5, 'Keep moving forward!', '0010', 'Don’t let up!', 'Keep pressing on!'), # 2
        (3, 'Close, but no cigar!', 'Persistence pays off!', 'Not this time, but you’ll get it!', 3, 'Patience is key!', '1100', 'It’s within reach!', 'Step by step!'), # c
        (4, 'Keep those guesses coming!', 'Not there yet, try again!', 'Remember, every failure is a step to success!', 4, 'Almost cracked it!', '0001', 'One step closer!', 'You’ll see it soon!'), # 1
        (5, 'Almost there, don’t stop!', 'Your answer is on the tip of your fingers!', 'Not quite, but I believe in you!', 6, 'Don’t lose hope!', '0011', 'Stay the course!', 'Try once more!'), # 3
        (6, 'You\'re getting warmer!', 'This isn’t the final clue!', 'Almost a breakthrough, keep trying!', 1, 'Final push needed!', '1010', 'Keep digging deeper!', 'Just around the corner!') # a
    ])

    connection.commit()
    connection.close()
    print("Database and table 'clues' created successfully.")

if __name__ == '__main__':
    create_database()
