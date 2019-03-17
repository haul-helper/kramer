from praw.models import Message
from apartment import Apartment
from login import login
from uuid import uuid4
import time

NY = Apartment()

if __name__ == "__main__":
    while True:
        try:
            r = login()

            print("[kramer=>main] looking for unread messages...\n")
            while True:
                # Look through all unread messages
                for message in r.inbox.unread(limit=None):
                    # Ignore inbox objects that arent Messages
                    if isinstance(message, Message):
                        # If they mention 'invite' in the subject
                        if "invite" in message.subject:
                            print(f"\n===={message.author}====\n")

                            print("[kramer=>main->Subject] " "Contains `invite`\n")

                            # If the user already has an invite or not
                            wasFound = NY.hey_buddy(message.author)

                            """
                                If they don't have an invite,
                                add em to the list & send invite
                            """
                            if not wasFound:
                                print(
                                    "[kramer=>main->wasFound(false)] "
                                    "Sending Message\n"
                                )

                                NY.kiss_hello(message.author)

                                full_uuid = uuid4()
                                uuid = str(full_uuid)[:6]
                                message.reply(uuid)
                                message.mark_read()

                            # If the user was found
                            else:
                                print(
                                    "[kramer=>main->wasFound(true)] "
                                    "Skipping User + Deleting Message\n"
                                )
                                message.delete()
                        # If the subject is formatted invalid-ly
                        else:
                            print(
                                "[kramer=>main->Subject]"
                                "Invalid Subject + Deleting Message\n"
                            )
                            message.delete()

                    print("====MESSAGE_END====")
                    time.sleep(10)

        except Exception as e:
            print("fuck:", e)
