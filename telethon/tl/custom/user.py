from .. import types, functions
from ... import utils 

class User:
    def __init__(self,
        id:int=None,
        is_self:bool=None,
        contact:bool=None,
        mutual_contact:bool=None,
        deleted:bool=None,
        bot:bool=None,
        bot_chat_history:bool=None,
        bot_nochats:bool=None,
        verified:bool=None,
        restricted:bool=None,
        min:bool=None,
        bot_inline_geo=None,
        support=None, scam=None, apply_min_photo=None, fake=None, access_hash=None,
        first_name=None, last_name=None, username=None,
        phone=None, photo=None, status=None, bot_info_version=None, restriction_reason=[],
        bot_inline_placeholder=None, lang_code=None, bot_attach_menu=None, *args, **kwargs):
        self._client = None
        self._id = id
        self.is_self = is_self
        self.contact = contact
        self.mutual_contact = mutual_contact
        self.deleted = deleted
        self.bot = bot
        self.bot_chat_history = bot_chat_history
        self.bot_nochats = bot_nochats
        self.verified = verified
        self.restricted = restricted
        self.min = min
        self.bot_inline_geo = bot_inline_geo
        self.bot_attach_menu = bot_attach_menu
        self.support = support
        self.scam = scam
        self.fake = fake
        self.apply_min_photo = apply_min_photo
        self.access_hash = access_hash
        self.first_name = first_name
        self.last_name = last_name
        self.username = username
        self.phone = phone
        self.photo = photo
        self.status = status
        self.bot_info_version = bot_info_version
        self.restriction_reason = restriction_reason
        self.bot_inline_placeholder = bot_inline_placeholder
        self.lang_code = lang_code
        self._fulluser = None


    def _set_client(self, client):
        self._client = client

    @property
    def id(self):
        return self._id

    @property
    def mention(self):
        return f"[{utils.get_display_name(self)}](tg://user?id={self.id})"

    @property
    def full_user(self):
        return self._full_user

    async def comman_chats(self, max_id=0, limit=0):
        if self._client:
            chat = await self._client(functions.messages.GetCommonChatsRequest(self.id, max_id=max_id, limit=limit))
            if not isinstance(chat, types.messages.ChatsSlice):
                chat.count = len(chat.chats)
            return chat

    async def get_fulluser(self):
        if self._client:
            full_user = await self._client(functions.users.GetFullUserRequest(self.id))
            self._full_user = full_user.full_user
            return full_user

    async def block(self):
        if self._client:
            return await self._client(functions.contacts.BlockRequest(self.id))

    async def unblock(self):
        if self._client:
            return await self._client(functions.contacts.UnblockRequest(self.id))

    async def send(self, *args, **kwargs):
        if self._client:
            return await self._client.send_message(self.id, *args, **kwargs)

    async def get_photos(self, *args, **kwargs):
        if self._client:
            return await self._client.get_profile_photos(self.id, *args, **kwargs)
