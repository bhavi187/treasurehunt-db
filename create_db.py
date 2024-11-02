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
            AI TEXT NOT NULL
        )
    ''')

    cursor.executemany(''' 
        INSERT INTO clues (id, Python, JavaScript, Docker, AI) VALUES (?, ?, ?, ?, ?)
    ''', [
        (1, 'Try, try again!', 'Almost there, keep pushing!', 'No luck yet, try again!', 'Back to the drawing board!'),
        (2, 'Oops, not quite right!', 'Keep the faith, you’re getting closer!', 'Not the answer, but nice try!', 'Don’t give up, keep going!'),
        (3, 'Close, but no cigar!', 'Persistence pays off!', 'Not this time, but you’ll get it!', 'Keep at it, you’re on the right track!'),
        (4, 'Keep those guesses coming!', 'Not there yet, try again!', 'Remember, every failure is a step to success!', 'You’ve got this, don’t quit!'),
        (5, 'Almost there, don’t stop!', 'Your answer is on the tip of your fingers!', 'Not quite, but I believe in you!', 'Retry and shine!'),
        (6, 'You\'re getting warmer!', 'This isn’t the final clue!', 'URL', 'Almost a breakthrough, keep trying!'),
        (7, 'Keep it up, you’re nearly there!', 'Keep your chin up, every attempt counts!', 'One more guess and you might get lucky!', 'Stay positive, the answer is close!'),
        (8, 'Every step is a step forward!', 'Don’t lose hope, you’re doing great!', 'Keep searching, the answer is out there!', 'Keep going, your effort is commendable!'),

    ])

    connection.commit()
    connection.close()
    print("Database and table 'clues' created successfully.")

if __name__ == '__main__':
    create_database()
