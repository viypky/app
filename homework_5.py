import json
from datetime import datetime

class Character:
    def __init__(self, *, name, hp, **kwargs):
        super().__init__(**kwargs)
        self.name = name
        self.hp = hp

    def take_damage(self, amount):
        if amount < 0:
            raise ValueError("Урон не может быть отрицательным")

        self.hp = max(0, self.hp - amount)
        print(f"{self.name} получил {amount} урона. HP: {self.hp}")

class MagicCasterMixin:
    def __init__(self, *, mana=0, **kwargs):
        super().__init__(**kwargs)
        self.mana = mana

    def cast_spell(self, cost):
        if cost < 0:
            raise ValueError("Стоимость заклинания не может быть отрицательной")

        if self.mana < cost:
            print("Недостаточно маны")
            return False

        self.mana -= cost
        print(f"Заклинание использовано. Мана: {self.mana}")
        return True


class FlyableMixin:
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.is_flying = False

    def fly(self):
        self.is_flying = True
        print(f"{self.name} взлетает!")


class BattleMage(MagicCasterMixin, FlyableMixin, Character):
    pass


mage = BattleMage(name="Gandalf", hp=100, mana=80)

mage.take_damage(25)
mage.cast_spell(30)
mage.fly()

print(BattleMage.__mro__)

class BaseReport:
    def __init__(self, *, title, data, **kwargs):
        super().__init__(**kwargs)
        self.title = title
        self.data = data


class JSONExportMixin:
    def to_json(self):
        return json.dumps(
            {
                "title": self.title,
                "data": self.data
            },
            ensure_ascii=False
        )


class CSVExportMixin:
    def to_csv(self):
        return "\n".join(
            f"{key},{value}"
            for key, value in self.data.items()
        )


class SalesAnalyticsReport(JSONExportMixin, CSVExportMixin, BaseReport):
    pass



class BasePaymentProcessor:
    def __init__(self, *, balance=0.0, **kwargs):
        super().__init__(**kwargs)
        self.balance = balance

    def process(self, amount: float):
        if self.balance < amount:
            return {
                "success": False,
                "status": "insufficient_funds",
                "amount": amount
            }

        self.balance -= amount

        return {
            "success": True,
            "status": "paid",
            "amount": amount,
            "balance": self.balance
        }


class ValidationMixin:
    def process(self, amount: float):
        if amount <= 0:
            raise ValueError("Сумма должна быть больше нуля")

        return super().process(amount)


class AuditLogMixin:
    def process(self, amount: float):
        timestamp = datetime.now().isoformat()

        print(f"[{timestamp}] Начало обработки платежа: {amount}")

        result = super().process(amount)

        print(
            f"[{timestamp}] Завершение обработки платежа: "
            f"status={result['status']}"
        )

        return result


class CryptoPaymentProcessor(
    AuditLogMixin,
    ValidationMixin,
    BasePaymentProcessor
):
    pass

  

# ТЗ 1
mage = BattleMage(name="Gandalf", hp=100, mana=80)
mage.take_damage(25)
mage.cast_spell(30)
mage.fly()

print("MRO BattleMage:", BattleMage.__mro__)
print()


# ТЗ 2
report = SalesAnalyticsReport(
    title="Продажи за август",
    data={
        "revenue": 150000,
        "orders": 1250,
        "average_check": 120
    }
)

print(report.to_json())
print(report.to_csv())

print("MRO SalesAnalyticsReport:", SalesAnalyticsReport.__mro__)
print()


# ТЗ 3
processor = CryptoPaymentProcessor(balance=1000.0)

result = processor.process(250.0)

print("Результат:", result)
print("Баланс:", processor.balance)

print("MRO CryptoPaymentProcessor:", CryptoPaymentProcessor.__mro__)