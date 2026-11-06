"""
TCP Echo Server
รับข้อความจาก client แล้วส่งข้อความเดิมกลับไป (echo)
รองรับหลาย client พร้อมกันด้วย threading
"""
import socket
import threading

HOST = "0.0.0.0"   # รับการเชื่อมต่อจากทุก interface
PORT = 5000
BUFFER_SIZE = 1024


def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")
    with conn:
        while True:
            data = conn.recv(BUFFER_SIZE)
            if not data:  # client ปิดการเชื่อมต่อ
                break
            message = data.decode("utf-8")
            print(f"[RECEIVED from {addr}] {message}")
            conn.sendall(data)  # echo กลับไป
            print(f"[ECHOED to {addr}] {message}")
    print(f"[DISCONNECTED] {addr} closed the connection.")


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen()
        print(f"[TCP SERVER] Listening on {HOST}:{PORT} ...")
        try:
            while True:
                conn, addr = server.accept()
                thread = threading.Thread(
                    target=handle_client, args=(conn, addr), daemon=True
                )
                thread.start()
        except KeyboardInterrupt:
            print("\n[TCP SERVER] Shutting down.")


if __name__ == "__main__":
    main()
