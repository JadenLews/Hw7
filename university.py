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
        <td><font size=+1"><b>Delete</b></font></td>
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
        <td><font size=+1"><b>ID</b></font></td>
        <td><font size=+1"><b>Name</b></font></td>
        <td><font size=+1"><b>Update</b></font></td>
        <td><font size=+1"><b>Delete</b></font></td>
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
        <td><font size=+1"><b>Delete</b></font></td>
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
        <td><font size=+1"><b>Delete</b></font></td>
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
    (number, capacity) = data[0]
    #return str(number)
    return """
    <h2>Update Your Room</h2>
    <p>
    <FORM METHOD="POST">
    <table>
        <tr>
            <td>Room Number</td>
            <td><INPUT TYPE="TEXT" NAME="update_number" VALUE="%s"></td>
        </tr>
        <tr>
            <td>Capacity</td>
            <td><INPUT TYPE="TEXT" NAME="update_capacity" VALUE="%s"></td>
        </tr>
        <tr>
            <td></td>
            <td>
                <input type="hidden" name="updateidNum" value="%s">
                <input type="submit" name="completeUpdate" value="Update!">
            </td>
        </tr>
    </table>
    </FORM>
    """ % (
        number,
        capacity,
        idNum,
    )

def processRoomUpdate(conn, oldnumber, newnumber, capacity):
    try:
        cursor = conn.cursor()
        if (oldnumber == newnumber):
            cursor.execute("UPDATE room SET capacity = %s WHERE number = %s", (capacity, newnumber,))
        else:
            cursor.execute("INSERT INTO room (number, capacity) VALUES (%s, %s)", (newnumber, capacity,))
            conn.commit()
            cursor.execute("UPDATE course SET room = %s WHERE room = %s", (newnumber, oldnumber,))
            cursor.execute("DELETE FROM room WHERE number = %s", (str(oldnumber),))
            conn.commit()
    except Exception as e:
        return f"error: {str(e)}"
    return 'Updated Room Success'

def getUpdateCourseForm(conn, idNum):
    # First, get current data for this profile
    cursor = conn.cursor()

    sql = """
    SELECT *
    FROM course
    WHERE number=%s
    """
    cursor.execute(sql, (idNum,))

    data = cursor.fetchall()
    # Create a form to update this profile
    (number, title, room) = data[0]
    #return str(number)
    return """
    <h2>Update Your Course</h2>
    <p>
    <FORM METHOD="POST">
    <table>
        <tr>
            <td>Course Number</td>
            <td><INPUT TYPE="TEXT" NAME="update_courseNumber" VALUE="%s"></td>
        </tr>
        <tr>
            <td>Course Title</td>
            <td><INPUT TYPE="TEXT" NAME="update_title" VALUE="%s"></td>
        </tr>
         <tr>
            <td>Course Room</td>
            <td><INPUT TYPE="TEXT" NAME="update_room" VALUE="%s"></td>
        </tr>
        <tr>
            <td></td>
            <td>
                <input type="hidden" name="updateidNum" value="%s">
                <input type="submit" name="completeUpdate" value="Update!">
            </td>
        </tr>
    </table>
    </FORM>
    """ % (
        number,
        title,
        room,
        idNum,
    )

def processCourseUpdate(conn, oldnumber, newnumber, title, room):
    try:
        cursor = conn.cursor()
        if (oldnumber == newnumber):
            cursor.execute("UPDATE course SET title = %s, room = %s WHERE number = %s", (title, room, newnumber,))
        else:
            cursor.execute("INSERT INTO course (number, title, room) VALUES (%s, %s, %s)", (newnumber, title, room,))
            conn.commit()
            cursor.execute("UPDATE enrolled SET course = %s WHERE course = %s", (newnumber, oldnumber,))
            cursor.execute("DELETE FROM course WHERE number = %s", (str(oldnumber),))
            conn.commit()
    except Exception as e:
        return f"error: {str(e)}"
    return 'Updated Course Success'

def getUpdateEnrollmentForm(conn, idNum):
    # First, get current data for this profile
    cursor = conn.cursor()

    sql = """
    SELECT *
    FROM enrolled
    WHERE student=%s
    """
    cursor.execute(sql, (idNum,))

    data = cursor.fetchall()
    # Create a form to update this profile
    (student, course) = data[0]
    #return str(number)
    return """
    <h2>Update Your Enrollment Information</h2>
    <p>
    <FORM METHOD="POST">
    <table>
        <tr>
            <td>Student ID</td>
            <td><INPUT TYPE="TEXT" NAME="update_student" VALUE="%s"></td>
        </tr>
        <tr>
            <td>Course Number</td>
            <td><INPUT TYPE="TEXT" NAME="update_course" VALUE="%s"></td>
        </tr>
        <tr>
            <td></td>
            <td>
                <input type="hidden" name="updateidNum" value="%s">
                <input type="submit" name="completeUpdate" value="Update!">
            </td>
        </tr>
    </table>
    </FORM>
    """ % (
        student,
        course,
        idNum,
    )

