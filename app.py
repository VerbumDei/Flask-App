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
    elif "sad" in mood:
        food = "Ice Cream"
    elif "hungry" in mood:
        food = "Burger"
    else:
        food = "Sandwich"

    return f"""
    <h2>Food Recommendation</h2>

    <p><b>Your Mood:</b> {mood}</p>
    <p><b>Suggested Food:</b> {food}</p>

    <br>
    <a href="/">Try Again</a>
    """


if __name__ == "__main__":
    app.run(port=5001,debug=True)
