class GetQueries:
    GET_ALL_ALARMS = "SELECT * FROM Alarms"
    GET_SPECIFIC_ALARM = "SELECT * FROM Alarms WHERE id = ?"
    GET_WAITING_ALARMS = "SELECT * FROM Alarms WHERE triggered = 0 AND  alarm_datetime < DATETIME('now', 'localtime')"


class InsertQueries:
    CREATE_ALARM = "INSERT INTO Alarms (name, alarm_datetime, triggered) VALUES (?, ?, ?)"


class UpdateQueries:
    UPDATE_ALARM = "UPDATE Alarms SET name = ?, alarm_datetime = ?, triggered = ? WHERE id = ?"


class DeleteQueries:
    DELETE_ALARM = "DELETE FROM Alarms WHERE id = ?"
