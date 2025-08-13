from address import Address
from mailing import Mailing

to_addr = Address("123456", "Москва", "Ленина", "10", "15")
from_addr = Address("654321", "Санкт-Петербург", "Пр. Невского", "36", "69")
mail = Mailing(to_addr, from_addr, 500, "AB123456789RU")

message = (
    f"Отправление {mail.track} из {mail.from_address.postal_code}, "
    f"{mail.from_address.city}, {mail.from_address.street}, "
    f"{mail.from_address.house} - {mail.from_address.apartment} "
    f"в {mail.to_address.postal_code}, {mail.to_address.city}, "
    f"{mail.to_address.street}, {mail.to_address.house} - "
    f"{mail.to_address.apartment}. Стоимость {mail.cost} рублей."
)

print(message)
