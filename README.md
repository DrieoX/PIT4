# PIT4
🛠️ Setup Instructions
Prerequisites
  Python 3.8 or higher
  PostgreSQL database

Installation
Clone the repository:

  git clone https://github.com/Drieox/PIT4.git
  cd PIT4


Create and activate a virtual environment:
##codeline
  python -m venv env
  source env/bin/activate  # On Windows: env\Scripts\activate

Install dependencies:
  pip install -r requirements.txt

Configure environment variables:

Create a .env file in the project root with the following content:
  DATABASE_URL=postgresql://username:password@localhost:5432/todo_db
Replace username, password, and todo_db with your PostgreSQL credentials and desired database name.

Endpoints:
get('/')

post('/', task);

put(`/${id}/`, updatedTask);

delete(`/${id}/`);
