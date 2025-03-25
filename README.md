<h2>⏪ Task Manager ⏩</h2>
<br>

### Installation
`pip install --no-cache-dir -r requirements.txt`

`streamlit run app.py`

Access the application at http://localhost:8501

</br>

### Containerize Streamlit app

+ Build the image:
`docker image build --no-cache -t todo-app:0.1 .`

+ Run the container:
`docker container run -d -p 8501:8501 todo-app:0.1`
