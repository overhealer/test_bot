import vk_api
import random
import time

vk = vk_api.VkApi(token='5e67707e9a734b2d0c95015bdf1d45fbe145612e76f1deb74bd2094ce37bfdab9357b24af2601a8d0d049')

while True:
    cur_time = time.ctime(time.time())
    messages = vk.method("messages.getConversations", {"offset": 0, "count": 20, "filter": "unanswered"})
    if messages["count"] >= 1:
        usr_id = messages["items"][0]["last_message"]["from_id"]
        mes_text = messages["items"][0]["last_message"]["text"]
        if mes_text.lower() == "привет" or mes_text.lower() == "ку" or mes_text.lower() == "здарова" or mes_text.lower() == "сап двач":
            vk.method("messages.send",
                      {"peer_id":usr_id, "message":"И тебе не хворать", "random_id": random.randint(1, 2147483647)})
        elif mes_text.lower() == "пока" or mes_text.lower() == "до свидания" or mes_text.lower() == "прощай":
            vk.method("messages.send",
                      {"peer_id": usr_id, "message": "Удачи", "random_id": random.randint(1, 2147483647)})
        elif mes_text.lower() == "сколько времени" or mes_text.lower() == "время":
            vk.method("messages.send",
                      {"peer_id": usr_id, "message": "Время по МСК: " + str(cur_time), "random_id": random.randint(1, 2147483647)})
        elif mes_text.lower() == "влад":
            vk.method("messages.send",
                      {"peer_id": usr_id, "message": "Владос пидор", "random_id": random.randint(1, 2147483647)})
        elif mes_text.lower() == "помощь":
            vk.method("messages.send",
                      {"peer_id": usr_id, "message": "Доступные команды: помощь, время, влад", "random_id": random.randint(1, 2147483647)})
        else:
            vk.method("messages.send",
                      {"peer_id": usr_id, "message": "бип-буп, моя не понимать, напииши помощь, чтобы посмотреть доступные команды", "random_id": random.randint(1, 2147483647)})
