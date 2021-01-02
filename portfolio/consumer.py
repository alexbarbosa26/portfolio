

from channels.generic.websocket import AsyncWebsocketConsumer
import json
#DEVE USTILIZAR O Redis 5.0.10
class DashConsumer(AsyncWebsocketConsumer):
    async def connect(self):
        self.room_name = 'dashboard'
        # Join room group
        await self.channel_layer.group_add(
            self.room_name,
            self.channel_name
        )

        await self.accept()

    async def disconnect(self, close_code):
        # Leave room group
        await self.channel_layer.group_discard(
            self.room_name,
            self.channel_name
        )

    # Receive message from WebSocket
    async def receive(self, text_data):
        text_data_json = json.loads(text_data)
        message = text_data_json['value']

        # Send message to room group
        await self.channel_layer.group_send(
            self.room_name,
            {
                'type': 'deprocessing',
                'value': message
            }
        )
        print('>>>>>>>',text_data)

    # Receive message from room group
    async def deprocessing(self, event):
        message = event['value']

        # Send message to WebSocket
        await self.send(text_data=json.dumps({
            'value': message
        }))