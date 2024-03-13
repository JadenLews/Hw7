import os
import time
from urllib.parse import parse_qs
from html import escape

import psycopg2


def wrapBody(body, title="Blank Title"):

    return (
        "<html>\n"
        f"<head><title>{title}</title></head>\n"
        "<body>\n"
        f"{body}\n"
        "</body>\n"
        "</html>\n"
    )


def showForm():

    body = (
        "<h1>Calculator</h1>\n"
        "<form method='post'>\n"
        "<b>First operand:</b>\n"
        "<input type='text' name='op1'><br>\n"
        "<b>Second operand:</b>\n"
        "<input type='text' name='op2'><br>\n"
        "<select name='operator'>\n"
        "<option value=''>--Choose an operator--</option>\n"
        "<option value='+'>+</option>\n"
        "<option value='-'>-</option>\n"
        "</select><br>\n"
        "<input type='submit' value='Calculate'><br>\n"
    )

    return body

def showRoom():

    body = (
    "<h1>Rooms</h1>\n"
    "<form method='post'>\n"
    "<b>Room Number:</b>\n"
    "<input type='text' name='number'><br>\n"
    "<b>Capacity:</b>\n"
    "<input type='text' name='capacity'><br>\n"
    "<input type='submit' value='Add Room'><br>\n"
    )

    return body

def testRoom():
    return """
    <h2>Add A Room</h2>
    <p>
    <FORM METHOD="POST">
    <table>
        <tr>
            <td>Room Number</td>
            <td><INPUT TYPE="TEXT" NAME="number" VALUE=""></td>
        </tr>
        <tr>
            <td>Capacity</td>
            <td><INPUT TYPE="TEXT" NAME="capacity" VALUE=""></td>
        </tr>
        <tr>
            <td></td>
            <td>
            <input type="submit" name="addRoom" value="Add!">
            </td>
        </tr>
    </table>
    </FORM>
    """

def testRoom2():
    return """
    <h2>Add A Room</h2>
    <p>
    <FORM METHOD="POST">
    <table>
        <tr>
            <td>Room Number</td>
            <td><INPUT TYPE="TEXT" NAME="number" VALUE=""></td>
        </tr>
        <tr>
            <td>Capacity</td>
            <td><INPUT TYPE="TEXT" NAME="capacity" VALUE=""></td>
        </tr>
        <tr>
            <td></td>
            <td>
            <input type="submit" name="addRoom" value="Add Room">
            </td>
        </tr>
    </table>
    </FORM>
    """


def calculate(op1, op2, operator):
    if operator == "+":
        return op1 + op2
    elif operator == "-":
        return op1 - op2
    else:
        return "Error"

def showProfilePage(conn):
    body = """
    <a href="./university.py">Return to main page.</a>
    """
    cur = conn.cursor()

    sql = """
    SELECT *
    FROM room
    """
    cur.execute(sql)
    data = cur.fetchall()

    body += """
    <h2>Rooms List</h2>
    <p>
    <table border=1>
      <tr>
        <td><font size=+1"><b>Room Number</b></font></td>
        <td><font size=+1"><b>Capacity</b></font></td>
        <td><font size=+1"><b>delete</b></font></td>
      </tr>
    """

    count = 0
    for item in data:
        count += 1
        body += (
            "<tr>"
            f"<td>{item[0]}</td>"
            f"<td>{str(item[1])}</td>"
            "<td><form method='post' action='miniFacebook.py'>"
            f"<input type='hidden' NAME='idNum' VALUE='{item[0]}'>"
            '<input type="submit" name="deleteProfile" value="Delete">'
            "</form></td>"
            "</tr>\n"
        )
        #body += item[0]
        #body += str(item[1])
    body += "</table>" f"<p>Found {count} rooms.</p>"
    return body


def deleteProfile(conn, idNum):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM room WHERE number = %s", (idNum,))
    data = cursor.fetchall()
    string = ""
    #for item in data:
        #string += str
    return str(data[0][0])
    return str(idNum)
    # cursor.execute("DELETE FROM profiles WHERE id = %s", (idNum,))
    # conn.commit()
    # if cursor.rowcount > 0:
    #     return "Delete Profile Succeeded."
    # else:
    #     return "Delete Profile Failed."


def get_qs_post(env):
    """
    :param env: WSGI environment
    :returns: A tuple (qs, post), containing the query string and post data,
              respectively
    """
    # the environment variable CONTENT_LENGTH may be empty or missing
    try:
        request_body_size = int(env.get("CONTENT_LENGTH", 0))
    except (ValueError):
        request_body_size = 0
    # When the method is POST the variable will be sent
    # in the HTTP request body which is passed by the WSGI server
    # in the file like wsgi.input environment variable.
    request_body = env["wsgi.input"].read(request_body_size).decode("utf-8")
    post = parse_qs(request_body)
    return parse_qs(env["QUERY_STRING"]), post


def application(env, start_response):
    qs, post = get_qs_post(env)
    body = "Available databases: "
    try:
        conn = psycopg2.connect(
            host="postgres",
            dbname=os.environ["POSTGRES_DB"],
            user=os.environ["POSTGRES_USER"],
            password=os.environ["POSTGRES_PASSWORD"],
        )
        cur = conn.cursor()
        cur.execute("SELECT * FROM room")
        body += str(cur.fetchall())
    except psycopg2.Warning as e:
        print(f"Database warning: {e}")
        body += "Check logs for DB warning"
    except psycopg2.Error as e:
        print(f"Database error: {e}")
        body += "Check logs for DB error"

    idNum = None
    if "idNum" in post:
        idNum = post["idNum"][0]
    #body = showForm()
    #body = showRoom()
    if 'addRoom' in post:
        body = showProfilePage(conn)
    elif 'addRoom2' in post:
        body = testRoom()
    elif "deleteProfile" in post:
            body += deleteProfile(conn, idNum)
            body += str(post)
            #idNum = None
    else:
        body = testRoom()
    if ("op1" in post) and ("op2" in post) and ("operator" in post):
        op1 = float(post["op1"][0])
        op2 = float(post["op2"][0])
        operator = post["operator"][0]
        body += (
            f"<b>Result:</b> "
            f"{op1} {operator} {op2} = {calculate(op1, op2, operator)}"
        )
    start_response("200 OK", [("Content-Type", "text/html")])
    return [wrapBody(body, title="Calculator").encode("utf-8")]


if __name__ == "__main__":
    main()
