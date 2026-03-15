# TODO Написать 3 класса с документацией и аннотацией типов

if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    pass
from abc import ABC, abstractmethod

# ---------------------------
# Абстрактный класс: Стол
# ---------------------------
class Table(ABC):
    def __init__(self, material: str, height: float, width: float):
        """
        Инициализация стола.

        :param material: материал стола (например, дерево, металл)
        :param height: высота стола в см, должна быть > 0
        :param width: ширина стола в см, должна быть > 0
        """
        if height <= 0:
            raise ValueError("Высота стола должна быть положительной")
        if width <= 0:
            raise ValueError("Ширина стола должна быть положительной")

        self.material = material
        self.height = height
        self.width = width

    @abstractmethod
    def move(self, direction: str) -> None:
        """
        Переместить стол в указанном направлении.

        :param direction: направление движения ('влево', 'вправо', 'вперед', 'назад')
        """
    @abstractmethod
    def resize(self, new_width: float, new_height: float) -> None:
        """
        Изменить размеры стола.

        :param new_width: новая ширина стола, >0
        :param new_height: новая высота стола, >0
        """
    @abstractmethod
    def clean(self) -> None:
        """
        Очистить поверхность стола.
        """

# ---------------------------
# Абстрактный класс: Дерево
# ---------------------------
class Tree(ABC):
    def __init__(self, species: str, age: int, height: float):
        """
        Инициализация дерева.

        :param species: вид дерева
        :param age: возраст дерева в годах, >=0
        :param height: высота дерева в метрах, >0
        """
        if age < 0:
            raise ValueError("Возраст дерева не может быть отрицательным")
        if height <= 0:
            raise ValueError("Высота дерева должна быть положительной")

        self.species = species
        self.age = age
        self.height = height

    @abstractmethod
    def grow(self, years: int) -> None:
        """
        Увеличить возраст и рост дерева.

        :param years: количество лет для роста, >0
        """

    @abstractmethod
    def shed_leaves(self) -> None:
        """
        Сбросить листья.
        """

    @abstractmethod
    def photosynthesize(self) -> str:
        """
        Процесс фотосинтеза.

        :return: строковое описание процесса
        """


# ---------------------------
# Абстрактный класс: Facebook
# ---------------------------
class Facebook(ABC):
    def __init__(self, users_count: int, active: bool):
        """
        Инициализация сервиса Facebook.

        :param users_count: количество пользователей, >=0
        :param active: активен ли сервис
        """
        if users_count < 0:
            raise ValueError("Количество пользователей не может быть отрицательным")

        self.users_count = users_count
        self.active = active

    @abstractmethod
    def post_update(self, content: str) -> None:
        """
        Опубликовать обновление статуса.

        :param content: текст обновления
        """

    @abstractmethod
    def add_friend(self, user_id: int, friend_id: int) -> bool:
        """
        Добавить друга пользователю.

        :param user_id: идентификатор пользователя
        :param friend_id: идентификатор друга
        :return: True если добавление успешно, иначе False
        """

    @abstractmethod
    def send_message(self, from_id: int, to_id: int, message: str) -> None:
        """
        Отправить сообщение от одного пользователя другому.

        :param from_id: идентификатор отправителя
        :param to_id: идентификатор получателя
        :param message: текст сообщения
        """
        ...