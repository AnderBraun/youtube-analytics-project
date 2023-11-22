import requests

class Channel:
    """Класс для ютуб-канала"""

    def __init__(self, channel_id: str) -> None:
        """Экземпляр инициализируется id канала. Данные будут подтягиваться по API."""
        self.channel_id = channel_id
        self.api_key = 'AIzaSyBwpysyWMHiI5JBQkS0xHTRZCvUVyRxe9g'  # ключ API

    def fetch_channel_info(self) -> dict:
        """Запрос к YouTube API для получения информации о канале."""
        url = f'https://www.googleapis.com/youtube/v3/channels'
        params = {
            'part': 'snippet,statistics',
            'id': self.channel_id,
            'key': self.api_key,
        }

        response = requests.get(url, params=params)
        return response.json()

    def print_info(self) -> None:
        """Выводит в консоль информацию о канале."""
        channel_info = self.fetch_channel_info()

        # Обработка данных и вывод информации
        snippet = channel_info['items'][0]['snippet']
        statistics = channel_info['items'][0]['statistics']

        print(f"Title: {snippet['title']}")
        print(f"Description: {snippet['description']}")
        print(f"Published At: {snippet['publishedAt']}")
        print(f"Country: {snippet['country']}")
        print(f"View Count: {statistics['viewCount']}")
        print(f"Subscriber Count: {statistics['subscriberCount']}")
        print(f"Video Count: {statistics['videoCount']}")

if __name__ == '__main__':
    moscowpython = Channel('UC-OVMPlMA3-YCIeg4z5z23A')
    moscowpython.print_info()