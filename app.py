from flask import Flask, render_template
import requests, logging, logging.config

app = Flask(__name__)

logging.config.fileConfig(fname="log_config.ini", disable_existing_loggers=False)

BASE_URL = "https://api.github.com/users"


def get_profile_info(username: str):
    logging.info(f"username: {username}")
    user_info = {}
    url = f"{BASE_URL}/{username}"
    try:
        response = requests.get(url).json()
        user_info["id"] = response["id"]
        user_info["name"] = response["name"]
        user_info["avatar_url"] = response["avatar_url"]
        user_info["bio"] = response["bio"]
        user_info["status_code"] = 200
    except:
        logging.error("Exception occurred", exc_info=True)
        user_info["status_code"] = 404
    return user_info


@app.route("/")
def health_check():
    return "<h1 style='color:green; text-align: center; padding-top: 20%'>OK</h1>"


@app.route("/info/<name>")
def get_info(name):
    user_data = get_profile_info(name)
    return user_data


@app.route("/profile/<name>")
def get_name_info(name):
    user_data = get_profile_info(name)
    if user_data.get("status_code") == 200:
        return render_template("profile_info.html", profile_data=user_data)
    else:
        return f'<h1 style="color:red">User no found status {user_data["status_code"]}</h1>'


if __name__ == "__main__":
    app.run()
