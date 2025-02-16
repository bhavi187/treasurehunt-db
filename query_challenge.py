import sqlite3
from quiz import run_quiz  

def execute_query(query):
    connection = sqlite3.connect('clues.db')
    cursor = connection.cursor()

    try:
        
        if "SELECT" not in query.upper() or "FROM" not in query.upper() or "WHERE" not in query.upper():
            print("⚠️ You must include a 'WHERE' clause to select only one element at a time.")
            return False

        
        columns = query.upper().split("SELECT")[1].split("FROM")[0].strip()
        if "," in columns:
            print("⚠️ Only one column can be selected at a time.")
            return False

        cursor.execute(query)
        result = cursor.fetchone()

        if result:
            print(result)
        else:
            print("No results found.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        connection.close()
    return False

def main():

    print("📝 Starting the quiz...")
    run_quiz()  
    print("✅ Quiz completed.\n")

    
    print("\nYou now have access to the specified columns in the **clues** database.")
    print("💡 Use structured SQL queries to explore each column's values, but remember:")
    print("📌 Only **one** value at a time is accessible per search. Patience is key!")
    print("🎯 Begin your search using the **id** column as the primary reference, and the answers the above quiz are the column names.")
    print("🚀 Have fun uncovering the hidden information—good luck!")

    while True:
        query = input("\nEnter your SQL query (or type 'exit' to quit): ")
        if query.lower() == 'exit':
            break

        execute_query(query)

if __name__ == '__main__':
    main()
