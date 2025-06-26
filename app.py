from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

# Load the course list and similarity matrix
try:
    similarity = pickle.load(open('models/similarity.pkl', 'rb'))
    courses_df = pickle.load(open('models/courses.pkl', 'rb'))
    course_list_dicts = pickle.load(open('models/course_list.pkl', 'rb'))
except FileNotFoundError:
    print("Error: One or more model files not found. Make sure 'models/similarity.pkl', 'models/courses.pkl', and 'models/course_list.pkl' exist.")
    exit()
except Exception as e:
    print(f"Error loading model files: {e}")
    exit()

course_names = courses_df['course_name'].values.tolist()
course_url_dict = courses_df.set_index('course_name')['course_url'].to_dict()

def recommend(course_name):
    if course_name not in courses_df['course_name'].values:
        return []

    try:
        index = courses_df[courses_df['course_name'] == course_name].index[0]
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])
        recommended_courses = []
        for i in distances[1:7]:
            recommended_name = courses_df.iloc[i[0]].course_name
            recommended_url = courses_df.iloc[i[0]].course_url
            recommended_courses.append({'name': recommended_name, 'url': recommended_url})
        return recommended_courses
    except IndexError:
        return []
    except Exception as e:
        print(f"Error during recommendation: {e}")
        return []

@app.route('/', methods=['GET', 'POST'])
def index():
    recommended_courses = []
    selected_course = None
    if request.method == 'POST':
        selected_course = request.form['course_name']
        recommended_courses = recommend(selected_course)
    return render_template('index.html', courses=course_names, recommendations=recommended_courses, selected_course=selected_course)

if __name__ == '__main__':
    app.run(debug=True)