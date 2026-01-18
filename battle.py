import random
import abc
import time




class CharacterBase(abc.ABC): 
    """Абстрактный класс — шаблон для классов‑наследников.
    В каждом наследнике должны быть реализованы эти методы.
    """ 

    @abc.abstractmethod
    def take_damage(self, damage):
        pass

    @abc.abstractmethod
    def attack(self, other):
        pass

    @abc.abstractmethod
    def is_alive(self):
        pass




class Character(CharacterBase):
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage
    
    def __str__(self):
        """Строковое представление объекта."""
        return f'Имя: {self.name}, Здоровье: {self.health}, Урон: {self.damage}'
    
    def take_damage(self, damage): 
        self.health -= damage
        if self.health < 0:
            self.health = 0  # Для того чтоб здоровье не ушло в минус
        print(f'💥 {self.name} получил {damage} урона! Осталось HP: {self.health}')
            
    def attack(self, other):
        print(f'{self.name} атакует {other.name}')
        other.take_damage(self.damage)

    def is_alive(self):
        return self.health > 0
        



class Hero(Character):
    """Класс для игровых персонажей с возможностью лечения."""

    def heal(self):
        heal_amount = 30
        self.health += heal_amount
        print(
            f'✨ {self.name} применил магию и восстановил {heal_amount} HP. '
            f'Теперь здоровья: {self.health}'
        )




class Enemy(Character):
    """Класс для врагов (мобов)."""
    pass




class Warrior(Hero):
    """Класс для воина (Мечника) с шансом критического удара."""

    def attack(self, other):
        if random.random() < 0.2:  # 20% выпадение крит урона
            crit_damage = self.damage * 2
            print(f'⚔️ {self.name} делает ЯРОСТНЫЙ ВЫПАД! (Крит x2)')
            other.take_damage(crit_damage)
        else:
            super().attack(other)  # super() обращается к родителю (Character) и берет его метод attack.




class Mage(Hero):
    """Класс для мага с усиленным уроном."""

    def attack(self, other):
        print(f'🔥 {self.name} кастует Огненный Шар в {other.name}!')
        other.take_damage(self.damage + 5)  # +5 к урону за счет магии.



# Создание персонажей
player = Mage('Demol', 210, 20)
enemy = Character('Zombie', 150, 40)

# Начало боя
print('--- 🔔 БОЙ НАЧИНАЕТСЯ! ---')
print(player)
print(enemy)
print('-' * 30)




while player.is_alive() and enemy.is_alive():
    time.sleep(1.5)

    player.attack(enemy)
    if not enemy.is_alive():
        print(f'\n🏆 {player.name} ОДЕРЖАЛ ПОБЕДУ!')
        break

    enemy.attack(player)
    if not player.is_alive():
        print(f'\n💀 {player.name} пал в бою... Game Over.')
        break

    if player.health < 40 and random.random() < 0.3:
        print('   🚑 Герой пытается найти зелье...')
        player.heal()

print('-' * 30)
