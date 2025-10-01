from fastapi import FastAPI

app = FastAPI()
users = []


@app.get("/")
def get_root():
    return {"message": "Welcome to the API!", "status": "success"}


@app.post("/users")
def create_user(
    name: str,
    email: str,
    password: str,
):
    users.append(
        {"id": len(users) + 1, "name": name, "email": email, "password": password}
    )
    return {
        "status": "success",
        "data": users[len(users) - 1],
    }


@app.get("/users/{user_id}")
def get_user_by_id(user_id: int):
    return {
        "status": "success",
        "data": users[user_id - 1],
    }


@app.get("/users")
def get_all_users():
    return {
        "status": "success",
        "data": users,
    }


@app.put("/users/{user_id}")
def update_user(user_id: int, name: str, email: str, password: str):

    users[user_id - 1]["name"] = name
    users[user_id - 1]["email"] = email
    users[user_id - 1]["password"] = password

    return {
        "status": "success",
        "data": users[user_id - 1],
    }


@app.patch("/users/{user_id}")
def update_user(user_id: int, name: str, email: str, password: str):
    users[user_id - 1]["name"] = name
    users[user_id - 1]["email"] = email

    return {
        "status": "success",
        "data": users[user_id - 1],
    }


@app.delete("/users/{user_id}")
def delete_user(user_id: int):
    users.remove(users[user_id - 1])

    return {
        "status": "success",
        "data": None,
    }
