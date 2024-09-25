import psycopg2
from faker import Faker

def seed_data():
    fake = Faker()

    try:
        conn = psycopg2.connect(
            dbname="postgres",   
            user="postgres", 
            password="567234",    
            host="localhost",            
            port="5432"                 
        )
        cur = conn.cursor()

        # Seed users table with fake data
        for _ in range(10):
            fullname = fake.name()
            email = fake.email()
            cur.execute(
                "INSERT INTO users (fullname, email) VALUES (%s, %s)",
                (fullname, email)
            )

        # Seed status table with predefined statuses
        statuses = ['new', 'in progress', 'completed']
        for status in statuses:
            cur.execute(
                "INSERT INTO status (name) VALUES (%s) ON CONFLICT (name) DO NOTHING",
                (status,)
            )

        # Seed tasks table with fake data
        for _ in range(20):
            title = fake.sentence(nb_words=6)
            description = fake.text(max_nb_chars=200)
            status_id = fake.random_int(min=1, max=3)  # Assuming status IDs are 1, 2, 3
            user_id = fake.random_int(min=1, max=10)   # Assuming user IDs are between 1 and 10
            cur.execute(
                "INSERT INTO tasks (title, description, status_id, user_id) VALUES (%s, %s, %s, %s)",
                (title, description, status_id, user_id)
            )

        # Commit changes
        conn.commit()

        # Close the cursor and connection
        cur.close()
        conn.close()

        print("Data successfully seeded!")

    except Exception as error:
        print(f"Error: {error}")
    finally:
        if conn is not None:
            conn.close()

if __name__ == '__main__':
    seed_data()
