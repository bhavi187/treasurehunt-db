import sqlite3

def create_view():
    connection = sqlite3.connect('clues.db')
    cursor = connection.cursor()

    cursor.execute('''
        CREATE VIEW limited_clues AS
        SELECT id, Python, JavaScript, Docker, AI
        FROM clues
    ''')

    connection.commit()
    connection.close()
    print("View 'limited_clues' created successfully.")

if __name__ == '__main__':
    create_view()
