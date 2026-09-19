import datetime, sqlite3
from turtle import title

def make_task(title: str, deadline: str):
    # Kết nối đến cơ sở dữ liệu
    conn = sqlite3.connect('realtime_data.db')
    cursor = conn.cursor()

    # Chèn nhiệm vụ mới vào bảng
    cursor.execute('''
        INSERT INTO realtime_data (title, deadline) VALUES (?, ?)
    ''', (title, deadline))

    # Lưu các thay đổi và đóng kết nối
    conn.commit()
    conn.close()

def finish_task(task_id: int):
    # Kết nối đến cơ sở dữ liệu
    conn = sqlite3.connect('realtime_data.db')
    cursor = conn.cursor()

    # Cập nhật trạng thái của nhiệm vụ thành hoàn thành (1)
    cursor.execute('''
        UPDATE realtime_data SET state = 1 WHERE id = ?
    ''', (task_id,))

    # Lưu các thay đổi và đóng kết nối
    conn.commit()
    conn.close()

def get_tasks():
    # Kết nối đến cơ sở dữ liệu
    conn = sqlite3.connect('realtime_data.db')
    cursor = conn.cursor()

    # Lấy tất cả các nhiệm vụ từ bảng
    cursor.execute('''
        SELECT * FROM realtime_data
    ''')
    tasks = cursor.fetchall()

    if not tasks:
        print("You don't have any tasks yet. Please add a task first.")
    else:
        for task in tasks:
            task_id, title, deadline, state = task
            status = "Completed" if state == 1 else "Pending"
            print(f"Task ID: {task_id}, Title: {title}, Deadline: {deadline}, Status: {status}")

    # Đóng kết nối
    conn.close()

    return tasks