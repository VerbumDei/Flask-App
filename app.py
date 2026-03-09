from flask import Flask, request

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h2>Food Recommendation App</h2>

    <form action="/result" method="post">
        Enter your mood:<br>
        <input type="text" name="mood"><br><br>

        <input type="submit" value="Get Food Suggestion">
    </form>
    """


@app.route("/result", methods=["POST"])
def result():
    mood = request.form["mood"].lower()

    if "happy" in mood:
        food = "Pizza"
    elif "tired" in mood:
        food = "Coffee"
    elif "hungry" in mood:
        food = "Burger"
    elif "sad" in mood:
        food = "Ice Cream"
    else:
        food = "Sandwich"

    return f"""
    <h2>Food Suggestion</h2>

    <p><b>Your mood:</b> {mood}</p>
    <p><b>Recommended food:</b> {food}</p>

    <br>
    <a href="/">Try Again</a>
    """


if __name__ == "__main__":
    app.run(debug=True, port=5001)
