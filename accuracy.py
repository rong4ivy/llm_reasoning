from tqdm import tqdm

def calculate_accuracy(data,correct_count = 0):
    errors = []
    yn_question_count = 0
    total_questions = 0

    for item in tqdm(data['data']):
        story = " ".join(item['story']) 
        for question_data in item['questions']:
            question = question_data['question']
            question_type = question_data["q_type"]
            total_questions += 1 
            if question_type == 'YN':
                yn_question_count += 1
                true_answer = ' '.join(question_data['answer']).lower().strip()

                step_needed = question_data["question_info"].get("reasoning_steps")

                input_prompt = f"Given context: {story} Question: {question}."

                result = call_model(input_prompt)

                if "error occurred" in result:
                    errors.append(result)

                    pattern = r"[^\w\s]"
                    expected_answer = re.sub(pattern,"",result).lower().strip()
                
                    if expected_answer == true_answer: 
                        correct_count += 1

  
    accuracy = correct_count / yn_question_count  * 100  # Calculate accuracy percentage
    return accuracy, step_needed


if __name__ == '__main__':
    calculate_accuracy()
