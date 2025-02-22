from classes.imports import *

class profileTestCase():

    def __init__(self):
        # Инициализация бота
        self.bot = telebot.TeleBot(tokenbot)
        # Инициализация кнопок
        self.buttonsmarkup = buttons()
        # Инициализация сообщений
        self.messagestouser = messages()
        # Тестовое сообщение
        self.testmessagetelegram = {'content_type': 'text', 'id': 584, 'message_id': 584, 'from_user': {'id': 1917167694, 'is_bot': False, 'first_name': 'Алексей', 'username': 'fleshkaomsk', 'last_name': 'Иванович', 'language_code': 'ru', 'can_join_groups': None, 'can_read_all_group_messages': None, 'supports_inline_queries': None, 'is_premium': None, 'added_to_attachment_menu': None, 'can_connect_to_business': None, 'has_main_web_app': None}, 'date': 1739936523, 'chat': {'id': 1917167694, 'type': 'private', 'title': None, 'username': 'fleshkaomsk', 'first_name': 'Алексей', 'last_name': 'Иванович', 'is_forum': None, 'max_reaction_count': None, 'photo': None, 'bio': None, 'join_to_send_messages': None, 'join_by_request': None, 'has_private_forwards': None, 'has_restricted_voice_and_video_messages': None, 'description': None, 'invite_link': None, 'pinned_message': None, 'permissions': None, 'slow_mode_delay': None, 'message_auto_delete_time': None, 'has_protected_content': None, 'sticker_set_name': None, 'can_set_sticker_set': None, 'linked_chat_id': None, 'location': None, 'active_usernames': None, 'emoji_status_custom_emoji_id': None, 'has_hidden_members': None, 'has_aggressive_anti_spam_enabled': None, 'emoji_status_expiration_date': None, 'available_reactions': None, 'accent_color_id': None, 'background_custom_emoji_id': None, 'profile_accent_color_id': None, 'profile_background_custom_emoji_id': None, 'has_visible_history': None, 'unrestrict_boost_count': None, 'custom_emoji_sticker_set_name': None, 'business_intro': None, 'business_location': None, 'business_opening_hours': None, 'personal_chat': None, 'birthdate': None, 'can_send_paid_media': None}, 'sender_chat': None, 'is_automatic_forward': None, 'reply_to_message': None, 'via_bot': None, 'edit_date': None, 'has_protected_content': None, 'media_group_id': None, 'author_signature': None, 'text': '09.11.1963', 'entities': None, 'caption_entities': None, 'audio': None, 'document': None, 'photo': None, 'sticker': None, 'video': None, 'video_note': None, 'voice': None, 'caption': None, 'contact': None, 'location': None, 'venue': None, 'animation': None, 'dice': None, 'new_chat_members': None, 'left_chat_member': None, 'new_chat_title': None, 'new_chat_photo': None, 'delete_chat_photo': None, 'group_chat_created': None, 'supergroup_chat_created': None, 'channel_chat_created': None, 'migrate_to_chat_id': None, 'migrate_from_chat_id': None, 'pinned_message': None, 'invoice': None, 'successful_payment': None, 'connected_website': None, 'reply_markup': None, 'message_thread_id': None, 'is_topic_message': None, 'chat_background_set': None, 'forum_topic_created': None, 'forum_topic_closed': None, 'forum_topic_reopened': None, 'has_media_spoiler': None, 'forum_topic_edited': None, 'general_forum_topic_hidden': None, 'general_forum_topic_unhidden': None, 'write_access_allowed': None, 'users_shared': None, 'chat_shared': None, 'story': None, 'external_reply': None, 'quote': None, 'link_preview_options': None, 'giveaway_created': None, 'giveaway': None, 'giveaway_winners': None, 'giveaway_completed': None, 'forward_origin': None, 'boost_added': None, 'sender_boost_count': None, 'reply_to_story': None, 'sender_business_bot': None, 'business_connection_id': None, 'is_from_offline': None, 'effect_id': None, 'show_caption_above_media': None, 'paid_media': None, 'refunded_payment': None, 'proximity_alert_triggered': None, 'video_chat_scheduled': None, 'video_chat_started': None, 'video_chat_ended': None, 'video_chat_participants_invited': None, 'web_app_data': None, 'message_auto_delete_timer_changed': None, 'json': {'message_id': 584, 'from': {'id': 1917167694, 'is_bot': False, 'first_name': 'Алексей', 'last_name': 'Иванович', 'username': 'fleshkaomsk', 'language_code': 'ru'}, 'chat': {'id': 1917167694, 'first_name': 'Алексей', 'last_name': 'Иванович', 'username': 'fleshkaomsk', 'type': 'private'}, 'date': 1739936523, 'text': '09.11.1963'}}

    def testprintdates(self):
        # Инициализация экземпляра класса
        testclass = profile(self.bot, self.messagestouser, self.buttonsmarkup)
        # Параметры для функции printdates
        testclass.printdates()

    def testselectfromdatabase(self):
        # Инициализация экземпляра класса
        testclass = profile(self.bot, self.messagestouser, self.buttonsmarkup)
        # Параметры для функции printdates
        testclass.town(None)

test = profileTestCase()
test.testprintdates()
#test.testselectfromdatabase()