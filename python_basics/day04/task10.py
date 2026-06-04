# Q10. Mini Project – OOP Chat System
# Let's create a Chat System using OOPs concepts. We have to create classes:
# • User
# • Message
# • ChatRoom
# And we have to implement functions:
# • sending messages
# • viewing chat history
# • user joining and leaving the chatroom

class Message:
    message_counter = 1  # simple counter

    def __init__(self, sender, content):
        self.sender = sender
        self.content = content
        self.id = Message.message_counter
        Message.message_counter += 1

    def __str__(self):
        return f"({self.id}) {self.sender.username}: {self.content}"


# User Class
class User:
    def __init__(self, username):
        self.username = username
        self.chatroom = None

    def join_chatroom(self, chatroom):
        if self.chatroom:
            print(f"{self.username} is already in a chatroom.")
        else:
            chatroom.add_user(self)
            self.chatroom = chatroom
            print(f"{self.username} joined {chatroom.name}")

    def leave_chatroom(self):
        if not self.chatroom:
            print(f"{self.username} is not in any chatroom.")
        else:
            self.chatroom.remove_user(self)
            print(f"{self.username} left {self.chatroom.name}")
            self.chatroom = None

    def send_message(self, content):
        if not self.chatroom:
            print(f"{self.username} cannot send a message (not in a chatroom).")
        else:
            self.chatroom.broadcast(self, content)


# ChatRoom Class
class ChatRoom:
    def __init__(self, name):
        self.name = name
        self.users = []
        self.messages = []

    def add_user(self, user):
        self.users.append(user)

    def remove_user(self, user):
        self.users.remove(user)

    def broadcast(self, sender, content):
        message = Message(sender, content)
        self.messages.append(message)
        print(message)  # Show message to all users

    def show_chat_history(self):
        print(f"\nChat History of {self.name}:")
        for msg in self.messages:
            print(msg)
        print()


# Example Usage
chatroom = ChatRoom("General")
user1 = User("Alice")
user2 = User("Bob")
user1.join_chatroom(chatroom)
user2.join_chatroom(chatroom)
user1.send_message("Hello everyone!")
user2.send_message("Hi Alice!")
chatroom.show_chat_history()
user1.leave_chatroom()
user2.leave_chatroom()

