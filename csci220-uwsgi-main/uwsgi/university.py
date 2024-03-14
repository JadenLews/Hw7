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
def tryaddRoom(conn, room_number, capacity):
    try:
        cur = conn.cursor()
        sql = "INSERT INTO room VALUES (%s,%s)"
        params = (room_number, capacity)
        cur.execute(sql, params)
        conn.commit()
    except:
        return "error"
    return "success"

def try_deleteRoom(conn, room_number):
    try:
        cur = conn.cursor()
        sql = "DELETE FROM room WHERE number = %s"
        params = (str(room_number),)
        cur.execute(sql, params)
        conn.commit()
    except:
        return "error"
    return "success"

def show_add_room(conn):
    return """
    <a href="./university.py">Return to main page.</a>
    <h2>Add A Room</h2>
    <p>
    <FORM METHOD="POST">
    <table>
        <tr>
            <td>Room Number</td>
            <td><INPUT TYPE="TEXT" NAME="room_number" VALUE=""></td>
        </tr>
        <tr>
            <td>Capacity</td>
            <td><INPUT TYPE="TEXT" NAME="capacity" VALUE=""></td>
        </tr>
        <tr>
            <td></td>
            <td>
            <input type="submit" name="submitRoom" value="Add Room!">
            </td>
        </tr>
    </table>
    </FORM>
    """



