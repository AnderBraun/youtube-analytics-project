import json
import os
from dotenv import load_dotenv
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Загрузка переменных окружения из файла .env
load_dotenv()

class Channel:

    def __init__(self, channel_id: str) -> None:
        self._channel_id = channel_id

        # Инициализируем сервис с помощью ключа API из переменной среды
        api_key = os.getenv("YOUTUBE_API_KEY")
        if api_key is None:
            raise ValueError("YouTube API key not found in the environment variable")

        self._service = self.get_service(api_key)

        # Получить информацию о канале с помощью сервиса
        channel_info = self.fetch_channel_info()

        # Rest of your code remains the same
        self._title = channel_info['items'][0]['snippet']['title']
        self._description = channel_info['items'][0]['snippet']['description']
        self._url = f'https://www.youtube.com/channel/{self._channel_id}'
        self._subscriber_count = int(channel_info['items'][0]['statistics']['subscriberCount'])
        self._video_count = int(channel_info['items'][0]['statistics']['videoCount'])
        self._view_count = int(channel_info['items'][0]['statistics']['viewCount'])

    @property
    def channel_id(self):
        return self._channel_id

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
    def get_service(api_key):
        """Возвращает объект для работы с API YouTube."""
        return build('youtube', 'v3', developerKey=api_key)

    def fetch_channel_info(self) -> dict:
        """Запрашивает API YouTube для получения информации о канале."""
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

    def save_to_json(self, filename: str) -> None:
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

    def __str__(self):
        """Возвращает строковое представление канала."""
        return f"{self._title} ({self._url})"

    def __add__(self, other):
        """Сложение двух каналов по количеству подписчиков."""
        if isinstance(other, Channel):
            return self._subscriber_count + other._subscriber_count
        else:
            raise TypeError("Unsupported operand type for +")

    def __sub__(self, other):
        """Вычитание двух каналов по количеству подписчиков."""
        if isinstance(other, Channel):
            return self._subscriber_count - other._subscriber_count
        else:
            raise TypeError("Unsupported operand type for -")

    def __eq__(self, other):
        """Сравнение двух каналов по количеству подписчиков."""
        if isinstance(other, Channel):
            return self._subscriber_count == other._subscriber_count
        else:
            raise TypeError("Unsupported operand type for ==")

    def __lt__(self, other):
        """Сравнение двух каналов по количеству подписчиков (меньше)."""
        if isinstance(other, Channel):
            return self._subscriber_count < other._subscriber_count
        else:
            raise TypeError("Unsupported operand type for <")

    def __gt__(self, other):
        """Сравнение двух каналов по количеству подписчиков (больше)."""
        if isinstance(other, Channel):
            return self._subscriber_count > other._subscriber_count
        else:
            raise TypeError("Unsupported operand type for >")

    def __ge__(self, other):
        """Сравнение двух каналов по количеству подписчиков (больше или равно)."""
        if isinstance(other, Channel):
            return self._subscriber_count >= other._subscriber_count
        else:
            raise TypeError("Unsupported operand type for >=")

if __name__ == '__main__':
    # Создаем два экземпляра класса
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    highload = Channel('UCwHL6WHUarjGfUM_586me8w')

    # Используем различные магические методы
    print(str(moscowpython))  # 'MoscowPython (https://www.youtube.com/channel/UC-OVMPlMA3-YCIeg4z5z23A)'
    print(moscowpython + highload)  # 100100
    print(moscowpython - highload)  # -48300
    print(highload - moscowpython)  # 48300
    print(moscowpython > highload)  # False
    print(moscowpython >= highload)  # False
    print(moscowpython < highload)  # True
    print(moscowpython <= highload)  # True
    print(moscowpython == highload)  # False
