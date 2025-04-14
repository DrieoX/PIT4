# PIT4
🛠️ Setup Instructions
Prerequisites
  Python 3.8 or higher
  PostgreSQL database

Installation
Clone the repository:

  <pre>git clone https://github.com/Drieox/PIT4.git
  cd PIT4</pre>


Create and activate a virtual environment:

  <pre>python -m venv env
  source env/bin/activate  # On Windows: env\Scripts\activate</pre>

Install dependencies:
  <pre>pip install -r requirements.txt</pre>

Configure environment variables:

Create a .env file in the project root with the following content:
  <pre>DATABASE_URL=postgresql://username:password@localhost:5432/todo_db</pre>
Replace username, password, and todo_db with your PostgreSQL credentials and desired database name.

Endpoints:
get('/')

post('/', task);

put(`/${id}/`, updatedTask);

delete(`/${id}/`);

Live dev links:
Netlify(React)
<pre>https://beautiful-gnome-a14487.netlify.app/</pre>

Render(FastAPI | PostgreSql):
<pre>https://pit4.onrender.com
https://pit4.onrender.com/api/todos</pre>
