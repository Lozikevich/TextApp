from datetime import datetime
from Message.MessageManager import *

if __name__ == '__main__':
    main_storage = ReadWriteMessageStorage('~/data')
    public_manager = MessageManager('public', main_storage)
    public_manager.add_new_message(Message('25.11.2021 20:05', 'user_1', 'note_1'))
    public_manager.add_new_message(Message('25.11.2021 20:06', 'user_2', 'note_2'))
    public_manager.add_new_message(Message(str(datetime.now()), 'user_3', 'note_3'))

    private_manager = MessageManager('private', main_storage)
    private_manager.add_new_message(Message('25.11.2021 20:05', 'user_1', 'note_1'))
    private_manager.add_new_message(Message('25.11.2021 20:06', 'user_2', 'note_2'))
    private_manager.add_new_message(Message(str(datetime.now()), 'user_3', 'note_3'))

    print(public_manager.get_all_messages)
    print('-------')
    public_manager.delete_message('25.11.2021 20:05')
    print(public_manager.get_all_messages)
    print('---------------')


