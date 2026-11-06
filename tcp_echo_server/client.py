"""
TCP Echo Client
เชื่อมต่อกับ TCP Echo Server ส่งข้อความ และแสดงข้อความที่ server ส่งกลับมา
พิมพ์ 'exit' เพื่อออก
"""
import socket
import sys

HOST = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
PORT = 5000
BUFFER_SIZE = 1024


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as client:
        client.connect((HOST, PORT))
        print(f"[TCP CLIENT] Connected to {HOST}:{PORT}")
        print("พิมพ์ข้อความแล้วกด Enter (พิมพ์ 'exit' เพื่อออก)")
        while True:
            message = input("> ")
            if message.lower() == "exit":
                break
            if not message:
                continue
            client.sendall(message.encode("utf-8"))
            data = client.recv(BUFFER_SIZE)
            print(f"[ECHO FROM SERVER] {data.decode('utf-8')}")
    print("[TCP CLIENT] Connection closed.")


if __name__ == "__main__":
    main()
