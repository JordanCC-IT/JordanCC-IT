import gevent
import zmq.green as zmq

# Global Context
context = zmq.Context()


def server():
    server_socket = context.socket(zmq.REQ)  # Server socket is REQ (request)
    server_socket.bind("tcp://127.0.0.1:5000")
    print("Server is waiting for client to connect...")

    for request in range(1, 10):
        try:
            print(f"Server sending 'Hello' message {request}")
            server_socket.send_string("Hello")  # Server sends message to client

            # Wait for the response from the client
            message = server_socket.recv_string()  # This will receive the response from the client
            print(f"Server received response: {message} for request {request}")
        except Exception as e:
            print(f"Server encountered an error: {e}")
            break

    print("Server finished sending all messages.")


def client():
    client_socket = context.socket(zmq.REP)  # Client socket is REP (reply)
    client_socket.connect("tcp://127.0.0.1:5000")
    print("Client is ready to process requests...")

    for request in range(1, 10):
        try:
            # Wait for the request from the server
            message = client_socket.recv_string()  # This will block until the server sends a message
            print(f"Client received message: {message} for request {request}")

            # Simulate some processing time
            gevent.sleep(1)

            # Send the response back to the server
            client_socket.send_string("World")
            print(f"Client sent response 'World' for request {request}")
        except Exception as e:
            print(f"Client encountered an error: {e}")
            break

    print("Client finished processing all requests.")


# Start server and client as greenlets
publisher = gevent.spawn(server)
client_g = gevent.spawn(client)

# Join both greenlets (wait for them to finish)
gevent.joinall([publisher, client_g])

print("Server and client communication finished.")
