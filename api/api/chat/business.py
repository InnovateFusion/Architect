import json
from api.chat.setup import generate_chat_response, add_message
from api.chat.data import  message_for_design,fail_response, examples, business, business_answer_sample, business_answer_example


def initialize_messages():
    """Initialize the chat messages with system and user messages."""
    return [
        {"role": "system", "content": "You're a kind helpful assistant, only respond with knowledge you know for sure, don't hallucinate information."},
        {"role": "user", "content": business['initial']}
    ]

def home_design_prompt(user_answer=None):
    """Generate a prompt for the design question."""
    return f"""
    {message_for_design[1].format(answers=user_answer)}
    {message_for_design[2]}
    {business_answer_sample}
    {" For example, {examples}".format(examples=business_answer_example)}
    {message_for_design[3]}
    {fail_response}
    {message_for_design[4]}
    """

def generate_bunisess_design_response(user_answer):
    messages = initialize_messages()
    chat_response = generate_chat_response(messages)

    try:
        response = json.loads(chat_response)
        add_message(messages, "assistant", chat_response)
        if 'status' in response and response['status'] == 'success':
            user_message = home_design_prompt(user_answer)
            add_message(messages, "user", user_message)
            chat_response = generate_chat_response(messages)
            print(chat_response)
            decode_response = json.loads(chat_response)
            keys_to_check = ['status', 'feasibility', 'building_details', 'occupancy_details', 'design_preferences', 'construction_and_timing', 'budget_analysis', 'timeline_analysis', 'recommendations', 'summary']
            if "status" not in decode_response or decode_response["status"] != "success":
                return None
            for key in decode_response:
                if key in keys_to_check:
                    response = decode_response[key]
                else:
                    print("key not found", key)
                    return None
            add_message(messages, "assistant", chat_response)
            return [decode_response, messages]          
        else:
            return None
        
    except json.JSONDecodeError as e:   
        return None 

    