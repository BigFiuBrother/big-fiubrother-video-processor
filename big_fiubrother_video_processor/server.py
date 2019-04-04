from aiohttp import web
import socketio

sio = socketio.AsyncServer()
app = web.Application()
sio.attach(app)

@sio.on('connect', namespace='/video')
def connect(sid, environ):
    print("User connected: {}".format(sid))

@sio.on('feed', namespace='/video')
async def message(sid, data):
    print('Message received from {}: {}'.format(sid, data))
    return 'Your message was {}'.format(data)

@sio.on('disconnect', namespace='/video')
def disconnect(sid):
    print("User disconnected: {}".format(sid))

if __name__ == '__main__':
    web.run_app(app)