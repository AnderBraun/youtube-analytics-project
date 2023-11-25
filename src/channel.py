import json
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Данные будут подтягиваться по API."""
        self._channel_id = channel_id
        self._service = self.get_service()

        # Заполняем атрибуты данными канала
        channel_info = self.fetch_channel_info()
        self._title = channel_info['items'][0]['snippet']['title']
        self._description = channel_info['items'][0]['snippet']['description']
        self._url = f'https://www.youtube.com/channel/{self._channel_id}'
        self._subscriber_count = int(channel_info['items'][0]['statistics']['subscriberCount'])
        self._video_count = int(channel_info['items'][0]['statistics']['videoCount'])
        self._view_count = int(channel_info['items'][0]['statistics']['viewCount'])

    @property
    def channel_id(self):
        return self._channel_id

    @channel_id.setter
    def channel_id(self, new_channel_id):
        raise AttributeError("Can't set attribute 'channel_id'")

    @property
    def title(self):
        return self._title

    @property
    def description(self):
        return self._description

    @property
    def url(self):
        return self._url

    @property
    def subscriber_count(self):
        return self._subscriber_count

    @property
    def video_count(self):
        return self._video_count

    @property
    def view_count(self):
        return self._view_count

    @staticmethod
    def get_service():
        """Возвращает объект для работы с YouTube API."""
        api_key = 'AIzaSyBwpysyWMHiI5JBQkS0xHTRZCvUVyRxe9g'  # ключ API
        return build('youtube', 'v3', developerKey=api_key)

    def fetch_channel_info(self) -> dict:
        """Запрос к YouTube API для получения информации о канале."""
        try:
            request = self._service.channels().list(
                part='snippet,statistics',
                id=self._channel_id
            )
            response = request.execute()

            if 'items' in response:
                return response
            else:
                print(f"Error in API response: {response}")
                return {}

        except HttpError as e:
            print(f"An error occurred: {e}")
            return {}

    def to_json(self, filename: str) -> None:
        """Сохраняет значения атрибутов экземпляра в файл JSON."""
        data = {
            'channel_id': self._channel_id,
            'title': self._title,
            'description': self._description,
            'url': self._url,
            'subscriber_count': self._subscriber_count,
            'video_count': self._video_count,
            'view_count': self._view_count,
        }

        with open(filename, 'w', encoding='utf-8') as json_file:
            json.dump(data, json_file, ensure_ascii=False, indent=4)

if __name__ == '__main__':
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')

    # Получаем значения атрибутов
    print(moscowpython.title)  # MoscowPython
    print(moscowpython.video_count)  # 685 (может уже больше)
    print(moscowpython.url)  # https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A

    # Попытка изменить channel_id
    moscowpython.channel_id = 'Новое название'
    # Вызывает AttributeError: Can't set attribute 'channel_id'