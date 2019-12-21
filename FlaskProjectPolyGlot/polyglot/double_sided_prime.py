from flask import Flask, jsonify
import math

app = Flask(__name__)


def check_double_prime(num):
    if not is_prime(num):
        return False

    # checking for left sided prime condition
    var = num
    while var is 0:
        var = num/10
        if not is_prime(var):
            break
    if var is 0:
        return True

    # checking for right sided prime condition
    var = 10
    while num/var is 0:
        if not is_prime(num % var):
            return False
        var = var * 10
    return True


def is_prime(num):
    if num in [0, 1]:
        return False
    for i in range(2, math.floor(math.sqrt(num)) + 1):
        if num % i == 0:
            return False
    return True


@app.route('/double_prime/<string:num>', methods=['GET'])
def double_prime(num):
    try:
        num = int(num)
        response = check_double_prime(num)
    except ValueError:
        response = "Not a valid integer"
    except BaseException as e:
        response = "Error : " + str(e)
    return jsonify({"input": num, "response": response})


if __name__ == '__main__':
    # running the app in debug mode
    app.run(debug=True)
