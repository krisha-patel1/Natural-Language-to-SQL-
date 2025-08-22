from sshtunnel import run_remote_stub
from llmbasic import get_sql_query

def main():
    print("💬 Ask a question about the database (type 'exit' to quit):")
    while True:
        question = input(">> ")

        if question.strip().lower() == "exit":
            print("👋 Exiting. Goodbye!")
            break

        try:
            print("\n🔄 Generating SQL...")
            sql_query = get_sql_query(question)

            print("\n📄 SQL generated:")
            print(sql_query)

            print("\n🔗 Running query on iLab...")
            result = run_remote_stub(sql_query)

            print("\n📊 Query Results:")
            print(result)

        except Exception as e:
            print("❌ Error:", e)

if __name__ == "__main__":
    main()
