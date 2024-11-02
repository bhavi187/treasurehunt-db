import sqlite3
from quiz import run_quiz 

def execute_query(query):
    connection = sqlite3.connect('clues.db')
    cursor = connection.cursor()

    try:
        cursor.execute(query)
        result = cursor.fetchone()
        if result:
            print(result)

            if result[0] == 'URL' and query.lower().strip() == "select docker from clues where id = 6":
                print("🎉 You've reached the end of the clues. No more queries will be accepted.")
                return True  
        else:
            print("No results found.")
    except sqlite3.Error as e:
        print(f"An error occurred: {e}")
    finally:
        connection.close()
    return False 

def main():
    if run_quiz():
        print("\nYou now have access to the specified columns in the **limited_clues** database.")
        print("💡 Use structured SQL queries to explore each column's values, but remember:")
        print("📌 Only **one** value at a time is accessible per search. Patience is key!")
        print("🎯 Begin your search using the **id** column as the primary reference.")
        print("🚀 Have fun uncovering the hidden information—good luck!")
        
        while True:
            query = input("\nEnter your SQL query (or type 'exit' to quit): ")
            if query.lower() == 'exit':
                break

            if execute_query(query):
                break  

if __name__ == '__main__':
    main()
