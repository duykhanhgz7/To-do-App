# khởi tạo database lưu thời gian thực
import sqlite3

def create_database():
    # Kết nối đến cơ sở dữ liệu (nếu chưa tồn tại, nó sẽ được tạo ra)
    conn = sqlite3.connect('realtime_data.db')
    cursor = conn.cursor()

    # Tạo bảng để lưu dữ liệu thời gian thực
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS realtime_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT,
            deadline DATETIME,
            state INTEGER DEFAULT 0
        )
    ''')

    # Lưu các thay đổi và đóng kết nối
    conn.commit()
    conn.close()