import socket


def main():
    # You can use print statements as follows for debugging, they'll be visible when running tests.
    print("Logs from your program will appear here!")


    server_socket = socket.create_server(("localhost", 4221), reuse_port=False)
 # Wait for a client connection
    client_socket, addr = server_socket.accept()
    print(f"Connection established with {addr}")

    try:
        # Read data from the client
        data = client_socket.recv(1024)  # Adjust the buffer size if necessary
        print(f"Received data: {data.decode()}")

        # Respond with HTTP/1.1 200 OK
        response = "HTTP/1.1 200 OK\r\n\r\n"
        client_socket.sendall(response.encode())

    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        # Close the client socket
        client_socket.close()
        # Close the server socket
        server_socket.close()


if __name__ == "__main__":
    main()
