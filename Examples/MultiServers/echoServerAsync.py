import asyncio

loop = asyncio.get_event_loop()

# an instance of EchoProtocol will be created for each client connection.
class EchoProtocol(asyncio.Protocol):
    def connection_made(self, transport):
        self.transport = transport

    def data_received(self, data):
        data = data.upper()
        self.transport.write(data)

    def connection_lost(self, exc):
        server.close()

# run the coroutine to establish the server connection, then keep running
# the event loop until the server is stopped.
server = loop.run_until_complete(loop.create_server(EchoProtocol, '127.0.0.1', 50007))
loop.run_until_complete(server.wait_closed())
