"""
UDP Client
ส่งข้อความไปยัง UDP Server และรอรับคำตอบ (timeout 3 วินาที)
พิมพ์ 'exit' เพื่อออก
"""
import socket
import sys

HOST = sys.argv[1] if len(sys.argv) > 1 else "127.0.0.1"
PORT = 6000
BUFFER_SIZE = 1024
TIMEOUT = 3  # วินาที เพราะ UDP ไม่รับประกันว่าแพ็กเก็ตจะถึง


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as client:
        client.settimeout(TIMEOUT)
        print(f"[UDP CLIENT] Sending to {HOST}:{PORT}")
        print("พิมพ์ข้อความแล้วกด Enter (พิมพ์ 'exit' เพื่อออก)")
        while True:
            message = input("> ")
            if message.lower() == "exit":
                break
            if not message:
                continue
            client.sendto(message.encode("utf-8"), (HOST, PORT))
            try:
                data, addr = client.recvfrom(BUFFER_SIZE)
                print(f"[REPLY FROM {addr}] {data.decode('utf-8')}")
            except socket.timeout:
                print("[TIMEOUT] ไม่ได้รับคำตอบจาก server")
    print("[UDP CLIENT] Closed.")


if __name__ == "__main__":
    main()