def processEnrollmentUpdate(conn, oldnumber, newnumber, course):
    try:
        cursor = conn.cursor()
        if (oldnumber == newnumber):
            cursor.execute("UPDATE enrolled SET course = %s WHERE student = %s", (course, newnumber,))
        else:
            cursor.execute("INSERT INTO enrolled (student, course) VALUES (%s, %s, %s)", (newnumber, course,))
            conn.commit()
            cursor.execute("DELETE FROM enrolled WHERE student = %s", (str(oldnumber),))
            conn.commit()
    except Exception as e:
        return f"error: {str(e)}"
    return 'Updated Enrollment Success'

def getUpdateStudentForm(conn, idNum):
    # First, get current data for this profile
    cursor = conn.cursor()

    sql = """
    SELECT *
    FROM student
    WHERE id=%s
    """
    cursor.execute(sql, (idNum,))

    data = cursor.fetchall()
    # Create a form to update this profile
    (Id, name) = data[0]
    #return str(number)
    return """
    <h2>Update Your Student Information</h2>
    <p>
    <FORM METHOD="POST">
    <table>
        <tr>
            <td>Student ID</td>
            <td><INPUT TYPE="TEXT" NAME="update_id" VALUE="%s"></td>
        </tr>
        <tr>
            <td>Student Name</td>
            <td><INPUT TYPE="TEXT" NAME="update_name" VALUE="%s"></td>
        </tr>
        <tr>
            <td></td>
            <td>
                <input type="hidden" name="updateidNum" value="%s">
                <input type="submit" name="completeUpdate" value="Update!">
            </td>
        </tr>
    </table>
    </FORM>
    """ % (
        Id,
        name,
        idNum,
    )

def processStudentUpdate(conn, oldnumber, newnumber, name):
    try:
        cursor = conn.cursor()
        if (oldnumber == newnumber):
            cursor.execute("UPDATE student SET name = %s WHERE id = %s", (name, newnumber,))
        else:
            cursor.execute("INSERT INTO student (id, name) VALUES (%s, %s)", (newnumber, name,))
            conn.commit()
            cursor.execute("UPDATE enrolled SET student = %s WHERE student = %s", (newnumber, oldnumber,))
            cursor.execute("DELETE FROM student WHERE id = %s", (str(oldnumber),))
            conn.commit()
    except Exception as e:
        return f"error: {str(e)}"
    return 'Updated Student Success'

def try_deleteCourse (conn, course_number):
    try: 
        cur = conn.cursor()
        sqlEnrollment = "DELETE FROM enrolled WHERE course = %s"
        params = (str(course_number),)
        cur.execute(sqlEnrollment, params)
        conn.commit()
    except:
        return "error"
    try:
        cur = conn.cursor()
        sqlCourse = "DELETE FROM course WHERE number = %s"
        params = (str(course_number),)
        cur.execute(sqlCourse, params)
        conn.commit()
    except:
        return "error"
    return "success"

def try_deleteStudent(conn, idNum):
    try:
        cur = conn.cursor()
        sql = "DELETE FROM enrolled WHERE student = %s"
        params = (str(idNum),)
        cur.execute(sql, params)
        conn.commit()
    except:
        return "error"
    
    try:
        cur = conn.cursor()
        sql = "DELETE FROM majors_in WHERE student = %s"
        params = (str(idNum),)
        cur.execute(sql, params)
        conn.commit()
    except:
        return "error"

    try:
        cur = conn.cursor()
        sql = "DELETE FROM student WHERE id = %s"
        params = (str(idNum),)
        cur.execute(sql, params)
        conn.commit()
    except:
        return "error"
    
    return "success"

def try_deleteEnrollment(conn, idNum, course):
    try:
        cur = conn.cursor()
        sql = "DELETE FROM enrolled WHERE student = %s AND course = %s"
        params = (str(idNum), course)
        cur.execute(sql, params)
        conn.commit()
    except:
        return "error"
    return "success"


def show_add_enrollment(conn):
    return """
    <a href="./university.py">Return to main page.</a>
    <h2>Add Enrollment</h2>
    <p>
    <FORM METHOD="POST">
    <table>
        <tr>
            <td>Student</td>
            <td><INPUT TYPE="TEXT" NAME="student" VALUE=""></td>
        </tr>
        <tr>
            <td>Course</td>
            <td><INPUT TYPE="TEXT" NAME="course" VALUE=""></td>
        </tr>
        <tr>
            <td></td>
            <td>
            <input type="submit" name="submitEnrollment" value="Add Enrollment!">
            </td>
        </tr>
    </table>
    </FORM>
    """

def tryaddEnrollment(conn, student, course):
    try:
        cur = conn.cursor()
        sql = "INSERT INTO enrolled VALUES (%s,%s)"
        params = (student, course)
        cur.execute(sql, params)
        conn.commit()
    except:
        return "error"
    return "success"

