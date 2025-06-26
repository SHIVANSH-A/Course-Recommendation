from flask import Flask, render_template, request
import pickle
import numpy as np
import pandas as pd

# Initialize Flask app
app = Flask(__name__)

# Load pre-trained data: similarity matrix, course details, and course list
try:
    similarity = pickle.load(open('models/similarity.pkl', 'rb'))  # Course similarity matrix
    courses_df = pickle.load(open('models/courses.pkl', 'rb'))      # DataFrame with course info (name + URL)
    course_list_dicts = pickle.load(open('models/course_list.pkl', 'rb'))  # Raw course list (not used directly here)
except FileNotFoundError:
    print("Error: One or more model files not found. Make sure 'models/similarity.pkl', 'models/courses.pkl', and 'models/course_list.pkl' exist.")
    exit()
except Exception as e:
    print(f"Error loading model files: {e}")
    exit()

# Extract course names and course URLs for use in the frontend and recommendation
course_names = courses_df['course_name'].values.tolist()
course_url_dict = courses_df.set_index('course_name')['course_url'].to_dict()

def recommend(course_name):
    """
    Recommend top 6 similar courses based on a selected course.

    Args:
        course_name (str): The input course selected by the user.

    Returns:
        list of dicts: Each dict contains 'name' and 'url' of a recommended course.
    """
    if course_name not in courses_df['course_name'].values:
        return []  # Invalid course input

    try:
        index = courses_df[courses_df['course_name'] == course_name].index[0]  # Get index of selected course
        distances = sorted(list(enumerate(similarity[index])), reverse=True, key=lambda x: x[1])  # Sort similar courses

        recommended_courses = []
        for i in distances[1:7]:  # Skip the first course (it's the same as input)
            recommended_name = courses_df.iloc[i[0]].course_name
            recommended_url = courses_df.iloc[i[0]].course_url
            recommended_courses.append({'name': recommended_name, 'url': recommended_url})
        return recommended_courses
    except IndexError:
        return []  # Index error, possibly out-of-bound access
    except Exception as e:
        print(f"Error during recommendation: {e}")
        return []

@app.route('/', methods=['GET', 'POST'])
def index():
    """
    Route for home page. Handles form submission and renders recommendations.
    """
    recommended_courses = []
    selected_course = None

    if request.method == 'POST':
        selected_course = request.form['course_name']  # Get selected course from form
        recommended_courses = recommend(selected_course)  # Get recommendations

    # Render the HTML page with form, course list, and any recommendations
    return render_template('index.html', 
                           courses=course_names, 
                           recommendations=recommended_courses, 
                           selected_course=selected_course)

# Run the app in debug mode (useful during development)
if __name__ == '__main__':
    app.run(debug=True)
