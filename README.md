🚀 Flask Docker App

📌 Description

A Flask-based web app running in Docker & Docker Compose, providing API endpoints for addition and multiplication.



⚙️ Setup & Run

1️⃣ Clone & Navigate
sh
Copy
Edit

git clone https://github.com/saurabh-mate/flask-docker-app.git
cd flask-docker-app

2️⃣ Build & Run
sh
Copy
Edit
                  
     docker-compose up --build -d


🔥 API Endpoints

Endpoint	Description

    /hello	Returns "Hello, World!"
    
    /add?num1=5&num2=3	Returns 5 + 3 = 8
    
    /multiply?num1=4&num2=2	Returns 4 * 2 = 8


📌 Example Usage

Open in Browser:
bash
Copy
Edit

http://localhost:5000/hello
    
http://localhost:5000/add?num1=5&num2=3
    
http://localhost:5000/multiply?num1=4&num2=2


💡 Future Enhancements

[] Add more operations (subtraction, division)

[] Implement authentication

[] Deploy to AWS (Amazon Web Services)



📝 Author

Saurabh Dnyaneshwar Mate
📧 saurabhmate226@gmail.com
🌐 GitHub