def show_add_student(conn):
    return """
    <a href="./university.py">Return to main page.</a>
    <h2>Add A Student</h2>
    <p>
    <FORM METHOD="POST">
    <table>
        <tr>
            <td>Id</td>
            <td><INPUT TYPE="TEXT" NAME="Id" VALUE=""></td>
        </tr>
        <tr>
            <td>Name</td>
            <td><INPUT TYPE="TEXT" NAME="Name" VALUE=""></td>
        </tr>
        <tr>
            <td></td>
            <td>
            <input type="submit" name="submitStudent" value="Add Student!">
            </td>
        </tr>
    </table>
    </FORM>
    """

def tryaddStudent(conn, id, name):
    try:
        cur = conn.cursor()
        sql = "INSERT INTO student VALUES (%s,%s)"
        params = (id, name)
        cur.execute(sql, params)
        conn.commit()
    except:
        return "error"
    return "success"

def show_add_course(conn):
    return """
    <a href="./university.py">Return to main page.</a>
    <h2>Add A Course</h2>
    <p>
    <FORM METHOD="POST">
    <table>
        <tr>
            <td>Number</td>
            <td><INPUT TYPE="TEXT" NAME="number" VALUE=""></td>
        </tr>
        <tr>
            <td>Title</td>
            <td><INPUT TYPE="TEXT" NAME="title" VALUE=""></td>
        </tr>
        <tr>
            <td>Room</td>
            <td><INPUT TYPE="TEXT" NAME="room" VALUE=""></td>
        </tr>
        <tr>
            <td></td>
            <td>
            <input type="submit" name="submitCourse" value="Add Student!">
            </td>
        </tr>
    </table>
    </FORM>
    """

def tryaddCourse(conn, number, title, room):
    try:
        cur = conn.cursor()
        sql = "INSERT INTO course VALUES (%s,%s,%s)"
        params = (number, title, room)
        cur.execute(sql, params)
        conn.commit()
    except:
        return "error"
    return "success"


def deleteRoom(conn, idNum):
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM room WHERE number = %s", (idNum,))
    data = cursor.fetchall()
    string = ""
    #for item in data:
        #string += str
    return str(data[0][0])
    return str(idNum)


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
    body = ""
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
    if "deleteRoom" in post:
            body += try_deleteRoom(conn, post['idNum'][0])
            body += showProfilePage(conn)
    elif "deleteCourse" in post:
        body += try_deleteCourse(conn, post['idNum'][0])
        body += showProfilePage(conn)
    elif "deleteStudent" in post:
            body += try_deleteStudent(conn, post['idNum'][0])
            # body += str(post)
            # body += str(post['idNum'][0])
            body += showProfilePage(conn)
    elif "deleteEnrollment" in post:
            body += try_deleteEnrollment(conn, post['idNum'][0], post['courseNum'][0])
            # body += str(post)
            # body += str(post['idNum'][0])
            body += showProfilePage(conn)
    elif "addRooms" in post:
        body += show_add_room(conn)
    elif "submitRoom" in post:
        body += tryaddRoom(conn, post["room_number"][0], post["capacity"][0])
        body += showProfilePage(conn)
    elif 'updateRoom' in post:
        body += getupdateRoomform(conn, post['update'][0])
    elif 'update_number' in post:
        body += processRoomUpdate(conn, post['updateidNum'][0], post['update_number'][0], post['update_capacity'][0])
        body += showProfilePage(conn)
    elif 'updateCourse' in post:
        body += getUpdateCourseForm(conn, post['idNum'][0])
    elif 'update_courseNumber' in post:
        body += processCourseUpdate(conn, post['updateidNum'][0], post['update_courseNumber'][0], post['update_title'][0], post['update_room'][0])
        body += showProfilePage(conn)
    elif 'updateEnrollment' in post:
        body += getUpdateEnrollmentForm(conn, post['idNum'][0])
    elif 'update_student' in post:
        body += processEnrollmentUpdate(conn, post['updateidNum'][0], post['update_student'][0], post['update_course'][0])
        body += showProfilePage(conn)
    elif 'updateStudent' in post:
        body += getUpdateStudentForm(conn, post['idNum'][0])
    elif 'update_id' in post:
        body += processStudentUpdate(conn, post['updateidNum'][0], post['update_id'][0], post['update_name'][0])
        body += showProfilePage(conn)
    elif "addEnrollment" in post:
        body += show_add_enrollment(conn)
    elif "submitEnrollment" in post:
        body += tryaddEnrollment(conn, post["student"][0], post["course"][0])
        body += showProfilePage(conn)
    elif "addStudent" in post:
        body += show_add_student(conn)
        body += str(post)
    elif "submitStudent" in post:
        body += tryaddStudent(conn, post["Id"][0], post["Name"][0])
        body += showProfilePage(conn)
    elif "addCourse" in post:
        body += show_add_course(conn)
        body += str(post)
    elif "submitCourse" in post:
        body += tryaddCourse(conn, post["number"][0], post["title"][0], post["room"][0])
        body += showProfilePage(conn)
    else:
        body = showProfilePage(conn)
        body += str(post)
    
    start_response("200 OK", [("Content-Type", "text/html")])
    return [wrapBody(body, title="University Web App").encode("utf-8")]


if __name__ == "__main__":
    main()