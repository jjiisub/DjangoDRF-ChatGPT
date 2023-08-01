from django.shortcuts import render
from django.views import View
from dotenv import load_dotenv
import openai
import os

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ConversationSerializer
from .models import ChatingRoom, Message
from rest_framework.authtoken.models import Token


load_dotenv()
openai.api_key = os.getenv('OPENAI_API_KEY')

class ChatView(APIView):
    def get(self, request, format=None):
        # loginToken = request.data.get('token')
        # room_name = request.data.get('room')
        loginToken = request.GET.get('token')
        room_name = request.GET.get('room')

        token = Token.objects.get(key=loginToken)
        user = token.user

        room = ChatingRoom.objects.get(name=room_name)

        prev_conversations = Message.objects.filter(ChatingRoom=room).order_by('created_at')
        if prev_conversations:
            conversations = []
            for elem in prev_conversations:
                conversations.append({'prompt':elem.prompt, 'response':elem.response})
        
        request.session['conversations'] = conversations
        
        serializer = ConversationSerializer(conversations, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        room_name = request.data.get('room')
        room = ChatingRoom.objects.get(name=room_name)
        prompt = request.data.get('prompt')

        if prompt:
            session_conversations = request.session.get('conversations', [])
            previous_conversations = "\n".join([f"User: {c['prompt']}\nAI: {c['response']}" for c in session_conversations])
            prompt_with_previous = f"{previous_conversations}\nUser: {prompt}\nAI:"

            model_engine = "text-davinci-003"
            completions = openai.Completion.create(
                engine=model_engine,
                prompt=prompt_with_previous,
                max_tokens=1024,
                n=5,
                stop=None,
                temperature=0.5,
            )
            response = completions.choices[0].text.strip()

            msg = Message.objects.create(prompt=prompt, response=response, ChatingRoom=room)

            conversation = {'prompt': prompt, 'response': response}
            session_conversations.append(conversation)
            request.session['conversations'] = session_conversations
            request.session.modified = True

        conversations = request.session.get('conversations', [])
        serializer = ConversationSerializer(conversations, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


# class ChatView(View):
#     def get(self, request, *args, **kwargs):
#         conversations = request.session.get('conversations', [])
#         return render(request, 'chat.html', {'conversations': conversations})

#     def post(self, request, *args, **kwargs):
#         prompt = request.POST.get('prompt')
#         if prompt:
#             # 이전 대화 기록 가져오기
#             session_conversations = request.session.get('conversations', [])
#             previous_conversations = "\n".join([f"User: {c['prompt']}\nAI: {c['response']}" for c in session_conversations])
#             prompt_with_previous = f"{previous_conversations}\nUser: {prompt}\nAI:"

#             model_engine = "text-davinci-003"
#             completions = openai.Completion.create(
#                 engine=model_engine,
#                 prompt=prompt_with_previous,
#                 max_tokens=1024,
#                 n=5,
#                 stop=None,
#                 temperature=0.5,
#             )
#             response = completions.choices[0].text.strip()

#             conversation = {'prompt': prompt, 'response': response}

#             # 대화 기록에 새로운 응답 추가
#             session_conversations.append(conversation)
#             request.session['conversations'] = session_conversations

#         return self.get(request, *args, **kwargs)