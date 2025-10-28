from sqlalchemy import create_engine, text

db_connection_string = "postgresql://qa:skyqa@5.101.50.27:5432/x_clients"
db = create_engine(db_connection_string)


def test_add_teacher():
    connection = db.connect()
    connection.execute(
        text(
            "INSERT INTO teacher (teacher_id, group_id, email) VALUES "
            "(1, 101, 'teacher1@example.com')"
        )
    )
    result = connection.execute(
        text("SELECT * FROM teacher WHERE teacher_id=1")
    )
    teacher = result.mappings().first()
    assert teacher["teacher_id"] == 1
    assert int(teacher["group_id"]) == 101
    connection.execute(
        text("DELETE FROM teacher WHERE teacher_id=1")
    )
    connection.close()


def test_update_teacher():
    connection = db.connect()
    connection.execute(
        text(
            "INSERT INTO teacher (teacher_id, group_id, email) VALUES "
            "(2, 102, 'teacher2@example.com')"
        )
    )
    connection.execute(
        text("UPDATE teacher SET group_id = 202 WHERE teacher_id=2")
    )
    result = connection.execute(
        text("SELECT * FROM teacher WHERE teacher_id=2")
    )
    teacher = result.mappings().first()
    assert int(teacher["group_id"]) == 202
    connection.execute(
        text("DELETE FROM teacher WHERE teacher_id=2")
    )
    connection.close()


def test_delete_teacher():
    connection = db.connect()
    connection.execute(
        text(
            "INSERT INTO teacher (teacher_id, group_id, email) VALUES "
            "(3, 103, 'teacher3@example.com')"
        )
    )
    connection.execute(
        text("DELETE FROM teacher WHERE teacher_id=3")
    )
    result = connection.execute(
        text("SELECT * FROM teacher WHERE teacher_id=3")
    )
    teacher = result.mappings().first()
    assert teacher is None
    connection.close()
