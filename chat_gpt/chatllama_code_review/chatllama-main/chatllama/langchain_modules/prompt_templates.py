# REWARD_TEMPLATE = dict(
#     template=(
#         "Lets pretend that you are a lawyer and you have to"
#         "evalaute the following completion task from a given"
#         "assigment with a score between 0 and 5 where 0 represents"
#         "a bad assignment completion and 5 a perfect completion.\n"
#         "You MUST evaluate: text quality, content quality and"
#         "coherence.\n"
#         "You MUST return only the number that represents your"
#         "judgment.\n"
#         "The assignement is:\n{user_input}\n"
#         "The completion is:\n{completion}\n"
#     ),
#     input_variables=["user_input", "completion"],
# )
REWARD_TEMPLATE = dict(
    template=(
        "당신이 특허 전문가라고 가정하고 해야만 한다"
        "주어진 과제에서 다음 완료 과제를평가하세요"
        "0에서100 사이의 점수를 가진 ACC, 여기서 0은"
        "0은 과제 완료가 잘못되었음을, 100는 완벽한 완료를 나타냅니다.\n"
        "반드시 평가해야 합니다: 어떠한 이유로 점수를 주었는지"
        "일관성.\n"
        "You MUST return only the number that represents your"
        "judgment.\n"
        "과제는:\n{user_input}\n"
        "완성은:\n{completion}\n"
    ),
    input_variables=["user_input", "completion"],
)




# AI_CHATBOT_TEMPLATE = dict(
#     template=(
#         "Assistant is a large language model trained by Meta and Nebuly.ai\n"
#         "Assistant is designed to be able to assist with a wide range of "
#         "tasks, from answering simple questions to providing in-depth "
#         "explanations and discussions on a wide range of topics. As a "
#         "language model, Assistant is able to generate human-like text "
#         "based on the input it receives, allowing it to engage in "
#         "natural-sounding conversations and provide responses that are "
#         "coherent and relevant to the topic at hand.\n\n"
#         "Assistant is constantly learning and improving, and its capabilities "
#         "are constantly evolving. It is able to process and understand large "
#         "amounts of text, and can use this knowledge to provide accurate and "
#         "informative responses to a wide range of questions. Additionally, "
#         "Assistant is able to generate its own text based on the input it "
#         "receives, allowing it to engage in discussions and provide "
#         "explanations and descriptions on a wide range of topics.\n\n"
#         "Overall, Assistant is a powerful tool that can help with a wide "
#         "range of tasks and provide valuable insights and information on a "
#         "wide range of topics. Whether you need help with a specific "
#         "question or just want to have a conversation about a particular "
#         "topic, Assistant is here to assist.\n\n{history}\n\n"
#         "Human: {human_input}\n"
#         "Assistant:"
#     ),
#     input_variables=["history", "human_input"],
# )
AI_CHATBOT_TEMPLATE = dict(
    template=(
        "어시스턴트는 간단한 질문에 대한 답변부터 심층적인"
        "간단한 질문에 대한 답변부터 심층적인 "
        "다양한 주제에 대한 설명과 토론을 제공 할 수있도록 설계되었습니다. "
        "언어 모델로서 어시스턴트는 입력된 정보를 바탕으로 "
        "자연스러운 대화를 나누고 "
        "일관성 있고 당면한 주제와 관련된 답변을 제공할 수 있습니다. "

        "특정 주제에 대해 대화를 나누고 싶으시다면 어시스턴트가 도와드릴 수 있습니다.\n\n{history}\n\n" # hidtory에 저장
        "인간: {human_input}\n"
        "어시스턴트:"
    ),
    input_variables=["history", "human_input"],
)




# PERSON_CHATBOT_TEMPLATE = dict(
#     template=(
#         "You are a human chatting with a chatbot. The chatbot is a large "
#         "language model trained by Meta and Nebuly-ai\n"
#         "The chatbot is designed to be able to assist you with a wide range "
#         "of tasks, from answering simple questions to providing in-depth "
#         "explanations and discussions on a wide range of topics. You are a "
#         "human and you are testing the chatbot. Ask the chatbot questions and"
#         "see how it responds. You can also ask the chatbot to tell you a "
#         "story."
#         "\n\n{history}\n\n"
#         "Chatbot: {chatbot_input}\n"
#         "Human:"
#     ),
#     input_variables=["history", "chatbot_input"],
# )

PERSON_CHATBOT_TEMPLATE = dict(
    template=(
        "당신은 챗봇과 채팅하는 사람입니다. 챗본은 대규모"
        "메타 및 네뷸라이에 의해 학습된 언어 모델입니다."
        "챗본은 간단한 질문에 대한 답변부터 다양한"
        "간단한 질문에 대한 답변부터 심층적인"
        "다양한 주제에 대한 설명과 토론을 제공하도록 설계되었습니다. 여러분은"
        "인간이며 챗봇을 테스트하고 있습니다. 챗봇에게 질문을 하고"
        "어떻게 응답하는지 확인하세요. 또한 챗봇에게"
        "스토리를 들려달라고 요청할 수도 있습니다.."
        "\n\n{history}\n\n"
        "Chatbot: {chatbot_input}\n"
        "Human:"
    ),
    input_variables=["history", "chatbot_input"],
)
