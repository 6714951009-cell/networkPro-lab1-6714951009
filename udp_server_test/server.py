"""
UDP Server
รับ datagram จาก client แสดงผล แล้วตอบกลับไปยังที่อยู่ของผู้ส่ง
"""
import socket

HOST = "0.0.0.0"
PORT = 6000
BUFFER_SIZE = 1024


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as server:
        server.bind((HOST, PORT))
        print(f"[UDP SERVER] Listening on {HOST}:{PORT} ...")
        try:
            while True:
                data, addr = server.recvfrom(BUFFER_SIZE)
                message = data.decode("utf-8")
                print(f"[RECEIVED from {addr}] {message}")
                reply = f"Server received: {message}"
                server.sendto(reply.encode("utf-8"), addr)
                print(f"[REPLIED to {addr}] {reply}")
        except KeyboardInterrupt:
            print("\n[UDP SERVER] Shutting down.")


if __name__ == "__main__":
    main()
