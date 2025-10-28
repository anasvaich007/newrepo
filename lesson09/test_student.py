from sqlalchemy import create_engine, text

db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"
db = create_engine(db_connection_string)


def test_add_student():
    connection = db.connect()
    connection.execute(
        text(
            "INSERT INTO student (student_id, group_id, email) VALUES "
            "(1, 101, 'student1@example.com')"
        )
    )
    result = connection.execute(
        text("SELECT * FROM student WHERE student_id=1")
    )
    student = result.mappings().first()
    assert student["student_id"] == 1
    assert int(student["group_id"]) == 101
    connection.execute(
        text("DELETE FROM student WHERE student_id=1")
    )
    connection.close()


def test_update_student():
    connection = db.connect()
    connection.execute(
        text(
            "INSERT INTO student (student_id, group_id, email) VALUES "
            "(2, 102, 'student2@example.com')"
        )
    )
    connection.execute(
        text("UPDATE student SET group_id = 202 WHERE student_id=2")
    )
    result = connection.execute(
        text("SELECT * FROM student WHERE student_id=2")
    )
    student = result.mappings().first()
    assert int(student["group_id"]) == 202
    connection.execute(
        text("DELETE FROM student WHERE student_id=2")
    )
    connection.close()


def test_delete_student():
    connection = db.connect()
    connection.execute(
        text(
            "INSERT INTO student (student_id, group_id, email) VALUES "
            "(3, 103, 'student3@example.com')"
        )
    )
    connection.execute(
        text("DELETE FROM student WHERE student_id=3")
    )
    result = connection.execute(
        text("SELECT * FROM student WHERE student_id=3")
    )
    student = result.mappings().first()
    assert student is None
    connection.close()
