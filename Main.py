import sqlite3

class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.userId = ""

class Task:
    def __init__(self, name, status, userId):
        self.name = name
        self.status = status
        self.userId = userId
        self.taskId = ""

class UserRepository:
    def addUser(self, user):
        con = sqlite3.connect('database.db')
        cur = con.cursor()
        cur.execute(f"INSERT INTO Users (Name, Email) VALUES (?, ?)", (user.name, user.email))
        userId = cur.lastrowid
        con.commit()
        con.close()
        return userId
        

    def getUserById(self, userId):
        con = sqlite3.connect("database.db")
        res = con.execute("SELECT * FROM Users WHERE UID = ?", (userId, ))
        userData = res.fetchone()
        con.close()
        if userData:
            return userData
        return None

class TaskRepository:
    def addTask(self, task):
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        cur.execute("INSERT INTO Tasks (Name, Status, UID) VALUES (?, ?, ?)", (task.name, task.status, task.userId))
        taskId = cur.lastrowid
        con.commit()
        con.close()
        return taskId

    def getTasksByUserId(self, userId):
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        res = cur.execute("SELECT * FROM Tasks WHERE UID = ?", (userId, ))
        tasks = res.fetchall()
        con.close()
        return tasks

    def updateTaskStatus(self, taskId, status):
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        cur.execute("UPDATE Tasks SET Status = ? WHERE TID = ?", (status, taskId))
        con.commit()
        con.close()
        return True

    def deleteTask(self, taskId):
        con = sqlite3.connect("database.db")
        cur = con.cursor()
        cur.execute("DELETE FROM Tasks WHERE TID = ?", (taskId, ))
        con.commit()
        con.close()
        return True


if __name__ == "__main__":
    userRepo = UserRepository()
    taskRepo = TaskRepository()
    