def showProfilePage(conn):
    #room
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
        <td><font size=+1"><b>Update</b></font></td>
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
            f"<input type='hidden' NAME='update' VALUE='{item[0]}'>"
            '<input type="submit" name="updateRoom" value="Update">'
            "<td><form method='post' action='miniFacebook.py'>"
            f"<input type='hidden' NAME='idNum' VALUE='{item[0]}'>"
            '<input type="submit" name="deleteRoom" value="Delete">'
            "</form></td>"
            "</tr>\n"
        )
        #body += item[0]
        #body += str(item[1])
    body += "</table>" f"<p>Found {count} rooms.</p>"
    body += """
    <h2>Add A Room</h2>
    <p>
    <FORM METHOD="POST">
    <table>
        <tr>
            <td></td>
            <td>
            <input type="submit" name="addRooms" value="Add!">
            </td>
        </tr>
    </table>
    </FORM>
    """

    #student part
    cur = conn.cursor()

    sql = """
    SELECT *
    FROM student
    """
    cur.execute(sql)
    data = cur.fetchall()

    body += """
    <h2>Students List</h2>
    <p>
    <table border=1>
      <tr>
        <td><font size=+1"><b>Id</b></font></td>
        <td><font size=+1"><b>Name</b></font></td>
        <td><font size=+1"><b>Update</b></font></td>
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
            '<input type="submit" name="updateStudent" value="Update">'
            "<td><form method='post' action='miniFacebook.py'>"
            f"<input type='hidden' NAME='idNum' VALUE='{item[0]}'>"
            '<input type="submit" name="deleteStudent" value="Delete">'
            "</form></td>"
            "</tr>\n"
        )
        #body += item[0]
        #body += str(item[1])
    body += "</table>" f"<p>Found {count} Students.</p>"
    body += """
    <p>
    <FORM METHOD="POST">
    <table>
        <tr>
            <td></td>
            <td>
            <input type="submit" name="addStudent" value="Add Student">
            </td>
        </tr>
    </table>
    </FORM>
    """

    #course part
    cur = conn.cursor()

    sql = """
    SELECT *
    FROM course
    """
    cur.execute(sql)
    data = cur.fetchall()

    body += """
    <h2>Course List</h2>
    <p>
    <table border=1>
      <tr>
        <td><font size=+1"><b>Number</b></font></td>
        <td><font size=+1"><b>Title</b></font></td>
        <td><font size=+1"><b>Room</b></font></td>
        <td><font size=+1"><b>Update</b></font></td>
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
            f"<td>{str(item[2])}</td>"
            "<td><form method='post' action='miniFacebook.py'>"
            f"<input type='hidden' NAME='idNum' VALUE='{item[0]}'>"
            '<input type="submit" name="updateCourse" value="Update">'
            "<td><form method='post' action='miniFacebook.py'>"
            f"<input type='hidden' NAME='idNum' VALUE='{item[0]}'>"
            '<input type="submit" name="deleteCourse" value="Delete">'
            "</form></td>"
            "</tr>\n"
        )
        #body += item[0]
        #body += str(item[1])
    body += "</table>" f"<p>Found {count} Courses.</p>"
    body += """
    <p>
    <FORM METHOD="POST">
    <table>
        <tr>
            <td></td>
            <td>
            <input type="submit" name="addCourse" value="Add Course">
            </td>
        </tr>
    </table>
    </FORM>
    """

    #enrolled part
    cur = conn.cursor()

    sql = """
    SELECT *
    FROM enrolled
    """
    cur.execute(sql)
    data = cur.fetchall()

    body += """
    <h2>Enrollment List</h2>
    <p>
    <table border=1>
      <tr>
        <td><font size=+1"><b>Student</b></font></td>
        <td><font size=+1"><b>Course</b></font></td>
        <td><font size=+1"><b>Update</b></font></td>
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
            '<input type="submit" name="updateEnrollment" value="Update">'
            "<td><form method='post' action='miniFacebook.py'>"
            f"<input type='hidden' NAME='idNum' VALUE='{item[0]}'>"
            '<input type="submit" name="deleteEnrollment" value="Delete">'
            "</form></td>"
            "</tr>\n"
        )
        #body += item[0]
        #body += str(item[1])
    body += "</table>" f"<p>Found {count} Enrollments.</p>"
    body += """
    <p>
    <FORM METHOD="POST">
    <table>
        <tr>
            <td></td>
            <td>
            <input type="submit" name="addEnrollment" value="Add Enrollment">
            </td>
        </tr>
    </table>
    </FORM>
    """
    return body

def getupdateRoomform(conn, idNum):
    # First, get current data for this profile
    cursor = conn.cursor()

    sql = """
    SELECT *
    FROM room
    WHERE number=%s
    """
    cursor.execute(sql, (idNum,))

    data = cursor.fetchall()

    # Create a form to update this profile
    (idNum, lastname, firstName, email, activities) = data[0]

    return """
    <h2>Update Your Profile Page</h2>
    <p>
    <FORM METHOD="POST">
    <table>
        <tr>
            <td>Last Name</td>
            <td><INPUT TYPE="TEXT" NAME="lastname" VALUE="%s"></td>
        </tr>
        <tr>
            <td>First Name</td>
            <td><INPUT TYPE="TEXT" NAME="firstname" VALUE="%s"></td>
        </tr>
        <tr>
            <td>Email</td>
            <td><INPUT TYPE="TEXT" NAME="email" VALUE="%s"></td>
        </tr>
        <tr>
            <td>Activities</td>
            <td><TEXTAREA COLS=60 NAME="activities">%s</TEXTAREA></td>
        </tr>
        <tr>
            <td></td>
            <td>
            <input type="hidden" name="idNum" value="%s">
            <input type="submit" name="completeUpdate" value="Update!">
            </td>
        </tr>
    </table>
    </FORM>
    """ % (
        lastname,
        firstName,
        email,
        activities,
        idNum,
    )



def deleteRoom(conn, idNum):
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
        #cur = conn.cursor()
        #cur.execute("SELECT * FROM room")
        #body += str(cur.fetchall())
    except psycopg2.Warning as e:
        print(f"Database warning: {e}")
        body += "Check logs for DB warning"
    except psycopg2.Error as e:
        print(f"Database error: {e}")
        body += "Check logs for DB error"

    idNum = None
    if "idNum" in post:
        idNum = post["idNum"][0]
    if 'addRoom' in post:
        body += deleteRoom(conn, idNum)
        body += str(post)
    if 'addStudent' in post:
        body += deleteRoom(conn, idNum)
        body += str(post)
    if 'addCourse' in post:
        body += deleteRoom(conn, idNum)
        body += str(post)
    if 'addEnrollment' in post:
        body += deleteRoom(conn, idNum)
        body += str(post)
    elif "deleteRoom" in post:
            body += try_deleteRoom(conn, post['idNum'][0])
            body += str(post)
            body += str(post['idNum'][0])
            body += showProfilePage(conn)
    elif "addRooms" in post:
        body += show_add_room(conn)
        body += str(post)
        body += 'hgngng'
    elif "submitRoom" in post:
        body += tryaddRoom(conn, post["room_number"][0], post["capacity"][0])
        body += showProfilePage(conn)
    else:
        body = showProfilePage(conn)
    
    start_response("200 OK", [("Content-Type", "text/html")])
    return [wrapBody(body, title="Calculator").encode("utf-8")]


if __name__ == "__main__":
    main()
